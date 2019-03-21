
cdfChinc
==============================================

Purpose
----------------
Computes the cumulative distribution function for the noncentral chi-square distribution.

Format
----------------
.. function:: cdfChinc(x, v, d)

    :param x: values of upper limits of integrals, must be greater than 0.
    :type x: Nx1 vector

    :param v: degrees of freedom, *v* > 0.
    :type v: scalar

    :param d: noncentrality parameter, *d* > 0.
        
        This is the square root of the noncentrality parameter
        that sometimes goes under the symbol lambda. (See Scheffe,
        The Analysis of Variance, App. IV, 1959.)

    :type d: scalar

    :returns: y (Nx1 vector)

Remarks
-------

*y* is the integral from 0 to *x* of the noncentral chi-square distribution
with *v* degrees of freedom and noncentrality *d*.

:func:`cdfChinc` can return a vector of values, but the degrees of freedom and
noncentrality parameter must be the same for all values of *x*.

For invalid inputs, :func:`cdfChinc` will return a scalar error code which, when
its value is assessed by function :func:`scalerr`, corresponds to the invalid
input. If the first input is out of range, :func:`scalerr` will return a 1; if
the second is out of range, :func:`scalerr` will return a 2; etc.

Relation to :func:`cdfChic`:

::

   cdfChic(x, v) = 1 - cdfChinc(x, v, 0);

Examples
----------------

::

    x = { .5, 1, 5, 25 };
    print cdfChinc(x,4,2);

The code above returns:

::

    0.0042086234
     0.016608592
     0.30954232
     0.99441140

.. seealso:: Functions :func:`cdfFnc`, :func:`cdfTnc`

