Time Series MT (TSMT)
=======================

Description
----------------
The GAUSS time series module TSMT provides a number of routines for performing:

* Pre-estimation data analysis.
* Model parameter estimation.
* Post-estimation diagnosis.

Installation
-----------------
Download TSMT throug the GAUSS package manager.

Commands
------------------------------

Time Series Functions
+++++++++++++++++++++++++++++++

========================== =====================================================================================================================
:func:`arimafit`           Estimates coefficients of a univariate time series model with autoregressive-moving average errors. Model may include fixed regressors.
:func:`arimass`            Estimates ARIMA models using a state space representation, the Kalman filter, and maximum likelihood.
:func:`autoregfit`         Estimates coefficients of a regression model with autoregressive errors of any specified order.
:func:`garchfit`           Estimates univariate GARCH model.
:func:`ecmfit`             Calculate and return parameter estimates for an error correction model.
:func:`kalmanfilter`       Data filtering algorithm.
:func:`sbreak`             Estimates the m-break structural break model.
:func:`switchfit`          Estimates the parameters of the Markov switching regression model.
:func:`tartest`            Estimates the p\ :sup:`th` order threshold autoregression model.
:func:`tscsfit`            Estimates the parameters of the pooled time-series cross-section regression model.
:func:`varmafit`           Computes exact maximum likelihood parameter estimates for a VARMA model.
:func:`vmdetrendmt`        Seasonally detrends data.
:func:`vmdiffmt`           Seasonally Differences matrices.
:func:`aggdata`            Aggregates time series data from higher to lower frequency.
:func:`arimapredict`       Estimates forecasts using estimation results obtained from :func:`arimaFit`.
:func:`breitung`           Panel series unit root testing.
:func:`cdtest`             Runs cross-sectional dependence, CD, tests for panel data.
:func:`dfgls`              Test for unit root in univariate time series.
:func:`garchmfit`          Estimates GARCH-in-mean model.
:func:`igarchfit`          Estimates integrated GARCH model, i.e., a model containing a unit root.
:func:`kpss`               Test for stationarity using a Lagrange Multiplier score statistic.
:func:`lsdvfit`            Estimates coefficients of a regression model with autoregressive errors of any specified order.
:func:`rolling`            Performs rolling OLS regressions for a provided vector of dependent data and matrix of independent regressors.
:func:`sarimass`           Estimates SARIMA models using a state space representation, the Kalman filter, and maximum likelihood.
:func:`selectlags`         Select lags based on method of statistical inference.
:func:`startest`           Estimates a p\ :sup:`th` order threshold autoregression and tests the hypothesis of a linear autoregression, using the statistics described in "Inference when a nuisance parameter is not identified under the null hypothesis." (Hansen, 1996).
:func:`varmapredict`       Calculates forecasts from a VARMAX model.
:func:`vmsdetrend`         Seasonally detrends data.
:func:`vmsdiffmt`          Seasonally Differences matrices.
:func:`zandrews`           The Zivot and Andrews (1992) unit root test uses a t-test statistic for testing the null hypothesis of stationarity.
========================== =====================================================================================================================

Further Reading
-----------------

* `How to Conduct Unit Root Tests in GAUSS <https://www.aptech.com/blog/how-to-conduct-unit-root-tests-in-gauss/>`_

.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Time Series Functions

    arimafit
    arimass
    autoregfit
    garchfit
    ecmfit
    kalmanfilter
    sbreak
    switchfit
    tartest
    tscsfit
    varmafit
    vmdetrendmt
    vmdiffmt
    aggdata
    arimapredict
    breitung
    cdtest
    dfgls
    garchmfit
    garchxfit
    igarchfit
    kpss
    lsdvfit
    rolling
    sarimass
    selectlags
    startest
    varmapredict
    vmsdetrend
    vmsdiffmt
    zandrews
