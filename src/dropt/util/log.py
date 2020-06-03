'''Logging utilities for DrOpt packages.'''


import logging
import functools
from pathlib import Path


class MetaLogger:
    '''Meta logger class.'''
    def __init__(self, name):
        self._logger = logging.getLogger(name)

    def debug(self, msg, *args, **kwargs):
        self._logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self._logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self._logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self._logger.error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        self._logger.error(msg, *args, **kwargs)

    def add_console_handler(self, level):
        '''Create a stream handler.'''
        ch = logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(self.chformatter)
        self._logger.addHandler(ch)
        if (self._logger.level == 0) or (self._logger.level > level):
            self._logger.setLevel(level)

    def add_file_handler(self, level, **kwargs):
        '''Create a file handler.

        "kwargs" coincides with that in logging.FileHandler,
        which should contain at least "filename."
        '''
        kwargs['filename'] = Path(kwargs['filename'])
        kwargs['filename'].parent.mkdir(parents=True, exist_ok=True)
        fh = logging.FileHandler(**kwargs)
        fh.setLevel(level)
        fh.setFormatter(self.fhformatter)
        self._logger.addHandler(fh)
        if (self._logger.level == 0) or (self._logger.level > level):
            self._logger.setLevel(level)


class BaseLogger(MetaLogger):
    '''Base logger class, which defines the logging format.'''
    # logging format
    dtfmt = '%Y-%m-%d %H:%M:%S'
    chfmt = '[%(asctime)s] %(name)s [%(levelname)s] %(message)s'
    chformatter = logging.Formatter(chfmt, dtfmt)
    fhfmt = '%(asctime)s|%(name)s|%(levelname)s|%(message)s'
    fhformatter = logging.Formatter(fhfmt, dtfmt)


class Logger(BaseLogger):
    '''DrOpt logger class.'''
    name = 'dropt'

    def __init__(self):
        super().__init__(self.name)


class SrvLogger(BaseLogger):
    '''DrOpt serviec logger class.'''
    name = 'dropt.srv'

    def __init__(self):
        super().__init__(self.name)


class CliLogger(BaseLogger):
    '''DrOpt client logger.'''
    name = 'dropt.cli'

    def __init__(self):
        super().__init__(self.name)


class UserLogger(BaseLogger):
    '''DrOpt User logger.'''
    name = 'dropt.user'

    def __init__(self, suffix):
        super().__init__(f'{self.name}.{suffix}')


class FuncLoggingWrapper:
    '''Logging wrapping class for function.'''
    def __init__(self, logger):
        self._logger = logger

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            self._logger.debug(f'Entering function "{func.__name__}".')
            r = func(*args, **kwargs)
            self._logger.debug(f'Exiting function "{func.__name__}".')
            return r
        return wrapper
