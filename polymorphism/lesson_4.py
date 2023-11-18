def stringify(tag):
    match tag.get('tag_type'):
        case 'pair':
            return f"<{tag.get('name')}{get_values(tag)}>{tag.get('body')}</{tag.get('name')}>"
        case 'single':
            return f"<{tag.get('name')}{get_values(tag)}>"


def get_values(tag):
    result = ' '
    for elem in tag.keys():
        if elem not in ['name', 'body', 'tag_type']:
            result = result + f"{elem}=\"{tag[elem]}\" "
    if result == ' ':
        return ''
    return result[:-1]


hr_tag = {
    'name': 'hr',
    'class': 'px-3',
    'id': 'myid',
    'tag_type': 'single',
}

html = stringify(hr_tag)
print(html)  # <hr class="px-3" id="myid">

div_tag = {
    'name': 'div',
    'tag_type': 'pair',
    'body': 'text2',
    'id': 'wow',
}
html = stringify(div_tag)
print(html)  # <div id="wow">text2</div>

empty_div_tag = {
    'name': 'div',
    'tag_type': 'pair',
    'body': '',
    'id': 'empty',
}
html = stringify(empty_div_tag)
print(html)  # <div id="empty"></div>
