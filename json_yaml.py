import json
import os

from ruamel.yaml import YAML


def yaml_init():
    yaml = YAML()
    yaml.allow_unicode = True
    yaml.default_flow_style = False
    yaml.indent(mapping=2, sequence=4, offset=2)
    return yaml


def json_to_yaml(path):
    with open(path, mode='r', encoding='utf-8') as in_f:
        d = json.load(in_f)
    file_name = os.path.splitext(os.path.basename(path))[0]
    yaml = yaml_init()
    with open(f'{file_name}.yml', mode='w', encoding='utf-8') as out_f:
        yaml.dump(d, out_f)


def yaml_to_json(path):
    pass


if __name__ == '__main__':
    json_to_yaml('./hoge.json')
