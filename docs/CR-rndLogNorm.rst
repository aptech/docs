
rndLogNorm
==============================================

Purpose
----------------

Computes lognormal pseudo-random numbers with the choice of underlying random number generator.

Format
----------------
.. function:: rndLogNorm(r, c, mu, sigma, state) 
			  rndLogNorm(r, c, mu, sigma)

    :param r: number of rows of resulting matrix.
    :type r: Scalar

    :param c: number of columns of resulting matrix.
    :type c: Scalar

    :param mu: or
        rx1 vector, or 1xc vector,
        or scalar, mean.
    :type mu: r x c matrix

    :param sigma: or
        rx1 vector, or 1xc vector,
        or scalar, standard deviation.
    :type sigma: r x c matrix

    :param state: 
        Scalar case:state = starting seed value only. If -1, GAUSS
        computes the starting seed based on the system clock.
        
        Opaque vector case:state = the state vector returned from a previous
        call to one of the rnd random number functions.
    :type state: Optional argument - scalar or opaque vector

    :returns: x (*r x c matrix*), lognormal
        distributed random numbers.

    :returns: newstate (*Opaque vector*), the updated state.

