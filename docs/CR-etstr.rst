
etstr
==============================================

Purpose
----------------

Formats an elapsed time measured in hundredths of a second to a string.

Format
----------------
.. function:: str = etstr(tothsecs)

    :param tothsecs: an elapsed time measured in hundredths of a second, as given, for instance, by the
        :func:`ethsec` function.
    :type tothsecs: scalar

    :return str: containing the elapsed time in the form:

        .. csv-table::
            :widths: auto

            "# days", "# hours", "# minutes", "#,## seconds"

    :type str: string

Examples
----------------

::

    // Set start time
    t_start = { 2012, 1, 2, 0 };

    // Set end time
    t_end = { 2012, 1, 14, 815642 };

    // Find elapsed time in hundredths of secs
    tothsecs = ethsec(t_start, t_end);

    // Convert elapsed time to string format
    str = etstr(tothsecs);

    print "tothsecs   = " tothsecs;
    print "str = " str;

Output:

::

    tothsecs   = 104495642.000
    str = 12 days  2 hours  15 minutes  56.42 seconds

Source
------

time.src

.. seealso:: Functions :func:`ethsec`
