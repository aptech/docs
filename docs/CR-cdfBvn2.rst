
cdfBvn2
==============================================

Purpose
----------------

Returns the bivariate Normal cumulative distribution function of a bounded rectangle.

Format
----------------
.. function:: cdfBvn2(h,  dh,  k,  dk, r)

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

    :returns: y (*Nx1 vector*), the integral over the rectangle bounded by h, h + dh,
        k, and k + dk of the standardized bivariate Normal distribution.

Examples
----------------

print  cdfBvn2(1,-1,1,-1,0.5);
   1.4105101488974692e-001
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

print cdfBvn2(1,-1e-15,1,-1e-15,0.5);
   4.9303806576313238e-32
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

print  cdfBvn2(1,-1e-45,1,-1e-45,0.5);
   0.0000000000000000e+000
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

trap 2,2;
  print cdfBvn2(1,-1e-45,1,1e-45,0.5);

  WARNING: Dubious accuracy from cdfBvn2:
  0.000e+000 +/- 2.8e-060
  0.0000000000000000e+000
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Source
++++++

lncdfn.src

.. seealso:: Functions :func:`cdfBvn2e`, :func:`lncdfbvn2`

cdfbvn bounded rectangle cdf cumulative distribution function
