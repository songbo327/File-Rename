import os

class RenameOperation:
    def __init__(self, old_name, new_name):
        self.old_name = old_name
        self.new_name = new_name
        self.undone = False
    def to_dict(self):
        return {
            'old_name': self.old_name,
            'new_name': self.new_name
        }
global rename_operations
def unredo(directory, rename_operations, operation_name):
    """
    Undo or redo a list of rename operations.
    """
    if not rename_operations:
        print("No rename operations have been performed.")
        return
    
    count = 0
    for operation in rename_operations:
        old_path = os.path.join(operation.old_name)
        new_path = os.path.join(operation.new_name)
        if operation_name == 'undo' and os.path.exists(new_path) and not operation.undone:
            count = count + 1
            # Undo the operation
            os.rename(new_path, old_path)
            operation.undone = True
        elif operation_name == 'redo' and operation.undone and os.path.exists(old_path):
            count = count + 1
            # Redo the operation
            os.rename(old_path, new_path)
            operation.undone = False
    if count == 0 and operation_name == 'undo':
        print("No rename operations to undo.")
    elif count == 0 and operation_name == 'redo':
        print("No rename operations to redo.")
    return rename_operations