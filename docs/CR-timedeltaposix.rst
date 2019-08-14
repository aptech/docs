
timeDeltaPosix
==============================================

Purpose
----------------
Adds (or subtracts) time to a POSIX date-time.
		
Format
----------------
.. function:: t_inc = timeDeltaPosix(dt_start, inc, unit)

    :param dt_start: containing 1 or more dates in POSIX time format.
    :type dt_start: NxK matrix

    :param inc: the number of units to increment *dt_start*.
    :type inc: scalar

    :param unit: indicating the units for the increments in *inc*.
        
        Valid unit options:
        
        - "years"
        - "months"
        - "days"
        - "hours"
        - "seconds"

    :type unit: string

    :return t_inc: *dt_start*, increased by *inc* units.

    :type t_inc: Scalar

Examples
----------------

::

    // January 1, 1970 at 00:00:00
    dt_start = 0;
    
    // Increment by 15 years
    dt_inc = timeDeltaPosix(dt_start, 15, "years");

The above code will set *dt_inc* equal to:

::

    473385600

::

    // January 1, 1985 at 00:00:00
    dt_start = 473385600;
    
    // Increment by 9 hours
    dt_inc = timeDeltaPosix(dt_start, 9, "hours");

The above code will set *dt_inc* equal to:

::

    473418000

::

    // January 1, 1985 at 00:00:00
    // January 1, 1985 at 09:00:00
    dt_start = { 473385600, 473418000 };
    
    // Increment by 45 seconds
    dt_inc = timeDeltaPosix(dt_start, 45, "seconds");

The above code will set *dt_inc* equal to:

::

    473385645
    473418045

.. seealso:: Functions :func:`timeDeltaDT`, :func:`seqadt`, :func:`seqaposix`, :func:`timediffPosix`, :func:`timediffDT`

