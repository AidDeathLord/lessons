import copy


class InMemoryKV:
    def __init__(self, _dict):
        self._dict = copy.deepcopy(_dict)

    def set_(self, key, value):
        self._dict[key] = value

    def unset_(self, key):
        self._dict.pop(key)

    def get_(self, key, default=None):
        return self._dict.get(key, default)

    def to_dict(self):
        return copy.deepcopy(self._dict)


data = {'key': 10}
data_copy = copy.deepcopy(data)
map = InMemoryKV(data)
data['key2'] = 'value2'
assert map.to_dict() == data_copy
map2 = map.to_dict()
map2['key2'] = 'value2'
assert map.to_dict() == data_copy
