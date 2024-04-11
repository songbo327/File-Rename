import unittest
import os
from rename_module import rename_bulk
from preview_module import preview_rename
from unredo_module import unredo

class TestRenameFunctions(unittest.TestCase):
    def setUp(self):
        self.directory = 'test_directory'
        self.rule = {'.txt': 'newname', '.jpg': 'newname', '.png': 'newname'}
        os.makedirs(self.directory, exist_ok=True)
        self.files = ['file1.txt', 'file2.jpg', 'file3.png']
        for file in self.files:
            with open(os.path.join(self.directory, file), 'w') as f:
                f.write('test')

    def tearDown(self):
        for file in os.listdir(self.directory):
            os.remove(os.path.join(self.directory, file))
        os.rmdir(self.directory)

    def test_rename_bulk(self):
        rename_operations = rename_bulk(self.directory, self.rule)
        renamed_files = os.listdir(self.directory)
        for file in renamed_files:
            self.assertTrue(file.startswith('newname'))
    def test_preview_rename(self):
        rename_operations = preview_rename(self.directory, self.rule)
        for operation in rename_operations:
            new_name = os.path.basename(operation.new_name)
            self.assertTrue(new_name.startswith('newname'))

    def test_unredo(self):
        rename_operations = rename_bulk(self.directory, self.rule)
        unredo(self.directory, rename_operations, 'undo')
        original_files = os.listdir(self.directory)
        for file in original_files:
            self.assertFalse(file.startswith('newname'))

if __name__ == '__main__':
    unittest.main()