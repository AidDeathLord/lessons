import json


class JSONParser:
    def get_data(self, path):
        with open(path) as f:
            data = f.read()
        return json.loads(data)
