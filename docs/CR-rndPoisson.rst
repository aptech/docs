
rndPoisson
==============================================

Purpose
----------------

Computes Poisson pseudo-random numbers with a choice of underlying random number generator.

Format
----------------
.. function:: rndPoisson(r, c,  lambda)

    :param r: number of rows of resulting matrix.
    :type r: Scalar

    :param c: number of columns of resulting matrix.
    :type c: Scalar

    :param lambda: or
        rx1 vector, or 1xc vector,
        or scalar, mean parameter for Poisson distribution.
    :type lambda: r x c matrix

    :param state: scalar or opaque vector.
        Scalar case:state = starting seed value only. If -1, GAUSS
        computes the starting seed based on the system clock.
        
        Opaque vector case:state = the state vector returned from a previous
        call to one of the rndMT random number functions.
    :type state: Optional argument

    :returns: x (*r x c matrix*), Poisson
        distributed random numbers.

    :returns: newstate (*Opaque vector*), the updated state.

Examples
----------------
The example below simulates 100 observations of a Poisson process with a mean of 17.

::

    lambda = 17;
    
    x = rndPoisson(100, 1, lambda);

Technical Notes
+++++++++++++++

The default generator for rndPoisson is the SFMT Mersenne-Twister 19937.
You can specifiy a different underlying random number generator with the
function rndCreateState.

.. seealso:: Functions :func:`rndCreateState`, :func:`rndStateSkip`

poisson distribution pseudo-random number generator
