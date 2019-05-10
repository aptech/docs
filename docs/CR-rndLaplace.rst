
rndLaplace
==============================================

Purpose
----------------

Computes Laplacian pseudo-random numbers with the choice of underlying random number generator.

Format
----------------
.. function:: rndLaplace(r, c, loc, scale[, state])

    :param r: number of rows of resulting matrix.
    :type r: scalar

    :param c: number of columns of resulting matrix.
    :type c: scalar

    :param loc: r x c matrix or rx1 vector, or 1xc vector, or scalar, location parameter.
    :type loc: matrix or vector or scalar

    :param scale: r x c matrix or rx1 vector, or 1xc vector, or scalar, scale parameter.
    :type scale: matrix or vector or scalar

    :param state: Optional argument.

        **scalar case**
        
            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **opaque vector case**
        
            *state* = the state vector returned from a previous call to one of the rnd random number functions.

    :type state: scalar or opaque vector

    :returns: x (*RxC matrix*), Laplacian distributed random numbers.

    :returns: newstate (*Opaque vector*), the updated state.

Remarks
-------

The properties of the pseudo-random numbers in *x* are:

.. DANGER:: fix equations

.. math::

   E(x) = location

   Var(x) = 2*scale2

*r* and *c* will be truncated to integers if necessary.

.. seealso:: Functions :func:`rndCreateState`, :func:`rndStateSkip`

