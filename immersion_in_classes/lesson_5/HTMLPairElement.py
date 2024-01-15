from HTMLElement import HTMLElement


# BEGIN (write your solution here)
class HTMLPairElement(HTMLElement):
    def __init__(self, attributes=None):
        super().__init__(attributes)
        self._text = ''

    def __str__(self):
        attributes = self._stringify_attributes()
        body = self._text
        tag_name = self.get_tag_name()
        return f"<{tag_name}{attributes}>{body}</{tag_name}>"

    def get_text_content(self):
        return self._text

    def set_text_content(self, text: str):
        self._text = text

# END
