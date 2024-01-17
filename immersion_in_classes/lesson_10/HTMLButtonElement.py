from HTMLElement import HTMLElement


class HTMLButtonElement(HTMLElement):
    ATTRIBUTE_NAMES = ['type']
    TYPE_NAMES = ['button', 'submit', 'reset']

    @classmethod
    def get_attribute_names(cls):
        return super().ATTRIBUTE_NAMES + cls.ATTRIBUTE_NAMES

    # BEGIN (write your solution here)
    def is_valid(self):
        valid_attr = super().ATTRIBUTE_NAMES
        valid_attr.extend(self.ATTRIBUTE_NAMES)

        attr = list(self.attributes.keys())
        for key in attr:
            if key not in valid_attr:
                return False
        if 'type' not in attr:
            return False
        if self.attributes.get('type') not in self.TYPE_NAMES:
            return False
        return True
    # END
