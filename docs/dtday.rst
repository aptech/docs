
dtday
==============================================

Purpose
----------------

Creates a matrix in DT scalar format containing only the year, month and day. Time of day information is zeroed out.

Format
----------------
.. function:: dt = dtday(year, month, day)

    :param year: Years
    :type year: NxK matrix

    :param month: Months. :math:`1 \leq month \leq 12`.
    :type month: NxK matrix

    :param day: Days. :math:`1 \leq day \leq 31`.
    :type day: matrix

    :return dt: DT scalar format dates.

    :rtype dt: NxK matrix

Examples
----------------

::

    year = 2007;
    month = 9;
    day = 13;

    dtday(year, month, day);

After the above code:

::

    20070913000000


Remarks
-------

This amounts to 00:00:00 or midnight on the given day. The arguments must be ExE conformable.


Source
------

time.src

.. seealso:: Functions :func:`dttime`, :func:`dtdate`, :func:`utctodt`, :func:`dttostr`
