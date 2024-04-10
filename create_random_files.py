import os
import random
from faker import Faker
from io_module import save_file
def create_random_files(directory, num_files):
    """
    Create random files of various types in a directory.
    """
    fake = Faker()
    file_types = ['.docx', '.pdf', '.jpg', '.png', '.mp3', '.wav', '.mp4', '.avi']
    for _ in range(num_files):
        file_type = random.choice(file_types)
        file_name = fake.file_name(extension=file_type.lstrip('.'))
        file_path = os.path.join(directory, file_name)
        save_file(file_path, '')

if __name__ == '__main__':
    create_random_files("C:\\DS 5010\\pythonProject\\rename\\rename\\test\\", 100)
