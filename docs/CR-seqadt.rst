
seqaDT
==============================================

Purpose
----------------
Creates a sequence of dates in DT scalar format.
		

Format
----------------
.. function:: seqaDT(dt_start, inc, unit, n)

    :param dt_start: containing a date/time in DT scalar format.
    :type dt_start: scalar

    :param inc: the number of units for each of the *n* increments.
    :type inc: scalar

    :param unit: indicating the units for the increments in *inc*.
        
        Valid unit options:
        
        - "years"
        - "months"
        - "days"
        - "hours"
        - "seconds"

    :type unit: string

    :param n: the number of elements to create.
    :type n: scalar

    :returns: dt_vec (*nx1 vector*), starting at *dt_start* and increasing by *inc* units.

Examples
----------------

::

    // Jan 20, 1980
    dt_start = 19800120;
    
    // Create a sequence of 10 dates separated by 4 years
    dt_vec = seqaDT(dt_start, 4, "years", 10);

The above code will set *dt_vec* equal to:

::

    19800120000000
    19840120000000
    19880120000000
    19920120000000
    19960120000000
    20000120000000
    20040120000000
    20080120000000
    20120120000000
    20160120000000

::

    // March 17, 2003 at 05:30:00
    dt_start = 20030317053000;
    
    // Create a sequence of 6 dates separated by 30 minutes
    dt_vec = seqaDT(dt_start, 30, "minutes", 6);

The above code will set *dt_vec* equal to:

::

    20030317053000
    20030317060000
    20030317063000
    20030317070000
    20030317073000
    20030317080000

.. seealso:: Functions :func:`timeDeltaDT`, :func:`timeDiffDT`, :func:`seqaPosix`, :func:`timeDiffPosix`

