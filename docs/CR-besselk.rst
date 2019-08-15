
besselk
==============================================

Purpose
----------------

Computes the modified Bessel function of the second kind, :math:`K_n(x)`.


Format
----------------
.. function:: besselk(n, x)

    :param n: order. Currently only integer orders are supported.
    :type n: scalar or matrix

    :param x: conformable with *n*. *x* must be greater than 0.
    :type x: scalar or matrix ExE

    :return K: the modified Bessel function result.

    :rtype K: scalar or matrix

Remarks
-------

Currently the algorithm has the following limitations:

-  The order, *n*, must be an integer.
-  The values of *x* must be positive.
-  The maximum supported value for *x* with an order greater than 1 is
   limited to approximately 740. If the input is out of range, a NaN
   (missing value) will be returned. If necessary, use the function
   :func:`ismiss` to check for NaN's in the output.


Examples
----------------

Basic usage
+++++++++

::

    x = { 0,
        0.5,
          1,
        1.5,
          2 };

    K = besselk(1, x);

After the above code, *K*, should equal:

::

    +INF
    1.6564411
    0.60190723
    0.27738780
    0.13986588

Compute data for first 3 orders
+++++++++++++++++++++++++++++++

::

    // Row vector of orders, 'n'
    n = { 0 1 2 };

    // Column vector 'x'
    x = { 0,
        0.5,
          1,
        1.5,
          2 };

    // Compute function for each order, 'n', at all 'x' points
    K = besselk(n, x);

After the code above, *K* should equal:

::

    +INF             +INF             +INF
    0.92441907       1.6564411        7.5501836
    0.42102444       0.60190723       1.6248389
    0.21380556       0.27738780       0.58365596
    0.11389387       0.13986588       0.25375975

 
.. seealso:: Functions :func:`bessely`, :func:`mbesseli`, :func:`besselj`
