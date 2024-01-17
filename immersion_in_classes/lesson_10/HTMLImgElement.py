from HTMLElement import HTMLElement


class HTMLImgElement(HTMLElement):
    ATTRIBUTE_NAMES = ['src']

    @classmethod
    def get_attribute_names(cls):
        return super().ATTRIBUTE_NAMES + cls.ATTRIBUTE_NAMES

    # BEGIN (write your solution here)
    def is_valid(self):
        valid_attr = super().ATTRIBUTE_NAMES
        valid_attr.extend(self.ATTRIBUTE_NAMES)
        attr = self.attributes.keys()
        for key in list(attr):
            if key not in valid_attr:
                return False
        return True
    # END


img1 = HTMLImgElement({'class': 'rounded', 'src': 'path/to/image'})
print(img1.is_valid())  # True
