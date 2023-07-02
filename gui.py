# import glob
# import os
# import tkinter as tk
# from tkinter import messagebox, PhotoImage, Button
# from text_summarizer import summarize_word_file

# def on_summarize_click():
#     files = glob.glob('/Users/davidgodinez/Desktop/GOBC/files/*.docx')  # adjust the path as needed
#     latest_file = max(files, key=os.path.getctime)
#     summary = summarize_word_file(file_path=latest_file)
#     messagebox.showinfo("Summary", summary)

# root = tk.Tk()
# root.title("Garden Oaks Baptist Church")
# root.geometry("300x200") # set size of the window
# frame = tk.Frame(root)
# frame.pack()

# # Load and display the logo image
# logo = PhotoImage(file="gobc_logo.png")
# logo_label = tk.Label(frame, image=logo)
# logo_label.pack()

# button = Button(root, text="Summarize Message", command=on_summarize_click)
# button.pack(side=tk.LEFT)

# root.mainloop()

import glob
import os
import tkinter as tk
from tkinter import messagebox, PhotoImage, Button
from PIL import Image, ImageTk
from text_summarizer import summarize_word_file
from PIL import Image, ImageTk

def on_summarize_click():
    files = glob.glob('/Users/davidgodinez/Desktop/GOBC/files/*.docx')  # adjust the path as needed
    latest_file = max(files, key=os.path.getctime)
    summary = summarize_word_file(file_path=latest_file)
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
