
cdfBvn2
==============================================

Purpose
----------------

Returns the bivariate Normal cumulative distribution function of a bounded rectangle.

Format
----------------
.. function:: p = cdfBvn2(x1, dx1, x2, dx2, corr)

    :param x1: starting points of integration for variable 1.
    :type x1: Nx1 vector

    :param dx1: increments for variable 1.
    :type dx1: Nx1 vector

    :param x2: starting points of integration for variable 2.
    :type x2: Nx1 vector

    :param dx2: increments for variable 2.
    :type dx2: Nx1 vector

    :param corr: correlation coefficients between the two variables.
    :type corr: Nx1 vector

    :return p: the integral over the rectangle bounded by *x1*, *x1* + *dx1*,
        *x2*, and *x2* + *dx2* of the standardized bivariate Normal distribution.

    :rtype p: Nx1 vector

Examples
----------------

Example 1
+++++++++

::

    // Starting point of integration for variable 1
    x1 = 1;

    // Increments for variable 1
    dx1 = -1;

    // Starting point of integration for variable 2
    x2 = 1;

    // Increments for variable 2
    dx2 = -1;

    // Correlation coefficient
    corr = 0.5;

    print  cdfBvn2(x1, dx1, x2, dx2, corr);

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

     cdfBvn(x1 + dx1, x2+ dx2, corr) + cdfBvn(x1, x2, corr) - cdfBvn(x1, x2 + dx2, corr) - cdfBvn(x1 + dx1, x2, corr)

:func:`cdfBvn2` computes an error estimate for each set of inputs. The size of
the error depends on the input arguments. If **trap 2** is set, a
warning message is displayed when the error reaches 0.01 :func:`abs(y)`. For an
estimate of the actual error, see :func:`cdfBvn2e`.

.. seealso:: Functions :func:`cdfBvn2e`, :func:`lncdfbvn2`
