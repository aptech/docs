
datestrymd
==============================================

Purpose
----------------

Returns a date in a string in the form ``yyyymmdd``.

Format
----------------
.. function:: datestrymd(d)

    :param d: A date in a 4-element column vector, in the order: year, month, day, and hundredths of a second since midnight. Same format as the :func:`date` function return. If this is 0, the :func:`date` function will be called for the current system date.
    :type d: 4x1 vector

    :returns: **str** (*string*) - 8 character string containing current date in
        the form: ``yyyymmdd``

Examples
----------------

::

    // Date
    d = { 2015, 10, 16 };

    // Convert date to the yyyymmdd format
    y = datestrymd(d);
    print y;

returns:

::

    20151016

Remarks
------

To create date strings with more formatting options, see :func:`dttostr`, :func:`dttostrc` and :func:`posixtostrc`.

Source
------

time.src

.. seealso:: Functions :func:`date`, :func:`datestr`, :func:`datestring`, :func:`time`, :func:`timestr`, :func:`ethsec`
