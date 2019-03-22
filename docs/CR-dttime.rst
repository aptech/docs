
dttime
==============================================

Purpose
----------------

Creates a matrix in DT scalar format containing only the hour, minute and second. The date information is zeroed out.

Format
----------------
.. function:: dttime(hour, minute, second)

    :param hour: 0-23.
    :type hour: NxK matrix of hours

    :param minute: 0-59.
    :type minute: NxK matrix of minutes

    :param second: 0-59.
    :type second: NxK matrix of seconds

    :returns: dt (*NxK matrix*) of DT scalar format times.



Remarks
-------

The arguments must be ExE conformable.



Source
------

time.src

.. seealso:: Functions :func:`dtday`, :func:`dtdate`, :func:`utctodt`, :func:`dttostr`
