
lncdfmvn
==============================================

Purpose
----------------

Computes natural log of multivariate Normal cumulative distribution function.

Format
----------------
.. function:: lnp = lncdfmvn(x, corr)

    :param x: abscissae.
    :type x: KxL matrix

    :param corr: correlation matrix.
    :type corr: KxK matrix

    :return lnp:

        .. math:: ln Pr(X < x|r)

    :rtype lnp: Lx1 vector

Examples
----------------

::

    x = { 0.87  0.62  0.67  0.25,
         0.5  -0.3  -0.19  1.25,
         -1.12  1.2  2.9  2.1};

  corr = { 1 0.23 -0.7,
           0.25 1 0,
           -0.7 0 1};

  p = lncdfmvn(x, corr);

::

  p =  -3.23918  -1.32135  -1.05564  -0.62031

Remarks
-------

You can pass more than one set of abscissae at a time; each column of *x*
is treated separately.

Source
------

lncdfn.src

.. seealso:: Functions :func:`cdfmvn`, :func:`lncdfbvn`
