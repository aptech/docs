
rndPoisson
==============================================

Purpose
----------------

Computes Poisson pseudo-random numbers with a choice of underlying random number generator.
*
Format
----------------
.. function:: x = rndPoisson(r, c, lambda)
              { x, newstate } = rndPoisson(r, c, lambda, state)

    :param r: number of rows of resulting matrix.
    :type r: scalar

    :param c: number of columns of resulting matrix.
    :type c: scalar

    :param lambda: r x c matrix or rx1 vector, or 1xc vector, or scalar, mean parameter for Poisson distribution.
    :type lambda: matrix or vector or scalar

    :param state: Optional argument.

        **scalar case**
        
            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **opaque vector case**
        
            *state* = the state vector returned from a previous call to one of the rnd random number functions.

    :type state: scalar or opaque vector

    :return x: Poisson distributed random numbers.

    :rtype x: r x c matrix

    :return newstate: the updated state.

    :rtype newstate: Opaque vector

Remarks
-------

The properties of the pseudo-random numbers in *x* are:

.. DANGER:: fix equations

.. math::

   E(x) = lambda

   Var(x) = lambda

*r* and *c* will be truncated to integers if necessary.

Examples
----------------
The example below simulates 100 observations of a Poisson process with a mean of 17.

::

    lambda = 17;
    
    x = rndPoisson(100, 1, lambda);

Technical Notes
----------------

The default generator for rndPoisson is the SFMT Mersenne-Twister 19937.
You can specifiy a different underlying random number generator with the
function rndCreateState.

.. seealso:: Functions :func:`rndCreateState`, :func:`rndStateSkip`

