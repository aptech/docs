
rndExp
==============================================

Purpose
----------------

Computes exponentially distributed random numbers with a choice of underlying random number generator.

Format
----------------
.. function:: rndExp(rows, cols, scale[, state])

    :param rows: number of rows of resulting matrix.
    :type rows: scalar

    :param cols: number of columns of resulting matrix.
    :type cols: scalar

    :param scale: scalar or matrix that is ExE conformable with the dimensions of the output. The scale parameter sometimes called :math:`β`
    :type scale: scalar or matrix

    :param state: Optional argument.

        **scalar case**
        
            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **opaque vector case**
        
            *state* = the state vector returned from a previous call to one of the rnd random number functions.

    :type state: scalar or opaque vector

    :returns: r (*rows x cols matrix*), exponentially distributed random numbers.

    :returns: newstate (*Opaque vector*), the updated state.

Remarks
-------

The properties of the pseudo-random numbers in *x* are specified in terms
of the *scale* parameter sometimes called :math:`β`. This is the reciprocal of the
*rate* parameter which is sometimes called :math:`λ`:

.. DANGER:: fix equations

.. math::

   E(x) = scale = β = 1/rate = 1/λ
   Var(x) = scale2 = β2 = 1/rate2 = 1/λ2

.. seealso:: Functions :func:`rndCreateState`, :func:`rndStateSkip`

