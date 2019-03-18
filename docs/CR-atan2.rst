
atan2
==============================================

Purpose
----------------
Computes an angle from an x, y coordinate.

Format
----------------
.. function:: atan2(y, x)

    :param y: NxK matrix or P-dimensional array where the last two dimensions are NxK, the y coordinate.
    :type y: TODO

    :param x: LxM matrix or P-dimensional array where the last two dimensions are LxM, ExE conformable with y, the x coordinate.
    :type x: TODO

    :returns: z (*TODO*), max(N,L) by max(K,M) matrix or P-dimensional array where the last two dimensions are max(N,L) by max(K,M).

Examples
----------------

::

    //Create the sequence -π, -π/2, 0, π/2, π
    x = seqa(-pi, pi/2, 5);
    y = 1;
    
    zpol = atan2(y,x);
    zdeg = zpol*(180/pi);
    print "x = " x;
    print "zpol = " zpol;
    print "zdeg = " zdeg;

After the code above:

::

    -3.142         2.833         162.343
       -1.571         2.575         147.518
    x = 0.000  zpol = 1.571  zdeg =  90.000
        1.571         0.567          32.482
        3.142         0.308          17.657

.. seealso:: Functions :func:`atan`, :func:`sin`, :func:`cos`, :func:`pi`, :func:`tan`, :func:`arcsin`, :func:`arccos`

arctan arctangent coordinate inverse tangent trigonometric
