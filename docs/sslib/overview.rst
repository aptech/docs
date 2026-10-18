GAUSS State-Space Modeling (SSLIB)
==============================================

Description
----------------
This package provides tools for estimating and evaluating state space models via Kalman filtering, for both time-invariant and time-varying-parameter (TVP) systems. In addition to providing the tools for custom state space models, it provides pre-built functions for state space modeling of:

* ARIMA models
* SARIMA models
* Structural time series (unobserved-components) models
* Dynamic factor models for nowcasting

New users should start with :doc:`getting-started`.

Installation
--------------
The GAUSS State Space library can be installed and updated directly in GAUSS using the `GAUSS Package Manager <https://www.aptech.com/blog/gauss-package-manager-basics/>`_. Version 2.0.0 and later (including 2.1.0, 2.1.1, and 2.1.2) require a working copy of **GAUSS 26.1.4+**.

.. note::
   **Version 1.0.0 remains the GAUSS 22+ compatible release.** Version 2.0.0 raises the minimum to GAUSS 26.1.4 in order to use typed structure returns and keyword arguments -- see :ref:`v1-to-v2-migration` below. Stay on 1.0.0 if you need to support GAUSS 22-26.0.

For more information on installing the GAUSS Package Manager please see our video blog, `Installing the GAUSS Package Manager <https://www.aptech.com/blog/installing-gauss-package-manager/>`_.

After installing, load the library together with its dependencies at the top of each program:

::

    library sslib, cmlmt, tsmt;

Dependencies
--------------
This library requires the installation of the following GAUSS libraries:

* `Time Series MT <https://store.aptech.com/gauss-applications-category/time-series-mt.html>`_
* `Constrained Maximum Likelihood MT <https://store.aptech.com/gauss-applications-category/constrained-maximum-likelihood-mt.html>`_

Commands
------------------------------

Estimating custom models
+++++++++++++++++++++++++++++++

========================== ===========================================================================================================
:func:`ssControlCreate`    Creates an :class:`ssControl` structure with default values and correctly sized system matrices.
:func:`ssFit`              Estimates parameters of a state-space model using Kalman filtering and maximum likelihood estimation.
:func:`ssIRF`              Computes the impulse response functions based on the final estimated parameters.
:func:`ssPredict`          Computes in sample predictions or out-of-sample forecasts based on the final estimated parameters.
:func:`ssPredictSE`        Computes the standard errors of the predictions/forecasts returned by :func:`ssPredict`, for building confidence intervals.
:func:`ssKalmanSmooth`     Computes fixed-interval (Rauch-Tung-Striebel) smoothed state estimates from a fitted model.
========================== ===========================================================================================================

Estimating time-varying-parameter models
+++++++++++++++++++++++++++++++++++++++++++++

========================== ===========================================================================================================
:func:`ssFitTVP`           Estimates parameters of a time-varying-parameter state-space model using Kalman filtering and maximum likelihood estimation.
:func:`ssIRFTVP`           Computes time-specific impulse response functions, with the system frozen at one chosen period.
:func:`ssPredictTVP`       Computes in-sample predictions or out-of-sample forecasts, with the system frozen at the last fitted period for the out-of-sample portion.
:func:`ssPredictSETVP`     Computes the standard errors of the predictions/forecasts returned by :func:`ssPredictTVP`, for building confidence intervals.
:func:`ssKalmanSmoothTVP`  Computes fixed-interval (Rauch-Tung-Striebel) smoothed state estimates from a fitted time-varying-parameter model.
========================== ===========================================================================================================

Pre-built models
+++++++++++++++++++++++++++

==============================  =================================================================================================================================================================
:func:`ssARIMA`                 Estimates an ARIMA(p, d, q) model via its state space representation, using Kalman filtering and maximum likelihood estimation.
:func:`ssSARIMA`                Estimates a seasonal ARIMA(p, d, q)(P_s, D_s, Q_s)_s model via its state space representation, using Kalman filtering and maximum likelihood estimation.
:func:`ssStructuralTS`          Estimates a structural time series (unobserved-components) model -- a local level or local linear trend, plus an optional seasonal component and stochastic cycle -- using the exact diffuse Kalman filter.
:func:`ssStructuralComponents`  Decomposes a fitted :func:`ssStructuralTS` model into its smoothed trend, seasonal, cycle, regression, signal and irregular components.
==============================  =================================================================================================================================================================


Dynamic factor models
+++++++++++++++++++++++++++

==============================  =================================================================================================================================================================
:func:`ssDFM`                   Estimates a dynamic factor model by EM for nowcasting monthly and quarterly series with missing data, returning smoothed series, nowcasts and factors.
:func:`ssDFMPredict`            Forecasts every series and factor of a fitted :func:`ssDFM` model, with standard errors.
==============================  =================================================================================================================================================================

Model evaluation
+++++++++++++++++++++

