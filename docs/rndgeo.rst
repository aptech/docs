
rndGeo
==============================================

Purpose
----------------

Computes geometric pseudo-random numbers with a choice of underlying random number generator.

Format
----------------
.. function:: y = rndGeo(r, c, prob)
              { y, newstate } = rndGeo(r, c, prob, state)

    :param r: row dimension.
    :type r: scalar

    :param c: column dimension.
    :type c: scalar

    :param prob: probability parameter, scalar or matrix ExE conformable with *r* and *c* columns
    :type prob: scalar or matrix

    :param state: Optional argument.

        **scalar case**

            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **opaque vector case**

        *state* = the state vector returned from a previous call to one of the ``rnd`` random number functions.

    :type state: scalar or opaque vector

    :return y: of geometrically distributed random numbers.

    :rtype y: RxC matrix

    :return newstate: the updated state.

    :rtype newstate: Opaque vector

Remarks
-------

The properties of the pseudo-random numbers in *y* are:

.. math::


   E(y) = \frac{1 - prob}{prob}

   Var(y) = \frac{1 - prob}{prob^2}

*r* and *c* will be truncated to integers if necessary.

.. seealso:: Functions :func:`rndCreateState`, :func:`rndStateSkip`
