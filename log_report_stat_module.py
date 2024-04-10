import os
import json
import datetime


class LogReportStat:
    def __init__(self, log_file='log.json'):
        self.log_file = log_file
        self.log_data = []

    def log(self, operation_name, directory, rule=None):
        """
        Log an operation.
        """
        operation = {
            'name': operation_name,
            'time': datetime.datetime.now().isoformat(),
            'directory': directory,
            'rule': rule
        }
        self.log_data.append(operation)
        self.save_json(self.log_file, self.log_data)


    def save_json(self, file, data):
        """
        Save data to a JSON file.
        """
        with open(file, 'w') as f:
            json.dump(data, f)

    def load_json(self, file):
        """
        Load data from a JSON file.
        """
        if os.path.exists(file):
            with open(file, 'r') as f:
                return json.load(f)
        else:
            return []