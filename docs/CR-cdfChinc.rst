
cdfChinc
==============================================

Purpose
----------------
Computes the cumulative distribution function for the noncentral chi-square distribution.

Format
----------------
.. function:: cdfChinc(x,  v,  d)

    :param x: values of upper limits of integrals,
        must be greater than 0.
    :type x: Nx1 vector

    :param v: degrees of freedom, v> 0.
    :type v: scalar

    :param d: noncentrality parameter, d> 0.
        
        This is the square root of the noncentrality parameter
        that sometimes goes under the symbol lambda. (See Scheffe,
        The Analysis of Variance, App. IV, 1959.)
    :type d: scalar

    :returns: y (*TODO*), Nx1 vector.

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

chi square noncentral cdf cumulative distribution function
