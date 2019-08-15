
rndBeta
==============================================

Purpose
----------------

Computes beta pseudo-random numbers with a choice of underlying random number generator.

Format
----------------
.. function:: { x, newstate } = rndBeta(r, c, a, b[, state])

    :param r: number of rows of resulting matrix.
    :type r: Scalar

    :param c: number of columns of resulting matrix.
    :type c: Scalar

    :param a: r x c matrix or r x 1 vector, or 1 x c vector, or scalar, first shape argument for beta distribution.
    :type a: matrix or vector or scalar

    :param b: r x c matrix or r x 1 vector, or 1 x c vector, or scalar, second shape argument for beta distribution.
    :type b: matrix or vector or scalar

    :param state: Optional argument.

        **scalar case**
        
            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **opaque vector case**
        
            *state* = the state vector returned from a previous call to one of the rnd random number functions.

    :type state: scalar or opaque vector

    :return x: beta distributed random numbers.

    :rtype x: RxC matrix

    :return newstate: the updated state.

    :rtype newstate: Opaque vector

Remarks
-------

The properties of the pseudo-random numbers in *x* are:

.. DANGER:: fix equations

.. math::

   E(x) = a/(a+b)

   Var(x) = a*b/((a+b+1)*(a+b)2)

   0 < x < 1
   a > 0
   b > 0

*r* and *c* will be truncated to integers if necessary.

Examples
----------------

Example 1
+++++++++

This example illustrates basic usage of :func:`rndBeta`, leaving the management of the random number state to GAUSS to handle internally.

::

    num_rows = 100;
    num_cols = 5;
    a = 3;
    b = 2;
    x = rndBeta(num_rows, num_cols, a, b);

Example 2
+++++++++

::

    //Starting seed for random number generator
    seed = 235235;
    
    //If a 'seed' or 'state' vector is passed in,
    //then a state vector will be returned
    { x, newstate } = rndBeta(100, 5, 3, 2, seed);

Technical Notes
------------

The default generator for :func:`rndBeta` is the SFMT Mersenne-Twister 19937. 
You can specifiy a different underlying random number generator with the function :func:`rndCreateState`.

.. seealso:: Functions :func:`rndCreateState`, :func:`rndStateSkip`

