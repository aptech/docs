
cdfFnc
==============================================

Purpose
----------------
Computes the cumulative distribution function of the noncentral F distribution.

Format
----------------
.. function:: p = cdfFnc(x, df_n, df_d, nonc)

    :param x: Values at which to evaluate the cdf of the noncentral F distribution. :math:`x > 0`.
    :type x: NxK matrix

    :param df_n: ExE conformable with *x*. Degrees of freedom of numerator, :math:`df_n > 0`.
    :type df_n: LxM matrix

    :param df_d: ExE conformable with *x* and *df_n*. Degrees of freedom of denominator, :math:`df_d > 0`.
    :type df_d: PxQ matrix

    :param nonc: ExE conformable with *x*. The noncentrality parameter. This is the square root of the noncentrality parameter
        that sometimes goes under the symbol :math:`\lambda`. :math:`nonc > 0`.
    :type nonc: RxS matrix

    :return p: Each element in *p* is the noncentral F distribution cdf value evaluated at the corresponding element in *x*.

    :rtype p: max(N,L,P,R) by max(K,M,Q,S) matrix

Remarks
-------

For invalid inputs, :func:`cdfFnc` will return a scalar error code which, when
its value is assessed by function :func:`scalerr`, corresponds to the invalid
input. If the first input is out of range, :func:`scalerr` will return a 1; if
the second is out of range, :func:`scalerr` will return a 2; etc.

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

  // Value to calculate p_value at
  f_stat = 2.4;

  // Non-centrality parameter
  nonc = 2;

  // Call cdfFnc
  p = cdfFnc(f_stat, df_n, df_d, nonc);
  print p;

will return:

::

  0.7468

.. seealso:: :func:`cdfTnc`, :func:`cdfChinc`
