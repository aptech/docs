
dtvtoutc
==============================================

Purpose
----------------

Converts DTV vector format to UTC scalar format.

Format
----------------
.. function:: dtvtoutc(dtv)

    :param dtv: DTV vector format.
    :type dtv: Nx8 matrix

    :returns: **utc** (*Nx1 vector*) - UTC scalar format.

Remarks
-------

A UTC scalar gives the number of seconds since or before January 1, 1970
Greenwich Mean Time.

Each row of *dtv*, in DTV vector format, contains:

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

    dtv = utctodtv(timeutc);
    utc = dtvtoutc(dtv);

::

    dtv = 2019    6   28    0   24   10    5  178
    utc = 1561706650

.. seealso:: Functions :func:`dtvnormal`, :func:`timeutc`, :func:`utctodt`, :func:`dttodtv`, :func:`dttoutc`, :func:`dtvtodt`, :func:`dtvtoutc`, :func:`strtodt`, :func:`dttostr`
