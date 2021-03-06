
arccos
==============================================

Purpose
----------------
Computes the inverse cosine.

Format
----------------
.. function:: y = arccos(x)

    :param x: 
    :type x: NxK matrix or N-dimensional array

    :return y: containing the angle in radians whose cosine is *x*.

    :rtype y: NxK matrix or N-dimensional array

Examples
----------------

::

    /*
    ** Format print statements to show 3 digits
    ** after the decimal point
    */
    format /rd 6,3;
    
    x = { -1, -0.5, 0, 0.5, 1 };
    y = arccos(x);
    
    print "x = " x;
    print "y = " y;

The code above, produces the following output:

::

    x =
        -1.000
        -0.500
         0.000
         0.500
         1.000
    y =
         3.142
         2.094
         1.571
         1.047
         0.000

Remarks
-------

If *x* is complex or has any elements whose absolute value is greater than
1, complex results are returned.

Source
------------

trig.src


