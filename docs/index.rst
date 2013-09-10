.. pygcvs documentation master file, created by
   sphinx-quickstart on Mon Sep 09 23:04:30 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

======
pygcvs
======

A Python library for reading variable star data from the
`General Catalog of Variable Stars <http://www.sai.msu.su/gcvs/gcvs/iii/html/>`_.

Installation
============

Installing **pygcvs** is easy, just use pip::

    pip install pygcvs

Usage
=====

Download the ``iii.dat`` file from `GCVS <http://www.sai.msu.su/gcvs/gcvs/iii/>`_
and point the :func:`~pygcvs.__init__.read_gcvs` function at its location.
The function returns a generator which yields a single star data dictionary
at a time. See below::

    >>> import pygcvs
    >>> for star in pygcvs.read_gcvs('iii.dat'):
    ...     print(star['name'])
    R AND
    S AND
    #...
    V0515 VUL
    V0516 VUL

See :doc:`usage` for description of dictionary fields and more usage examples.

Contents
========

.. toctree::
   :maxdepth: 4

   usage
   reference


License
=======

pygcvs is free software, licensed under the MIT/X11 License. A copy of
the license is provided with the source code in the LICENSE file.


Author
======

`Zbigniew Siciarz <http://siciarz.net>`_


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

