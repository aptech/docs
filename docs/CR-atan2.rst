
atan2
==============================================

Purpose
----------------
Computes an angle from an x, y coordinate.

Format
----------------
.. function:: z = atan2(y, x)

    :param y: NxK matrix or P-dimensional array where the last two dimensions are NxK, the *y* coordinate.
    :type y: matrix

    :param x: LxM matrix or P-dimensional array where the last two dimensions are LxM, ExE conformable with *y*, the *x* coordinate.
    :type x: matrix

    :return z: max(N,L) by max(K,M) matrix or P-dimensional array where the last two dimensions are max(N,L) by max(K,M).

    :rtype z: matrix

Remarks
-------

Given a point *x*, *y* in a Cartesian coordinate system, :func:`atan2` will give the
correct angle with respect to the positive X axis. The answer will be in
radians from :math:`-π` to :math:`+π`.

To convert radians to degrees, multiply by :math:`180/π`.

:func:`atan2` operates only on the real component of *x*, even if *x* is complex.

Examples
----------------

::

    // Create the sequence -π, -π/2, 0, π/2, π
    x = seqa(-pi, pi/2, 5);
    y = 1;

    zpol = atan2(y, x);
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
