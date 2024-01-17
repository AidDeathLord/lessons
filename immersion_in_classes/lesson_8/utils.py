import os
from File import File
from NotExistsError import NotExistsError
from NotReadableError import NotReadableError
from FileError import FileError


def read_files(list_of_path):
    result = []
    for elem in list_of_path:
        file = File(elem)
        try:
            result.append(file.read())
        except FileError:
            result.append(None)
    return result


file_path = '/home/aid/python/lessons/annotations.py'
error = NotExistsError()
assert isinstance(error, FileError)

error = NotReadableError()
assert isinstance(error, FileError)

values = read_files([])
assert values == []

values = read_files(['/etc/shadow', '/opt/asdf'])
print(values)
assert (values[1]) is None
