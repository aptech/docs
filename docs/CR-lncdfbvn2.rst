
lncdfbvn2
==============================================

Purpose
----------------

Returns natural log of standardized bivariate Normal cumulative distribution function of a bounded rectangle.

Format
----------------
.. function:: lnp = lncdfbvn2(h, dh, k, dk, corr)

    :param h: upper limits of integration for variable 1.
    :type h: Nx1 vector

    :param dh: increments for variable 1.
    :type dh: Nx1 vector

    :param k: upper limits of integration for variable 2.
    :type k: Nx1 vector

    :param dk: increments for variable 2.
    :type dk: Nx1 vector

    :param corr: correlation coefficients between the two variables.
    :type corr: Nx1 vector

    :return lnp: the log of the integral from *h*, *k* to  *h+dh*, *k+dk*
        of the standardized bivariate Normal distribution.

    :rtype lnp: Nx1 vector

Examples
----------------

Example 1
+++++++++

::

    // Upper limits of integration for variable 1
    h = 1;

    // Increment for variable 1
    dh = 1;

    // Upper limits of integration for variable 2
    k = 1;

    // Increment for variable 2
    dk = 1;

    // Correlation
    corr = 0.5;

    lncdfbvn2(h, dh, k, dk, corr);

produces

::

    -3.2180110258198771e+000


Example 2
+++++++++

::

    trap 0, 2;
    // Upper limits of integration for variable 1
    h = 1;

    // Increment for variable 1
    dh = 1e-15;

    // Upper limits of integration for variable 2
    k = 1;

    // Increment for variable 2
    dk = 1e-15;

    // Correlation
    corr = 0.5;

    lncdfbvn2(h, dh, k, dk, corr);

produces

::

    -7.098869e+001

Example 3
+++++++++

::

    trap 2,2;
    // Upper limits of integration for variable 1
    h = 1;

    // Increment for variable 1
    dh = 1e-45;

    // Upper limits of integration for variable 2
    k = 1;

    // Increment for variable 2
    dk = 1e-45;

    // Correlation
    corr = 0.5;

    lncdfbvn2(h, dh, k, dk, corr);

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
