
rndChiSquare
==============================================

Purpose
----------------

Creates pseudo-random numbers with a chi-squared distribution, with an optional non-centrality parameter and a choice of underlying random number generator.

Format
----------------
.. function:: x = rndChiSquare(r, c, df[, s_ncp])
              { x, newstate } = rndChiSquare(r, c, df, s_ncp, state)

    :param r: number of rows of resulting matrix.
    :type r: scalar

    :param c: number of columns of resulting matrix.
    :type c: scalar

    :param df: degrees of freedom.
    :type df: scalar

    :param s_ncp: Optional argument, non-centrality parameter.

        .. NOTE:: This is the square root of the noncentrality parameter that sometimes goes under the symbol :math:`\lambda`.

    :type s_ncp: scalar

    :param state: Optional argument.

        **scalar case**

            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **opaque vector case**

        *state* = the state vector returned from a previous call to one of the ``rnd`` random number functions.

    :type state: scalar or opaque vector

    :return x: chi-square distributed random numbers.

    :rtype x: RxC matrix

    :return newstate: the updated state.

    :rtype newstate: Opaque vector

Remarks
-------

The properties of the pseudo-random numbers in *x* are:

.. math::

   E(x) = k + \lambda\\

   \sigma^2(x) = 2*k + 4*\lambda

where:

.. math::

   k = df

   \lambda = s\_ncp^2

Technical Notes
--------------------

The default generator for :func:`rndChiSquare` is the SFMT Mersenne-Twister 19937.
You can specify a different underlying random number generator with the function :func:`rndCreateState`.

.. seealso:: Functions :func:`rndCreateState`, :func:`rndStateSkip`
