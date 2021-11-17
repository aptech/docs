
timeDeltaPosix
==============================================

Purpose
----------------
Adds (or subtracts) time to (from) a date-time.

Format
----------------
.. function:: t_inc = timeDeltaPosix(dt_start, inc, unit)

    :param dt_start: contains 1 more dates as a string array, dates, or in POSIX date/time format (seconds since Jan 1, 1970).

          If using strings, valid formats include:

          - ``"YYYY-MM-DD HH:MI:SS"``
          - ``"YYYY-MM-DD HH:MI"``
          - ``"YYYY-MM-DD HH"``
          - ``"YYYY-MM-DD"``
          - ``"YYYY-MM"``
          - ``"YYYY"``

    :type dt_start: NxK string array, dataframe, or matrix

    :param inc: the number of units to increment *dt_start*.
    :type inc: scalar

    :param unit: indicating the units for the increments in *inc*.

        Valid unit options:

        - ``"years"``
        - ``"months"``
        - ``"days"``
        - ``"hours"``
        - ``"seconds"``

    :type unit: string

    :return t_inc: *dt_start*, increased by *inc* units, in same date format as *dt_start*.
    :rtype t_inc: NxK dataframe or matrix

Examples
----------------

::

    // January 1, 1970 at 00:00:00
    dt_start = "1970-01-01";

    // Increment by 15 years
    dt_inc = timeDeltaPosix(dt_start, 15, "years");

The above code will set *dt_inc* equal to:

::

    1985-01-01

::

    // January 1, 1985 11:30:00
    dt_start = "1985-01-01 11:30:00";

    // Increment by 9 hours
    dt_inc = timeDeltaPosix(dt_start, 9, "hours");

The above code will set *dt_inc* equal to:

::

    1985-01-01 20:30:00

::

    // January 1, 1985 at 09:00:00
    // January 1, 1985 at 11:00:00
    dt_start = "1985-01-01 09:00:00"$|"1985-01-01 11:00:00";

    // Increment by 45 seconds
    dt_inc = timeDeltaPosix(dt_start, 45, "seconds");

The above code will set *dt_inc* equal to:

::

  1985-01-01 09:00:45
  1985-01-01 11:00:45

.. seealso:: Functions :func:`timeDeltaDT`, :func:`seqadt`, :func:`seqaposix`, :func:`timediffPosix`, :func:`timediffDT`
