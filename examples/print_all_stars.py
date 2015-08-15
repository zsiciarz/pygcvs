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
        for star in read_gcvs(gcvs_file):
            print(star)
