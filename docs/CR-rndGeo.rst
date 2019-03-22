
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

    :param prob: 
    :type prob: Scalar or matrix: ExE conformatble with r and c columns

    :param state: 
        Scalar case:state = starting seed value. If -1, GAUSS
        computes the starting seed based on the system clock.
        
        Opaque vector case:state = the state vector returned from a previous
        call to one of the rnd random number generators.
    :type state: Optional argument - scalar or opaque vector

    :returns: y (*r x c matrix*) of geometrically distributed random numbers.

    :returns: newstate (*Opaque vector*), the updated state.



Remarks
-------

The properties of the pseudo-random numbers in y are:

::


   E(y) = (1 - prob)/prob;

   Var(y) = (1 - prob)/prob2

r and c will be truncated to integers if necessary.

.. seealso:: Functions :func:`rndCreateState`, :func:`rndStateSkip`
