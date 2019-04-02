
dttime
==============================================

Purpose
----------------

Creates a matrix in DT scalar format containing only the hour, minute and second. The date information is zeroed out.

Format
----------------
.. function:: dttime(hour, minute, second)

    :param hour: NxK matrix of hours. 0-23.
    :type hour: matrix

    :param minute: NxK matrix of minutes. 0-59.
    :type minute: matrix

    :param second: NxK matrix of seconds. 0-59.
    :type second: matrix

    :returns: dt (*NxK matrix*) of DT scalar format times.

Remarks
-------

The arguments must be ExE conformable.

Source
------

time.src

.. seealso:: Functions :func:`dtday`, :func:`dtdate`, :func:`utctodt`, :func:`dttostr`

