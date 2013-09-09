import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pygcvs',
    version=__import__('pygcvs').__version__,
    description='A Python library for reading variable star data from GCVS.',
    long_description=read('README.rst'),
    author='Zbigniew Siciarz',
    author_email='zbigniew@siciarz.net',
    url='http://github.com/zsiciarz/pygcvs',
    download_url='http://pypi.python.org/pypi/pygcvs',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    tests_require=['nose'],
    test_suite='nose.collector',
    platforms='any',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Utilities'
    ],
)
