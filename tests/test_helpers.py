import tempfile
import unittest

import ephem
from pygcvs.helpers import dict_to_body, read_gcvs


GCVS_CONTENTS = """
  NNo     GCVS         2000.0        Type        Max        Min I          Min II      Epoch         Year      Period          M-m       Spectrum      References  Other design
------------------ ---------------------------------------------------------------------------------------------------------------- -----------------------------------------
320031 |TX    Del *|205012.7+033908 |CWB:      |  8.84   |   9.54     |            |V |42947.009   |     |     6.165907       |33   |G0-G5            |08632 08953|
"""


class ReadGcvsTestCase(unittest.TestCase):
    def test_open_file(self):
        with tempfile.NamedTemporaryFile(mode='w') as f:
            f.write(GCVS_CONTENTS)
            f.seek(0)
            stars = read_gcvs(f.name)
            star = next(stars)
            self.assertEqual(star['name'], 'TX DEL')


class DictToBodyTestCase(unittest.TestCase):
    def setUp(self):
        self.star = {
            'name': 'TX DEL',
            'ra': '20:50:12.7',
            'dec': '+03:39:08',
        }

    def test_basics(self):
        body = dict_to_body(self.star)
        self.assertIsInstance(body, ephem.FixedBody)
        self.assertEqual(body.name, 'TX DEL')
