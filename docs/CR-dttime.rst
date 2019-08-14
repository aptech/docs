
dttime
==============================================

Purpose
----------------

Creates a matrix in DT scalar format containing only the hour, minute and second. The date information is zeroed out.

Format
----------------
.. function:: dt = dttime(hour, minute, second)

    :param hour: Hours. :math:`0 \leq hour \leq 23`.
    :type hour: NxK matrix

    :param minute: Minutes. :math:`0 \leq minute \leq 59`.
    :type minute: NxK matrix

    :param second: Seconds. :math:`0 \leq second \leq 59`.
    :type second: NxK matrix

    :returns: **dt** (*NxK matrix*) - DT scalar format times.

Remarks
-------

The arguments must be ExE conformable.

Examples
----------------

::

    hour = 11;
    minute = 27;
    seconds = 56;

    dttime(hour, minute, seconds);

After the above code:

::

    112756


Source
------

time.src

.. seealso:: Functions :func:`dtday`, :func:`dtdate`, :func:`utctodt`, :func:`dttostr`
