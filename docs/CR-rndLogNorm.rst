
rndLogNorm
==============================================

Purpose
----------------

Computes lognormal pseudo-random numbers with the choice of underlying random number generator.

Format
----------------
.. function:: x = rndLogNorm(r, c, mu, sigma)
              { x, newstate } = rndLogNorm(r, c, mu, sigma, state)

    :param r: number of rows of resulting matrix.
    :type r: scalar

    :param c: number of columns of resulting matrix.
    :type c: scalar

    :param mu: r x c matrix or rx1 vector, or 1xc vector, or scalar, mean.
    :type mu: matrix or vector or scalar

    :param sigma: r x c matrix or rx1 vector, or 1xc vector, or scalar, standard deviation.
    :type sigma: matrix or vector or scalar

    :param state: Optional argument.

        **scalar case**
        
            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **opaque vector case**
        
            *state* = the state vector returned from a previous call to one of the rnd random number functions.

    :type state: scalar or opaque vector

    :return x: lognormal distributed random numbers.

    :rtype x: RxC matrix

    :return newstate: the updated state.

    :rtype newstate: Opaque vector

Remarks
-------

The properties of the pseudo-random numbers in *x* are:

.. DANGER:: fix equations

.. math::

   E(x) = exp(mu - 0.5*sigma2)

   Var(x) = (exp(sigma2) - 1) * exp(2*mu + sigma2)

*r* and *c* will be truncated to integers if necessary.

.. seealso:: Functions :func:`rndCreateState`, :func:`rndStateSkip`

