adjrsq
======

Purpose
-------
Finds the adjusted R-Squared statistic following the estimation of a linear regression model. It requires both the original data and the residuals from the estimate as inputs.

Format
------
.. function::  { r_sq, adj_rsq } = adjRsq(yt, res, num_vars)

  :param yt: data.
  :type yt: TxM matrix

  :param res: estimation residuals.
  :type res: TxM matrix

  :param num_vars: number of estimated coefficients (including constant) in the original regression.
  :type num_vars: Scalar

  :return r_sq: standard R-Squared statistics.
  :rtype r_sq: Mx1 matrix

  :return adj_rsq: adjusted R-Squared statistics.
  :rtype adj_rsq: Mx1 matrix

Example
-------
This example utilizes a simple multivariate linear model. To begin we generate a sample of independent data (Y):

::

  rndseed 89102;
  xt = rndn(100, 5);
  yt = 0.4 + 4.75*xt[., 1] + 0.9*xt[., 2] + 3.2*xt[., 3] - 2.1*xt[., 4] - 2.9*xt[., 5] + rndn(100, 1);

Next, estimate an ols model using the generated data:

::

  // Estimate OLS model
  struct olsmtControl oc0_2;
  struct olsmtOut oOut_2;
  oc0_2 = olsmtControlCreate();

  // Compute residuals
  oc0_2.res = 1;

  // Estimate model
  oOut_2 = olsmt(oc0_2, 0, yt, xt);

  res = oOut_2.resid;
  num_var = cols(xt) + oc0_2.con;

Finally, call adjRsq:

::

  // Residual input
  res = oOut_2.resid;

  // Number of variables
  num_var = cols(xt) + oc0_2.con;

  // Compute adjust Rsq
  { r, adj_r } = adjRsq(yt, res, num_var);

This produces the following output:

::

  Valid cases:        100      Dependent variable:       Y
  Missing cases:        0      Deletion method:       None
  Total SS:      3461.187      Degrees of freedom:      94
  R-squared:        0.972      Rbar-squared:         0.971
  Residual SS:     95.912      Std error of est:     1.010
  F(5,94):        659.640      Probability of F:     0.000
  Durbin-Watson:    2.093
  Standard         Prob   Standardized Cor with
  Var  Estimate Error   t-value  >|t|  Estimate  Dep Var
  --------------------------------------------------------
  CONST  0.2996  0.1032   2.9036   0.005   ---        ---
  X1     4.7128  0.1076  43.7811   0.000   0.7671   0.6528
  X2     0.9561  0.1058   9.0379   0.000   0.1600   0.3434
  X3     3.3507  0.1178  28.4434   0.000   0.5081   0.3188
  X4    -2.0465  0.1078 -18.9913   0.000  -0.3302  -0.2412
  X5    -2.8348  0.1055 -26.8741   0.000  -0.4814  -0.3634

  The standard R squared is 0.972289

  The adjusted R squared is 0.970502

Library
-------
tsmt

Source
------
var_lm.src
