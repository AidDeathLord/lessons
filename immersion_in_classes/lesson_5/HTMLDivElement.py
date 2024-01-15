from HTMLPairElement import HTMLPairElement


class HTMLDivElement(HTMLPairElement):
    def get_tag_name(self):
        return 'div'


div = HTMLDivElement({'name':'div', 'data-toggle':'true'})

div.get_text_content()
div.set_text_content('Body Text')
div.get_text_content()  # Body Text
print(div)  # => '<div name="div" data-toggle="true">Body Text</div>'
