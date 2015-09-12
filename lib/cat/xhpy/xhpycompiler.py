import compiler
import marshal
import os.path
import os
import fnmatch

from .parser.parser import parse

import logging
logger = logging.getLogger(__name__)

class XHPyCompiler(object):

    __xhpy_ext = '.xhpy'

    @classmethod
    def compile(cls):
        cwd = os.getcwd()

        filelist = []
        for root, dirs, files in os.walk(cwd):
            for file in fnmatch.filter(files, '*'+cls.__xhpy_ext):
                filelist.append(os.path.join(root, file))

        for filepath in filelist:
            cls.compile_file(filepath)

    @classmethod
    def compile_file(cls, filepath):
        py_name = filepath.replace(cls.__xhpy_ext, '.py')
        pyc_name = filepath.replace(cls.__xhpy_ext, '.pyc')

        if os.path.isfile(py_name) and \
           os.path.getmtime(py_name) >= os.path.getmtime(filepath):
            logger.info('now compile {} ... skipped'.format(filepath))
            return

        with open(filepath, 'r') as xhpy_fp:
            xhpy_code = xhpy_fp.read()
        py_code = parse(xhpy_code)
        with open(py_name, 'w') as xhpypy_name:
            xhpypy_name.write(py_code)
        code = compiler.compile(py_code, filepath, 'exec')
        with open(pyc_name, 'wb') as pyc_fp:
            marshal.dump(code, pyc_fp)

        logging.info('now compile {} ... done'.format(filepath))

if __name__ == '__main__':
    XHPyCompiler.compile()
