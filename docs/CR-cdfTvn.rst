
cdfTvn
==============================================

Purpose
----------------

Computes the cumulative distribution function of the
standardized trivariate Normal density (lower tail).

Format
----------------
.. function:: c = cdfTvn(x1, x2, x3, rho12, rho23, rho13)

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

    :return p: result of the triple integral
        from :math:`-\infty\:\ to\:\ x_1`, :math:`-\infty\:\ to\:\ x_2`, and :math:`-\infty\:\ to\:\ x_3`
        of the standardized trivariate Normal density.

    :rtype p: Nx1 vector

Remarks
-------

Allowable ranges for the arguments are:

.. math:: 

     −\infty < x1 < \infty\\
     −\infty \lt x2 \lt \infty\\
     −\infty \lt x3 \lt \infty\\
     −1 \lt rho12 \lt 1\\
     −1 \lt rho23 \lt 1\\
     −1 \lt rho13 \lt 1\\

In addition, *rho12*, *rho23* and *rho13* must come from a legitimate positive
definite matrix. A -1 is returned for those rows with invalid inputs.

A separate integral is computed for each row of the inputs.

To find the integral under a general trivariate density, with *x1*, *x2*,
and *x3* having nonzero means and any positive standard deviations,
transform by subtracting the mean and dividing by the standard
deviation. For example:

.. math::  x1 = \frac{(x1 ⁢− meanc(x1))}{stdc(x1)}

The absolute error for :func:`cdfTvn` is approximately ±2.5e-8 for the entire
range of arguments.

Examples
----------------

::

    // Variables
    x1 = 0.6;
    x2 = 0.23;
    x3 = 0.46;

    //Correlations
    rho12 = 0.2;
    rho23 = 0.65;
    rho13 = 0.78;

    /*
    ** Compute the CDF
    */
    p = cdfTvn(x1, x2, x3, rho12, rho23, rho13);
    print "p =" p;

After the above code, `x` will equal:

::

    p =  0.4373

References
----------

#. Daley, D.J. ''Computation of Bi- and Tri-variate Normal Integral.''
   Appl. Statist. Vol. 23, No. 3, 1974, 435-38.

#. Steck, G.P. ''A Table for Computing Trivariate Normal
   Probabilities.'' Ann. Math. Statist. Vol. 29, 780-800.


.. seealso:: :func:`cdfN`, :func:`cdfBvn`
