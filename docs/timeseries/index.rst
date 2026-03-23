GAUSS Time Series
==================

A comprehensive time series analysis package for GAUSS, covering ARIMA/SARIMA,
VAR/BVAR with stochastic volatility, structural identification, forecasting,
and forecast evaluation.

Description
-----------

**GAUSS Time Series** consolidates TSMT, SSLIB, and FANPAC into a single product.
It provides:

- **Univariate models:** ARIMA, SARIMA, ARIMAX with automatic order selection
- **Vector autoregression:** OLS VAR, Bayesian VAR (Minnesota prior), BVAR with stochastic volatility
- **Structural identification:** Cholesky IRF, generalized IRF, sign-restricted SVAR
- **Forecasting:** Point, density, and conditional (scenario) forecasts
- **Model comparison:** Marginal likelihood, Diebold-Mariano test, Model Confidence Set
- **Diagnostics:** MCMC convergence (R-hat, ESS), forecast calibration (PIT)

Installation
------------

Please `contact us <https://www.aptech.com/contact-us>`_ for pricing and installation information.

Requires GAUSS v26 or higher.

Usage::

    library timeseries;

Commands
--------

ARIMA / Univariate
+++++++++++++++++++

.. list-table::
   :widths: auto

   * - :func:`arimaFit`
     - Fit ARIMA, SARIMA, or ARIMAX models with automatic or fixed order selection.
   * - :func:`arimaForecast`
     - Generate h-step-ahead forecasts with prediction intervals.
   * - :func:`arimaControlCreate`
     - Create control structure with default settings.
   * - :func:`arimaResults`
     - Reprint estimation summary table.
   * - :func:`arimaCoefTable`
     - Return coefficient table as dataframe.

VAR Estimation
+++++++++++++++

.. list-table::
   :widths: auto

   * - :func:`varFit`
     - Fit VAR(p) by OLS with stability diagnostics.
   * - :func:`bvarFit`
     - Fit Bayesian VAR with conjugate Minnesota or flat prior.
   * - :func:`bvarSvFit`
     - Fit BVAR with stochastic volatility and optional SSVS variable selection.
   * - :func:`varLagSelect`
     - Select lag order by AIC, BIC, or Hannan-Quinn.
   * - :func:`bvarHyperopt`
     - Optimize Minnesota hyperparameters via marginal likelihood (GLP 2015).

Forecasting
++++++++++++

.. list-table::
   :widths: auto

   * - :func:`varForecast`
     - Point forecasts with confidence intervals from VAR.
   * - :func:`bvarForecast`
     - Posterior predictive forecasts with credible bands.
   * - :func:`bvarSvForecast`
     - Density forecasts from SV-BVAR with time-varying volatility.
   * - :func:`condForecast`
     - Conditional (scenario) forecasts with hard constraints.

Impulse Responses & Structural Analysis
++++++++++++++++++++++++++++++++++++++++

.. list-table::
   :widths: auto

   * - :func:`irfCompute`
     - Orthogonalized (Cholesky) impulse response functions.
   * - :func:`irfSvCompute`
     - Posterior IRF bands from SV-BVAR draws.
   * - :func:`girfCompute`
     - Generalized IRF (Pesaran & Shin 1998), ordering-invariant.
   * - :func:`fevdCompute`
     - Forecast error variance decomposition.
   * - :func:`hdCompute`
     - Historical decomposition into structural shock contributions.
   * - :func:`irfPlotData`
     - Reshape IRF results into plot-ready dataframe.

SVAR Identification
++++++++++++++++++++

.. list-table::
   :widths: auto

   * - :func:`svarIdentify`
     - Find a sign-restricted structural rotation.
   * - :func:`svarIrf`
     - Posterior sign-restricted IRF, cumulative IRF, and FEVD bands.

Diagnostics
++++++++++++

