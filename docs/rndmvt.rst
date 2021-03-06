
rndMVt
==============================================

Purpose
----------------

Computes multivariate Student-t distributed random numbers given a covariance matrix.

Format
----------------
.. function:: r = rndMVt(num, cov, df)
              { r, newstate } = rndMVt(num, cov, df, state)

    :param num: number of random vectors to create.
    :type num: scalar

    :param cov: covariance matrix
    :type cov: NxN matrix

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

    // Degrees of freedom
    df = 8;

    // Covariance matrix
    sigma = {   1 0.3,
              0.3   1 };

    x = rndMVt(100, sigma, df);

Remarks
-------

The properties of the pseudo-random numbers in *x* are:

.. math::

   E(x) = 0\\

   Var(x) = \bigg(\frac{df}{df - 2}\bigg) * \sigma


.. seealso:: Functions :func:`rndMVn`, :func:`rndCreateState`
