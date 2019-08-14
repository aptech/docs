
rndGeo
==============================================

Purpose
----------------

Computes geometric pseudo-random numbers with a choice of underlying random number generator.

Format
----------------
.. function:: { y, newstate } = rndGeo(r, c, prob[, state])

    :param r: row dimension.
    :type r: scalar

    :param c: column dimension.
    :type c: scalar

    :param prob: scalar or matrix ExE conformatble with *r* and *c* columns
    :type prob: scalar or matrix

    :param state: Optional argument.

        **scalar case**
        
            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **opaque vector case**
        
            *state* = the state vector returned from a previous call to one of the rnd random number functions.

    :type state: scalar or opaque vector

    :returns: y (*RxC matrix*) of geometrically distributed random numbers.

    :returns: newstate (*Opaque vector*), the updated state.

Remarks
-------

The properties of the pseudo-random numbers in *y* are:

.. DANGER:: fix equations

.. math::


   E(y) = (1 - prob)/prob;

   Var(y) = (1 - prob)/prob2

*r* and *c* will be truncated to integers if necessary.

.. seealso:: Functions :func:`rndCreateState`, :func:`rndStateSkip`

