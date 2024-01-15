class HTMLElement:
    def __init__(self, attributes=None):
        self.attributes = attributes if attributes else {}

    def _stringify_attributes(self):
        line = ''.join(f' {k}="{v}"' for k, v in self.attributes.items())
        return line
