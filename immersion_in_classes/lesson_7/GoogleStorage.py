class GoogleStorage:
    def __init__(self):
        self.elements = {}

    def set(self, key, value):
        self.elements[key] = value

    def get(self, key):
        return self.elements.get(key)

    def count(self):
        raise Exception
