
ssHeteroskedasticityTest
==============================================

Purpose
----------------

Tests the null hypothesis of no heteroskedasticity by comparing the sum-of-squares of the first third of the sample to the sum-of-squares of last third of the sample. Analogous to a Goldfeld-Quandt test.

.. note::
   **GAUSS 26.1.4+ (sslib 2.0.0).** The optional arguments below are
   keyword arguments and may be supplied by name, in any order. The
   positional order is unchanged from 1.0.0, so existing positional calls
   keep working. See :ref:`v1-to-v2-migration`.

Format
----------------
.. function:: { test_stat, p_val } = ssHeteroskedasticityTest(resid [, alternative])

    :param resid: Model residuals.
    :type resid: Vector

    :param alternative: Optional argument, specifies alternative to use for finding critical values. Options include: ``"increasing"``, ``"decreasing"``, or ``"two-sided"``. Default = ``"two-sided"``.
    :type alternative: String

    :return test_stat: Test statistic for the heteroskedasticity.
    :rtype test_stat: Scalar

    :return p_val: P-value for the test statistic for the heteroskedasticity.
    :rtype p_val: Scalar

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

ssdiagnostics.src

.. seealso:: Functions :func:`ssLjungBox`, :func:`ssJarqueBera`
