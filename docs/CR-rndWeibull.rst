
rndWeibull
==============================================

Purpose
----------------

Computes Weibull pseudo-random numbers with the choice of underlying random number generator.

Format
----------------
.. function:: { x, newstate } = rndWeibull(r, c, shape[, scale])

    :param r: number of rows of resulting matrix.
    :type r: scalar

    :param c: number of columns of resulting matrix.
    :type c: scalar

    :param shape: r x c matrix or rx1 vector, or 1xc vector, or scalar, shape parameter.
    :type shape: matrix or vector or scalar

    :param scale: r x c matrix or rx1 vector, or 1xc vector, or scalar, scale parameter.
    :type scale: matrix or vector or scalar

    :param state: Optional argument.

        **scalar case**
        
            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **opaque vector case**
        
            *state* = the state vector returned from a previous call to one of the rnd random number functions.

    :type state: scalar or opaque vector

    :return x: Weibull distributed random numbers.

    :rtype x: RxC matrix

    :return newstate: the updated state.

    :rtype newstate: Opaque vector

Remarks
-------

The properties of the pseudo-random numbers in *x* are:

.. DANGER:: fix equations

.. math::

   E(x) = scale * gamma(1 + 1/shape)

   Var(x) = scale2*( gamma(1 + 2/shape) - (gamma(1 + 1/shape))2 )

*r* and *c* will be truncated to integers if necessary.

.. seealso:: Functions :func:`rndCreateState`, :func:`rndStateSkip`

