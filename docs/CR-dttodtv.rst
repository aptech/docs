
dttodtv
==============================================

Purpose
----------------

Converts DT scalar format to DTV vector format.

Format
----------------
.. function:: dtv = dttodtv(dt)

    :param dt: DT scalar format.
    :type dt: Nx1 vector

    :return dtv: DTV vector format.

    :type dtv: Nx8 matrix

Remarks
-------

In DT scalar format, 15:10:55 on July 3, 2005 is 20050703151055.

Each row of *dtv*, in DTV vector format, contains:

+-----------------+-----------------------------------------------------+
| [N,1]           | Year                                                |
+-----------------+-----------------------------------------------------+
| [N,2]           | Month in Year, 1-12                                 |
+-----------------+-----------------------------------------------------+
| [N,3]           | Day of month, 1-31                                  |
+-----------------+-----------------------------------------------------+
| [N,4]           | Hours since midnight, 0-23                          |
+-----------------+-----------------------------------------------------+
| [N,5]           | Minutes, 0-59                                       |
+-----------------+-----------------------------------------------------+
| [N,6]           | Seconds, 0-59                                       |
+-----------------+-----------------------------------------------------+
| [N,7]           | Day of week, 0-6, 0 = Sunday                        |
+-----------------+-----------------------------------------------------+
| [N,8]           | Days since Jan 1 of current year, 0-365             |
+-----------------+-----------------------------------------------------+


Examples
----------------

::

    dt = 20100326110722;
    print "dt = " dt;

::

    20100326110722

::

    // Convert dt to dtv
    dtv = dttodtv(dt);
    print "dtv = " dtv;

::

    2010 3 26 11 7 22 5 84

Source
------

time.src

.. seealso:: Functions :func:`dtvnormal`, :func:`timeutc`, :func:`utctodtv`, :func:`dtvtodt`, :func:`dttoutc`, :func:`dtvtodt`, :func:`strtodt`, :func:`dttostr`
