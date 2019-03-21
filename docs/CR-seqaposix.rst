
seqaPosix
==============================================

Purpose
----------------
Creates a sequence of dates in Posix date/time format.
		

Format
----------------
.. function:: seqaPosix(dt_start, inc, unit, n)

    :param dt_start: containing the starting date in Posix date/time format (seconds since Jan 1, 1970).
    :type dt_start: Scalar

    :param inc: the number of units for each of the n increments.
    :type inc: Scalar

    :param unit: indicating the units for the increments in inc.
        
        Valid unit options:"years""months""days""hours""seconds"
    :type unit: String

    :param n: the number of elements to create.
    :type n: Scalar

    :returns: dt_vec (*nx1 vector*), starting at  dt_start and increasing by inc units.

Examples
----------------

::

    // Jan 20, 1980
    dt_start = strcToPosix("01/20/1980", "%m/%d/%Y");
    
    // Create a sequence of 10 dates separated by 4 years
    dt_vec = seqaPosix(dt_start, 4, "years", 10);

The above code will set dt_vec equal to:

::

    317174400
     443404800
     569635200
     695865600
     822096000
     948326400
    1074556800
    1200787200
    1327017600
    1453248000

::

    // March 17, 2003 at 05:30:00
    dt_start = strcToPosix("March 17, 2003 05:30:00", "%B %d, %Y %H:%M:%S");
    
    // Create a sequence of 6 dates separated by 30 minutes
    dt_vec = seqaPosix(dt_start, 30, "minutes", 6);

The above code will set dt_vec equal to:

::

    1047879000
    1047880800
    1047882600
    1047884400
    1047886200
    1047888000

.. seealso:: Functions :func:`timeDeltaDT`, :func:`timeDiffDT`, :func:`seqaDT`, :func:`timeDiffPosix`
