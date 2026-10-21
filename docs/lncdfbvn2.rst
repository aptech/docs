
lncdfbvn2
==============================================

Purpose
----------------

Returns natural log of standardized bivariate Normal cumulative distribution function of a bounded rectangle.

Format
----------------
.. function:: lnp = lncdfbvn2(x1, dx1, x2, dx2, corr)

    :param x1: upper limits of integration for variable 1.
    :type x1: Nx1 vector

    :param dx1: increments for variable 1.
    :type dx1: Nx1 vector

    :param x2: upper limits of integration for variable 2.
    :type x2: Nx1 vector

    :param dx2: increments for variable 2.
    :type dx2: Nx1 vector

    :param corr: correlation coefficients between the two variables.
    :type corr: Nx1 vector

    :return lnp: the log of the integral from *x1*, *x2* to  *x1+dx1*, *x2+dx2*
        of the standardized bivariate Normal distribution.

    :rtype lnp: Nx1 vector

Examples
----------------

Example 1
+++++++++

::

    // Upper limits of integration for variable 1
    x1 = 1;

    // Increment for variable 1
    dx1 = 1;

    // Upper limits of integration for variable 2
    x2 = 1;

    // Increment for variable 2
    dx2 = 1;

    // Correlation
    corr = 0.5;

    lncdfbvn2(x1, dx1, x2, dx2, corr);

produces

::

    -3.2180110258198771e+000


Example 2
+++++++++

::

    trap 0, 2;
    // Upper limits of integration for variable 1
    x1 = 1;

    // Increment for variable 1
    dx1 = 1e-15;

    // Upper limits of integration for variable 2
    x2 = 1;

    // Increment for variable 2
    dx2 = 1e-15;

    // Correlation
    corr = 0.5;

    lncdfbvn2(x1, dx1, x2, dx2, corr);

produces

::

    -7.098869e+001

Example 3
+++++++++

::

    trap 2,2;
    // Upper limits of integration for variable 1
    x1 = 1;

    // Increment for variable 1
    dx1 = 1e-45;

    // Upper limits of integration for variable 2
    x2 = 1;

    // Increment for variable 2
    dx2 = 1e-45;

    // Correlation
    corr = 0.5;

    lncdfbvn2(x1, dx1, x2, dx2, corr);

produces

::

     WARNING: Dubious accuracy from lncdfbvn2:
     0.000e+000 +/- 2.8e-060
     -INF

Remarks
-------

Scalar input arguments are okay; they will be expanded to Nx1 vectors.

:func:`lncdfbvn2` will abort if the computed integral is negative.

:func:`lncdfbvn2` computes an error estimate for each set of inputs-the real
integral is :math:`exp(y) \pm err`. The size of the error depends on the input
arguments. If ``trap 2`` is set, a warning message is displayed when :math:`err \geq= exp(y)/100`.

For an estimate of the actual error, see :func:`cdfBvn2e`.

.. seealso:: Functions :func:`cdfbvn2`, :func:`cdfbvn2e`
