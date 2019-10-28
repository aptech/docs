
rndGamma
==============================================

Purpose
----------------

Computes gamma pseudo-random numbers with a choice of underlying random number generator.

Format
----------------
.. function:: x = rndGamma(r, c, shape, scale)
              { x, newstate } = rndGamma(r, c, shape, scale, state)

    :param r: number of rows of resulting matrix.
    :type r: scalar

    :param c: number of columns of resulting matrix.
    :type c: scalar

    :param shape: *shape* argument for gamma distribution, scalar or ExE conformable matrix with *r* and *c*.
    :type shape: matrix or vector or scalar

    :param scale: *scale* argument for gamma distribution, scalar or ExE conformable matrix with *r* and *c*.
    :type scale: matrix or vector or scalar

    :param state: Optional argument.

        **scalar case**

            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **opaque vector case**

        *state* = the state vector returned from a previous call to one of the ``rnd`` random number functions.

    :type state: scalar or opaque vector

    :return x: gamma distributed random numbers.

    :rtype x: RxC matrix

    :return newstate: the updated state.

    :rtype newstate: Opaque vector

Examples
----------------

Example 1
+++++++++

::

    num_rows = 5;
    num_cols = 1;
    shape = 3;
    scale = 2;

    x = rndGamma(num_rows, num_cols, shape, scale);

Example 2
+++++++++

The gamma distribution is sometimes described in terms of a shape parameter and an inverse
*scale* parameter, called the *rate* parameter. The *rate* parameter is the reciprocal of the *scale* parameter.
With this parameterization, the random numbers will have the following properties:

.. math::

    E(x) = \frac{shape}{rate}\\

    Var(x) = \frac{shape}{rate^2}

If you prefer to think about the gamma distribution in these terms, then pass in the
reciprocal of the *rate* parameter as the fourth argument to :func:`rndGamma`.

::

    shape = 3;
    rate = 2;

    x = rndGamma(5, 1, shape, 1/rate);

Remarks
-------

The properties of the pseudo-random numbers in *x* are:

.. math::

   E(x) = shape*scale\\

   Var(x) = shape*scale^2\\

   x > 0\\

   shape > 0\\

   scale > 0


Technical Notes
---------------

The default generator for :func:`rndGamma` is the SFMT Mersenne-Twister 19937.
You can specify a different underlying random number generator with the
function :func:`rndCreateState`.

.. seealso:: Functions :func:`rndCreateState`, :func:`rndStateSkip`
