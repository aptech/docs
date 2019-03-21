
rndKMbeta
==============================================

Purpose
----------------
Computes beta pseudo-random numbers.

Format
----------------
.. function:: rndKMbeta(r, c, a, b, state)

    :param r: number of rows of resulting matrix.
    :type r: scalar

    :param c: number of columns of resulting matrix.
    :type c: scalar

    :param a: or
        rx1 vector, or 1xc vector,
        or scalar, first shape argument for beta distribution.
    :type a: r x c matrix

    :param b: or
        rx1 vector, or 1xc vector,
        or scalar, second shape argument for beta distribution.
    :type b: r x c matrix

    :param state: 
        Scalar case:state = starting seed value only. If -1, GAUSS
        computes the starting seed based on the system clock.
        
        500x1 vector case:state = the state vector returned from a previous
        call to one of the rndKM random number functions.
    :type state: scalar or 500x1 vector

    :returns: x (*r x c matrix*), beta
        distributed random numbers.

    :returns: newstate (*500x1 vector*), the updated state.



Remarks
-------

The properties of the pseudo-random numbers in x are:

::

   E(x) = a/(a+b)
   Var(x) = a*b/((a+b+1)*(a+b2)
   0 < x < 1a > 0b > 0

r and c will be truncated to integers if necessary.



Source
------

randkm.src

