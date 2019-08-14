
dtdate
==============================================

Purpose
----------------

Creates a matrix in DT scalar format.

Format
----------------
.. function:: dt = dtdate(year, month, day, hour, minute, second)

    :param year: Years
    :type year: NxK matrix

    :param month: Months. :math:`1 \leq month \leq 12`.
    :type month: NxK matrix

    :param day: Days. :math:`1 \leq day \leq 31`.
    :type day: NxK matrix

    :param hour: Hours. :math:`0 \leq hour \leq 23`.
    :type hour: NxK matrix

    :param minute: Minutes. :math:`0 \leq minutes \leq 59`.
    :type minute: NxK matrix

    :param second: Seconds. :math:`0 \leq seconds \leq 59`.
    :type second: NxK matrix

    :returns: **dt** (*NxK matrix*) - DT scalar format dates.



Remarks
-------

The arguments must be ExE conformable.


Examples
----------------

::

    year = 2012;
    month = 12;
    day = 21;
    hour = 11;
    minute = 27;
    seconds = 56;

    dtdate(year, month, day, hour, minute, seconds);

After the above code:

::
  
    20121221112756


Source
------

time.src

.. seealso:: Functions :func:`dtday`, :func:`dttime`, :func:`utctodt`, :func:`dttostr`, :func:`dayofweek`
