
lncdfbvn2
==============================================

Purpose
----------------

Returns natural log of standardized bivariate Normal cumulative distribution function of a bounded rectangle.

Format
----------------
.. function:: lncdfbvn2(h, dh, k, dk, r)

    :param h: upper limits of integration for variable 1.
    :type h: Nx1 vector

    :param dh: increments for variable 1.
    :type dh: Nx1 vector

    :param k: upper limits of integration for variable 2.
    :type k: Nx1 vector

    :param dk: increments for variable 2.
    :type dk: Nx1 vector

    :param r: correlation coefficients between the two variables.
    :type r: Nx1 vector

    :returns: y (*Nx1 vector*), the log of the integral from h, k to  h+dh, k+dk
        of the standardized bivariate Normal distribution.

Remarks
-------

Scalar input arguments are okay; they will be expanded to Nx1 vectors.

lncdfbvn2 will abort if the computed integral is negative.

lncdfbvn2 computes an error estimate for each set of inputs-the real
integral is exp(y)±err. The size of the error depends on the input
arguments. If **trap 2** is set, a warning message is displayed when err
>= exp(y)/100.

For an estimate of the actual error, see cdfBvn2e.


Examples
----------------

lncdfbvn2(1,1,1,1,0.5);
+++++++++++++++++++++++

::

    -3.2180110258198771e+000

trap 0,2;
lncdfbvn2(1,1e-15,1,1e-15,0.5);
+++++++++++++++++++++++++++++++++++++++++

::

    -7.1171016046360151e+001

trap 2,2;
lncdfbvn2(1,-1e-45,1,1e-45,0.5);
++++++++++++++++++++++++++++++++++++++++++

::

    WARNING: Dubious accuracy from lncdfbvn2:
     0.000e+000 +/- 2.8e-060
     -INF

.. seealso:: Functions :func:`cdfbvn2`, :func:`cdfbvn2e`

natural log bivariate normal cdf range bound cumulative distribution
function
