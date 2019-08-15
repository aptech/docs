
cdfFncInv
==============================================

Purpose
----------------
Computes the quantile or inverse of noncentral F cumulative distribution function.

Format
----------------
.. function:: x = cdfFncInv(p, df_n, df_d, nonc)

    :param p: Probabilities at which to compute the inverse of the noncentral F cumulative distribution function. :math:`0 \lt p \lt 1`.
    :type p: NxK matrix, Nx1 vector or scalar

    :param df_n: The degrees of freedom numerator. :math:`df_n > 0`.
    :type df_n: ExE conformable with *p*

    :param df_d: The degrees of freedom denominator. :math:`df_d > 0`.
    :type df_d: ExE conformable with *p*

    :param nonc: The noncentrality parameter. Note: This is the square root of the noncentrality parameter that sometimes goes under the symbol :math:`\lambda`. :math:`nonc > 0`.
    :type nonc: ExE conformable with *p*

    :return x: each value of *x* is the value such that the noncentral F cumulative distribution function with *df_n*, *df_d*, and *nonc* evaluated at *x* is equal to the corresponding value of *p*.

    :rtype x: NxK matrix, Nx1 vector or scalar

Remarks
-------

For invalid inputs, :func:`cdfFncInv` will return a scalar error code which,
when its value is assessed by function :func:`scalerr`, corresponds to the
invalid input. If the first input is out of range, :func:`scalerr` will return a
1; if the second is out of range, :func:`scalerr` will return a 2; etc.

Examples
----------------

::

  /*
  ** Computing the parameters
  */
  // Number of observations
  n_obs = 100;

  // Number of variables
  n_vars = 5;

  // Degrees of freedom
  df_n = n_vars;
  df_d = n_obs - n_vars - 1;

  // Probabilities
  p = {0.1, 0.25, 0.5, 0.75, 0.95};

  // Non-centralty parameter
  nonc = 2;

  x = cdfFncInv(p, df_n, df_d, nonc);
  print x;

After running the above code,

::

   0.6483
   1.0416
   1.6350
   2.4132
   3.9044

.. seealso:: :func:`cdfFnc`, :func:`cdfChinc`, :func:`cdfChic`, :func:`cdfTnc`
