import os
import datetime

class RenameOperation:
    def __init__(self, old_name, new_name):
        self.old_name = old_name
        self.new_name = new_name
        self.undone = False
global rename_operations
def rename_file(old_name, new_name):
    """
    Rename a single file from old_name to new_name.
    """
    os.rename(old_name, new_name)


def rename_bulk(directory, prefix_dict, verbose_count=False, verbose_time=False):
    """
    Rename files in a directory based on a rule.
    The rule is a fixed prefix (different for each file type) plus a variable suffix and the file extension.
    """
    rename_operations = []
    counters = {}
    for filename in os.listdir(directory):
        file_extension = os.path.splitext(filename)[1]
        prefix = prefix_dict.get(file_extension)
        # If there is no rule for this file type, skip this file
        if prefix is None:
            continue
        # Get the counter for this file type, or start a new one
        counter = counters.get(file_extension, 1)
        # Get the current date and time
        date_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        new_name = f"{prefix}_{counter}{file_extension}"
        rename_file(os.path.join(directory, filename), os.path.join(directory, new_name))
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)
        rename_operations.append(RenameOperation(old_name=old_path, new_name=new_path))
        # Increment the counter for this file type
        counters[file_extension] = counter + 1

    # Print the date and time of renaming
    if verbose_time:
        print(f"Renaming completed at {date_time}")

    # Print the count of renamed files
    if verbose_count:
        for file_type, count in counters.items():
            print(f"Renamed {count} files of type {file_type}")

    return rename_operations