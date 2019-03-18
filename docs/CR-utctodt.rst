
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
++++++

time.src

.. seealso:: Functions :func:`dtvnormal`, :func:`timeutc`, :func:`utctodtv`, :func:`dttodtv`, :func:`dtvtodt`, :func:`dttoutc`, :func:`dtvtodt`, :func:`strtodt`, :func:`dttostr`
