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

Model
-----

The PIT value for observation :math:`t` is:

.. math::

   u_t = \hat{F}_t(y_t) = \frac{1}{S} \sum_{s=1}^{S} \mathbf{1}(\hat{y}_t^{(s)} \leq y_t)

where :math:`\hat{y}_t^{(s)}` are posterior predictive draws. If the density forecast is
correctly specified, :math:`u_t \sim U(0,1)` (Diebold, Gunther & Tay 1998).

**Berkowitz test** additionally tests serial independence by fitting an AR(1) to the
probit-transformed PITs :math:`z_t = \Phi^{-1}(u_t)` and testing :math:`H_0: \mu = 0, \sigma = 1, \rho = 0`.


References
----------

- Diebold, F.X., T.A. Gunther, and A.S. Tay (1998). "Evaluating density forecasts with applications to financial risk management." *International Economic Review*, 39(4), 863-883.
- Berkowitz, J. (2001). "Testing density forecasts, with applications to risk management." *Journal of Business & Economic Statistics*, 19(4), 465-474.


Library
-------
timeseries

Source
------
scoring.src

.. seealso:: Functions :func:`pitHistogram`, :func:`fcScore`
