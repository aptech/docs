
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

    :return Q_stat: Ljung-Box test statistic for residual autocorrelation.
    :rtype Q_stat: Scalar

    :return p_val: P-value of the Ljung-Box test statistic.
    :rtype p_val: Scalar

Examples
----------------

::

  // Generate random vector of residuals
  rndseed 929212;
  resid = rndn(150, 1);

  // Test for autocorrelation
  { Q_stat, p_val } = ssLjungBox(resid);

The code above results in the following:

::

  Q_stat = 2.0876
  p_val = 0.1485


Source
------

ssdiagnostics.src

.. seealso:: Functions :func:`ssHeteroskedasticityTest`, :func:`ssJarqueBera`
