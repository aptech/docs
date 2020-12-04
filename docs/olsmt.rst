
olsmt
==============================================

Purpose
----------------

Computes a least squares regression.

Format
----------------
.. function:: out = olsmt(dataset, formula[, ctl])
              out = olsmt(dataset, depvar, indvars[, ctl])

    :param dataset: name of dataset, dataframe in memory, or null string.
        If *dataset* is a null string, the procedure assumes that the actual data has been passed in the next two arguments.
    :type dataset: string or dataframe

    :param formula: formula string of the model.
        E.g ``"y ~ X1 + X2"``, ``y`` is the name of dependent variable, ``X1`` and ``X2`` are names of independent variables;

        E.g ``"y ~ ."``, ``.`` means including all variables except dependent variable ``y``;

        E.g ``"y ~ -1 + X1 + X2"``, ``-1`` means no intercept model.

    :type formula: string

    :param depvar: If *dataset* contains a string, then *depvar* can be a:

        =========== ==============
           type         value
        =========== ==============
        string      name of dependent variable
        scalar      index of dependent variable. If scalar 0, the last column of the dataset will be used.
        =========== ==============

        If *dataset* is a null string, name of dataframe, or 0:

        =========== ==============
           type         value
        =========== ==============
        Nx1 vector  the dependent variable.
        =========== ==============

    :param indvars: If *dataset* contains a string:

        ===================== ==============
           type                   value
        ===================== ==============
        Kx1 character vector  names of independent variables
        Kx1 numeric vector    indices of independent variables. These can be any size subset of the variables in the dataset
                              and can be in any order. If a scalar 0 is passed, all columns of the dataset will be used except
                              for the one used for the dependent variable.
        ===================== ==============

        If *dataset* is a null string, dataframe, or 0:

        =========== ==============
           type         value
        =========== ==============
        NxK matrix  the independent variables
        =========== ==============

    :type indvars: Kx1 vector or NxK matrix

    :param ctl: Optional input. instance of an :class:`olsmtControl` structure containing the following members:

        .. list-table::
            :widths: auto

            * - ctl.altnam
              - string array, default ``""``.

                This can be a :math:`(K+1) \times 1` or :math:`(K+2) \times 1` string array of alternate variable names for the output.
                If *ctl.con* is 1, and *ctl.altnam* has :math:`(K+2)` elements, then the first element will control the name displayed for the constant term. The name of the dependent variable is the last element.

            * - ctl.con
              - scalar, default 1.

                :1: a constant term will be added, :math:`D = K+1`.
                :0: no constant term will be added, :math:`D = K`.

                A constant term will always be used in constructing the moment matrix *m*.

            * - ctl.cov
              - string, set covariance type. Default = "iid".

                :``"iid"``: Error terms assumed to be identical independently distributed.
                :``"robust"``: Huber/White/sandwich estimator.
                :``"cluster"``: Clustered sandwich estimator. Must specify cluster variable identifier.

            * - ctl.clusterID
              - Matrix, vector of categorical group variable used for computing cluster robust standard errors.
            * - ctl.clusterVar
              - String, name of cluster group variable. Only valid if dataset and formula is specified.
            * - ctl.miss
              - scalar, default 0.

                :0: there are no missing values (fastest).
                :1: listwise deletion, drop any cases in which missings occur.
                :2: pairwise deletion, this is equivalent to setting missings to 0 when calculating *m*. The number of cases computed is equal to the total number of cases in the dataset.

            * - ctl.row
              - scalar, the number of rows to read per iteration of the read loop. Default 0.

                If 0, the number of rows will be calculated internally. If you get an *Insufficient memory* error message while
                executing :func:`olsmt`, you can supply a value for *ctl.row* that works on your system.

                The answers may vary slightly due to rounding error differences when a different number of rows is read per iteration.
                You can use *ctl.row* to control this if you want to get exactly the same rounding effects between several runs.
            * - ctl.vpad
              - scalar, default 1.

                If 0, internally created variable names are not padded to the same length (e.g. ``X1, X2,..., X10``). If 1, they are padded with zeros to the same length (e.g., ``X01, X02,..., X10``).
            * - ctl.output
              - scalar, default 1.

                :1: print the statistics.
                :0: do not print statistics.

            * - ctl.res
              - scalar, default 0.

                :1: compute residuals (*oOut.resid*) and Durbin-Watson statistic (*oOut.dwstat*.)
                :0: *oOut.resid* = 0, *oOut.dwstat* = 0.

            * - ctl.rnam
              - string, default "_olsmtres".


                If the data is taken from a dataset, a new dataset will be created for the residuals, using the name in *ctl.rnam*.
            * - ctl.maxvec
              - scalar, default 20000.

                The largest number of elements allowed in any one matrix.
            * - ctl.fcmptol
              - scalar, default 1e-12.

                Tolerance used to fuzz the comparison operations to allow for round off error.
            * - ctl.alg
              - string, default "cholup".

                Selects the algorithm used for computing the parameter estimates. The default Cholesky update method is more computationally efficient. However, accuracy can suffer for poorly conditioned data. For higher accuracy set *ctl.alg* to either  qr or  svd.

                :``"qr"``: Solves for the parameter estimates using a  qr decomposition.
                :``"svd"``: Solves for the parameter estimates using a singular value decomposition.
            * - ctl.weights
              - Nx1 Vector, if defined, specifies weights to be used in the weighted least squares. If not defined, ordinary least squares will be computed.
            * - ctl.weightsVar
              - String, name of the variable used for weighting. Only valid if dataset and formula is specified. Will override any weights in *ctl.weights*.
    :type ctl: struct

    :return out: instance of :class:`olsmtOut` struct containing the following members:

        .. list-table::
            :widths: auto

            * - out.vnam
              - :math:`(K+2) \times 1` or :math:`(K+1) \times 1` character vector, the variable names used in the regression. If a constant term is used, this vector will be :math:`(K+2) \times 1`, and the first name will be ``CONSTANT``. The last name will be the name of the dependent variable.
            * - out.m
              - MxM matrix, where :math:`M = K+2`, the moment matrix constructed by calculating ``X'X`` where *X* is a matrix containing all useable observations and having columns in the order:

                .. csv-table::
                    :widths: auto

                    "1.0", "indvars", "depvar"
                    "(constant)", "(independent variables)", "(dependent variable)"

                A constant term is always used in computing *m*.

            * - out.b
              - Dx1 vector, the least squares estimates of parameters.

                Error handling is controlled by the low order bit of the `trap` flag.

                :trap 0: terminate with error message
                :trap 1: return scalar error code in *b*

                    .. csv-table::
                        :widths: auto

                        "30", "system singular"
                        "31", "system underdetermined"
                        "32", "same number of columns as rows"
                        "33", "too many missings"
                        "34", "file not found"
                        "35", "no variance in an independent variable"

                The system can become underdetermined if you use listwise deletion and have missing values. In that case, it is possible to skip so many cases that there are fewer usable rows than columns in the dataset.

            * - out.stb
              - Kx1 vector, the standardized coefficients.
            * - out.vc
              - DxD matrix, the variance-covariance matrix of estimates.
            * - out.stderr
              - Dx1 vector, the standard errors of the estimated parameters.
            * - out.sigma
              - scalar, standard deviation of residual.
            * - out.cx
              - :math:`(K+1) \times (K+1)` matrix, correlation matrix of variables with the dependent variable as the last column.
            * - out.rsq
              - scalar, R square, coefficient of determination.
            * - out.resid
              - residuals, :math:`out.resid = y -  x * out.b`.

                If *ctl.olsres* = 1, the residuals will be computed.

                If the data is taken from a dataset, a new dataset will be created for the residuals, using the name in *ctl.rnam*.
                The residuals will be saved in this dataset as an Nx1 column. The *out.resid* return value will be a string
                containing the name of the new dataset containing the residuals. If the data is passed in as a matrix,
                the *out.resid* return value will be the Nx1 vector of residuals.
            * - out.dwstat
              - scalar, Durbin-Watson statistic.

    :rtype out: struct

