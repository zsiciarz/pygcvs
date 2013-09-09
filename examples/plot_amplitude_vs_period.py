from __future__ import unicode_literals, print_function

"""
Visualisation of brightness amplitude vs variability period.
"""

import sys

import matplotlib.pyplot as plot

from pygcvs import read_gcvs


if __name__ == '__main__':
    try:
        gcvs_file = sys.argv[1]
    except IndexError:
        print('Usage: python plot_amplitude_vs_period.py <path to iii.dat>')
    else:
        periods = []
        amplitudes = []
        with open(gcvs_file, 'rb') as fp:
            for star in read_gcvs(fp):
                if star['period'] and star['min_magnitude'] and star['max_magnitude']:
                    periods.append(star['period'])
                    amplitudes.append(star['min_magnitude'] - star['max_magnitude'])
        plot.title('GCVS variable stars amplitudes')
        plot.semilogx(periods, amplitudes, 'ro')
        plot.xlabel('Period [days]')
        plot.ylabel('Brightness amplitude [mag]')
        plot.show()
