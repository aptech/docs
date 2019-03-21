
tocart
==============================================

Purpose
----------------

Converts from polar to Cartesian coordinates.

Format
----------------
.. function:: tocart(r, theta)

    :param r: radius.
    :type r: NxK real matrix

    :param theta: ExE conformable with
        r, angle in radians.
    :type theta: LxM real matrix

    :returns: xy (*TODO*), max(N,L) by max(K,M) complex matrix containing
        the x coordinate in the real part and the y
        coordinate in the imaginary part.



Source
------

coord.src

