
timestr
==============================================

Purpose
----------------

Formats a time in a vector to a string.

Format
----------------
.. function:: ts = timestr(t)

    :param t: 4x1 vector from the time function or a zero. If
        the input is 0, the :func:`time` function will be called
        to return the current system time.
    :type t: scalar or vector 

    :return ts: containing current time in the format: ``hr:mn:sc``

    :rtype ts: 8 character string

Examples
----------------

::

    t = { 7, 31, 46, 33 };
    ts = timestr(t);
    print ts;

::

    7:31:46

Source
------

time.src

.. seealso:: Functions :func:`date`, :func:`datestr`, :func:`datestring`, :func:`datestrymd`, :func:`ethsec`, :func:`etstr`, :func:`time`

