import json
import logging
import logging.config
import os
import sys
import traceback

from typing import List
from util import yaml_init


logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)


def get_filename(path: str) -> List[str]:
    return os.path.splitext(os.path.basename(path))


def json_to_yaml(path: str) -> None:
    yaml = yaml_init()
    try:
        with open(path, mode='r', encoding='utf-8') as in_f:
            d = json.load(in_f)
        with open(f'./out/{get_filename(path)[0]}_out.yml', mode='w', encoding='utf-8') as out_f:
            yaml.dump(d, out_f)
        logger.info('Parse to YAML succeeded.')
    except FileNotFoundError:
        logger.error(traceback.format_exc())


def yaml_to_json(path: str) -> None:
    yaml = yaml_init()
    try:
        with open(path, mode='r', encoding='utf-8') as in_f:
            d = yaml.load(in_f)
        with open(f'./out/{get_filename(path)[0]}_out.json', mode='w', encoding='utf-8') as out_f:
            json.dump(d, out_f, indent=2, ensure_ascii=False)
        logger.info('Parse to JSON succeeded.')
    except FileNotFoundError:
        logger.error(traceback.format_exc())


def parse_file(path: str) -> None:
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
    args = sys.argv
    try:
        parse_file(args[1])
    except Exception:
        logger.error(traceback.format_exc())
