from urllib.parse import urlparse, parse_qs


class Url:
    def __init__(self, address):
        self.address = address
        adr_parse = urlparse(address)
        self.scheme = adr_parse.scheme
        self.hostname = adr_parse.hostname
        query = adr_parse.query
        self.query_params = parse_qs(query)
        print(adr_parse)

    def get_scheme(self):
        return self.scheme

    def get_hostname(self):
        return self.hostname

    def get_query_params(self):
        return self.query_params

    def get_query_param(self, param, info=None):
        if param in self.query_params:
            return self.query_params.get(param)[0]
        return info

    def __eq__(self, other):
        return self.address == other


url = Url('http://hexlet.io:80?key=value&key2=value2')
print(url.get_scheme())  # http
print(url.get_hostname())  # hexlet.io
print(url.get_query_params())
# {
#  key: [value],
#  key2: [value2],
# }
print(url.get_query_param('key'))  # value
# второй параметр — значение по умолчанию
print(url.get_query_param('key2', 'lala'))  # value2
print(url.get_query_param('new', 'ehu'))  # ehu
print(url.get_query_param('new'))  # None
print(url == Url('http://hexlet.io:80?key=value&key2=value2'))  # True
print(url == Url('http://hexlet.io:80?key=value'))  # False
