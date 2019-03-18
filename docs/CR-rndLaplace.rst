
rndLaplace
==============================================

Purpose
----------------

Computes Laplacian pseudo-random numbers with the choice of underlying random number generator.

Format
----------------
.. function:: rndLaplace(r, c, loc, scale)

    :param r: number of rows of resulting matrix.
    :type r: Scalar

    :param c: number of columns of resulting matrix.
    :type c: Scalar

    :param loc: or
        rx1 vector, or 1xc vector,
        or scalar, location parameter.
    :type loc: r x c matrix

    :param scale: or
        rx1 vector, or 1xc vector,
        or scalar, scale parameter.
    :type scale: r x c matrix

    :param state: Optional argument - scalar or opaque vector.
        Scalar case:state = starting seed value only. If -1, GAUSS
        computes the starting seed based on the system clock.
        Opaque vector case:state = the state vector returned from a previous
        call to one of the rnd random number functions.
    :type state: TODO

    :returns: x (*r x c matrix*), Laplacian
        distributed random numbers.

    :returns: newstate (*Opaque vector*), the updated state.

