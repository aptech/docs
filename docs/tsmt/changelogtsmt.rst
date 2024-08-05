===================
TSMT Change Log
===================

The following is a list of changes from the previous version of GAUSS.

4.0.0
------

#. Expanded output printing and implemented consistent printing format. All models now print standardized header with model details and evaluation statistics. 
#. Added new `tsmtModelDesc` structure to store model descriptions include dependent variable name, timespan, number of observations, and degrees of freedom.
#. Added new `tsmtSummaryStats` structure to hold model summary statistics include SSE, MSE, RMSE, SEE, R-squared, Adjuste R-squared, SSY, and the Durbin-Watson statistic. 
#. Expanded all functions to compute and return model summary statistics including SSE, MSE, RMSE, SEE, R-squared, Adjuste R-squared, SSY, and the Durbin-Watson statistic. 
#. Added functionality to allow date variables to be passed with independent and/or dependent variable. Dates are automatically detected and data timespans are reported. 
#. Standard errors now reported for constant for :func:`arimamt` model.
#. :func:`autoregmt` now accepts scalar input to specify that same number of lags should be used for all independent variables.  
#. Update printing of unit root tests to specify null hypothesis in output header and conclusion from test as a footer, whenever possible. 