Examples
----------------

Basic usage with matrices
+++++++++++++++++++++++++

::

    // Set y matrix
    y = { 2,
          3,
          1,
          7,
          5 };

    //  Set x matrix
    x = { 1 3 2,
          2 3 1,
          7 1 7,
          5 3 1,
          3 5 5 };

    // Perform least squares regression and print report to the screen
    // The empty string, "" indicates that no dataset is used
    call olsmt("", y, x);

Basic usage with a dataset and a formula string
++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Create string with the name and full file path of the dataset
    dataset = getGAUSSHome() $+ "examples/detroit.sas7bdat";

    // Create formula string specifying dependent and independent variables
    formula  = "homicide ~ unemployment + hourly_earn";

    // Perform estimation
    call olsmt(dataset, formula);

In this example, the dataset "detroit.sas7bdat" is used to compute a
regression. The dependent variable is *homicide*. The independent variables are: *unemployment* and *hourly_earn*. The output is:

::

    Valid cases:                    13      Dependent variable:            homicide
    Missing cases:                   0      Deletion method:                   None
    Total SS:                 3221.790      Degrees of freedom:                  10
    R-squared:                   0.834      Rbar-squared:                     0.801
    Residual SS:               533.814      Std error of est:                 7.306
    F(2,10):                    25.177      Probability of F:                 0.000

                             Standard                 Prob   Standardized  Cor with
    Variable     Estimate      Error      t-value     >|t|     Estimate    Dep Var
    -----------------------------------------------------------------------------------

    CONSTANT       -35.982790    9.437246   -3.812849     0.003       ---         ---
    unemployment    -0.004998    0.918817   -0.005440     0.996   -0.000720    0.210142
    hourly_earn     15.487191    2.242660    6.905722     0.000    0.913572    0.913406

