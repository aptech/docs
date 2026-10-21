
rndWishartInv
==============================================

Purpose
----------------
Computes the inverse Wishart distributed random numbers given a scale matrix.

Format
----------------
.. function:: y = rndWishartInv(scale, df)

    :param scale: p x p positive definite scale matrix. It is not a covariance matrix: the draws average :math:`scale/(df - p - 1)` for :math:`df > p + 1`.
    :type scale: matrix

    :param df: degrees of freedom.
    :type df: scalar

    :return y: a random matrix from inverse Wishart distribution.

    :rtype y: matrix

Examples
----------------

::

    // Set seed for repeatable output
    rndseed 12345;

    scale = { 1 .5,
             .5  1 };
    df = 10;

    // A random matrix from inverse Wishart distribution
    y = rndWishartInv(scale, df);

    print y;

After the code above, *y* is:

::

      0.12810680      0.058073486
     0.058073486       0.11794912

.. seealso:: :func:`rndWishart`, :func:`rndMVn`, :func:`rndCreateState`

