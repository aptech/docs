
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

    :type xy: max(N,L) by max(K,M) complex matrix

Source
------

coord.src

