
dtvtodt
==============================================

Purpose
----------------
Converts DT vector format to DT scalar format.

Format
----------------
.. function:: dt = dtvtodt(dtv)

    :param dtv: DTV vector format.
    :type dtv: Nx8 matrix

    :return dt: DT scalar format.

    :rtype dt: Nx1 vector

Remarks
-------

In DT scalar format, 11:06:47 on March 15, 2012 is 20120315110647.

Each row of dtv, in DTV vector format, contains:

+-----------------+-----------------------------------------------------+
|    [N,1]        | Year                                                |
+-----------------+-----------------------------------------------------+
|    [N,2]        | Month in Year, 1-12                                 |
+-----------------+-----------------------------------------------------+
|    [N,3]        | Day of month, 1-31                                  |
+-----------------+-----------------------------------------------------+
|    [N,4]        | Hours since midnight, 0-23                          |
+-----------------+-----------------------------------------------------+
|    [N,5]        | Minutes, 0-59                                       |
+-----------------+-----------------------------------------------------+
|    [N,6]        | Seconds, 0-59                                       |
+-----------------+-----------------------------------------------------+
|    [N,7]        | Day of week, 0-6, 0 = Sunday                        |
+-----------------+-----------------------------------------------------+
|    [N,8]        | Days since Jan 1 of current year, 0-365             |
+-----------------+-----------------------------------------------------+


Examples
----------------

::

    dtv = { 2012 9 16 11 7 22 1 84 };
    dt = dtvtodt(dtv);

The code above assigns *dt* as follows:

::

    20120916110722

Source
------

time.src

.. seealso:: Functions :func:`dtvnormal`, :func:`timeutc`, :func:`utctodtv`, :func:`dttodtv`, :func:`dttoutc`, :func:`strtodt`, :func:`dttostr`
