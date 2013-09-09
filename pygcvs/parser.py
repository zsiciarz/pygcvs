from __future__ import unicode_literals, print_function

import csv
import logging

logger = logging.getLogger(__name__)


class GcvsParser(object):
    def parse_magnitude(self, magnitude_str):
        mag_symbol = magnitude_str[0].strip()
        magnitude = magnitude_str[1:6].strip()
        return float(magnitude) if magnitude else None
