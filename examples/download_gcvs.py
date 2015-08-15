"""
An example of directly using the parser to read downloaded GCVS data.
"""

import requests

from pygcvs.parser import GcvsParser


if __name__ == '__main__':
    url = 'http://www.sai.msu.su/gcvs/gcvs/iii/iii.dat'
    response = requests.get(url, stream=True)
    parser = GcvsParser(response.iter_lines(decode_unicode=True))
    for star in parser:
        print(star)
