class HTMLElement:
    def __init__(self, attributes=None):
        if attributes is None:
            self.attributes = {}
        else:
            self.attributes = attributes

    def get_attribute(self, key):
        return self.attributes.get(key)

    # BEGIN (write your solution here)
    def _get_value(self):
        return self.attributes.get('tag').split()

    def _add_value(self, line):
        new_line = ''.join(f'{value} ' for value in line)
        self.attributes['tag'] = new_line.strip()

    def add_tag(self, tag_name):
        self_list = self._get_value()
        if tag_name not in self_list:
            self_list.append(tag_name)
        self._add_value(self_list)

    def remove_tag(self, tag_name):
        self_list = self._get_value()
        if tag_name in self_list:
            self_list.remove(tag_name)
            print(self_list)
        self._add_value(self_list)

    def toggle_tag(self, tag_name):
        self_list = self._get_value()
        if tag_name in self_list:
            self.remove_tag(tag_name)
        else:
            self.add_tag(tag_name)
    # END


class HTMLDivElement(HTMLElement):
    pass


div = HTMLDivElement({'tag': 'one two'})
div.get_attribute('tag')  # 'one two'
print(div._get_value())
div.add_tag('111')
print(div.get_attribute('tag'))
div.remove_tag('111')
print(div.get_attribute('tag'))
