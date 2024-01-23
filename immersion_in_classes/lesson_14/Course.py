from Enumerable import Enumerable


class Course(Enumerable):
    def __init__(self, lessons):
        self.lessons = lessons

    def get_iterator(self):
        print(self.lessons)
        return self.lessons
