from HTMLElement import HTMLElement


# BEGIN (write your solution here)
class HTMLHrElement(HTMLElement):
    def __str__(self):
        attributes = self.get_attribute()
        str_attributes = ''
        for keys, values in attributes.items():
            str_attributes = str_attributes + f' {keys}="{values}"'
        return f'<hr{str_attributes}>'

# END

hr = HTMLHrElement({'class':'w-75', 'id':'wop'})
print(hr)
