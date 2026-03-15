
topolar
==============================================

Purpose
----------------
Converts from Cartesian to polar coordinates. 

Format
----------------
.. function:: { r, theta } = topolar(xy)

    :param xy: NxK complex matrix containing the *x* coordinate in the real part and the *y* coordinate in the imaginary part
    :type xy: complex matrix
        
    :return r: radius.

    :rtype r: NxK real matrix

    :return theta: angle in radians.

    :rtype theta: NxK real matrix

Examples
----------------

::

    // Create a Cartesian point (x=3, y=4)
    // as a complex number
    xy = complex(3, 4);

    { r, theta } = topolar(xy);
    print r;
    print theta;

The code above produces the following output:

::

    5.0000000
    0.92729522

Source
------

coord.src

.. seealso:: Functions :func:`tocart`
