import json
from pathlib import Path


class DatabaseConfigLoader:
    def __init__(self, path):
        self.path = path

    def load(self, config):
        with open(f'{self.path}/database.{config}.json') as f:
            templates = json.load(f)
            if 'extend' in templates:
                a = self.load(templates['extend'])
                for key in a:
                    if key not in templates:
                        templates[key] = a.get(key)
                templates.pop('extend')
        return templates


path_to_configs = Path('fixtures_5les')
loader = DatabaseConfigLoader(path_to_configs)
config = loader.load('production')
config_2 = loader.load('development')
print(config)  # {host: 'google.com', username: 'postgres'}
