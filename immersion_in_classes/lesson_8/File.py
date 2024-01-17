import os
from NotExistsError import NotExistsError
from NotReadableError import NotReadableError


class File:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        file_path = self.file_path

        # BEGIN (write your solution here)
        if not os.path.exists(file_path):
            raise NotExistsError
        if not os.access(file_path, os.R_OK):
            raise NotReadableError
        # END
        with open(file_path, 'r') as file:
            return file.read()
