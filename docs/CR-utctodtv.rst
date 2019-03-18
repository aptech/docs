
utctodtv
==============================================

Purpose
----------------
Converts UTC scalar format to DTV vector format.

Format
----------------
.. function:: utctodtv(utc)

    :param utc: UTC scalar format.
    :type utc: Nx1 vector

    :returns: dtv (*Nx8 matrix*), DTV vector format.

Examples
----------------

::

    //Set 'tc' equal to the number of seconds since January 1,
    //1970
    tc = timeutc;
    print "tc = " tc;
    
    dtv = utctodtv(tc);
    print "dtv = " dtv;

produces:

::

    tc = 1340315529
    dtv = 2012 6 21 14 52 9 4 172

.. seealso:: Functions :func:`dtvnormal`, :func:`timeutc`, :func:`utctodt`, :func:`dttodtv`, :func:`dttoutc`, :func:`dtvtodt`, :func:`dtvtoutc`, :func:`strtodt`, :func:`dttostr`
