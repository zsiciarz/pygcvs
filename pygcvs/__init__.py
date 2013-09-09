from __future__ import unicode_literals, print_function

from .parser import GcvsParser


__version_info__ = (0, 1, 0, 'dev', 0)


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


def read_gcvs(fp):
    """
    Reads variable star data in `GCVS format`_ from a file-like object.

    .. _`GCVS format`: http://www.sai.msu.su/gcvs/gcvs/iii/html/
    """
    parser = GcvsParser(fp)
    for star in parser:
        yield star
