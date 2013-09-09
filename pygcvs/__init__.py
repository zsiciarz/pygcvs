from __future__ import unicode_literals, print_function

import csv
import logging

logger = logging.getLogger(__name__)

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
    reader = csv.reader(fp, delimiter=str('|'))
    # skip two initial lines
    next(reader)
    next(reader)
    for row in reader:
        if len(row) != 15:
            continue
        try:
            name = row[1][:9]
            name = ' '.join(name.split()).upper()
            variable_type = row[3].strip()
            mag_symbol = row[4][0].strip()
            max_magnitude = row[4][1:6].strip()
            max_magnitude = float(max_magnitude) if max_magnitude else None
            mag_symbol = row[5][0].strip()
            min_magnitude = row[5][1:6].strip()
            min_magnitude = float(min_magnitude) if min_magnitude else None
            if mag_symbol == '(' and max_magnitude is not None:
                # this is actually amplitude
                min_magnitude = max_magnitude + min_magnitude
            epoch = row[8][:10].strip()
            epoch = 2400000.0 + float(epoch) if epoch else None
            period = row[10][1:17].strip()
            period = float(period) if period else None
            yield {
                'name': name,
                'variable_type': variable_type,
                'max_magnitude': max_magnitude,
                'min_magnitude': min_magnitude,
                'epoch': epoch,
                'period': period,
            }
        except Exception:
            logger.exception('Error in row: %s', row)
            continue
