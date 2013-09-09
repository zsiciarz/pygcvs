from __future__ import unicode_literals, print_function

"""
A simple example of reading GCVS data.

Information for every star is printed on standard output.
"""

import sys

from pygcvs import read_gcvs


if __name__ == '__main__':
    try:
        gcvs_file = sys.argv[1]
    except IndexError:
        print('Usage: python print_all_stars.py <path to iii.dat>')
    else:
        with open(gcvs_file, 'rb') as fp:
            for star in read_gcvs(fp):
                print(star)
