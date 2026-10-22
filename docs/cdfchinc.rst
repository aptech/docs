
cdfChinc
==============================================

Purpose
----------------
Computes the cumulative distribution function for the noncentral chi-squared distribution.

Format
----------------
.. function:: p = cdfChinc(x, df, nonc)

    :param x: Values at which to evaluate the cdf of the noncentral chi-squared distribution. An *x* below 0 returns 0.
    :type x: Nx1 vector

    :param df: degrees of freedom, :math:`df > 0`.
    :type df: scalar

    :param nonc: noncentrality parameter, :math:`nonc \geq 0`. Note: This is the square root of the noncentrality parameter that sometimes goes under the symbol :math:`\lambda`.
    :type nonc: scalar

    :return p: Each element in *p* is the noncentral chi-squared cdf value evaluated at the corresponding element in *x*.

    :rtype p: Nx1 vector

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

Remarks
-------

*p* is the integral from 0 to *x* of the noncentral chi-square distribution
with *df* degrees of freedom and noncentrality *nonc*.

:func:`cdfChinc` can return a vector of values, but the degrees of freedom and
noncentrality parameter must be the same for all values of *x*.

If *df* is not greater than 0 or *nonc* is below 0, :func:`cdfChinc` returns a
scalar error code and :func:`scalerr` returns the position of that argument: 2
for *df*, 3 for *nonc*. An *x* below 0 is not an error: it returns 0. A missing
value in any argument returns a missing value.

Relation to :func:`cdfChic`:

::

   cdfChic(x, df) = 1 - cdfChinc(x, df, 0);

.. seealso:: Functions :func:`cdfFnc`, :func:`cdfTnc`
