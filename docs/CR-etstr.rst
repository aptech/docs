
etstr
==============================================

Purpose
----------------

Formats an elapsed time measured in hundredths of a second to a string.

Format
----------------
.. function:: etstr(tothsecs)

    :param tothsecs: an elapsed time measured in hundredths of a second, as given, for instance, by the
        ethsec function.
    :type tothsecs: scalar

    :returns: str (string), containing the elapsed time in the form:

    .. csv-table::
        :widths: auto

        "# days", "# hours", "# minutes", "#,## seconds"

Examples
----------------

::

    d1 = { 2012, 1, 2, 0 };
    d2 = { 2012, 1, 14, 815642 };
    t = ethsec(d1,d2);
    str = etstr(t);
    
    print "t   = " t;
    print "str = " str;

Output:

::

    t   = 104495642.000
    str = 12 days  2 hours  15 minutes  56.42 seconds

Source
------

time.src

.. seealso:: Functions :func:`ethsec`
