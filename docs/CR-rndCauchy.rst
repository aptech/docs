
rndCauchy
==============================================

Purpose
----------------

Computes Cauchy random numbers with a choice of underlying random number generator.

Format
----------------
.. function:: r = rndCauchy(rows, cols, location, scale)
              { r, newstate } = rndCauchy(rows, cols, location, scale, state)

    :param rows: number of rows of resulting matrix.
    :type rows: scalar

    :param cols: number of columns of resulting matrix.
    :type cols: scalar

    :param location: scalar or ExE conformable matrix with rows and cols
    :type location: scalar or matrix

    :param scale: scalar or ExE conformable matrix with rows and cols
    :type scale: scalar or matrix

    :param state: Optional argument.

        **scalar case**
        
            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **opaque vector case**
        
            *state* = the state vector returned from a previous call to one of the rnd random number functions.

    :type state: scalar or opaque vector

    :return r: Cauchy distributed random numbers.

    :rtype r: rows x cols matrix

    :return newstate: the updated state.

    :rtype newstate: Opaque vector

Remarks
-------

The properties of the pseudo-random numbers in *x* are:

.. DANGER:: fix equations

.. math::

   E(x) = undefined
   Var(x) = undefined
   Median(x) = location

*r* and *c* will be truncated to integers if necessary.

.. seealso:: Functions :func:`rndCreateState`, :func:`rndStateSkip`

