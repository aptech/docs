
cdfWeibull
==============================================

Purpose
----------------

Computes the cumulative distribution function for the Weibull distribution.  

Format
----------------
.. function:: cdfWeibull(x,k,lambda)

    :param x: must be greater than 0.
    :type x: NxK matrix, Nx1 vector or scalar

    :param k: Shape parameter. ExE conformable with *x*. *k* must be greater than 0.
    :type k: NxK matrix, Nx1 vector or scalar

    :param lambda: Scale parameter, ExE conformable with *x*. *lambda* must be greater than 0.
    :type lambda: NxK matrix, Nx1 vector or scalar

    :returns: y (*NxK matrix, Nx1 vector or scalar*)

Remarks
------------

The Weibull cumulative distribution function is defined as:

.. math::  f(x;k,λ) = 1 - e-(x/λ)k

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

.. figure:: _static/images/cdfWeibull_1.png

.. seealso:: Functions :func:`pdfWeibull`, :func:`cdfWeibullInv`

