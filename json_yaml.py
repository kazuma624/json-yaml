import json
import logging
import logging.config
import os

from ruamel.yaml import YAML

logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)


def yaml_init():
    yaml = YAML()
    yaml.allow_unicode = True
    yaml.default_flow_style = False
    yaml.indent(mapping=2, sequence=4, offset=2)
    return yaml


def get_filename(path):
    return os.path.splitext(os.path.basename(path))


def json_to_yaml(path):
    yaml = yaml_init()
    try:
        with open(path, mode='r', encoding='utf-8') as in_f:
            d = json.load(in_f)
        with open(f'{get_filename(path)[0]}.yml', mode='w', encoding='utf-8') as out_f:
            yaml.dump(d, out_f)
        logger.info('Parse YAML succeeded.')
    except FileNotFoundError:
        import traceback
        logger.error(traceback.format_exc())


def yaml_to_json(path):
    yaml = yaml_init()
    try:
        with open(path, mode='r', encoding='utf-8') as in_f:
            d = yaml.load(in_f)
        with open(f'{get_filename(path[0])}.json', mode='w', encoding='utf-8') as out_f:
            json.dump(d, out_f, indent=2, ensure_ascii=False)
        logger.info('Parse JSON succeeded.')
    except FileNotFoundError:
        import traceback
        logger.error(traceback.format_exc())


def main(path):
    suffix = get_filename(path)[-1]
    if suffix == '.yaml' or suffix == '.yml':
        logger.info('Input file is YAML.')
        yaml_to_json(path)
    elif suffix == '.json':
        logger.info('Input file is JSON.')
        json_to_yaml(path)
    else:
        logger.warning('Input file is not YAML either JSON.')
        logger.warning('Nothing to do.')

if __name__ == '__main__':
    main('./hoge.json')
