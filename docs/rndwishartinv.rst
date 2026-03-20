
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

    :return y: a random matrix from inverse Wishart distribution.

    :rtype y: matrix

Examples
----------------

::

    // Set seed for repeatable output
    rndseed 12345;

    cov = { 1 .5,
           .5  1 };
    df = 10;

    // A random matrix from inverse Wishart distribution
    y = rndWishartInv(cov, df);

    print y;

After the code above, *y* is:

::

      0.12810680      0.058073486
     0.058073486       0.11794912

.. seealso:: :func:`rndWishart`, :func:`rndMVn`, :func:`rndCreateState`

