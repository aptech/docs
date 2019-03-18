
cdfWeibull
==============================================

Purpose
----------------

Computes the cumulative distribution function for the Weibull distribution.  

Format
----------------
.. function:: cdfWeibull(x,k,lambda)

    :param x: Nx1 vector or scalar. x must be greater than 0.
    :type x: NxK matrix

    :param k: Shape parameter; NxK matrix, Nx1 vector or scalar, ExE conformable with x.  k must be greater than 0.
    :type k: TODO

    :param lambda: Scale parameter; NxK matrix, Nx1 vector or scalar, ExE conformable with x.  lambda must be greater than 0.
    :type lambda: TODO

    :returns: y (*NxK matrix*), Nx1 vector or scalar.

Examples
----------------
Calculate the cdf for the Weibull distribution with different shape parameters.

::

    // lambda = 1
    x = seqa(0,0.01,301);
    k = 0.5~1~1.5~5;
    lambda = 1;
    y = cdfWeibull(x, k, lambda);
    plotxy(x, y);

After running above code,

Remarks
+++++++

The Weibull cumulative distribution function is defined as:

::

   f(x;k,λ) = 1 - e-(x/λ)k

.. seealso:: Functions :func:`pdfWeibull`, :func:`cdfWeibullInv`

Weibull cdf cumulative distribution function
