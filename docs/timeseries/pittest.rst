pitTest
=======

Purpose
-------
Density forecast calibration tests via the Probability Integral Transform.

Format
------

.. function:: pt = pitTest(sorted_draws, actual)
              pt = pitTest(sorted_draws, actual, n_bins=20)

   :param sorted_draws: sorted forecast draws. Each column is the sorted draws for one observation.
   :type sorted_draws: (n_draws)xN matrix

   :param actual: realized values.
   :type actual: Nx1 vector

   :param n_bins: Optional keyword, number of bins for chi-squared test. Default = 10.
   :type n_bins: scalar

   :param quiet: Optional keyword, set to 1 to suppress output. Default = 0.
   :type quiet: scalar

   :return pt: An instance of a :class:`pitResult` structure containing KS test, chi-squared test, Berkowitz test, and raw PIT values.
   :rtype pt: struct

Examples
--------

::

    new;
    library timeseries;

    // PIT calibration check
    pt = pitTest(sorted_draws, actual);

    print "KS test: stat=" pt.ks_stat "p=" pt.ks_pval;
    print "Berkowitz: stat=" pt.berk_stat "p=" pt.berk_pval;

    // PIT histogram (should be uniform if calibrated)
    counts = pitHistogram(pt.pit_values);

Remarks
-------

If the density forecast is correctly calibrated, the PIT values are
uniformly distributed on [0, 1]. Three tests are applied:

- **KS test:** Kolmogorov-Smirnov test against U(0,1).
- **Chi-squared test:** Binned goodness-of-fit against uniform.
- **Berkowitz test:** Tests both uniformity and serial independence of
  PITs via a likelihood ratio test on the probit-transformed values.

A well-calibrated forecast should have non-significant p-values for all
three tests.

Library
-------
timeseries

Source
------
scoring.src

.. seealso:: Functions :func:`pitHistogram`, :func:`fcScore`
