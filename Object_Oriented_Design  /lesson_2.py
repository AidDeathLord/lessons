from dataclasses import dataclass


@dataclass
class Klass:
    pass


def to_Klass(data:dict):
    value = Klass()
    for elem in data:
        setattr(value, elem, data[elem])
    return value


data = {
    'key': 'value',
    'key2': 'value2',
}

to_Klass(data)
config = to_Klass(data)
print(config.key)  ## value
print(config.key2)  ## value2
