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
| :func:`smooth`         | Computes a two-dimensional interpolatory spline.                            |
+------------------------+-----------------------------------------------------------------------------+

Finding moving averages
----------------------------------------------
Three procedures are available for computing moving averages.

* The :func:`movingave` procedure computes the moving average given a specified order of moving average.
* The :func:`movingaveWgt` procedure computes the weighted moving average given a specified order and weights.
* The :func:`movingaveExpWgtave` procedure computes  exponentially weighted moving average of a series given a specified order of moving average and a smoothing coefficient.

Example: Smoothing a random walk series
++++++++++++++++++++++++++++++++++++++++++

::

  // Create random data, setting initial seed
  // value to be the hundredths of a second
  // since midnight
  numPoints = 1000;
  seed = hsec;
  { delta, state } = rndn(numPoints, 1, seed);

  // Set mean of data to be > 0
  // to give data long term positive bias
  delta = delta + 0.01;

  // Increase magnitude of delta to
  // create desired level of volatiliy
  delta = 2*delta;

  // Instantiate y : index price data
  y = 1000*ones(numPoints,1);

  // Loop through y and add the cumulative
  // sums of delta to create random walk
  for i(2, numPoints, 1);
        y[i]= y[i-1] + delta[i];
  endfor;

  // Find moving average
  twentyMA = movingave(y, 20);

  // Find moving average
  twentyExpWgtMA = movingaveExpwgt(y, 20, 0.8);


Locally weighted linear regression smoothing
----------------------------------------------
The :func:`loessmt` procedure smooths data using locally weighted linear regression. Because it relies on linear regression, the function requires both a dependent variable to be smoothed and a matrix of independent variables to be used in the weighted regression.

Example: Lowess smoother
+++++++++++++++++++++++++++++++++

::

  // Load dataset
  fname = getGAUSSHome() $+ "examples/lowess1.dta";
  data = loadd(fname, "h1 + depth");

  // Define independent variable
  depvar = data[., 1];

  // Defined dependent variable
  indvars = data[., 2];

  { yhat, ys, xs } = loessmt(depvar, indvars);
