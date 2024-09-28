import json


def load_json(path):
    with open(path) as out:
        return json.load(out)