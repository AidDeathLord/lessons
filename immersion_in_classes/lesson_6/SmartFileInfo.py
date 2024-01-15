from FileInfo import FileInfo


# BEGIN (write your solution here)
class SmartFileInfo(FileInfo):
    def get_size(self, unit='b'):
        match unit:
            case 'b':
                return self.file_stat.st_size
            case 'kb':
                return self.file_stat.st_size / 1024
            case _:
                raise ValueError('неправильная единица измерения')

# END
