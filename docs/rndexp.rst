
rndExp
==============================================

Purpose
----------------

Computes exponentially distributed random numbers with a choice of underlying random number generator.

Format
----------------
.. function:: x = rndExp(r, c, scale)
              { x, newstate } = rndExp(r, c, scale, state)

    :param r: number of rows of resulting matrix.
    :type r: scalar

    :param c: number of columns of resulting matrix.
    :type c: scalar

    :param scale: scalar or matrix that is ExE conformable with the dimensions of the output. The scale parameter sometimes called :math:`\beta`
    :type scale: scalar or matrix

    :param state: Optional argument.

        **scalar case**

            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **opaque vector case**

        *state* = the state vector returned from a previous call to one of the ``rnd`` random number functions.

    :type state: scalar or opaque vector

    :return x: exponentially distributed random numbers.

    :rtype x: RxC matrix

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

Examples
----------------

::

    // Set seed for repeatable output
    rndseed 12345;

    // Generate a 3x2 matrix of exponential
    // random numbers with scale = 2
    x = rndExp(3, 2, 2);
    print x;

After the code above, *x* is:

::

      0.19999741        1.6175607
      0.54211710        4.0899319
       1.3480216        5.5601364

.. seealso:: Functions :func:`rndCreateState`, :func:`rndStateSkip`
