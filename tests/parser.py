from __future__ import unicode_literals

import unittest

from six import StringIO

from pygcvs.parser import GcvsParser


class GcvsParserTestCase(unittest.TestCase):
    """
    Tests for GcvsParser class.
    """
    def setUp(self):
        # two line breaks so parser's __init__ does not raise StopIteration
        self.fp = StringIO("\n\n")
        self.parser = GcvsParser(self.fp)

    def tearDown(self):
        self.fp.close()

    def test_parse_simple_magnitude(self):
        """
        Check that magnitude value without any flags is parsed correctly.
        """
        magnitude_str = '  8.45   '
        magnitude, symbol = self.parser.parse_magnitude(magnitude_str)
        self.assertAlmostEqual(magnitude, 8.45)

    def test_parse_two_digit_magnitude(self):
        """
        Check that first digit of magnitude is not stripped away.
        """
        magnitude_str = ' 12.2    '
        magnitude, symbol = self.parser.parse_magnitude(magnitude_str)
        self.assertAlmostEqual(magnitude, 12.2)
