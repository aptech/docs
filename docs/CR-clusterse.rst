
clusterSE
==============================================

Purpose
----------------
 Procedure to compute the White cluster-robust standard errors.

Format
----------------
.. function:: vce_cluster = clusterSE(x, grp, resid[, const[, verbose[, var_names]]])
              vce_cluster = clusterSE(dataset, formula, grp_var, resid[, const[, verbose[, var_names]]])

    :param x: independent regression variables, should not include a const.
    :type x: NxK matrix

    :param grp: vector of group indicators.
    :type grp: NTx1 matrix

    :param resid: ols residuals.

        .. NOTE:: if using :func:`olsmt` these are stored in the :class:`olsOut` structure member *resid*.

    :type resid: NTx1 matrix

    :param dataset: name of dataset.
    :type dataset: string

    :param formula: `formula string` of the independent variables.
        E.g :code:`"X1 + X2"`, '*X1*' and '*X2*' are names of independent variables;
    :type formula: String

    :param grp_var: name of the group variable.
    :type grp_var: string

    :param const: Optional input, indicator variable for including a const. 1 for including a const, 0 for no const. Default = 1.
    :type const: scalar

    :param verbose: Optional input, 1 to print results, 0 for no printing. Default = 1.
    :type verbose: scalar

    :param var_names: Optional input, variable names. Default = X1, X2, ..., XK.
    :type var_names: string array

    :returns: **vce_cluster** (*KxK matrix*) - White cluster-robust variance-covariance matrix.


Examples
----------------

::

    new;

    // Load data using auto dataset
    fname = getGAUSSHome $+ "examples/regsmpl.dta";
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

Calling :func:`clusterSE` estimates the cluster-robust standard errors:

::

    // Find cluster-robust standard errors regression includes const
    vce_cluster = clusterse(fname, "age + age:age + tenure", "idcode", o_out.resid );

The results:

::

    Total observations:                                        28101
    Number of variables:                                           4

              VARIABLE     Clustered SE
      -------------------------------------

                 const         0.064192
                   age        0.0045711
               age:age       7.7846e-05
                tenure        0.0014425
      -------------------------------------

.. seealso:: Functions :func:`olsmt`, :func:`robustSE`

|
