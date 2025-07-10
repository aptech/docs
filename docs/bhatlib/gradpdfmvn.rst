gradpdfmvn
==============================================

Purpose
----------------

Computes the probability density function (PDF) of a non-standard multivariate normal distribution for multiple observations. 

Format
----------------
.. function:: { gcov, gx } = gradpdfmvn(cov, x)


    :param cov: (KxK) correlation matrix (must be positive definite).
    :type cov: (Specify type)
    :param x: (Kx1) vector of abscissae, where K corresponds to the number of variates.
    :type x: (Specify type)

    :return gcov: ((K*(K-1))/2 x 1) vector of gradients of the multivariate normal PDF
    :rtype gcov: (Specify type)
    :return gx: (Kx1) gradient vector of the multivariate normal PDF with respect to x.
    :rtype gx: (Specify type)

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);

Remarks
------------

- - The correlation matrix `cov` must be positive definite.
- - If _Cholesky = 1, gcov is computed with respect to Cholesky elements instead of correlation elements.
- - The function is useful in sensitivity analysis and maximum likelihood estimation.

Global Variables
------------

- _Cholesky - If 1, computes gradients with respect to the Cholesky decomposition of cov.
- If 0, computes gradients with respect to the correlation elements.
- 

Source
------------

gradients-mvn.src
