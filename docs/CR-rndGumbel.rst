
rndGumbel
==============================================

Purpose
----------------

Computes Gumbel distributed random numbers with a choice of underlying random number generator.

Format
----------------
.. function:: rndGumbel(rows,  cols,  scale)

    :param rows: number of rows of resulting matrix.
    :type rows: Scalar

    :param cols: number of columns of resulting matrix.
    :type cols: Scalar

    :param location: Scalar or ExE conformable matrix with  rows and  cols.
    :type location: TODO

    :param scale: Scalar or ExE conformable matrix with  rows and  cols.
    :type scale: TODO

    :param state: Optional argument - scalar or opaque vector.
        Scalar case:state = starting seed value only. If -1, GAUSS
        computes the starting seed based on the system clock.
        
        Opaque vector case:state = the state vector returned from a previous
        call to one of the rnd random number functions.
    :type state: TODO

    :returns: r (*rows x cols matrix*), Gumbel distributed random numbers.

    :returns: newstate (*Opaque vector*), the updated state.

