
hacSE
==============================================

Purpose
----------------
 Procedure to compute the Newey-West HAC robust standard errors.

Format
----------------
.. function:: vce_hac = hacSE(x, resid [, constant, nwtrunc, ss])
              vce_hac = hacSE(dataset, formula, resid [, constant, nwtrunc, ss])
              vce_hac = hacSE(dataframe, formula, resid [, constant, nwtrunc, ss])

    :param x: independent regression variables, should not include a const.
    :type x: NxK matrix

    :param resid: ols residuals.

        .. NOTE:: if using :func:`olsmt` these are stored in the :class:`olsOut` structure member *resid*.

    :type resid: NTx1 matrix

    :param dataset: name of dataset.
    :type dataset: string

    :param formula: `formula string` of the independent variables.
        E.g :code:`"X1 + X2"`, '*X1*' and '*X2*' are names of independent variables;
    :type formula: String

    :param constant: Optional input, indicator variable for including a const. 1 for including a const, 0 for no const. Default = 1.
    :type const: Scalar

    :param nwtrunc: Optional input, scalar, the Newey-West iteration constant. Set to 0 to have GAUSS use Newey and West's the suggested number of iterations, 4(T/100)^2/9 where T is the number of observations. Default = 0;
    :type nwtrunc: Scalar

    :param ss: Optional input, indicator variable for using the small sample correction. 1 to compute the small sample correction, 0 for no correction. Default = 1.
    :type ss: Scalar

    :return vce_hac: Newey-West HAC-robust variance-covariance matrix.
    :rtype vce_hac: KxK matrix

Examples
----------------

::

    new;

    // Load data using auto dataset
    fname = getGAUSSHome $+ "examples/regsmpl.dta";
    data = loadd(fname);

    // Control structure
    struct olsmtControl o_ctl;
    o_ctl = olsmtControlCreate();

    // Turn on to estimate residuals
    o_ctl.res = 1;

    // Declare output structure
    struct olsmtOut o_out;

    // Run initial ols
    o_out = olsmt(fname, "ln_wage ~ age + age:age + tenure", o_ctl);

This estimates the OLS regression and finds the i.i.d. standard errors:

::

    Valid cases:                 28101      Dependent variable:             ln_wage
    Missing cases:                 433      Deletion method:               Listwise
    Total SS:                 6414.965      Degrees of freedom:               28097
    R-squared:                   0.164      Rbar-squared:                     0.164
    Residual SS:              5360.440      Std error of est:                 0.437
    F(3,28097):               1842.448      Probability of F:                 0.000
    Durbin-Watson:               0.906

                             Standard                 Prob   Standardized  Cor with
    Variable     Estimate      Error      t-value     >|t|     Estimate    Dep Var
    -------------------------------------------------------------------------------

    const        0.333982    0.050441    6.621206     0.000       ---         ---
    age          0.075217    0.003474   21.653863     0.000    1.054270    0.278922
    age:age     -0.001085    0.000058  -18.862899     0.000   -0.916788    0.265497
    tenure       0.039088    0.000774   50.479037     0.000    0.306895    0.370584

Calling :func:`hacrSE` estimates the HAC-robust standard errors:

::

    // Find cluster-robust standard errors regression includes const
    vce_hac = hacse(fname, "age + age:age + tenure", o_out.resid );

The resulting standard errors are:

::

              VARIABLE     HAC SE
      -------------------------------------

                 const         0.066368
                   age        0.0047206
               age:age       8.0260e-05
                tenure        0.0013722
      -------------------------------------

.. seealso:: Functions :func:`olsmt`, :func:`robustSE`, :func:`clusterSE`

|
