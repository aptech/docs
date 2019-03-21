
rndWishart
==============================================

Purpose
----------------

Computes Wishart distributed random numbers given a covariance matrix.

Format
----------------
.. function:: rndWishart(numMats, cov, df, state) 
			  rndWishart(numMats, cov, df)

    :param numMats: number of Wishart random matrices to create.
    :type numMats: Scalar

    :param cov: 
    :type cov: NxM covariance matrix

    :param df: degrees of freedom.
    :type df: Scalar

    :param state: 
        Scalar case:state = starting seed value only. If -1, GAUSS
        computes the starting seed based on the system clock.
        
        Opaque vector case:state = the state vector returned from a previous
        call to one of the rnd random number functions.
    :type state: Optional argument - scalar or opaque vector

    :returns: r (*TODO*), numMats * rows(cov) x N matrix, wishart random matrices.

    :returns: newstate (*Opaque vector*), the updated state.

Examples
----------------

::

    //covariance matrix
    cov = {  1   0.5,
           0.5     1 };
    
    //degrees of freedom
    df = 7;
    
    X = rndWishart(1, cov, df);

::

    X = 7.6019339 4.7744799 
        4.7744799 7.7341260

.. seealso:: Functions :func:`rndWishartInv`, :func:`rndMVn`, :func:`rndCreateState`

Wishart pseudo-random random number generator
