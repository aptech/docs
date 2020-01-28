
datestr
==============================================

Purpose
----------------
Returns a date in a string.

Format
----------------
.. function:: str = datestr(d)

    :param d: like the :func:`date` function returns. If this is 0, the :func:`date` function will be called for
        the current system date.
    :type d: 4x1 vector

    :return str: 8 character string containing current date in the form: ``mo/dy/yr``

    :rtype str: string

Examples
----------------

::

    // Date
    d = { 2015, 10, 09, 0 };

    // Convert to mo/dy/yr format
    y = datestr(d);
    print y;

produces the following output:

::

    10/09/15

Remarks
-------

To create date strings with more formatting options, see :func:`dttostr`, :func:`dttostrc` and :func:`posixtostrc`.

Source
------

time.src

.. seealso:: Functions :func:`date`, :func:`datestring`, :func:`datestrymd`, :func:`time`, :func:`timestr`, :func:`ethsec`
