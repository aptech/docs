===================
TSMT Change Log
===================

The following is a list of changes from the previous version of GAUSS.

4.0.0
------

#. Expanded output printing and implemented consistent printing format. All models now print standardized header with model details and evaluation statistics. 
#. Enhancement: Added new `tsmtModelDesc` structure to store model descriptions include dependent variable name, timespan, number of observations, and degrees of freedom.
#. Enhancement: Added new `tsmtSummaryStats` structure to hold model summary statistics include SSE, MSE, RMSE, SEE, R-squared, Adjuste R-squared, SSY, and the Durbin-Watson statistic. 
#. Enhancement: Expanded all functions to compute and return model summary statistics including SSE, MSE, RMSE, SEE, R-squared, Adjuste R-squared, SSY, and the Durbin-Watson statistic. 
#. Expanded functionality: Added functionality to allow date variables to be passed with independent and/or dependent variable. Dates are automatically detected and data timespans are reported. 
#. Expanded functionality: Standard errors now reported for constant for :func:`arimamt` model.
#. Enhancement: :func:`autoregmt` now accepts scalar input to specify that same number of lags should be used for all independent variables.  
#. Update printing of unit root tests to specify null hypothesis in output header and conclusion from test as a footer, whenever possible. 
#. Enhancement: :func:`autoregmt` now checks for model constant and additional non-variant variables in the independent variables.
#. Enhancement: :func:`selectLags` now takes p_max, method, and printout as optional arguments with internal defaults.  