Basic usage with a dataframe and categorical variable
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Load data
    fname = getGAUSSHome $+ "examples/auto2.dta";

    // Include the `rep78`categorical variable in
    call olsmt(fname, "price ~ mpg + rep78");

In this example, the dependent variable *price* is regressed on *mpg* and *rep78*. The categorical variable *rep78* will automatically be included in the OLS regression as a dummy variable with the base case excluded from the regression. The coefficients for the categoies, *Fair, Average, Good, Excellent* are included in the printed output table. The *Poor* category is excluded from the regression, as it is the base case.

::


    Standard                                                  Prob   Standardized  Cor with
    Variable             Estimate      Error      t-value     >|t|     Estimate    Dep Var
    ---------------------------------------------------------------------------------------

    CONSTANT                10450     2251.04     4.64229     0.000       ---         ---
    mpg                  -280.261     61.5767    -4.55142     0.000   -0.564519   -0.455949
    rep78: Fair           877.635     2063.28    0.425358     0.672   0.0971824  -0.0223477
    rep78: Average        1425.66     1905.44    0.748204     0.457     0.24444   0.0859051
    rep78: Good           1693.84     1942.67    0.871914     0.387    0.257252   -0.015317
    rep78: Excellent      3131.98     2041.05      1.5345     0.130    0.396546   -0.035102

Use a dataset, a list of variable names plus a control and output structure.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    new;

    // Declare 'ols_ctl' to be an olsmtControl structure
    // and fill with default settings
    struct olsmtControl ols_ctl;
    ols_ctl = olsmtControlCreate();

    // Set the 'res' member of the olsmtControl structure
    // so that 'olsmt' will compute residuals and the Durbin-Watson statistic
    ols_ctl.res = 1;

    // Declare 'ols_out' to be an olsmtOut structure
    // to hold the results of the computations
    struct olsmtOut ols_out;

    // Create string with the name and full file path of the dataset
    data = getGAUSSHome() $+ "examples/credit.dat";

    // Create a string with the name of the dependent variable
    depvar = "Limit";

    // Create 3x1 string array, containing the dependent variable names
    indvars = "Balance" $| "Income" $|  "Age";

    // Perform estimation, using settings in the 'ols_ctl'
    // control structure and store the results in 'ols_out'
    ols_out = olsmt(data, depvar, indvars, ols_ctl);

