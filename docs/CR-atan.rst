
atan
==============================================

Purpose
----------------
Returns the arctangent of its argument.

Format
----------------
.. function:: atan(x)

    :param x: NxK matrix or N-dimensional array.
    :type x: TODO

    :returns: y (*TODO*), NxK matrix or N-dimensional array containing the arctangents of x in
        radians.

Examples
----------------

::

    //Create a sequence with 5 elements starting at -pi and
    //increasing by pi/2
    x = seqa(-pi, pi/2, 5)
    y = atan(x);
    print "x = " x;
    print "y = " y;

After the code above:

::

    -3.142      -1.263
       -1.571      -1.004
    x = 0.000  y =  0.000
        1.571       1.004
        3.142       1.263

.. seealso:: Functions :func:`atan2`, :func:`sin`, :func:`cos`, :func:`pi`, :func:`tan`

arctan arctangent inverse tangent trigonometric
