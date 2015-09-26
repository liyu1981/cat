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
    def compile_dir(cls, **kwargs):
        if 'dir' in kwargs:
            cwd = kwargs['dir']
        else:
            cwd = os.getcwd()

        filelist = []
        for root, dirs, files in os.walk(cwd):
            for file in fnmatch.filter(files, '*'+cls.__xhpy_ext):
                filelist.append(os.path.join(root, file))

        compiled = []
        for filepath in filelist:
            (py_name, pyc_name) = cls.compile_file(filepath)
            if py_name:
                compiled.append((filepath, py_name, pyc_name))

        if 'add_gitignore' in kwargs:
            (rootdir, gitignorepath) = kwargs['add_gitignore']
            try:
                with open(gitignorepath, 'a+') as gi:
                    cls.add_gitignore_entries(gi, compiled, rootdir)
            except IOError,e:
                logger.warn('Oops: {}'.format(e))

        return compiled

    @classmethod
    def compile_file(cls, filepath, **kwargs):
        py_name = filepath.replace(cls.__xhpy_ext, '.py')
        pyc_name = filepath.replace(cls.__xhpy_ext, '.pyc')

        if os.path.isfile(py_name) and \
           os.path.getmtime(py_name) >= os.path.getmtime(filepath):
            logger.debug('now compile {} ... skipped'.format(filepath))
            return (None, None)

        with open(filepath, 'r') as xhpy_fp:
            xhpy_code = xhpy_fp.read()
        py_code = parse(xhpy_code)
        with open(py_name, 'w') as xhpypy_name:
            xhpypy_name.write(py_code)
        code = compiler.compile(py_code, filepath, 'exec')
        with open(pyc_name, 'wb') as pyc_fp:
            marshal.dump(code, pyc_fp)

        logging.info('now compile {} ... done'.format(filepath))
        return (py_name, pyc_name)

    @classmethod
    def add_gitignore_entries(cls, fp, compiled, rootdir):
        fp.seek(0)
        content = fp.read()
        towrite = []
        for _, py_name, _ in compiled:
            entry = os.path.relpath(py_name, rootdir)
            if content.find(entry) < 0:
                towrite.append(entry)
        for entry in towrite:
            fp.write(entry + '\n')
            logger.info('added {} to .gitignore'.format(entry))

    @classmethod
    def debug(cls):
        from .parser.utils import set_parser_debug
        set_parser_debug()
        logger.info('debug mode turned on.')

if __name__ == '__main__':
    XHPyCompiler.compile()
