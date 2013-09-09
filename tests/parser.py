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

    def test_parse_empty_magnitude(self):
        """
        Check that empty magnitude field parses to None.
        """
        magnitude_str = '         '
        magnitude, symbol = self.parser.parse_magnitude(magnitude_str)
        self.assertIsNone(magnitude)

    def test_parse_name_spaces(self):
        """
        Check that multiple spaces between star name and constellation name
        collapse to one space.
        """
        name_str = 'VY    AND  '
        name = self.parser.parse_name(name_str)
        self.assertEqual(name, 'VY AND')

    def test_parse_name_uppercase(self):
        """
        Check that normalized star name is always uppercase.
        """
        name_str = 'VY    And  '
        name = self.parser.parse_name(name_str)
        self.assertEqual(name, 'VY AND')

    def test_parse_epoch(self):
        """
        Check that epoch has 24... prefix.
        """
        epoch_str = '34618.185   '
        epoch = self.parser.parse_epoch(epoch_str)
        self.assertAlmostEqual(epoch, 2434618.185)

    def test_parse_empty_epoch(self):
        """
        Check that empty epoch normalizes to None.
        """
        epoch_str = '            '
        epoch = self.parser.parse_epoch(epoch_str)
        self.assertIsNone(epoch)

    def test_parse_period(self):
        """
        Check that the period field parses correctly.
        """
        period_str = '    23.285213       '
        period = self.parser.parse_period(period_str)
        self.assertAlmostEqual(period, 23.285213)

    def test_parse_empty_period(self):
        """
        Check that empty period normalizes to None.
        """
        period_str = '                    '
        period = self.parser.parse_period(period_str)
        self.assertIsNone(period)
