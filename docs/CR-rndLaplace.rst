
rndLaplace
==============================================

Purpose
----------------

Computes Laplacian pseudo-random numbers with the choice of underlying random number generator.

Format
----------------
.. function:: x = rndLaplace(r, c, loc, scale)
              { x, newstate } = rndLaplace(r, c, loc, scale, state)

    :param r: number of rows of resulting matrix.
    :type r: scalar

    :param c: number of columns of resulting matrix.
    :type c: scalar

    :param loc: location parameter, scalar or ExE conformable matrix with *r* and *c*.
    :type loc: matrix, vector or scalar

    :param scale: scalar or ExE conformable matrix with *r* and *c*.
    :type scale: matrix, vector or scalar

    :param state: Optional argument.

        **scalar case**

            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **opaque vector case**

        *state* = the state vector returned from a previous call to one of the ``rnd`` random number functions.

    :type state: scalar or opaque vector

    :return x: Laplacian distributed random numbers.

    :rtype x: RxC matrix

    :return newstate: the updated state.

    :rtype newstate: Opaque vector

Remarks
-------

The properties of the pseudo-random numbers in *x* are:

.. math::

   E(x) = location\\
   Var(x) = 2*scale^2

*r* and *c* will be truncated to integers if necessary.

.. seealso:: Functions :func:`rndCreateState`, :func:`rndStateSkip`
