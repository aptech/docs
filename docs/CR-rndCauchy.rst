
rndCauchy
==============================================

Purpose
----------------

Computes Cauchy random numbers with a choice of underlying random number generator.

Format
----------------
.. function:: rndCauchy(rows, cols, location, scale, state) 
			  rndCauchy(rows, cols, location, scale)

    :param rows: number of rows of resulting matrix.
    :type rows: Scalar

    :param cols: number of columns of resulting matrix.
    :type cols: Scalar

    :param location: 
    :type location: Scalar or ExE conformable matrix with rows and cols

    :param scale: 
    :type scale: Scalar or ExE conformable matrix with rows and cols

    :param state: 
        Scalar case:state = starting seed value only. If -1, GAUSS
        computes the starting seed based on the system clock.Opaque vector case:state = the state vector returned from a previous
        call to one of the standard random number functions.
    :type state: Optional argument - scalar or opaque vector

    :returns: r (*rows x  cols matrix*), Cauchy distributed random numbers.

    :returns: newstate (*Opaque vector*), the updated state.



Remarks
-------

The properties of the pseudo-random numbers in x are:

::

   E(x) = undefined
   Var(x) = undefined
   Median(x) = location

r and c will be truncated to integers if necessary.

