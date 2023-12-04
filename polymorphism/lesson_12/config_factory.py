import os
from parsers.json_parser import JSONParser
from parsers.yaml_parser import YAMLParser
from config_klass import Config


PARSERS = {
    '.yaml': YAMLParser,
    '.yml': YAMLParser,
    '.json': JSONParser,
}


# BEGIN (write your solution here)
class ConfigFactory:
    def factory(filepath):
        format = os.path.splitext(filepath)[-1]
        parser = PARSERS[format]()
        data = parser.get_data(filepath)
        return Config(data)
# END


config = ConfigFactory.factory('fixtures/test.yml')
assert config.get_value('key') == 'value'

