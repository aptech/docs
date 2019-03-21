
timeDeltaDT
==============================================

Purpose
----------------
Adds (or subtracts) time to a DT scalar.
		

Format
----------------
.. function:: timeDeltaDT(dt_start, inc, unit)

    :param dt_start: containing 1 or more DT scalars.
    :type dt_start: NxK matrix

    :param inc: the number of units to increment dt_start.
    :type inc: Scalar

    :param unit: indicating the units for the increments in inc.
        
        
        Valid unit options:
        
        "years"
        "months"
        "days"
        "hours"
        "seconds"
    :type unit: String

    :returns: t_inc (*Scalar*), dt_start, increased by inc units.

Examples
----------------

::

    // March 17, 1954 at 04:30:21
    dt_start = 19540317043021;
    
    // Increment by 60 years
    dt_inc = timeDeltaDT(dt_start, 60, "years");

The above code will set dt_inc equal to:

::

    20140317043021

::

    // March 17, 2003 at 05:29:12
    dt_start = 20030317052912;
    
    // Increment by 18 months
    dt_inc = timeDeltaDT(dt_start, 18, "months");

The above code will set dt_inc equal to:

::

    20040917052912

::

    // December 31, 1999 at 23:59:00
    // December 31, 2000 at 23:59:00
    dt_start = { 19991231235900, 20001231235900 };
    
    // Increment by 1 minute
    dt_inc_1 = timeDeltaDT(dt_start, 1, "minutes");
    
    // Increment by 60 seconds
    dt_inc_2 = timeDeltaDT(dt_start, 60, "seconds");

The above code will set dt_inc_1 and dt_inc_2 equal to:

::

    20000101000000
    20010101000000

.. seealso:: Functions :func:`timeDeltaPosix`, :func:`seqadt`, :func:`seqaposix`, :func:`timediffPosix`, :func:`timediffDT`
