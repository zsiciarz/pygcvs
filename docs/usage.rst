=====
Usage
=====

Basic usage
===========

The function :func:`~pygcvs.__init__.read_gcvs` is the main entry point to the
library. When called, it will return a generator yielding a single dictionary
at a time. The dictionary fields correspond to variable star attributes such
as name, location, min/max brightness, variability type etc.

The following fields are available:

``name``
    Variable star designation, such as *RR LYR*, *V838 MON* etc. The name
    is always normalized to upper case.

``ra``
    Right ascension of the variable star in J2000.0 epoch, eg. ``'20:50:12.7'``.

``dec``
    Declination of the variable star in J2000.0 epoch, eg. ``'+03:39:08'``.

.. note::

   The coordinates are returned as strings compatible with the popular
   `PyEphem <http://rhodesmill.org/pyephem/index.html>`_ astronomy package.
   For example, ``ra`` field can be passed directly to ``pyephem.hours``
   function.

``variable_type``
    Type of variability, for example *M* for Mira-like pulsating red giants.
    This value is literal as it appears in the GCVS, meaning that uncertain
    types contain `:` (a colon), etc.

``max_magnitude``
    Maximum brightness of a star as a floating point number. Can be `None` if
    unspecified in GCVS.

``min_magnitude``
    Brightness of the variable star at minimum, as a floating point number.
    `None` if unspecified in GCVS.

.. note::

   At the moment some special characters are stripped from both maximum and
   minimum magnitude. For example, if GCVS denotes the minimum brightness
   as <16.0 (fainter than 16.0), the value of ``min_magnitude`` will be 16.0
   and the *fainter than* information will be lost. However, if the field
   in GCVS represents an amplitude instead of minimum magnitude,
   ``min_magnitude`` field will contain a correctly calculated absolute value.

``epoch``
    Julian Day epoch of the maximum brightness as a float. `None` if the star
    is not periodic or there is no epoch data in GCVS.

``period``
    Variability period in days, or `None` if unspecified or not periodic.

PyEphem compatibility
=====================

If you have `PyEphem <http://rhodesmill.org/pyephem/index.html>`_ installed,
you can use the :func:`~pygcvs.__init__.dict_to_body` function to convert
star data to a `Body` instance more suitable for various astronomical
computations. See the example below, which checks if **TX Del** (a Type II
cepheid variable) is currently visible in Warsaw.`

.. literalinclude:: ../examples/check_visibility.py

Using GcvsParser directly
=========================

Most of the time, the :func:`~pygcvs.__init__.read_gcvs` function works just
fine. However, it's limited (on purpose!) to read GCVS data from a file on
disk. If you have the data in some other form, you can pass it directly
to the :class:`~pygcvs.parser.GcvsParser`, provided the data source supports
the iterator protocol.

For example, when using `requests <http://python-requests.org/>`_, the
response object has a ``iter_lines`` method which, well, iterates over the
lines of the response.

.. literalinclude:: ../examples/download_gcvs.py

Visualisations with matplotlib
==============================

You can use `matplotlib <http://matplotlib.org/>`_ to visualise various
aspects of GCVS variable star data.

Maximum vs minimum magnitude
----------------------------

.. literalinclude:: ../examples/plot_magnitudes.py

Brightness amplitude vs period
------------------------------

.. literalinclude:: ../examples/plot_amplitude_vs_period.py
