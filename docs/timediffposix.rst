
timediffposix
==============================================

Purpose
----------------
Computes the difference between two dates in POSIX date/time format.

Format
----------------
.. function:: diff = timediffposix(dt_1, dt_2, units)

    :param dt_1: contains 1 more dates as a string array, dates, or in POSIX date/time format (seconds since Jan 1, 1970).

          If string, valid formats include:

          - ``"YYYY-MM-DD HH:MI:SS"``
          - ``"YYYY-MM-DD HH:MI"``
          - ``"YYYY-MM-DD HH"``
          - ``"YYYY-MM-DD"``
          - ``"YYYY-MM"``
          - ``"YYYY"``

    :type dt_1: NxK string array, dataframe, or matrix

    :param dt_2: contains 1 more dates as a string array, dates, or in POSIX date/time format. ExE conformable with *dt_1*.

          If string, valid formats include:

          - ``"YYYY-MM-DD HH:MI:SS"``
          - ``"YYYY-MM-DD HH:MI"``
          - ``"YYYY-MM-DD HH"``
          - ``"YYYY-MM-DD"``
          - ``"YYYY-MM"``
          - ``"YYYY"``

    :type dt_2: String array, dataframe, or matrix

    :param units: indicating the units in which to report the difference.

        Valid unit options:

        - ``"days"``
        - ``"hours"``
        - ``"minutes"``
        - ``"seconds"``

    :type units: string

    :return diff: the difference between *dt_1* and *dt_2* in terms of the specified units.
    :rtype diff: NxK matrix

Examples
----------------

::

    // Dates in YYYY-MM-DD HH:MM:SS format
    dt_1 = "1979-02-14 19:30:21";
    dt_2 = "1979-02-14 14:30:21";

    // Compute the difference in terms of hours
    diff = timediffposix(dt_1, dt_2, "hours");

The above code will set *diff* equal to:

::

    5

::

    // Dates as seconds since Jan 1, 1970
    dt_1 = -61446476430;
    dt_2 = -61446477127;

    // Calculate the difference
    diff = timediffposix(dt_1, dt_2, "minutes");

The above code will set *diff* equal to:

::

    11.617

::

    // Dates in YYYY-MM format
    dt_1 =  "2020-12"$|"2021-01"$|"2021-03";
    dt_2 =   "2020-04";

    // Find the time difference between the dates
    diff = timediffposix(dt_1, dt_2, "days");

The above code will set *diff* equal to:

::

    244
    275
    334

.. seealso:: Functions :func:`timeDiffDT`, :func:`timeDeltaPosix`, :func:`seqadt`, :func:`seqaposix`
