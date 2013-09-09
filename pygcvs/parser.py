from __future__ import unicode_literals, print_function

import csv
import logging

logger = logging.getLogger(__name__)


class GcvsParser(object):
    """
    A parser for GCVS data format.
    """

    def __init__(self, fp):
        """
        Creates the parser and feeds it a file-like object.
        """
        self.reader = csv.reader(fp, delimiter=str('|'))
        # skip two initial lines
        next(self.reader)
        next(self.reader)

    def __iter__(self):
        for row in self.reader:
            yield self.row_to_dict(row)

    def row_to_dict(self, row):
        """
        TODO
        """
        return {}

    def parse_magnitude(self, magnitude_str):
        """
        Converts magnitude field to a float value, or ``None`` if GCVS does
        not list the magnitude.
        """
        mag_symbol = magnitude_str[0].strip()
        magnitude = magnitude_str[1:6].strip()
        return float(magnitude) if magnitude else None
