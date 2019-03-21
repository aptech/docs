
rndKMp
==============================================

Purpose
----------------
Computes Poisson pseudo-random numbers.

Format
----------------
.. function:: rndKMp(r, c, lambda, state)

    :param r: number of rows of resulting matrix.
    :type r: scalar

    :param c: number of columns of resulting matrix.
    :type c: scalar

    :param lambda: or
        r x 1 vector, or 1 x c vector,
        or scalar, shape argument for Poisson distribution.
    :type lambda: r x c matrix

    :param state: 
        Scalar case:state = starting seed value only. If -1, GAUSS
        computes the starting seed based on the system clock.
        
        500x1 vector case:state = the state vector returned from a previous
        call to one of the rndKM random number functions.
    :type state: scalar or 500x1 vector

    :returns: x (*r x c matrix*), Poisson
        distributed random numbers.

    :returns: newstate (*500x1 vector*), the updated state.



Remarks
-------

The properties of the pseudo-random numbers in x are:

::

   E(x) =  lambdaVar(x) =  lambdax  =  0, 1,....lambda  >  0

r and c will be truncated to integers if necessary.



Source
------

randkm.src

