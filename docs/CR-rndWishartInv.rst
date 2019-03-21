
rndWishartInv
==============================================

Purpose
----------------
Computes the inverse Wishart distributed random numbers given a covariance matrix.

Format
----------------
.. function:: rndWishartInv(cov, df)

    :param cov: 
    :type cov: p x p positive definite covariance matrix

    :param df: degrees of freedom.
    :type df: Scalar

    :returns: y (*Matrix*), a random matrix from inverse Wishart distribution.

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

See also
++++++++

`rndWishart <CR-rndWishart.html#rndWishart>`__\,\ `rndMVn <CR-rndMVn.html#rndMVn>`__\,\ `rndCreateState <CR-rndCreateState.html#rndCreateState>`__

inverse Wishart pseudo-random random number generator
