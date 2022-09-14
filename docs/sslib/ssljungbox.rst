
ssLjungBox
==============================================

Purpose
----------------

Computes the Ljung-Box test of the null hypothesis that the residuals are independently distributed..

Format
----------------
.. function:: { Q_stat, p_val } = ssLjungBox(resid)

    :param resid: Model residuals.
    :type resid: Vector

    :return Q_stat: Ljung-Box test statistic for the heteroskedasticity.
    :rtype Q_stat: Scalar

    :return p_value: P-value for the test statistic for the Ljung-Box test statistic.
    :rtype p_value: Scalar

Examples
----------------

::

  // Generate random vector of residuals
  rndseed 929212;
  resid = rndn(150, 1);

  // Test for heteroskedasticity
  { Q_stat, p_val } = ssLjungBox(resid);

The code above results in the following:

::

  Q_stat = 2.0876
  p_val = 0.1485

In this case, the p-values suggests that we fail to reject the null hypothesis that the residuals are independently distributed.

Source
------

ssmain.src

.. seealso:: Functions :func:`ssHeteroskedasticityTest`, :func:`ssJarqueBera`
