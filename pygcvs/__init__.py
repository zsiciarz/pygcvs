from .parser import GcvsParser
from .helpers import dict_to_body, read_gcvs

__all__ = ['GcvsParser', 'dict_to_body', 'read_gcvs']


__version_info__ = (1, 1, 0, 'final', 0)


def get_version():
    version = '%s.%s' % (__version_info__[0], __version_info__[1])
    if __version_info__[2]:
        version = '%s.%s' % (version, __version_info__[2])
    if __version_info__[3] != 'final':
        version = '%s%s' % (version, __version_info__[3])
        if __version_info__[4]:
            version = '%s%s' % (version, __version_info__[4])
    return version


__version__ = get_version()
