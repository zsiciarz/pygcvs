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
        magnitude = '  8.45   '
        self.assertAlmostEqual(self.parser.parse_magnitude(magnitude), 8.45)

    def test_parse_two_digit_magnitude(self):
        """
        Check that first digit of magnitude is not stripped away.
        """
        magnitude = ' 12.2    '
        self.assertAlmostEqual(self.parser.parse_magnitude(magnitude), 12.2)
