import imp
import sys
import os
import logging
import types
import tornado.web
import tornado.ioloop
import importlib

# config log level before everything
logging.basicConfig(level=logging.DEBUG)

import conf
import xhpy

s = conf.get('server')

def load_classes_from_path(path):
    def is_pyfile(filename):
        return filename.endswith('.py')

    def get_filepaths(directory, filter_func):
        file_paths = []
        for root, directories, files in os.walk(directory):
            for filename in files:
                if filter_func(filename):
                    filepath = os.path.join(root, filename)
                    file_paths.append(filepath)
        return file_paths

    def load_classes_from_file(filepath):
        mod_name,file_ext = os.path.splitext(os.path.split(filepath)[-1])
        if file_ext.lower() == '.py':
            py_mod = imp.load_source(mod_name, filepath)
        elif file_ext.lower() == '.pyc':
            py_mod = imp.load_compiled(mod_name, filepath)
        elif file_ext.lower() == '.xhpy':
            print 'will load xhpy:' + mod_name
            importlib.import_module(mod_name)
            py_mod = sys.modules[mod_name]

        return [py_mod.__dict__.get(a)
            for a in dir(py_mod)
            if isinstance(py_mod.__dict__.get(a), (type, types.ClassType)) and
                issubclass(py_mod.__dict__.get(a), tornado.web.RequestHandler)]

    all_classes = []
    for filepath in get_filepaths(path, is_pyfile):
        classes = load_classes_from_file(filepath)
        all_classes = all_classes + classes

    return all_classes

def prepare_application():
    routes = []
    routes_dict = {}
    # internal first
    for cls in load_classes_from_path('lib/cat'):
        path = cls.get_path()
        routes.append((path, cls))
        routes_dict[path] = cls
        logging.info('path {} register with {}.'.format(path, cls))
    # external second
    for cls in load_classes_from_path('lib/site'):
        path = cls.get_path()
        if path in routes_dict:
            logging.warn('path {} is used by {}, will skip {}.'.format(
                path,
                routes_dict[path],
                cls
            ))
        else:
            routes.append((path, cls))
            logging.info('path {} register with {}.'.format(path, cls))
            routes_dict[path] = cls

    application = tornado.web.Application(
        routes,
        debug=(True if ('debug' in s and s['debug']) else False)
    )

    return application

if __name__ == "__main__":
    application = prepare_application()
    application.listen(s['listen_port'] if 'listen_port' in s else 8888)
    tornado.ioloop.IOLoop.current().start()
