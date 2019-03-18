
rndKMvm
==============================================

Purpose
----------------

Computes von Mises pseudo-random numbers.

Format
----------------
.. function:: rndKMvm(r, c,  m,  k, state)

    :param r: number of rows of resulting matrix.
    :type r: scalar

    :param c: number of columns of resulting matrix.
    :type c: scalar

    :param m: or
        rx1 vector, or 1xc vector,
        or scalar, means for vm distribution.
    :type m: r x c matrix

    :param k: or
        rx1 vector, or 1xc vector,
        or scalar, shape argument for vm distribution.
    :type k: r x c matrix

    :param state: scalar or 500x1 vector.
        Scalar case:state = starting seed value only. If -1, GAUSS
        computes the starting seed based on the system clock.
        
        500x1 vector case:state = the state vector returned from a previous
        call to one of the rndKM random number functions.
    :type state: TODO

    :returns: x (*r x c matrix*), von Mises
        distributed random numbers.

    :returns: newstate (*500x1 vector*), the updated state.

