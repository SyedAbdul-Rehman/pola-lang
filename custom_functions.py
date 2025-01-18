import os

def jod(a, b):
    return a + b

def read(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
def append_to_file(file_path, text):
    with open(file_path, 'a') as file:
        file.write(text + '\n')
def make_folder(folder_name):
    try:
        os.makedirs(folder_name, exist_ok=True)
    except Exception as e:
        print(f"An error occurred while creating the folder: {e}")        
