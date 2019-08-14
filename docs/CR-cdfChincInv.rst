
cdfChincInv
==============================================

Purpose
----------------
Computes the quantile or inverse of noncentral chi-squared cumulative distribution function.

Format
----------------
.. function:: x = cdfChincInv(p, df, nonc)

    :param p: Probabilities at which to compute the inverse of noncentral chi-squared cumulative distribution function. :math:`0 < p < 1`.
    :type p: NxK matrix, Nx1 vector or scalar

    :param df:  The degrees of freedom. :math:`df > 0`.
    :type df: ExE conformable with *p*

    :param nonc:  The noncentrality parameter. Note: This is the squared root of the noncentrality parameter that sometimes goes under the symbol :math:`\lambda`.  :math:`nonc > 0`.
    :type nonc: ExE conformable with *p*

    :returns: **x** (*NxK matrix, Nx1 vector or scalar*) - each value of *x* is the value such that the noncentral chi-squared cdf with *df* degrees of freedom and *nonc* noncentrality evaluated at *x* is equal to the corresponding value of *p*.

Remarks
-------

For invalid inputs, :func:`cdfChincinv` will return a scalar error code which,
when its value is assessed by function :func:`scalerr`, corresponds to the
invalid input. If the first input is out of range, :func:`scalerr` will return a
1; if the second is out of range, scalerr will return a 2; etc.

Examples
----------------

::

    // Probabilities
    p = { .05, .1, .25, .5, .75, 0.90, 0.95 };

    // Degrees of freedom
    df = 4;

    // Non-centrality parameter
    nonc = 2;

    print cdfChincInv(p, df, nonc);

The code above returns:

::

  1.7650
  2.5583
  4.3564
  7.1016
  10.6736
  14.6157
  17.3093

.. seealso:: :func:`cdfChinc`, :func:`cdfChic`, :func:`cdfFnc`, :func:`cdfTnc`
