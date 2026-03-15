
tocart
==============================================

Purpose
----------------

Converts from polar to Cartesian coordinates.

Format
----------------
.. function:: xy = tocart(r, theta)

    :param r: radius.data
    :type r: NxK real matrix

    :param theta: ExE conformable with *r*, angle in radians.
    :type theta: LxM real matrix

    :return xy: containing
        the *x* coordinate in the real part and the *y*
        coordinate in the imaginary part.

    :rtype xy: max(N,L) by max(K,M) complex matrix

Examples
----------------

::

    // Convert polar coordinates (r=5, theta=pi/4)
    // to Cartesian coordinates
    r = 5;
    theta = pi / 4;
    xy = tocart(r, theta);
    print xy;

The code above produces the following output:

::

    3.5355339 + 3.5355339i

The real part is the *x* coordinate and the imaginary part is the *y* coordinate.

Source
------

coord.src

