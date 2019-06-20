
cdfBvn2e
==============================================

Purpose
----------------

Returns the bivariate Normal cumulative distribution function of a bounded rectangle.

Format
----------------
.. function:: cdfBvn2e(h, dh, k, dk, r)

    :param h: starting points of integration for variable 1.
    :type h: Nx1 vector

    :param dh: increments for variable 1.
    :type dh: Nx1 vector

    :param k: starting points of integration for variable 2.
    :type k: Nx1 vector

    :param dk: increments for variable 2.
    :type dk: Nx1 vector

    :param r: correlation coefficients between the two variables.
    :type r: Nx1 vector

    :returns: **p** (*Nx1 vector*), the integral over the rectangle bounded by *h*, *h* + *dh*, *k*, and *k* + *dk* of the standardized bivariate Normal distribution.

    :returns: **e** (*Nx1 vector*), an error estimate.

Remarks
-------

Scalar input arguments are okay; they will be expanded to Nx1 vectors.

:func:`cdfBvn2e` computes:

::

     cdfBvn(h + dh, k +  dk, r) + cdfBvn(h, k, r) - cdfBvn(h, k + dk, r) - cdfBvn(h + dh, k, r)

The real answer is :math:`y ± e`. The size of the error depends on the input arguments.

Examples
----------------

Example 1
+++++++++

::

  // Starting point of integration for variable 1
  h = 1;

  // Increments for variable 1
  dh = -1;

  // Starting point of integration for variable 2
  k = 1;

  // Increments for variable 2
  dk = -1;

  // Correlation coefficient
  rho = 0.5;

  print cdfBvn2e(h, dh, k, dk, rho);

After running the above code,

::

    1.4105101488974692e-001
    1.9927918166193113e-014

Example 2
+++++++++

::

    print cdfBvn2e(1,-1e-15,1,-1e-15,0.5);

After running the above code,

::

    7.3955709864469857e-032
    2.8306169312687801e-030

Example 3
+++++++++

::

    print cdfBvn2e(1,-1e-45,1,-1e-45,0.5);

After running the above code,

::

    0.0000000000000000e+000
    2.8306169312687770e-060

.. seealso:: Functions :func:`cdfBvn2`, :func:`lncdfbvn2`
