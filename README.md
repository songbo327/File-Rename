File Renaming Tool
This is a simple file renaming tool that allows you to rename files in bulk within a specified directory. It provides features such as previewing the renaming results, undoing and redoing operations, and generating operation logs and statistics.

Features
Bulk Rename: Rename all files in a specified directory according to a given rule. The rule is a dictionary where the keys are the file extensions and the values are the prefixes to be added to the file names.

Preview Rename: Preview the results of the renaming operation without actually renaming the files.

Undo/Redo: Undo or redo the last renaming operation.

Generate Log: Generate a log of all operations. The log includes the name of the operation, the time it was performed, the directory it was performed in, and the renaming rule (if applicable).

Generate Statistics: Generate statistics of the operations, showing the number of times each operation ('Rename files', 'Preview rename', 'Undo', 'Redo') was performed.

Usage
Run the test.py script. You will be presented with a menu of operations to perform:
Please enter the operation you want to perform:
1. Rename files
2. Preview rename
3. Undo/Redo
4. Generate log
5. Generate stat
6. Exit
Enter the number of the operation you want to perform and follow the prompts.

Requirements
This tool requires Python 3.6 or later. No additional packages are required.