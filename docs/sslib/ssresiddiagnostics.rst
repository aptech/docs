
ssResidDiagnostics
==============================================

Purpose
----------------

Computes residual-based model diagnostics from a filled :class:`ssOut` structure -- standardized forecast errors, a per-series Ljung-Box test for residual autocorrelation, a heteroskedasticity test, skewness/kurtosis, and the Jarque-Bera goodness-of-fit test. Called automatically by :func:`ssFit`/:func:`ssFitTVP`/:func:`ssARIMA`/:func:`ssSARIMA`/:func:`ssStructuralTS` as part of filling their own returned :class:`ssOut`; exposed publicly for a caller who has otherwise built or modified an :class:`ssOut` and wants these diagnostics (re)computed.

.. note::
   **GAUSS 26.1.4+ (sslib 2.0.0).** This procedure declares its return
   type, so the result needs no preceding ``struct`` declaration. See
   :ref:`v1-to-v2-migration`.

Format
----------------
.. function:: sOut = ssResidDiagnostics(sOut)

    :param sOut: a partially-filled instance of an :class:`ssOut` structure -- specifically needs ``sOut.kfResults`` (``forecast_error``, ``forecast_error_cov``), ``sOut.numObs``, and ``sOut.likelihoodburn`` already set (as :func:`ssFit`/:func:`ssFitTVP`/:func:`ssControlCreate` already do).
    :type sOut: struct

    :return sOut: the same structure, with the following members filled in:

        .. list-table::
            :widths: auto

            * - sOut.standardized_forecast_errors
              - Matrix, nobs x k_endog, each column's forecast error divided by its own per-period forecast standard deviation.
            * - sOut.ljung_box
              - Vector, k_endog x 1, one univariate Ljung-Box test statistic per endogenous series.
            * - sOut.ljung_box_pval
              - Vector, k_endog x 1, p-values for the Ljung-Box test(s).
            * - sOut.hetero_test
              - Vector, k_endog x 1, heteroskedasticity test statistic(s).
            * - sOut.hetero_test_pval
              - Vector, k_endog x 1, p-values for the heteroskedasticity test(s).
            * - sOut.skew
              - Vector, k_endog x 1, sample skewness.
            * - sOut.kurtosis
              - Vector, k_endog x 1, sample kurtosis.
            * - sOut.jb_stat
              - Vector, k_endog x 1, Jarque-Bera test statistic(s).
            * - sOut.jb_pval
              - Vector, k_endog x 1, p-values for the Jarque-Bera test(s).

    :rtype sOut: struct

Examples
----------------

::

    // A fragment: updateSSModel, param_vec_st, y and ssctl are set up
    // exactly as in the ssFit example.
    sOut = ssFit(&updateSSModel, param_vec_st, y, ssctl);

    // Recompute the diagnostics, e.g. after modifying sOut
    sOut = ssResidDiagnostics(sOut);

Remarks
-------

Every test is computed on ``standardized_forecast_errors`` AFTER dropping the first ``sOut.likelihoodburn`` periods -- this excludes the diffuse (or, under ``"mixed"`` init, non-stationary diffuse) phase, whose forecast errors are not directly comparable to the rest of the sample. This only affects these residual-based diagnostics; it does not trim ``sOut``'s reported log-likelihood/AIC/BIC (see e.g. :func:`ssStructuralTS`'s own Remarks for why). For a multivariate model (k_endog > 1), every diagnostic here decomposes into one univariate test per series -- there is no joint multivariate test.

Source
------

ssdiagnostics.src

.. seealso:: Functions :func:`ssFit`, :func:`ssSummaryStats`, :func:`ssLjungBox`, :func:`ssHeteroskedasticityTest`, :func:`ssJarqueBera`, :func:`ssSkewness`, :func:`ssKurtosis`
