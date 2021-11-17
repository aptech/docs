
seqaPosix
==============================================

Purpose
----------------
Creates a sequence of dates.

Format
----------------
.. function:: dt_vec = seqaPosix(dt_start, inc, unit, n)

    :param dt_start: contains the starting date as a string, date, or in POSIX date/time format (seconds since Jan 1, 1970).

      If string, valid formats include:

      - ``"YYYY-MM-DD HH:MI:SS"``
      - ``"YYYY-MM-DD HH:MI"``
      - ``"YYYY-MM-DD HH"``
      - ``"YYYY-MM-DD"``
      - ``"YYYY-MM"``
      - ``"YYYY"``

    :type dt_start: string or scalar

    :param inc: the number of units for each of the *n* increments.
    :type inc: scalar

    :param unit: indicating the units for the increments in *inc*.

        Valid unit options:

        - ``"years"``
        - ``"months"``
        - ``"days"``
        - ``"hours"``
        - ``"seconds"``

    :type unit: string

    :param n: the number of elements to create.
    :type n: scalar

    :return dt_vec: starting at *dt_start* and increasing by *inc* units. The *dt_vec* will be in same date format as *dt_start*.
    :rtype dt_vec: nx1 dataframe

Examples
----------------

::

    // Create a sequence of 10 dates separated by 4 years
    dt_vec = seqaPosix("1980-01-20", 4, "years", 10);

The above code will set *dt_vec* equal to:

::

   1980-01-20
   1984-01-20
   1988-01-20
   1992-01-20
   1996-01-20
   2000-01-20
   2004-01-20
   2008-01-20
   2012-01-20
   2016-01-20

::

    // Create a sequence of 6 dates separated by 30 minutes
    dt_vec = seqaPosix("March 17, 2003 05:30:00", 30, "minutes", 6);

The above code will set *dt_vec* equal to:

::

  2003-03-17 05:30:00
  2003-03-17 06:00:00
  2003-03-17 06:30:00
  2003-03-17 07:00:00
  2003-03-17 07:30:00
  2003-03-17 08:00:00

::

  // Jan 20, 1980
  dt_start = strcToPosix("01/20/1980", "%m/%d/%Y");

  // Create a sequence of 10 dates separated by 4 years
  dt_vec = seqaPosix(dt_start, 4, "years", 10);

In the above example, *dt_start* is:

::

  01/20/1980

This will set *dt_vec* equal to:

::

  01/20/1980
  01/20/1984
  01/20/1988
  01/20/1992
  01/20/1996
  01/20/2000
  01/20/2004
  01/20/2008
  01/20/2012
  01/20/2016


.. seealso:: Functions :func:`timeDeltaDT`, :func:`timeDiffDT`, :func:`seqaDT`, :func:`timeDiffPosix`
