
ssLjungBox
==============================================

Purpose
----------------

Computes the Ljung-Box test for autocorrelation.

Format
----------------
.. function:: { Q_stat, p_val } = ssLjungBox(resid)

    :param resid: Model residuals.
    :type resid: Vector

    :return Q_stat: Ljung-Box test statistic for the heteroskedasticity.
    :return Q_stat: Scalar

    :return p_value: P-value for the test statistic for the Ljung-Box test statistic.
    :return p_value: Scalar

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


Source
------

ssmain.src

.. seealso:: Functions :func:`ssHeteroskedasticityTest`, :func:`ssJarqueBera`
