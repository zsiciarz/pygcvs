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

    def test_row_to_dict_simple(self):
        """
        Check that row_to_dict returns correct data for row.
        """
        row = "320031 |TX    Del *|205012.7+033908 |CWB:      |  8.84   |   9.54     |            |V |42947.009   |     |     6.165907       |33   |G0-G5            |08632 08953|".split('|')
        data = self.parser.row_to_dict(row)
        self.assertEqual(data['name'], 'TX DEL')
        self.assertEqual(data['variable_type'], 'CWB:')
        self.assertAlmostEqual(data['epoch'], 2442947.009)
        self.assertAlmostEqual(data['period'], 6.165907)

    def test_amplitude_to_magnitude(self):
        """
        Check that amplitude is correctly converted to min magnitude.
        """
        row = "869001 |alf   Vir *|132511.6-110941 |ELL+BCEP  |  0.95   |(  0.10    )|(  0.08    )|V |19530.49    |     |     4.014604       |     |B1III-IV+B2V     |04627 BD   |".split('|')
        data = self.parser.row_to_dict(row)
        self.assertAlmostEqual(data['min_magnitude'], 1.05)
