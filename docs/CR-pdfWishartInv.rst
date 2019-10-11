
pdfWishartInv
==============================================

Purpose
----------------

Computes the probability density function of the inverse Wishart distribution.

Format
----------------
.. function:: p = pdfWishartInv(IW, S, df)

    :param IW: T, the values used to compute the inverse Wishart distribution.
    :type IW: p x p positive definite matrix

    :param S: :math:`\Psi`, the positive definite scale matrix parameter
    :type S: p x p matrix

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

    S = {1 .5, .5 1};

    df = 3;

    // pdf of inverse Wishart distribution
    y = pdfWishartInv(x, S, df);

    print y;

After above code,

::

    6.0267322e-007

Remarks
-------

`pdfWishartInv` calculates the probability density function for the
inverse Wishart distribution, which is defined as

.. math::

    f(T) = \frac{ |\Psi|^{\nu/2} }{ |T|^{ \frac{ \nu + p + 1}{2} }⁢ 2^{\frac{\nu p}{2}}⁢\Gamma_p(\frac{\nu}{2}) } exp\big⁡(−\frac{1}{2}tr(\Gamma T^{−1})\big)


.. seealso:: :func:`rndWishart`, :func:`rndWishartInv`

