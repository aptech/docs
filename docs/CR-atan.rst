
atan
==============================================

Purpose
----------------
Returns the arctangent of its argument.

Format
----------------
.. function:: atan(x)

    :param x:
    :type x: NxK matrix or N-dimensional array

    :returns: y (*NxK matrix or N-dimensional array*), containing the arctangents of *x* in
        radians.

Remarks
-------

*y* will be the same size as *x*, containing the arctangents of the
corresponding elements of *x*.

For real *x*, the arctangent of *x* is the angle whose tangent is *x*. The
result is a value in radians in the range :math:`-π/2` to :math:`+π/2`. To convert
radians to degrees, multiply by :math:`180/π`.

For complex *x*, the arctangent is defined everywhere except *i* and *-i*. If
*x* is complex, *y* will be complex.

Examples
----------------

::

    /*
    ** Create a sequence with 5 elements starting at -pi and
    ** increasing by pi/2
    */
    x = seqa(-pi, pi/2, 5);
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
