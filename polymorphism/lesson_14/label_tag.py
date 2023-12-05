from input_tag import InputTag


class LabelTag:
    def __init__(self, text, input_tag):
        self.text = text
        self.input_tag = input_tag

    def render(self):
        return f'<label>{self.text}{self.input_tag}</label>'

    def __str__(self):
        return self.render()



input_tag = InputTag('submit', 'Save')
label_tag = LabelTag('Press Submit', input_tag)
print(label_tag.render())
expected = '<label>Press Submit<input type="submit" value="Save"></label>'
print(input_tag)
assert label_tag.render() == expected
assert str(label_tag) == expected
