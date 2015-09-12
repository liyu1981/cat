import imp
import os
import types
import tornado.web
import tornado.ioloop

import conf
s = conf.get('server')

import logging
logger = logging.getLogger(__name__)


class WebServer(object):

    @classmethod
    def is_pyfile(cls, filename):
        return filename.endswith('.py')

    @classmethod
    def get_filepaths(cls, directory, filter_func):
        file_paths = []
        for root, directories, files in os.walk(directory):
            for filename in files:
                if filter_func(filename):
                    filepath = os.path.join(root, filename)
                    file_paths.append(filepath)
        return file_paths

    @classmethod
    def load_classes_from_file(cls, filepath):
        mod_name,file_ext = os.path.splitext(os.path.split(filepath)[-1])
        if file_ext.lower() == '.py':
            py_mod = imp.load_source(mod_name, filepath)
        elif file_ext.lower() == '.pyc':
            py_mod = imp.load_compiled(mod_name, filepath)

        return [py_mod.__dict__.get(a)
            for a in dir(py_mod)
            if isinstance(py_mod.__dict__.get(a), (type, types.ClassType)) and \
               issubclass(py_mod.__dict__.get(a), tornado.web.RequestHandler)]

    @classmethod
    def load_classes_from_path(cls, path):
        all_classes = []
        for filepath in cls.get_filepaths(path, cls.is_pyfile):
            if filepath.endswith('__init__.py'):
                continue
            classes = cls.load_classes_from_file(filepath)
            logger.info('class loaded from {}'.format(filepath))
            all_classes = all_classes + classes
        return all_classes

    @classmethod
    def prepare_application(cls):
        routes = []
        routes_dict = {}
        d = os.path.dirname(os.path.realpath(__file__))
        cat_site_dir = os.path.abspath(os.path.join(d, '..', 'cat', 'site'))
        site_dir = os.path.abspath(os.path.join(d, '..', 'site'))
        print cat_site_dir
        print site_dir

        # internal first
        for clsobj in cls.load_classes_from_path(cat_site_dir):
            path = clsobj.get_path()
            routes.append((path, clsobj))
            routes_dict[path] = clsobj
            logger.info('path {} register with {}.'.format(path, clsobj))

        # external second
        for clsobj in cls.load_classes_from_path(site_dir):
            path = clsobj.get_path()
            if path in routes_dict:
                logging.warn('path {} is used by {}, will skip {}.'.format(
                    path,
                    routes_dict[path],
                    clsobj
                ))
            else:
                routes.append((path, clsobj))
                routes_dict[path] = clsobj
                logger.info('path {} register with {}.'.format(path, clsobj))

        application = tornado.web.Application(
            routes,
            debug=(True if ('debug' in s and s['debug']) else False)
        )

        return application

    @classmethod
    def start(cls):
        application = cls.prepare_application()
        application.listen(s['listen_port'] if 'listen_port' in s else 8888)
        tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    WebServer.start()