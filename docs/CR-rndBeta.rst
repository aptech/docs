
rndBeta
==============================================

Purpose
----------------

Computes beta pseudo-random numbers with a choice of underlying random number generator.

Format
----------------
.. function:: rndBeta(r, c, a, b, state) 
			  rndBeta(r, c, a, b)

    :param r: number of rows of resulting matrix.
    :type r: Scalar

    :param c: number of columns of resulting matrix.
    :type c: Scalar

    :param a: or r x 1 vector, or 1 x c vector,
        or scalar, first shape argument for beta distribution.
    :type a: r x c matrix

    :param b: or r x 1 vector, or 1 x c vector,
        or scalar, second shape argument for beta distribution.
    :type b: r x c matrix

    :param state: Optional argument - scalar or opaque vector.
        Scalar case:state = starting seed value only. If -1, GAUSS
        computes the starting seed based on the system clock.Opaque vector case:state = the state vector returned from a previous
        call to one of the rnd random number functions.
    :type state: TODO

    :returns: x (*r x c matrix*), beta distributed random numbers.

    :returns: newstate (*Opaque vector*), the updated state.

Examples
----------------

This example illustrates basic usage of rndBeta, leaving the management of the random number state to GAUSS to handle internally.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    num_rows = 100;
    num_cols = 5;
    a = 3;
    b = 2;
    x = rndBeta(num_rows, num_cols, a, b);

//Starting seed for random number generator
seed = 235235;

//If a 'seed' or 'state' vector is passed in,
//then a state vector will be returned
{ x, newstate } = rndBeta(100, 5, 3, 2, seed);
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Technical Notes
+++++++++++++++

The default generator for rndBeta is the SFMT Mersenne-Twister 19937.
You can specifiy a different underlying random number generator with the
function rndCreateState.

.. seealso:: Functions :func:`rndCreateState`, :func:`rndStateSkip`

random number Beta distribution
