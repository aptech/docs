
dayinyr
==============================================

Purpose
----------------
Returns day number in the year of a given date.

Format
----------------
.. function:: daynum = dayinyr(dt)

    :param dt: A date in a 4-element column vector, in the order: year, month, day, and hundredths of a second since midnight. Same format as the :func:`date` function return.
    :type dt: 3x1 or 4x1 vector

    :returns: daynum (*scalar*) - the day number of that date in that year.

Examples
----------------

::
  
    // Date
    x = { 1973, 8, 31, 0 };

    // Find the day number of date
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
