
rndMVn
==============================================

Purpose
----------------

Computes multivariate normal random numbers given a covariance matrix.

Format
----------------
.. function:: rndMVn(num, mu, cov, state) 
			  rndMVn(num, mu, cov)

    :param num: number of random vectors to create.
    :type num: Scalar

    :param mu: mean vector.
    :type mu: Nx1 matrix

    :param cov: 
    :type cov: NxN covariance matrix

    :param state: 
        Scalar case:state = starting seed value only. If -1, GAUSS
        computes the starting seed based on the system clock.
        
        Opaque vector case:state = the state vector returned from a previous
        call to one of the rnd random number functions.
    :type state: Optional argument - scalar or opaque vector

    :returns: r (*numxN matrix*), multivariate normal random numbers.

    :returns: newstate (*Opaque vector*), the updated state.

Remarks
-------

The properties of the pseudo-random numbers in x are:

::

   E(x) = mu
   Var(x) = cov


Examples
----------------

::

    //covariance matrix
    cov = { 1 0.3,
          0.3   1 };
    
    //mean for each column of 'cov'
    mu = { 0, 0 };
    
    x = rndMVn(100, mu, cov);

.. seealso:: Functions :func:`rndCreateState`, :func:`rndStateSkip`

multivariate normal random number covariance matrix
