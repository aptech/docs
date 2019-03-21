
arccos
==============================================

Purpose
----------------
Computes the inverse cosine.

Format
----------------
.. function:: arccos(x)

    :param x: 
    :type x: NxK matrix or N-dimensional array

    :returns: y (*NxK matrix or N-dimensional array*), containing the angle in radians whose cosine is *x*.

Remarks
-------

If *x* is complex or has any elements whose absolute value is greater than
1, complex results are returned.

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

Source
------------

trig.src


