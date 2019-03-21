
rndMVt
==============================================

Purpose
----------------

Computes multivariate Student-t distributed random numbers given a covariance matrix.

Format
----------------
.. function:: rndMVt(num, cov, df, state) 
			  rndMVt(num, cov, df)

    :param num: number of random vectors to create.
    :type num: Scalar

    :param cov: 
    :type cov: NxN covariance matrix

    :param df: degrees of freedom.
    :type df: Scalar

    :param state: 
        Scalar case:state = starting seed value only. If -1, GAUSS
        computes the starting seed based on the system clock.
        
        Opaque vector case:state = the state vector returned from a previous
        call to one of the rnd random number functions.
    :type state: Optional argument - scalar or opaque vector

    :returns: r (*num x N matrix*), multivariate student-t distributed random numbers.

    :returns: newstate (*Opaque vector*), the updated state.

Remarks
-------

The properties of the pseudo-random numbers in x are:

::

   E(x) = 0
   Var(x) = (df/(df - 2)) * sigma


Examples
----------------

::

    //degrees of freedom
    df = 8;
    
    //covariance matrix
    sigma = {   1 0.3,
              0.3   1 };
    
    x = rndMVt(100, sigma, df);

.. seealso:: Functions :func:`rndMVn`, :func:`rndCreateState`

multivariate student t random number covariance matrix
