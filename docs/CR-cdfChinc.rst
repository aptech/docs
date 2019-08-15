
cdfChinc
==============================================

Purpose
----------------
Computes the cumulative distribution function for the noncentral chi-squared distribution.

Format
----------------
.. function:: y = cdfChinc(x, df, nonc)

    :param x: Values at which to evaluate the cdf of the noncentral chi-squared distribution. :math:`x > 0`.
    :type x: Nx1 vector

    :param df: degrees of freedom, :math:`df > 0`.
    :type df: scalar

    :param nonc: noncentrality parameter, :math:`nonc > 0`. Note: This is the squared root of the noncentrality parameter that sometimes goes under the symbol :math:`\lambda`.  :math:`nonc > 0`.
    :type nonc: scalar

    :return p: Each element in *p* is the noncentral chi-squared cdf value evaluated at the corresponding element in *x*.

    :rtype p: Nx1 vector

Remarks
-------

*p* is the integral from 0 to *x* of the noncentral chi-square distribution
with *df* degrees of freedom and noncentrality *nonc*.

:func:`cdfChinc` can return a vector of values, but the degrees of freedom and
noncentrality parameter must be the same for all values of *x*.

For invalid inputs, :func:`cdfChinc` will return a scalar error code which, when
its value is assessed by function :func:`scalerr`, corresponds to the invalid
input. If the first input is out of range, :func:`scalerr` will return a 1; if
the second is out of range, :func:`scalerr` will return a 2; etc.

Relation to :func:`cdfChic`:

::

   cdfChic(x, df) = 1 - cdfChinc(x, df, 0);

Examples
----------------

::

    // Values
    x = { .5, 1, 5, 25 };

    // Degrees of freedom
    df = 4;

    // Non-centrality parameter
    nonc = 2;

    print cdfChinc(x, df, nonc);

The code above returns:

::

     0.0042086234
     0.016608592
     0.30954232
     0.99441140

.. seealso:: Functions :func:`cdfFnc`, :func:`cdfTnc`
