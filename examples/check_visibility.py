"""
Check if TX Del is visible in Warsaw at the moment.
"""

import sys
import ephem

from pygcvs import read_gcvs, dict_to_body


if __name__ == '__main__':
    try:
        gcvs_file = sys.argv[1]
    except IndexError:
        print('Usage: python check_visibility.py <path to iii.dat>')
    else:
        city = ephem.city('Warsaw')
        stars = {star['name']: star for star in read_gcvs(gcvs_file)}
        body = dict_to_body(stars['TX DEL'])
        body.compute(city)
        if body.alt > 0:
            print('TX Del is visible in Warsaw right now, go observe!')
        else:
            print('TX Del is not visible in Warsaw right now. Try later.')
