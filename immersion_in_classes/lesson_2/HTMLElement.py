class HTMLElement:
    def __init__(self, attributes=None):
        self.attributes = attributes if attributes else {}

    # BEGIN (write your solution here)
    def set_attribute(self, **kwargs):
        for key, values in kwargs:
            self.attributes[key] = values

    def get_attribute(self):
        return self.attributes
    # END
