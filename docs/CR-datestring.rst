
datestring
==============================================

Purpose
----------------
Returns a date in a string with a 4-digit year.

Format
----------------
.. function:: datestring(d)

    :param d: like the date function returns. If this is 0, the date function will be called for
        the current system date.
    :type d: 4x1 vector

    :returns: str (*TODO*), 10 character string containing current date in
        the form: mm/dd/yyyy

Examples
----------------

::

    dt = { 2015, 12, 18, 0 };
    y = datestring(dt);
    print y;

produces the following output:

::

    12/18/2015

Source
++++++

time.src

.. seealso:: Functions :func:`date`, :func:`datestr`, :func:`datestrymd`, :func:`time`, :func:`timestr`, :func:`ethsec`
