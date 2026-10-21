
rndMVt
==============================================

Purpose
----------------

Computes multivariate Student-t distributed random numbers given a scale matrix.

Format
----------------
.. function:: r = rndMVt(num, scale, df)
              { r, newstate } = rndMVt(num, scale, df, state)

    :param num: number of random vectors to create.
    :type num: scalar

    :param scale: scale matrix. It is not the covariance matrix: for :math:`df > 2` the draws have covariance :math:`df/(df-2)` times *scale*.
    :type scale: NxN matrix

    :param df: degrees of freedom.
    :type df: scalar

    :param state: Optional argument.

        **scalar case**

            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **opaque vector case**

            *state* = the state vector returned from a previous call to one of the ``rnd`` random number functions.

    :type state: scalar or opaque vector

    :return r: multivariate student-t distributed random numbers.

    :rtype r: num x N matrix

    :return newstate: the updated state.

    :rtype newstate: Opaque vector

Examples
----------------

::

    // Set seed for repeatable output
    rndseed 12345;

    // Degrees of freedom
    df = 8;

    // Scale matrix
    scale = {   1 0.3,
              0.3   1 };

    x = rndMVt(100, scale, df);
    print (meanc(x));

::

    -0.055890701
    -0.034103818

The column means are both close to zero, the expected value for a multivariate t-distribution.

Remarks
-------

The properties of the pseudo-random numbers in *x* are:

.. math::

   E(x) = 0\\

   Var(x) = \bigg(\frac{df}{df - 2}\bigg) * scale


.. seealso:: Functions :func:`rndMVn`, :func:`rndCreateState`
