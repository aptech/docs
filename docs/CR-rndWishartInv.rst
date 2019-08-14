
rndWishartInv
==============================================

Purpose
----------------
Computes the inverse Wishart distributed random numbers given a covariance matrix.

Format
----------------
.. function:: y = rndWishartInv(cov, df)

    :param cov: p x p positive definite covariance matrix
    :type cov: matrix

    :param df: degrees of freedom.
    :type df: scalar

    :returns: y (*matrix*), a random matrix from inverse Wishart distribution.

Examples
----------------

::

    rndseed 223; 
    cov = {1 .5,
           .5 1};				
    df = 10;
    
    // A random matrix from inverse Wishart distribution
    y = rndWishartInv(cov, df);	
    
    print y;

After above code,

::

    0.081211791      0.036818644 
    0.036818644      0.097064472

.. seealso:: :func:`rndWishart`, :func:`rndMVn`, :func:`rndCreateState`

