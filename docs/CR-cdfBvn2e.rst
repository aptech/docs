
cdfBvn2e
==============================================

Purpose
----------------

Returns the bivariate Normal cumulative distribution function of a bounded rectangle.

Format
----------------
.. function:: cdfBvn2e(h,  dh,  k,  dk, r)

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

    :returns: y (*Nx1 vector*), the integral over the rectangle bounded by  h,  h +  dh,  k, and  k +  dk of the standardized bivariate Normal distribution.

    :returns: e (*Nx1 vector*), an error estimate.

Examples
----------------

print 
   cdfBvn2e(1,-1,1,-1,0.5);

   1.4105101488974692e-001
   1.9927918166193113e-014
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

print 
   cdfBvn2e(1,-1e-15,1,-1e-15,0.5);

   7.3955709864469857e-032
   2.8306169312687801e-030
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

print
   cdfBvn2e(1,-1e-45,1,-1e-45,0.5);

   0.0000000000000000e+000
   2.8306169312687770e-060
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. seealso:: Functions :func:`cdfBvn2`, :func:`lncdfbvn2`

cdfbvn bounded rectangle cdf cumulative distribution function
