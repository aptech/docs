===================
TSMT Change Log
===================

The following is a list of changes from the previous version of GAUSS.

4.0.0
------

#. New function: :func:`svarFit` estimates structural vector autoregressive models. Supports zero short-run restrictions, zero long-run restrictions, and sign restrictions for structural identification.
#. New function: :func:`plotIrf` plots impulse response functions after estimating SVAR models using :func:`svarFit`.
#. New function: :func:`getFEVD` computes forecast error variance decomposition using IRFs after :func:`svarFit`. 
#. New function: :func:`plotFEVD` generates area plot of forecast error variance decompositions after :func:`svarFit`.
#. New function: :func:`plotHD` generates stacked bar plot of historical decompositions after :func:`svarFit`.
#. New function: :func:`sbreakFit` estimates m-break structural break models. Includes improvements over :func:`sbreak`, such as formula string inputs, user-configurable settings, dataframe metadata support, and structured output formatting.  
#. New function: :func:`getP0` computes prior covariance initialization for use with :func:`kalmanFilter`. Supports both `diffuse` and `stationary` initialization methods, with automatic root modulus inspection to determine the appropriate approach.
#. New standardized output printing across all models, including a header with model details and summary evaluation statistics. 
#. Enhancement: Added :func:`tsmtModelDesc` structure to store model metadata such as dependent variable name, time span, number of observations, and degrees of freedom.
#. Enhancement: Added :func:`tsmtSummaryStats` structure to hold model diagnostics including SSE, MSE, RMSE, SEE, R-squared, Adjusted R-squared, SSY, and the Durbin-Watson statistic.
#. Enhancement: All modeling functions now compute and return summary statistics (SSE, MSE, RMSE, SEE, R-squared, Adjusted R-squared, SSY, Durbin-Watson).
#. Expanded functionality: Models now accept time series date variables for dependent and independent variables. Date ranges are automatically detected and reported.
#. Expanded functionality: Standard errors are now reported for the constant term in the :func:`arimaFit` model.
#. Enhancement: :func:`autoregmt` now accepts a scalar input to specify the same lag length for all independent variables.
#. Enhancement: Unit root test outputs have been updated to include null hypotheses in the header and test conclusions in the footer (where applicable).
#. Enhancement: :func:`autoregmt` now checks for redundant constants or non-varying variables in the independent variable matrix.
#. Enhancement: :func:`selectLags` now accepts optional arguments `p_max`, `method`, and `printout`, all with sensible internal defaults.
#. Enhancement: :func:`arimaSS` now accepts optional arguments for `p`, `d`, `q`, `constant`, and `trend`, with documented default values.
#. Enhancement: Improved stationarity and invertibility enforcement in :func:`arimaSS` using a `tanh` transformation approach. This method improves numerical stability, supports higher-order AR and MA terms, and enhances convergence behavior.
#. Enhancement: The time trend component for :func:`arimaSS` is now centered and scaled for improved numerical conditioning. 
#. Enhancement: Special handling added to :func:`arimaSS` for the case with no ARMA terms. In these models, MLE is skipped and closed-form OLS estimates with valid standard errors are returned.
#. Enhancement: New improved starting values implemented for :func:`arimaSS` using a naive regression-based approach.
#. Improved covariance estimation in :func:`arimaSS`: Implemented the delta method (a Jacobian-adjusted sandwich estimator) to compute standard errors that properly account for parameter transformations used to enforce stationarity and invertibility.
#. Enhancement: :func:`arimaSS` covariance computation now falls back to a pseudo-inverse when the Hessian is singular or near-singular.
#. Enhancement: :func:`arimaPredict` now checks for metadata and prints dates and variable names.
#. Enhancement: :func:`arimaPredict` now supports optional graph generation.
#. Bug fix: :func:`kalmanFilter` previously mishandled trend components. This has been corrected.
#. Bug fix: :func:`arimaSS` now properly supports models with no AR or MA terms.
 
