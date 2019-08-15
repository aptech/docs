
timeDiffDT
==============================================

Purpose
----------------
Computes the difference between two dates in DT scalar format.
		

Format
----------------
.. function:: diff = timeDiffDT(dt_1, dt_2, units)

    :param dt_1: containing 1 or more DT scalars.
    :type dt_1: NxK matrix

    :param dt_2: the second date.
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

    // February 14, 1979 at 12:30:21
    dt_1 = 19790214123021;
    
    // February 14, 1979 at 18:30:21
    dt_2 = 19790214183021;
    
    // Compute the difference in terms of hours
    diff = timeDiffDT(dt_1, dt_2, "hours");

The above code will set *diff* equal to:

::

    -6

::

    // April 15, 1947 19:30:00
    dt_1 = 194704151930;
    
    // April 15, 1947 07:53:00
    dt_2 = 194704150753;
    
    // Increment by 18 months
    diff = timeDiffDT(dt_1, dt_2, "minutes");

The above code will set *diff* equal to:

::

    697

::

    // December 31, 2000 at 22:59:00
    // December 31, 2000 at 23:59:00
    dt_1 = { 20001231225900, 20001231235900 };
    
    // January 1, 2001 at 02:13:00
    dt_2 =   20010101021300;
    
    // Find the time difference between the dates
    diff = timeDiffDT(dt_1, dt_2, "minutes");

The above code will set *diff* equal to:

::

    -194
    -134

.. seealso:: Functions :func:`timeDeltaPosix`, :func:`seqadt`, :func:`seqaposix`

