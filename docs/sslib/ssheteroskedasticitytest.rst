
ssHeteroskedasticityTest
==============================================

Purpose
----------------

Tests the null hypothesis of no heteroskedasticity by comparing the sum-of-squares of the first third of the sample to the sum-of-squares of last third of the sample. Analogous to a Goldfeld-Quandt test.

Format
----------------
.. function:: { test_statistic, p_value } = ssHeteroskedasticityTest(resid [,alternative])

    :param resid: Model residuals.
    :type resid: Vector

    :param alternative: Optional argument, specifies alternative to use for finding critical values. Options include: ``"increasing"``, ``"decreasing"``, or ``"two-sided"``. Default = ``"two-sided"``.
    :type alternative: String

    :return test_stat: Test statistic for the heteroskedasticity.
    :rtype test_stat: Scalar

    :return p_value: P-value for the test statistic for the heteroskedasticity.
    :rtype p_value: Scalar

Examples
----------------

::

  // Generate random vector of residuals
  rndseed 929212;
  resid = rndn(150, 1);

  // Test for heteroskedasticity
  { test_stat, p_val } = ssHeteroskedasticityTest(resid);

The code above results in the following:

::

  test_stat = 0.9598
  p_val = 0.8854


Source
------

ssmain.src

.. seealso:: Functions :func:`ssLjungBox`, :func:`ssJarqueBera`