.. list-table::
   :widths: auto

   * - :func:`varDiagnose`
     - MCMC convergence diagnostics (R-hat, ESS, acceptance rates).
   * - :func:`varDiagnoseMulti`
     - Multi-chain convergence diagnostics.
   * - :func:`varDiagnosePrint`
     - Reprint diagnostics summary.
   * - :func:`grangerTest`
     - Granger causality F-test.

Forecast Evaluation
++++++++++++++++++++

.. list-table::
   :widths: auto

   * - :func:`fcScore`
     - Compute scoring rules (RMSE, MASE, sMAPE).
   * - :func:`dmTest`
     - Diebold-Mariano test for equal predictive ability.
   * - :func:`cwTest`
     - Clark-West test for nested model comparison.
   * - :func:`mcsTest`
     - Model Confidence Set (Hansen, Lunde & Nason 2011).
   * - :func:`pitTest`
     - PIT calibration tests (KS, chi-squared, Berkowitz).
   * - :func:`pitHistogram`
     - PIT histogram bin counts.

Utilities
++++++++++

.. list-table::
   :widths: auto

   * - :func:`varCompanion`
     - Extract companion matrix, eigenvalues, and stability indicator.
   * - :func:`varCoefTable`
     - Return coefficient table as dataframe.
   * - :func:`varResults`
     - Reprint estimation summary for any result type.
   * - :func:`stlDecompose`
     - Seasonal-Trend decomposition via LOESS (STL).
   * - :func:`fcMetrics`
     - Compute RMSE, MASE, and sMAPE.

Plotting
+++++++++

.. list-table::
   :widths: auto

   * - :func:`plotForecast`
     - Forecast fan chart with historical data and prediction bands.
   * - :func:`plotIrf`
     - Impulse response function grid (m × m).
   * - :func:`plotSvIrf`
     - Posterior IRF grid with credible bands from SV-BVAR.
   * - :func:`plotResiduals`
     - Residual diagnostics: time plot, ACF, histogram.
   * - :func:`plotStl`
     - STL decomposition: data, trend, seasonal, remainder.

Control Structure Creators
+++++++++++++++++++++++++++

.. list-table::
   :widths: auto

   * - :func:`varControlCreate`
     - Create :class:`varControl` with defaults.
   * - :func:`bvarControlCreate`
     - Create :class:`bvarControl` with defaults.
   * - :func:`bvarSvControlCreate`
     - Create :class:`bvarSvControl` with defaults.
   * - :func:`svForecastControlCreate`
     - Create :class:`svForecastControl` with defaults.
   * - :func:`svarControlCreate`
     - Create :class:`svarControl` with defaults.

.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: ARIMA

    arimafit
    arimaforecast
    arimacontrolcreate
    arimaresults
    arimacoeftable

.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Guides

    getting-started
    getting-started-arima
    choosing-a-var-model
    comparison
    textbook-mapping
    bgr-replication
    var-verification

.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: VAR Estimation

    varfit
    bvarfit
    bvarsvfit
    varlagselect
    bvarhyperopt
    varcontrolcreate
    bvarcontrolcreate
    bvarsvcontrolcreate

.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Forecasting

    varforecast
    bvarforecast
    bvarsvforecast
    condforecast
    svforecastcontrolcreate

.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: IRF / FEVD / HD

    irfcompute
    irfsvcompute
    girfcompute
    fevdcompute
    hdcompute
    irfplotdata

.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: SVAR

    svaridentify
    svarirf
    svarcontrolcreate

.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Diagnostics

    vardiagnose
    vardiagnosemulti
    vardiagnoseprint
    grangertest

.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Forecast Evaluation

    fcscore
    dmtest
    cwtest
    mcstest
    pittest
    pithistogram

.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Utilities

    varcompanion
    varcoeftable
    varresults
    stldecompose
    fcmetrics

.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Plotting

    plotforecast
    plotirf
    plotsvirf
    plotresiduals
    plotstl
