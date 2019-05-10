
rndMVt
==============================================

Purpose
----------------

Computes multivariate Student-t distributed random numbers given a covariance matrix.

Format
----------------
.. function:: rndMVt(num, cov, df[, state])

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
        
            *state* = the state vector returned from a previous call to one of the rnd random number functions.

    :type state: scalar or opaque vector

    :returns: r (*num x N matrix*), multivariate student-t distributed random numbers.

    :returns: newstate (*Opaque vector*), the updated state.

Remarks
-------

The properties of the pseudo-random numbers in *x* are:

.. DANGER:: fix equations

.. math::

   E(x) = 0

   Var(x) = (df/(df - 2)) * sigma


Examples
----------------

::

    // degrees of freedom
    df = 8;
    
    // covariance matrix
    sigma = {   1 0.3,
              0.3   1 };
    
    x = rndMVt(100, sigma, df);

.. seealso:: Functions :func:`rndMVn`, :func:`rndCreateState`

