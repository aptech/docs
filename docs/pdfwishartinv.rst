
pdfWishartInv
==============================================

Purpose
----------------

Computes the probability density function of the inverse Wishart distribution.

Format
----------------
.. function:: p = pdfWishartInv(x, scale, df)

    :param x: :math:`T`, the values used to compute the inverse Wishart distribution.
    :type x: p x p positive definite matrix

    :param scale: :math:`\Psi`, the positive definite scale matrix parameter. It is not a covariance matrix: draws from this distribution average :math:`\Psi/(\nu - p - 1)` for :math:`\nu > p + 1`.
    :type scale: p x p matrix

    :param df: :math:`\nu`, degrees of freedom.
    :type df: Scalar

    :return p: probability density function.
    :rtype p: Scalar

Examples
----------------

::

    new ;
    cls ;
    rndseed 2223;

    x = {9.2517907  7.4283670,
         7.4283670 10.503325 };

    scale = {1 .5, .5 1};

    df = 3;

    // pdf of inverse Wishart distribution
    y = pdfWishartInv(x, scale, df);

    print y;

After above code,

::

    6.0267322e-007

Remarks
-------

`pdfWishartInv` calculates the probability density function for the
inverse Wishart distribution, which is defined as

.. math::

    f(T;\Psi,\nu) = \frac{|\Psi^{\frac{\nu}{2}}|}{2^{\nu p/2}\Gamma_p(\frac{\nu}{2})}|T|^{-(\nu+p+1)/2} e^{-\frac{1}{2}tr(\Psi T^{-1})}




.. seealso:: :func:`rndWishart`, :func:`rndWishartInv`
