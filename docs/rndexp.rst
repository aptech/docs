
rndExp
==============================================

Purpose
----------------

Computes exponentially distributed random numbers with a choice of underlying random number generator.

Format
----------------
.. function:: r = rndExp(rows, cols, scale)
              { r, newstate } = rndExp(rows, cols, scale, state)

    :param rows: number of rows of resulting matrix.
    :type rows: scalar

    :param cols: number of columns of resulting matrix.
    :type cols: scalar

    :param scale: scalar or matrix that is ExE conformable with the dimensions of the output. The scale parameter sometimes called :math:`\beta`
    :type scale: scalar or matrix

    :param state: Optional argument.

        **scalar case**

            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **opaque vector case**

        *state* = the state vector returned from a previous call to one of the ``rnd`` random number functions.

    :type state: scalar or opaque vector

    :return r: exponentially distributed random numbers.

    :rtype r: rows x cols matrix

    :return newstate: the updated state.

    :rtype newstate: Opaque vector

Remarks
-------

The properties of the pseudo-random numbers in *x* are specified in terms
of the *scale* parameter sometimes called :math:`\beta`. This is the reciprocal of the
*rate* parameter which is sometimes called :math:`\lambda`:

.. math::

   E(x) = scale = \beta = 1/rate = 1/\lambda\\
   Var(x) = scale^2 =\beta^2 = 1/rate^2 = 1/\lambda^2

.. seealso:: Functions :func:`rndCreateState`, :func:`rndStateSkip`
