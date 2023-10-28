import os
import json


def read_json_file(filename):
    root = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(root, 'data', f'{filename}.json')

    with open(file_path, 'r') as file:
        data = json.load(file)

    return data