================================  =======================================================================================================================================================
:func:`ssgetAIC`                  Computes Akaike's information criterion from loglikelihood.
:func:`ssgetAICC`                 Computes the corrected Akaike's information criterion from loglikelihood.
:func:`ssgetBIC`                  Computes the Schwarz' Bayesian information criterion from loglikelihood.
:func:`ssgetHQIC`                 Computes the Hannan-Quinn information criterion from loglikelihood.
:func:`ssHeteroskedasticityTest`  Tests the null hypothesis of no heteroskedasticity by comparing the sum-of-squares of the first third of the sample to the sum-of-squares of last third of the sample. Analogous to a Goldfeld-Quandt test.
:func:`ssJarqueBera`              Performs the Jarque-Bera goodness-of-fit test on model residuals.
:func:`ssLjungBox`                Computes the Ljung-Box test for autocorrelation.
:func:`ssSkewness`                Computes the sample skewness.
:func:`ssKurtosis`                Computes the sample kurtosis.
:func:`ssResidDiagnostics`        Computes residual-based diagnostics (Ljung-Box, heteroskedasticity, Jarque-Bera, skew/kurtosis) from a filled ssOut structure.
:func:`ssSummaryStats`            Computes model summary statistics and information criteria from a filled ssOut structure.
================================  =======================================================================================================================================================

Filtering and printing
+++++++++++++++++++++++++++

========================== ===========================================================================================================
:func:`ssKalmanFilter`     Runs the ordinary (non-diffuse) Kalman filter directly against a filled ssModel structure and initial state.
:func:`ssPrint`            Prints a fitted model's full results table to the screen.
:func:`ssPrintArima`       :func:`ssPrint`'s counterpart for a model fit via ssARIMA/ssSARIMA.
========================== ===========================================================================================================



.. _v1-to-v2-migration:

Migrating from 1.0.0 to 2.x
--------------------------------

Version 2.0.0 requires **GAUSS 26.1.4+** and uses two of its language features throughout the public API:

* **Typed structure returns.** Every public procedure that returns a known structure declares it, so a result can be assigned without being declared first. This depends on the procedure declaration *and*, when calling through an installed package, on the library index (``.lcg``) metadata that records it -- so reinstall rather than copying source files.
* **Named arguments with explicit defaults.** Every documented optional argument is now a keyword parameter with a visible default instead of a positional "dynamic argument". **The positional order is unchanged**, so a 1.0.0 positional call that was valid in 1.0.0 still runs; the keyword names are part of the 2.0.0 public API contract. Positional arguments still cannot be skipped, so prefer keywords whenever an argument late in the list is needed.

Running unchanged does not always mean identical results: later releases fixed bugs and changed some defaults (for example, a single cycle's default starting period in :func:`ssStructuralTS`). Read the upgrade notes in ``CHANGELOG.md`` before refitting a model you have already reported.

Prefer the keyword form whenever more than one optional argument is supplied.

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - 1.0.0
     - 2.0.0
   * - ::

           struct ssControl ssctl;
           ssctl = ssControlCreate(4, 1);
     - ::

           ssctl = ssControlCreate(4, 1);
   * - ::

           struct ssOut sOut;
           sOut = ssStructuralTS(y, "level", 12);
     - ::

           sOut = ssStructuralTS(y, seasonal_period=12);
   * - ::

           sOut = ssStructuralTS(y, "trend", 12, 1);
     - ::

           sOut = ssStructuralTS(y,
                                 trend="trend",
                                 seasonal_period=12,
                                 cycle=1);
   * - Positionally, ``seasonal_type`` and ``seasonal_harmonics`` can only be
       reached by also passing real ``param_start`` and ``ssctl`` values.
     - ::

           sOut = ssStructuralTS(y,
                                 trend="trend",
                                 seasonal_period=4|12,
                                 seasonal_type={"dummy", "trig"},
                                 seasonal_harmonics=0|2);
   * - ::

           struct ssOut sOut;
           sOut = ssFit(&upd, params, y, ssctl);
     - ::

           sOut = ssFit(&upd, params, y, ssctl=ssctl);
   * - ::

           irf = ssIRF(sOut.ssmFinal, 20, 1, 0, 1);
     - ::

           irf = ssIRF(sOut.ssmFinal, 20, 1, cumulative=1);
   * - *(not available)*
     - ::

           components = ssStructuralComponents(sOut, y);

A handful of defaults could not be written as literals in the signature, because a GAUSS keyword default must be a literal and cannot refer to another parameter. Those use an empty-matrix ``{}`` sentinel resolved inside the procedure, with the same effective default as 1.0.0: ``ssControlCreate``'s ``k_posdef`` (defaults to ``k_states``), ``ssStructuralTS``'s ``param_start`` and ``ssctl``, ``ssPredict``/``ssPredictSE``'s ``start_pred``/``end_pred``, and ``ssJarqueBera``'s ``skew``/``kurtosis``.

Further Reading
-----------------


.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: State space modeling

    getting-started
    sscontrolcreate
    ssfit
    ssfittvp
    ssarima
    sssarima
    ssstructuralts
    ssstructuralcomponents
    ssdfm
    ssdfmpredict
    ssgetaic
    ssgetaicc
    ssgetbic
    ssgethqic
    ssheteroskedasticitytest
    ssirf
    ssirftvp
    ssjarquebera
    sskalmanfilter
    sskalmansmooth
    sskalmansmoothtvp
    sskurtosis
    ssljungbox
    ssprint
    ssprintarima
    sspredict
    sspredictse
    sspredicttvp
    sspredictsetvp
    ssresiddiagnostics
    ssskewness
    sssummarystats
