
dtvnormal
==============================================

Purpose
----------------

Normalizes a date and time (DTV) vector.

Format
----------------
.. function:: d = dtvnormal(t)

    :param t: 1x8 date and time vector that has one or more elements outside the normal range.
    :type t: matrix

    :return d: Normalized 1x8 date and time vector.

    :rtype d: 1x8 vector

Remarks
-------

The date and time vector is a 1x8 vector whose elements consist of:

+-----------------+-----------------------------------------------------+
|    Year         | Year, four digit integer.                           |
+-----------------+-----------------------------------------------------+
|    Month        | 1-12, Month in year.                                |
+-----------------+-----------------------------------------------------+
|    Day          | 1-31, Day of month.                                 |
+-----------------+-----------------------------------------------------+
|    Hour         | 0-23, Hours since midnight.                         |
+-----------------+-----------------------------------------------------+
|    Min          | 0-59, Minutes.                                      |
+-----------------+-----------------------------------------------------+
|    Sec          | 0-59, Seconds.                                      |
+-----------------+-----------------------------------------------------+
|    DoW          | 0-6, Day of week, 0 = Sunday.                       |
+-----------------+-----------------------------------------------------+
|    DiY          | 0-365, Days since Jan 1 of year.                    |
+-----------------+-----------------------------------------------------+

On input missing values are treated as zeros and the last two elements
are ignored.


Examples
----------------

::

    format /rd 4,0;

    dStart = { 2011 08 21 6 21 37 0 0 };
    mnth = { 0 1 0 0 0 0 0 0 };

    /*
    ** Add 6 months to 'dStart' which will give a 14 for the
    ** month
    */
    dEnd = dStart + 6*mnth;

    // Normalize the date vector
    dEnd2 = dtvnormal(dEnd);

After the code above:

::

    dEnd  = 2011   14   21    6   21   37    0    0
    dEnd2 = 2012    2   21    6   21   37    2   51

.. seealso:: Functions :func:`date`, :func:`ethsec`, :func:`etstr`, :func:`time`, :func:`timestr`, :func:`timeutc`, :func:`utctodtv`
