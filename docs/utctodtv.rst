
utctodtv
==============================================

Purpose
----------------
Converts UTC scalar format to DTV vector format.

Format
----------------
.. function:: dtv = utctodtv(utc)

    :param utc: UTC scalar format.
    :type utc: Nx1 vector

    :return dtv: DTV vector format.

    :rtype dtv: Nx8 matrix

Examples
----------------

::

    // Set 'tc' equal to the number of seconds since January 1,
    // 1970
    tc = timeutc;
    print "tc = " tc;
    
    dtv = utctodtv(tc);
    print "dtv = " dtv;

produces:

::

    tc = 1340315529
    dtv = 2012 6 21 14 52 9 4 172

Remarks
-------

A UTC scalar gives the number of seconds since or before January 1, 1970
Greenwich Mean Time.

Each row of dtv, in DTV vector format, contains:

+-------------------+------------------------------------------+
| :math`[N,1]`      | Year, four digit integer.                |
+-------------------+------------------------------------------+
| :math`[N,2]`      | Month in Year, 1-12.                     |
+-------------------+------------------------------------------+
| :math`[N,3]`      | Day of month, 1-31.                      |
+-------------------+------------------------------------------+
| :math`[N,4]`      | Hours since midnight, 0-23.              |
+-------------------+------------------------------------------+
| :math`[N,5]`      | Minutes, 0-59.                           |
+-------------------+------------------------------------------+
| :math`[N,6]`      | Seconds, 0-59.                           |
+-------------------+------------------------------------------+
| :math`[N,7]`      | Day of week, 0-6, 0=Sunday.              |
+-------------------+------------------------------------------+
| :math`[N,8]`      | Days since Jan 1 of current year, 0-365. |
+-------------------+------------------------------------------+


.. seealso:: Functions :func:`dtvnormal`, :func:`timeutc`, :func:`utctodt`, :func:`dttodtv`, :func:`dttoutc`, :func:`dtvtodt`, :func:`dtvtoutc`, :func:`strtodt`, :func:`dttostr`

