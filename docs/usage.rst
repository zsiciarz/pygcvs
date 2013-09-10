=====
Usage
=====

Using GcvsParser directly
=========================

Most of the time, the :func:`~pygcvs.__init__.read_gcvs` function works just
fine. However, it's limited (on purpose!) to read GCVS data from a file on
disk. If you have the data in some other form, you can pass it directly
to the :class:`~pygcvs.parser.GcvsParser`, provided the data source supports
the iterator protocol.

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
