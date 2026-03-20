
rndMVn
==============================================

Purpose
----------------

Computes multivariate normal random numbers given a covariance matrix.

Format
----------------
.. function:: r = rndMVn(num, mu, cov)
              { r, newstate } = rndMVn(num, mu, cov, state)

    :param num: number of random vectors to create.
    :type num: Scalar

    :param mu: mean vector.
    :type mu: Nx1 matrix

    :param cov: covariance matrix
    :type cov: NxN matrix

    :param state: Optional argument.

        **scalar case**

            *state* = starting seed value only. If -1, GAUSS computes the starting seed based on the system clock.

        **opaque vector case**

        *state* = the state vector returned from a previous call to one of the ``rnd`` random number functions.

    :type state: scalar or opaque vector

    :return r: multivariate normal random numbers.

    :rtype r: numxN matrix

    :return newstate: the updated state.

    :rtype newstate: Opaque vector

Examples
----------------

::

    // Set seed for repeatable output
    rndseed 12345;

    // covariance matrix
    cov = { 1 0.3,
          0.3   1 };

    // mean for each column of 'cov'
    mu = { 0, 0 };

    x = rndMVn(100, mu, cov);
    print (meanc(x));

::

    -0.024045422
   -0.0015723702

The column means are both close to zero, the expected value for each dimension.

Remarks
-------

The properties of the pseudo-random numbers in *x* are:

.. math::

   E(x) = mu\\

   Var(x) = cov


.. seealso:: Functions :func:`rndCreateState`, :func:`rndStateSkip`
