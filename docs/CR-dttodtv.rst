
dttodtv
==============================================

Purpose
----------------

Converts DT scalar format to DTV vector format.

Format
----------------
.. function:: dttodtv(dt)

    :param dt: DT scalar format.
    :type dt: Nx1 vector

    :returns: dtv (*Nx8 matrix*), DTV vector format.

Examples
----------------

::

    dt = 20100326110722;
    print "dt = " dt;

::

    20100326110722

::

    dtv = dttodtv(dt);
    print "dtv = " dtv;

::

    2010 3 26 11 7 22 1 84

Source
++++++

time.src

.. seealso:: Functions :func:`dtvnormal`, :func:`timeutc`, :func:`utctodtv`, :func:`dtvtodt`, :func:`dttoutc`, :func:`dtvtodt`, :func:`strtodt`, :func:`dttostr`
