
cdfBvn2
==============================================

Purpose
----------------

Returns the bivariate Normal cumulative distribution function of a bounded rectangle.

Format
----------------
.. function:: p = cdfBvn2(h, dh, k, dk, r)

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

    :return p: the integral over the rectangle bounded by *h*, *h* + *dh*,
        *k*, and *k* + *dk* of the standardized bivariate Normal distribution.

    :rtype p: Nx1 vector

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

    print  cdfBvn2(h, dh, k, dk, rho);

After running the above code,

::

      1.4105101488974692e-001

Example 2
+++++++++

::

    print cdfBvn2(1, -1e-15, 1, -1e-15, 0.5);

After running the above code,

::

    4.9303806576313238e-32

Example 3
+++++++++

::

    print cdfBvn2(1, -1e-45, 1, -1e-45, 0.5);

After running the above code,

::

    0.0000000000000000e+000

Example 4
+++++++++

::

    trap 2,2;
    print cdfBvn2(1, -1e-45, 1, 1e-45, 0.5);

After running the above code,

::

    WARNING: Dubious accuracy from cdfBvn2:
    0.000e+000 +/- 2.8e-060
    0.0000000000000000e+000

Remarks
-------

Scalar input arguments are okay; they will be expanded to Nx1 vectors.

:func:`cdfBvn2` computes:

::

     cdfBvn(h + dh, k+ dk, r) + cdfBvn(h, k, r) - cdfBvn(h, k + dk, r) - cdfBvn(h + dh, k, r)

:func:`cdfBvn2` computes an error estimate for each set of inputs. The size of
the error depends on the input arguments. If **trap 2** is set, a
warning message is displayed when the error reaches 0.01 :func:`abs(y)`. For an
estimate of the actual error, see :func:`cdfBvn2e`.

.. seealso:: Functions :func:`cdfBvn2e`, :func:`lncdfbvn2`
