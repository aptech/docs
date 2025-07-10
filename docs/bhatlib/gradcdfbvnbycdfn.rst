gradcdfbvnbycdfn
==============================================

Purpose
----------------

Computes the gradients of the ratio of a standard bivariate normal cumulative function  to a standard univariate normal cumulative distribution function: P = cdfbvn(w1, w2, rho) / cdfn(w1).

Format
----------------
.. function:: { gw1, gw2, grho } = gradcdfbvnbycdfn(w1, w2, rho)

    :param w1: Abscissae points.
    :type w1: N x 1 vector

    :param w2: Abscissae points.
    :type w2: N x 1 vector
    
    :param rho: Correlation coefficients.
    :type rho: N x 1 vector

    :param gw1: Gradients of cdfbvn with respect to w1.
    :type gw1: K x 1 vector 
    
    :param gw2: Gradients of cdfbvn with respect to w2.
    :type gw2: scalar

    :return grho: Gradients of cdfbvn with respect to rho.
    :rtype grho: scalar

Examples
----------------

::

    // Example usage of {func}
    result = {func}(...);

Remarks
------------

- This function computes the sensitivity of the ratio P with respect to w1, w2, and rho.
- If _cholesky = 1, gradients are computed with respect to Cholesky elements instead of correlation coefficients.

Global Inputs
---------------

.. data:: _cholesky

    Controls the method of computation for Cholesky gradients.

    .. list-table::
        :widths: auto

        * - [0]
          - Gradients are computed with respect to correlation elements.
        * - [1]
          - Gradients are computed with respect to the Cholesky decomposition of covariance.
       

Source
------------

gradients-mvn.src
