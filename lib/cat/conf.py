import json
import logging

logger = logging.getLogger(__name__)

all = {
  'live': {}
}

def get(name):
    global all

    def read_conf(name):
        path = 'etc/{}.json'.format(name)
        try:
            with open(path, 'r') as f:
                c = json.load(f)
                logger.info('loaded conf {} => {}.'.format(path, name))
                return c
        except IOError,e:
            logger.warn('Error {} while loading {}'.format(e, path))
            return {}

    if not name:
        return all
    else:
        if not name in all:
            c = read_conf(name)
            all[name] = c
        return all[name] if name in all else None

def set(k, v):
    global all
    logger.info('live changed: {} = {}'.format(k, v))
    all['live'][k] = v
