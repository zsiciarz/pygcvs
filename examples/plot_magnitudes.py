"""
Visualisation of maximum/minimum magnitude for GCVS stars.
"""

import sys

import matplotlib.pyplot as plot

from pygcvs import read_gcvs


if __name__ == '__main__':
    try:
        gcvs_file = sys.argv[1]
    except IndexError:
        print('Usage: python plot_magnitudes.py <path to iii.dat>')
    else:
        min_magnitudes = []
        max_magnitudes = []
        for star in read_gcvs(gcvs_file):
            if star['min_magnitude'] and star['max_magnitude']:
                min_magnitudes.append(star['min_magnitude'])
                max_magnitudes.append(star['max_magnitude'])
        plot.title('GCVS variable star magnitudes')
        plot.plot(min_magnitudes, max_magnitudes, 'ro')
        plot.xlabel('Min magnitude')
        plot.ylabel('Max magnitude')
        # invert axes because brightest stars have lowest magnitude value
        plot.gca().invert_xaxis()
        plot.gca().invert_yaxis()
        plot.show()
