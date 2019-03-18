
rndGeo
==============================================

Purpose
----------------

Computes geometric pseudo-random numbers with a choice of underlying random number generator.

Format
----------------
.. function:: rndGeo(r, c, prob)

    :param r: row dimension.
    :type r: Scalar

    :param c: column dimension.
    :type c: Scalar

    :param prob: Scalar or matrix: ExE conformatble with r and c columns.
    :type prob: TODO

    :param state: Optional argument - scalar or opaque vector.
        Scalar case:state = starting seed value. If -1, GAUSS
        computes the starting seed based on the system clock.
        
        Opaque vector case:state = the state vector returned from a previous
        call to one of the rnd random number generators.
    :type state: TODO

    :returns: y (*TODO*), r x c matrix of geometrically distributed random numbers.

    :returns: newstate (*Opaque vector*), the updated state.

