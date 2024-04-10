import os

def load_file(file_path):
    """
    Load a file from the given path.
    """
    if not os.path.isfile(file_path):
        return None

    with open(file_path, 'r') as file:
        content = file.read()

    return content

def save_file(file_path, content):
    """
    Save content to a file at the given path.
    """
    with open(file_path, 'w') as file:
        file.write(content)

def show_file(file_path):
    """
    Display the content of a file from the given path.
    """
    content = load_file(file_path)
    if content is not None:
        print(content)