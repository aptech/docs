Time Series MT (TSMT)
=======================
A time series package for GAUSS.

Description
----------------
Provides tools for comprehensive treatment of time series models, including model diagnostics, MLE and state-space estimation,
and forecasts. Time Series MT also includes tools for managing panel series data and estimating and diagnosing panel series models,
including random effects and fixed effects.


Installation
--------------
Please `contact us <https://www.aptech.com/contact-us>`_ with to request pricing and installation information.

If you already own TSMT, you can use the `GAUSS Package Manager <https://www.aptech.com/blog/gauss-package-manager-basics/>`_ to install TSMT.

Requires GAUSS/GAUSS Engine v18 or higher.

Commands
------------------------------

Univariate Time Series Models
+++++++++++++++++++++++++++++++

Conditional mean models
^^^^^^^^^^^^^^^^^^^^^^^^

========================== =====================================================================================================================
:func:`arimafit`           Estimates coefficients of a univariate time series model with autoregressive-moving average errors. Model may include fixed regressors.
:func:`arimass`            Estimates ARIMA models using a state space representation, the Kalman filter, and maximum likelihood.
:func:`arimapredict`       Estimates forecasts using estimation results obtained from :func:`arimaFit`.
:func:`autoregfit`         Estimates coefficients of a regression model with autoregressive errors of any specified order.
:func:`sarimass`           Estimates SARIMA models using a state space representation, the Kalman filter, and maximum likelihood.
========================== =====================================================================================================================

Conditional variance models
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
========================== =====================================================================================================================
:func:`garchfit`           Estimates univariate GARCH model.
:func:`garchgjrfit`        Estimates GARCH-GJR model. 
:func:`garchmfit`          Estimates GARCH-in-mean model.
:func:`igarchfit`          Estimates integrated GARCH model, i.e., a model containing a unit root.
========================== =====================================================================================================================

Multivariate Time Series Models
++++++++++++++++++++++++++++++++

Conditional mean models
^^^^^^^^^^^^^^^^^^^^^^^^
========================== =====================================================================================================================
:func:`varmafit`           Computes exact maximum likelihood parameter estimates for a VARMA model.
:func:`ecmfit`             Calculate and return parameter estimates for an error correction model.
:func:`svarfit`            Estimate structural VAR models using short-run, long-run, or sign restrictions. 
========================== =====================================================================================================================

Panel data and other models
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
========================== =====================================================================================================================
:func:`tscsfit`            Estimates the parameters of the pooled time-series cross-section regression model.
:func:`lsdvfit`            Estimates coefficients of a regression model with autoregressive errors of any specified order.
:func:`kalmanfilter`       Data filtering algorithm.
========================== =====================================================================================================================


Nonlinear Time Series Model
++++++++++++++++++++++++++++++++
========================== =====================================================================================================================
:func:`switchfit`          Estimates the parameters of the Markov switching regression model.
:func:`sbreak`             Estimates the m-break structural break model.
:func:`tartest`            Estimates the p\ :sup:`th` order threshold autoregression model.
========================== =====================================================================================================================

Miscellaneous
++++++++++++++

========================== =====================================================================================================================
:func:`aggdata`            Aggregates time series data from higher to lower frequency.
:func:`breitung`           Panel series unit root testing.
:func:`ips`                Conduct the Im, Pesaran, and Shin panel data unit root test.  
:func:`cdtest`             Runs cross-sectional dependence, CD, tests for panel data.
:func:`dfgls`              Test for unit root in univariate time series.
:func:`hansen`             Test for stability of all parameters.
:func:`httest`             Perform the Harris–Tzavalis panel series unit root testing.
:func:`kpss`               Test for stationarity using a Lagrange Multiplier score statistic.
:func:`lagreport`          Compute and graph the autocorrelation function and partial autocorrelation function for a time series.
:func:`rolling`            Performs rolling OLS regressions for a provided vector of dependent data and matrix of independent regressors.
:func:`selectlags`         Select lags based on method of statistical inference.
:func:`startest`           Estimates a p\ :sup:`th` order threshold autoregression and tests the hypothesis of a linear autoregression, using the statistics described in "Inference when a nuisance parameter is not identified under the null hypothesis." (Hansen, 1996).
:func:`tsdiff`             Differences matrices with or without seasonality.
:func:`varmapredict`       Calculates forecasts from a VARMAX model.
:func:`vmdetrendmt`        Detrends data. (DEPRECATED)
:func:`vmdiffmt`           Differences matrices.
:func:`vmsdetrend`         Seasonally detrends data.
:func:`vmsdiffmt`          Seasonally differences matrices. (DEPRECATED)
:func:`zandrews`           The Zivot and Andrews (1992) unit root test uses a t-test statistic for testing the null hypothesis of stationarity.
========================== =====================================================================================================================


Further Reading
-----------------

* `Introduction to the Fundamentals of Time Series Data and Analysis <https://www.aptech.com/blog/introduction-to-the-fundamentals-of-time-series-data-and-analysis/>`_
* `Introduction to the Fundamentals of Vector autoregressive Models <https://www.aptech.com/blog/introduction-to-the-fundamentals-of-vector-autoregressive-models/>`_
* `The Structural VAR Model at Work: Analyzing Monetary Policy <https://www.aptech.com/blog/the-structural-var-model-at-work-analyzing-monetary-policy/>`_
* `How to Conduct Unit Root Tests in GAUSS <https://www.aptech.com/blog/how-to-conduct-unit-root-tests-in-gauss/>`_
* `A Guide to Conducting Cointegration Tests <https://www.aptech.com/blog/a-guide-to-conducting-cointegration-tests/>`_
* `Unit Root Tests with Structural Breaks <https://www.aptech.com/blog/unit-root-tests-with-structural-breaks/>`_
* `Introduction to Structural Breaks <https://www.aptech.com/structural-breaks/>`_

.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Time Series Functions

    adjrsq
    aggdata
    arimafit
    arimamtcontrolcreate
    arimapredict
    arimass
    autocormt
    autocovmt
    automtcontrolcreate
    autoregfit
    breitung
    cdtest
    chowfcst
    covmmt
    cusum
    dfgls
    ecmfit
    garchfit
    garchgjrfit
    garchmfit
    hansen 
    httest 
    igarchfit
    ips
    kalmanfilter
    kpss
    lagreport
    lsdvfit
    plotfevd 
    plotirf
    rolling
    sarimass 
    sbreak
    selectlags
    startest
    svarfit
    switchfit
    tartest
    tscsfit
    tsdiff
    varmafit
    varmapredict
    vmdetrendmt
    vmdiffmt
    vmsdetrend
    zandrews
