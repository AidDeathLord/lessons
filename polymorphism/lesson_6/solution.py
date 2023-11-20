from in_memory_kv import InMemoryKV


def swap_key_value(_dict):
    copy = _dict
    for elem in copy.to_dict():
        print(elem)
        value = _dict.get_(elem)
        _dict.set_(value, elem)
    for elem in copy.to_dict():
        _dict.unset_(elem)
    return _dict


map = InMemoryKV({'key': 10})
map.set_('key2', 'value2')
swap_key_value(map)

print(map.get_('key'))
assert map.get_('key') is None
print(map.to_dict())
assert map.get_(10) == 'key'
assert map.get_('value2') == 'key2'

map = InMemoryKV({'foo': 'bar', 'bar': 'zoo'})
swap_key_value(map)
print(map.to_dict())
assert map.to_dict() == {'bar': 'foo', 'zoo': 'bar'}
