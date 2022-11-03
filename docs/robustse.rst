
robustSE
==============================================

Purpose
----------------
 Procedure to compute the Huber-White heteroscedastic robust standard errors.
 The procedure uses the "sandwich" variance-covariance estimator with a small sample correction of :math:`(n)/(n-1)`.

Format
----------------
.. function:: vce_robust = robustSE(x, resid [, const, verbose, var_names])
              vce_robust = robustSE(dataset, formula, resid [, const, verbose, var_names])
              vce_robust = robustSE(dataframe, formula, resid [, const, verbose, var_names])

    :param x: independent regression variables, should not include a constant.
    :type x: NxK matrix

    :param dataset: name of dataset.
    :type dataset: string

    :param formula: formula string of the independent variables. E.g ``"X1 + X2"``, ``X1`` and ``X2`` are names of independent variables;
    :type formula: string

    :param resid: regression residuals.
    :type resid: Nx1 vector

    :param const: Optional input, indicator variable for including a constant. 1 for including a constant, 0 for no constant. Default = 1.
    :type const: scalar

    :param verbose: Optional input, 1 to print results, 0 for no printing. Default = 1.
    :type verbose: scalar

    :param var_names: Optional input, variable names. Default = ``X1, X2, ..., XK``.
    :type var_names: string array

    :return vce_robust: Huber-White heteroscedastic robust variance-covariance matrix.

    :rtype vce_robust: KxK matrix

Examples
----------------

::

    new;

    // Load data from 'auto' dataset
    fname = getGAUSSHome $+ "/examples/auto.dat";
    data = loadd(fname);

    // Transform data
    mpg = data[., 3];
    weight = data[., 7];
    foreign = data[., 12];

    // Set independent and dependent variables
    y = ((1/mpg) ./ weight) * 100 * 1000;
    x = foreign;

    // Control structure
    struct olsmtControl o_ctl;
    o_ctl = olsmtControlCreate();

    // Turn on to estimate residuals
    o_ctl.res = 1;

    // Declare output structure
    struct olsmtOut o_out;

    // Run initial ols
    o_out = olsmt("", y, x, o_ctl);

This estimates the OLS regression and finds the i.i.d. standard errors:

::

      Valid cases:                    74      Dependent variable:                   Y
      Missing cases:                   0      Deletion method:                   None
      Total SS:                    4.298      Degrees of freedom:                  72
      R-squared:                   0.218      Rbar-squared:                     0.207
      Residual SS:                 3.361      Std error of est:                 0.216
      F(1,72):                    20.068      Probability of F:                 0.000
      Durbin-Watson:               2.455

                               Standard                 Prob   Standardized  Cor with
      Variable     Estimate      Error      t-value     >|t|     Estimate    Dep Var
      -------------------------------------------------------------------------------

      CONSTANT     1.609004    0.029961   53.703680     0.000       ---         ---
      X1           0.246153    0.054949    4.479678     0.000    0.466867    0.466867

Calling :func:`robustSE` estimates the heteroscedastic-robust standard errors:

::

    // Find robust standard errors
    vce_robust = robustSE(x, o_out.resid);

The results:

::

      Total observations:                                           74
      Number of variables:                                           2

              VARIABLE        Robust SE
      -------------------------------------

              CONSTANT         0.023453
                    X1         0.067924
      -------------------------------------

.. seealso:: Functions :func:`olsmt`, :func:`clusterSE`, :func:`hacSE`
