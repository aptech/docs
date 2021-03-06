
utctodt
==============================================

Purpose
----------------
Converts UTC scalar format to DT scalar format.

Format
----------------
.. function:: dt = utctodt(utc)

    :param utc: UTC scalar format.
    :type utc: Nx1 vector

    :return dt: DT scalar format.

    :rtype dt: Nx1 vector

Examples
----------------

::

    // Time in utc format
    tc = 1346290409;
    print "tc = " tc;

    // Convert tc to dt format
    dt = utctodt(tc);
    print "dt = " dt;

produces:

::

    tc = 1346290409
    dt = 20120829183329

Remarks
-------

A UTC scalar gives the number of seconds since or before January 1, 1970
Greenwich Mean Time. In DT scalar format, 08:35:52 on June 11, 2005 is
20050611083552.


Source
------

time.src

.. seealso:: Functions :func:`dtvnormal`, :func:`timeutc`, :func:`utctodtv`, :func:`dttodtv`, :func:`dtvtodt`, :func:`dttoutc`, :func:`dtvtodt`, :func:`strtodt`, :func:`dttostr`
