def get_links(link_list):
    result = []
    for link in link_list:
        match link.get('name'):
            case 'img':
                result.append(link.get('src'))
            case 'link' | 'a':
                result.append(link.get('href'))
    return result


tags = [
    {'name': 'img', 'src': 'hexlet.io/assets/logo.png'},
    {'name': 'div'},
    {'name': 'link', 'href': 'hexlet.io/assets/style.css'},
    {'name': 'h1'},
]

links = get_links(tags)
print(links)  # ['hexlet.io/assets/logo.png', 'hexlet.io/assets/style.css']
