
datestr
==============================================

Purpose
----------------
Returns a date in a string.

Format
----------------
.. function:: datestr(d)

    :param d: like the date function returns. If
        this is 0, the date function will be called for
        the current system date.
    :type d: 4x1 vector

    :returns: str (*TODO*), 8 character string containing current date in the form: mo/dy/yr

Examples
----------------

::

    d = { 2015, 10, 09, 0 };
    y = datestr(d);
    print y;

produces the following output:

::

    10/09/15

Source
------

time.src

.. seealso:: Functions :func:`date`, :func:`datestring`, :func:`datestrymd`, :func:`time`, :func:`timestr`, :func:`ethsec`