In this example, the dataset :file:`credit.dat` is used to compute a
regression. The dependent variable is *Limit*. The independent
variables are: *Balance*, *Income*, and *Age*. The residuals and Durbin-Watson statistic will be computed.

Use a dataset and variable indices
+++++++++++++++++++++++++++++++++++

::

    // Set dataset name
    dataset = getGAUSSHome() $+ "examples/credit.dat";

    // Set the third variable in 'credit.dat', 'Rating'
    // to be the dependent variable
    depvar = 3;

    // Set the first, second and fifth variables in 'credit.dat'
    // to be the independent variables
    indepvar = { 1, 2, 5 };

    call olsmt(dataset, depvar, indepvar);

The above code will produce the following output:

::

    Valid cases:                   400      Dependent variable:              Rating
    Missing cases:                   0      Deletion method:                   None
    Total SS:              9551884.560      Degrees of freedom:                 396
    R-squared:                   0.994      Rbar-squared:                     0.994
    Residual SS:             59390.952      Std error of est:                12.247
    F(3,396):                21097.644      Probability of F:                 0.000

                             Standard                 Prob   Standardized  Cor with
    Variable     Estimate      Error      t-value     >|t|     Estimate    Dep Var
    -------------------------------------------------------------------------------
    CONSTANT    37.675546    2.415716   15.596014     0.000       ---         ---
    Income       0.018253    0.028857    0.632538     0.527    0.004158    0.791378
    Limit        0.066587    0.000436  152.717620     0.000    0.993363    0.996880
    Age          0.019892    0.036174    0.549896     0.583    0.002218    0.103165

Basic usage with weights
+++++++++++++++++++++++++

::

  new;

  // Define data
  parent = { 0.21, 0.2, 0.19, 0.18, 0.17, 0.16, 0.15 };
  progeny = { 0.1726, 0.1707, 0.1637, 0.164, 0.1613, 0.1617, 0.1598 };
  sd = { 0.01988, 0.01938, 0.01896, 0.02037, 0.01654, 0.01594, 0.01763 };

  // Calculate weights
  weights = 1 ./ SD.^2;

  // Set up olsControl structure
  struct olsmtControl ctl;
  ctl = olsmtControlCreate();
  ctl.weights = weights;

  call olsmt("", progeny, parent, ctl);

The above code will produce the following output:

::

  Valid cases:                     7      Dependent variable:                   Y
  Missing cases:                   0      Deletion method:                   None
  Total SS:                  572.494      Degrees of freedom:                   5
  R-squared:                   0.852      Rbar-squared:                     0.823
  Residual SS:                 0.061      Std error of est:                 0.110
  F(1,5):                     28.812      Probability of F:                 0.002

                            Standard                 Prob   Standardized  Cor with
  Variable     Estimate      Error      t-value     >|t|     Estimate    Dep Var
  -------------------------------------------------------------------------------

  CONSTANT     0.127964  0.00681124     18.7872     0.000    0.778572    0.999643
  X1           0.204801   0.0381548     5.36763     0.003    0.222444    0.996209

Remarks
-------

- For poorly conditioned data the default setting for *ctl.olsalg*, using
  the Cholesky update, may produce only four or five digits of accuracy
  for the parameter estimates and standard error. For greater accuracy,
  use either the qr or singular value decomposition algorithm by
  setting *ctl.olsalg* to ``qr`` or ``svd``. If you are unsure of the condition of
  your data, set *ctl.olsalg* to ``qr``.
- No output file is modified, opened, or closed by this procedure. If
  you want output to be placed in a file, you need to open an output
  file before calling :func:`olsmt`.
- The supported dataset types are CSV, XLS, XLSX, HDF5, FMT, DAT
- For HDF5 file, the dataset must include `file schema` and both file name and
  dataset name must be provided, e.g.

  ::

      olsmt("h5://C:/gauss/examples/testdata.h5/mydata", formula)

Source
------

olsmt.src

.. seealso:: Functions :func:`glm`, :func:`gmmFitIV`, :func:`olsmtControlCreate`, :func:`olsqrmt`, `Formula string`, :func:`clusterSE`, :func:`robustSE`
