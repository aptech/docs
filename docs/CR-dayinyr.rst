
dayinyr
==============================================

Purpose
----------------
Returns day number in the year of a given date.

Format
----------------
.. function:: dayinyr(dt)

    :param dt: date to check. The date should be in the form returned by :func:`date`.
    :type dt: 3x1 or 4x1 vector

    :returns: daynum (*scalar*), the day number of that date in that year.

Examples
----------------

::

    x = { 1973, 8, 31, 0 };
    y = dayinyr(x);
    print y;

produces:

::

    y = 243.00000

Source
------

time.src

Globals
+++++++

`_isleap`

