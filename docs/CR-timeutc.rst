
timeutc
==============================================

Purpose
----------------

Returns the number of seconds since January 1, 1970 Greenwich Mean Time.

Format
----------------
.. function:: tc = timeutc

    :returns: tc (*scalar*), number of seconds since January 1, 1970 Greenwich Mean Time.

Examples
----------------

::

    // Retrieve seconds since January 1, 1970 GMT
    tc = timeutc;
    
    // Convert to a date time vector
    utv = utctodtv(tc);

After the code above, *tc* and *utv* are equal to:

::

    tc = 1340080112
    
    utv = 2012 06 18 21 28 32 1 169

.. seealso:: Functions :func:`dtvnormal`, :func:`utctodtv`

