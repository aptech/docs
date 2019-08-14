
dtvtoutc
==============================================

Purpose
----------------

Converts DTV vector format to UTC scalar format.

Format
----------------
.. function:: utc = dtvtoutc(dtv)

    :param dtv: DTV vector format.
    :type dtv: Nx8 matrix

    :return utc: UTC scalar format.

    :type utc: Nx1 vector

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

    // Create a 1x8 DTV vector equal
    // to January 1, 1970 00:00:00
    dtv = { 1970 01 01 0 0 0 0 0 };

    // Convert to number of seconds since
    // January 1, 1970 GMT 
    utc = dtvtoutc(dtv);

If the code above is run from a computer set to American Mountain Standard Time (UTC-7), then *utc* will equal

::

    utc = 25200

This is because the input, *dtv*, is assumed to represent the local time, while the output is GMT. As the clock turned to 00:00:00 January 1, 1970 MST, GMT was seven hours ahead (7 * 60 * 60 = 25,200). 

.. seealso:: Functions :func:`dtvnormal`, :func:`timeutc`, :func:`utctodt`, :func:`dttodtv`, :func:`dttoutc`, :func:`dtvtodt`, :func:`dtvtoutc`, :func:`strtodt`, :func:`dttostr`
