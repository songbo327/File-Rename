
from io_module import save_file
from rename_module import rename_bulk
from preview_module import preview_rename
from unredo_module import unredo
from log_report_stat_module import LogReportStat
import ast
from collections import Counter
def main():
    global rename_operations
    log_report_stat = LogReportStat()
    while True:
        print("Please enter the operation you want to perform:")
        print("1. Rename files")
        print("2. Preview rename")
        print("3. Undo/Redo")
        print("4. Generate log")
        print("5. Generate stat")
        print("6. Exit")
        operation = input("Your choice: ")
        if operation == '1':
            directory = input("Please enter the directory: ")
            rule = input("Please enter the rename rule (format: '.ext:prefix,.ext:prefix'): ")
            rule = ast.literal_eval(rule)
            rename_operations = rename_bulk(directory, rule)
            log_report_stat.log('Rename files', directory, rule)
        elif operation == '2':
            directory = input("Please enter the directory: ")
            rule = input("Please enter the rename rule (format: '.ext:prefix,.ext:prefix'): ")
            rule = ast.literal_eval(rule)
            rename_operations = preview_rename(directory, rule)
            log_report_stat.log('Preview rename', directory, rule)
        elif operation == '3':
            undo_redo = input("Please enter 'undo' or 'redo': ")
            if undo_redo == 'undo':
                rename_operations = unredo(directory, rename_operations, 'undo')
                log_report_stat.log('Undo', directory)
            elif undo_redo == 'redo':
                rename_operations = unredo(directory, rename_operations, 'redo')
                log_report_stat.log('Redo', directory)
            else:
                print("Invalid input. Please enter 'undo' or 'redo'.")
        elif operation == '4':
            log_data = log_report_stat.load_json(log_report_stat.log_file)
            for log in log_data:
                print("Operation: {name}, Time: {time}, Directory: {directory}, Rule: {rule}".format(**log))
        elif operation == '5':
            log_data = log_report_stat.load_json(log_report_stat.log_file)
            f = ['Rename files', 'Preview rename', 'Undo', 'Redo']
            stat_data = Counter([op['name'] for op in log_data if op['name'] in f])
            for i in stat_data:
                print(f"{i}: {stat_data[i]}")
        elif operation == '6':
            break
        else:
            print("Invalid input. Please enter a number between 1 and 6.")

if __name__ == '__main__':
    main()
    ## rule = {'.txt': 'newname', '.jpg': 'newname', '.png': 'newname'}