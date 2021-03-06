
datestring
==============================================

Purpose
----------------
Returns a date in a string with a 4-digit year.

Format
----------------
.. function:: str = datestring(d)

    :param d: A date in a 4-element column vector, in the order: year, month, day, and hundredths of a second since midnight. Same format as the :func:`date` function return. If this is 0, the :func:`date` function will be called for the current system date.
    :type d: 4x1 vector

    :return str: 10 character string containing current date in
        the form: ``mm/dd/yyyy``

    :rtype str: string

Examples
----------------

::

    // Date
    dt = { 2015, 12, 18, 0 };

    // Convert to the mm/dd/yyyy format
    y = datestring(dt);
    print y;

produces the following output:

::

    12/18/2015

Remarks
-------

To create date strings with more formatting options, see :func:`dttostr`, :func:`dttostrc` and :func:`posixtostrc`.

Source
------

time.src

.. seealso:: Functions :func:`date`, :func:`datestr`, :func:`datestrymd`, :func:`time`, :func:`timestr`, :func:`ethsec`
