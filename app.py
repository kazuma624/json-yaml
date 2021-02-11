import json
import logging
import logging.config
import traceback

from bottle import (
    Bottle,
    request,
    run,
    template,
)
from typing import Any
from util import yaml_init, MyYAML


logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)

app = Bottle()


@app.route('/transform', method='POST')
def parse() -> Any:
    result = ''
    try:
        content = request.forms.get('content')
        src = request.forms.get('src')
        yaml = yaml_init()
        if src.upper() == 'JSON':
            d = json.loads(content)
            result = MyYAML().dump(d)
        elif src.upper() == 'YAML':
            d = yaml.load(content)
            result = json.dumps(d, indent=2, ensure_ascii=False)
        else:
            logger.warning('Input file is not YAML either JSON.')
            logger.warning('Nothing to do.')
    except Exception:
        logger.error(traceback.format_exc())

    return template('index', result=result)


@app.route('/', method='GET')
def index() -> Any:
    return template('index', result='')


if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True, reloader=True)
