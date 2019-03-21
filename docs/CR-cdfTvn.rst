
cdfTvn
==============================================

Purpose
----------------

Computes the cumulative distribution function of the
standardized trivariate Normal density (lower tail).

Format
----------------
.. function:: cdfTvn(x1, x2, x3, rho12, rho23, rho13)

    :param x1: upper limits of integration for variable 1
    :type x1: Nx1 vector

    :param x2: upper limits of integration for variable 2
    :type x2: Nx1 vector

    :param x3: upper limits of integration for variable 3
    :type x3: Nx1 vector

    :param rho12: correlation coefficients between the two variables *x1* and *x2*
    :type rho12: scalar or Nx1 vector

    :param rho23: correlation coefficients between the two variables *x2* and *x3*
    :type rho23: scalar or Nx1 vector

    :param rho13: correlation coefficients between the two variables *x1* and *x3*
    :type rho13: scalar or Nx1 vector

    :returns: c (*Nx1 vector*) result of the triple integral
        from :math:`-∞` to *x1*, :math:`-∞` to *x2*, and :math:`-∞` to *x3*
        of the standardized trivariate Normal density.

Remarks
-------

Allowable ranges for the arguments are:

.. DANGER:: FIX EQUATION

.. math:: −∞<x1<∞−∞<x2<∞−∞<x3<∞−1<rho12<1−1<rho23<1−1<rho13<1

In addition, *rho12*, *rho23* and *rho13* must come from a legitimate positive
definite matrix. A -1 is returned for those rows with invalid inputs.

A separate integral is computed for each row of the inputs.

The first 3 arguments (*x1*, *x2*, *x3*) must be the same length, *N*. The
second 3 arguments (*rho12*, *rho23*, *rho13*) must also be the same length,
and this length must be N or 1. If it is 1, then these values will be
expanded to apply to all values of *x1*, *x2*, *x3*. All inputs must be column
vectors.

To find the integral under a general trivariate density, with *x1*, *x2*,
and *x3* having nonzero means and any positive standard deviations,
transform by subtracting the mean and dividing by the standard
deviation. For example:

.. math::  x1=(      x1⁢− meanc(x1)   )  /  stdc(x1)

The absolute error for :func:`cdfTvn` is approximately ±2.5e-8 for the entire
range of arguments.

References
----------

#. Daley, D.J. ''Computation of Bi- and Tri-variate Normal Integral.''
   Appl. Statist. Vol. 23, No. 3, 1974, 435-38.

#. Steck, G.P. ''A Table for Computing Trivariate Normal
   Probabilities.'' Ann. Math. Statist. Vol. 29, 780-800.


.. seealso:: :func:`cdfN`, :func:`cdfBvn`

