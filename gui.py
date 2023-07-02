import glob
import os
import tkinter as tk
from tkinter import messagebox, PhotoImage, Button
from PIL import Image, ImageTk
from text_summarizer import summarize_word_file, read_word_file, read_text_file
from PIL import Image, ImageTk



def on_summarize_click():
    # Get all .docx files from the directory
    # files = glob.glob('/Users/davidgodinez/Desktop/GOBC/files/*.docx')  # adjust the path as needed# Get the directory that this script is in
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Construct the path to the 'files' directory
    files_dir = os.path.join(script_dir, 'files')

    # Now use files_dir when you call glob
    files = glob.glob(os.path.join(files_dir, '*.docx'))

    # Process each file
    for file_path in files:
        result = summarize_word_file(file_path=file_path)

        # If the file was already processed, show the message
        if "has already been processed" in result:
            messagebox.showinfo("Info", result)
        else:
            # Otherwise, display a message with the summary
            summary = read_text_file(file_path=result)
            messagebox.showinfo("Summary", summary)





root = tk.Tk()
root.title("Garden Oaks Baptist Church")
root.geometry("300x200") # set size of the window
frame = tk.Frame(root)
frame.pack()

# Load and resize the logo image
image = Image.open("gobc_logo.png")
image = image.resize((80, 80), Image.LANCZOS)  # Resize the image to 80x80 pixels
logo = ImageTk.PhotoImage(image)

logo_label = tk.Label(frame, image=logo)
logo_label.pack()

button = Button(root, text="Summarize Message", command=on_summarize_click)
button.pack(side=tk.TOP)

root.mainloop()
