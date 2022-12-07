Data Smoothing
=============================
+------------------------+-----------------------------------------------------------------------------+
|      Function          |  Description                                                                |
+========================+================================+============================================+
|:func:`movingave`       | Computes moving average of a series.                                        |
+------------------------+-----------------------------------------------------------------------------+
|:func:`movingaveExpWgt` | Computes exponentially weighted moving average of a series.                 |
+------------------------+-----------------------------------------------------------------------------+
|:func:`movingaveWgt`    | Computes weighted moving average of a series                                |
+------------------------+-----------------------------------------------------------------------------+
| :func:`loessmt`        | Computes coefficients of locally weighted regression.                       |
+------------------------+-----------------------------------------------------------------------------+
| :func:`curve`          | Computes a one-dimensional smoothing curve.                                 |
+------------------------+-----------------------------------------------------------------------------+
| :func:`spline`         | Computes a two-dimensional interpolatory spline.                            |
+------------------------+-----------------------------------------------------------------------------+

Finding moving averages
----------------------------------------------
Three procedures are available for computing moving averages.

* The :func:`movingave` procedure computes the moving average given a specified order of moving average.
* The :func:`movingaveWgt` procedure computes the weighted moving average given a specified order and weights.
* The :func:`movingaveExpWgt` procedure computes exponentially weighted moving average of a series given a specified order of moving average and a smoothing coefficient.

Example: Smoothing a random walk series
++++++++++++++++++++++++++++++++++++++++++

::

  // Load data
  fname = getGAUSSHome("examples/tbill_3mo.xlsx");
  y = loadd(fname, "date($obs_date, '%m/%d/%Y %T.%L') + tbill_3m");

  // Find 3 month moving average
  twentyMA = movingave(y[., "tbill_3m"], 3);

  // Find 3 month exponenetial moving average
  twentyExpWgtMA = movingaveExpwgt(y[., "tbill_3m"], 3, 0.8);


Locally weighted linear regression smoothing
----------------------------------------------
The :func:`loessmt` procedure smooths data using locally weighted linear regression. Because it relies on linear regression, the function requires both a dependent variable to be smoothed and a matrix of independent variables to be used in the weighted regression.

Example: Lowess smoother
+++++++++++++++++++++++++++++++++

::

  // Load dataset
  fname = getGAUSSHome("examples/lowess1.dta");
  data = loadd(fname, "h1 + depth");

  // Define independent variable
  depvar = data[., "h1"];

  // Defined dependent variable
  indvars = data[., "depth"];

  { yhat, ys, xs } = loessmt(depvar, indvars);
