
utctodt
==============================================

Purpose
----------------
Converts UTC scalar format to DT scalar format.

Format
----------------
.. function:: utctodt(utc)

    :param utc: UTC scalar format.
    :type utc: Nx1 vector

    :returns: dt (*Nx1 vector*), DT scalar format.

Remarks
-------

A UTC scalar gives the number of seconds since or before January 1, 1970
Greenwich Mean Time. In DT scalar format, 08:35:52 on June 11, 2005 is
20050611083552.


Examples
----------------

::

    tc = 1346290409;
    print "tc = " tc;
    dt = utctodt(tc);
    print "dt = " dt;

::

    tc = 1346290409
    dt = 20120829183329

Source
------

time.src

.. seealso:: Functions :func:`dtvnormal`, :func:`timeutc`, :func:`utctodtv`, :func:`dttodtv`, :func:`dtvtodt`, :func:`dttoutc`, :func:`dtvtodt`, :func:`strtodt`, :func:`dttostr`
