import yaml


class YAMLParser:
    def get_data(self, path):
        with open(path) as f:
            data = f.read()
        return yaml.safe_load(data)
