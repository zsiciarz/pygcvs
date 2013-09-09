from __future__ import unicode_literals

import unittest

from pygcvs.parser import GcvsParser


class GcvsParserTestCase(unittest.TestCase):
    def test_parse_simple_magnitude(self):
        parser = GcvsParser()
        magnitude = '  8.45   '
        self.assertAlmostEqual(parser.parse_magnitude(magnitude), 8.45)

    def test_parse_two_digit_magnitude(self):
        parser = GcvsParser()
        magnitude = ' 12.2    '
        self.assertAlmostEqual(parser.parse_magnitude(magnitude), 12.2)
