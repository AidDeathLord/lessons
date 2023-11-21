class User:
    def __init__(self, name):
        self.name = name
        # BEGIN (write your solution here)
        self.access = 'User'
        # END

    def get_name(self):
        return self.name

    # BEGIN (write your solution here)
    def get_access(self):
        return self.access
    # END
