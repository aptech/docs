gradpdfbvn
==============================================

Purpose
----------------

Computes the probability density function (PDF) of a standard multivariate normal distribution for multiple observations. 

Format
----------------
.. function:: { gw1, gw2, grho } = gradpdfbvn(w1, w2, rho)


    :param w1: (Nx1) vector of abscissae points.
    :type w1: (Specify type)
    :param w2: (Nx1) vector of abscissae points.
    :type w2: (Specify type)
    :param rho: (Nx1) vector of correlation coefficients.
    :type rho: (Specify type)

    :return gw1: (Nx1) gradient vector of the bivariate normal PDF with respect to w1.
    :rtype gw1: (Specify type)
    :return gw2: (Nx1) gradient vector of the bivariate normal PDF with respect to w2.
    :rtype gw2: (Specify type)
    :return grho: (Nx1) gradient vector of the bivariate normal PDF with respect to rho.
    :rtype grho: (Specify type)

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);

Remarks
------------

- - This function computes the partial derivatives of the standard bivariate normal density function.
- - The correlation coefficient rho should be within the range (-1, 1).
- - The function is useful in sensitivity analysis and maximum likelihood estimation.

Source
------------

gradients-mvn.src
