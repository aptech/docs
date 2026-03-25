pitHistogram
============

Purpose
-------
Compute and display a PIT histogram for visual calibration assessment.

Format
------

.. function:: counts = pitHistogram(pit_values)
              counts = pitHistogram(pit_values, n_bins)

   :param pit_values: PIT values from :func:`pitTest`.
   :type pit_values: Nx1 vector

   :param n_bins: Optional, number of bins. Default = 10.
   :type n_bins: scalar

   :return counts: bin counts.
   :rtype counts: n_bins x 1 vector

Examples
--------

::

    new;
    library timeseries;

    pt = pitTest(sorted_draws, actual, quiet=1);
    counts = pitHistogram(pt.pit_values);

    // A uniform histogram indicates good calibration
    print counts;

Remarks
-------

A well-calibrated density forecast produces a uniform PIT histogram.
Humps indicate underdispersion (too narrow intervals); U-shapes indicate
overdispersion. Skewness indicates bias.

Model
-----

The PIT histogram bins the empirical CDF values :math:`u_t = \hat{F}_t(y_t)` into
equal-width bins on [0, 1]. Under correct calibration, all bins should have
approximately equal height (:math:`T / n_{\text{bins}}`). Deviations indicate:

- **Hump in center:** Underdispersion (intervals too narrow — overconfident).
- **U-shape (high at edges):** Overdispersion (intervals too wide — underconfident).
- **Skewed:** Systematic bias in the predictive mean.


References
----------

- Diebold, F.X., T.A. Gunther, and A.S. Tay (1998). "Evaluating density forecasts." *International Economic Review*, 39(4), 863-883.


Library
-------
timeseries

Source
------
scoring.src

.. seealso:: Functions :func:`pitTest`, :func:`fcScore`
