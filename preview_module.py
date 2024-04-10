import os
from rename_module import rename_bulk

def preview_rename(directory, prefix_dict, suffix_start=1,verbose_count=False, verbose_time=False):
    """
    Preview the result of a rename operation and ask for confirmation.
    The rename operation is defined by a fixed prefix (different for each file type) plus a variable suffix and the file extension.
    """
    counters = {}
    preview = {}
    for filename in os.listdir(directory):
        file_extension = os.path.splitext(filename)[1]
        prefix = prefix_dict.get(file_extension)
        if prefix is None:
            continue
        # Get the counter for this file type, or start a new one
        counter = counters.get(file_extension, suffix_start)
        # Get the current date and time
        new_name = f"{prefix}_{counter}{file_extension}"
        preview[filename] = new_name
        # Increment the counter for this file type
        counters[file_extension] = counter + 1

    # Print the preview
    for old_name, new_name in preview.items():
        print(f"{old_name} -> {new_name}")

    # Ask for confirmation
    confirm = input("Do you want to confirm the rename operation? (yes/no): ")
    if confirm.lower() == 'yes':
        rename_operation = rename_bulk(directory, prefix_dict,verbose_count, verbose_time)
        return rename_operation