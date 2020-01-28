
timediffposix
==============================================

Purpose
----------------
Computes the difference between two dates in POSIX date/time format.

Format
----------------
.. function:: diff = timediffposix(dt_1, dt_2, units)

    :param dt_1: containing 1 or more date/times in POSIX format.
    :type dt_1: NxK matrix

    :param dt_2: the second date in POSIX format.
    :type dt_2: scalar

    :param units: indicating the units in which to report the difference.
        
        Valid unit options:
        
        - "days"
        - "hours"
        - "minutes"
        - "seconds"

    :type units: string

    :return diff: the difference between *dt_1* and *dt_2* in terms of the specified units.

    :rtype diff: Scalar

Examples
----------------

::

    // Create dates from string for readability
    dt_1 = strctoposix("February 14, 1979 19:30:21","%B %d, %Y %H:%M:%S");
    dt_2 = strctoposix("February 14, 1979 14:30:21", "%B %d, %Y %H:%M:%S");
    
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

    // Dates as seconds since Jan 1, 1970
    dt_1 = { 3490181, 3490101 };
    dt_2 =   3490000;
    
    // Find the time difference between the dates
    diff = timediffposix(dt_1, dt_2, "seconds");

The above code will set *diff* equal to:

::

    181
    101

.. seealso:: Functions :func:`timeDiffDT`, :func:`timeDeltaPosix`, :func:`seqadt`, :func:`seqaposix`

