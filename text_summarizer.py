import os
import openai
from docx import Document
import json
from datetime import datetime

file_path = '/Users/davidgodinez/Desktop/GOBC/files/sample_doc1.docx'

# Get api key from credentials.json file
def get_api_key(path):
    with open(path, 'r') as file:
        credentials = json.load(file)
    return credentials["OPENAI_KEY"]

openai.api_key = get_api_key('credentials.json')

# Read a word file and return the text
def read_word_file(file_path):
    doc = Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

# Summarize text using OpenAI's Davinci engine
def summarize_text(text):
    messages = [
        {"role": "system", "content": "You are a helpful assistant that summarizes documents."},
        {"role": "user", "content": "Summarize the following document for a 12th grader. Give it to me in a short paragraph and your three main takeaways in bullet points:\n" + text}
    ]

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",  # replace with the correct model ID for GPT-4
      messages=messages,
      max_tokens=500,
      temperature=0.2,
    )

    # The assistant's reply can be found in the last message in the response
    return response['choices'][0]['message']['content'].strip()


# Summarize a word file and save the summarized text to a new file
def summarize_word_file(file_path):
    text_to_summarize = read_word_file(file_path)
    summarized_text = summarize_text(text_to_summarize)

    if not os.path.exists('summarized_files'):
        os.makedirs('summarized_files')

    now = datetime.now()
    now_str = now.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f'summarized_files/summarized_text_{now_str}.txt'

    with open(filename, 'w') as file:
        file.write(summarized_text)
    
    return filename  # Return the filename to show where the summarized text was saved.

# Use the function like this:
# filename = summarize_word_file(file_path=file_path)
# print(f"Summarized text saved to: {filename}")
