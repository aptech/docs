
olsmt
==============================================

Purpose
----------------

Computes a least squares regression.

Format
----------------
.. function:: out = olsmt(data, formula[, ctl])
              out = olsmt(data, depvar, indvars[, ctl])

    :param data: name of dataset, dataframe in memory, or an empty string.
        If *data* is an empty string,``""``, the procedure assumes that the actual data has been passed in the next two arguments.
    :type data: string or dataframe

    :param formula: formula string of the model.
        E.g ``"y ~ X1 + X2"``, ``y`` is the name of dependent variable, ``X1`` and ``X2`` are names of independent variables;

        E.g ``"y ~ ."``, ``.`` means including all variables except dependent variable ``y``;

        E.g ``"y ~ -1 + X1 + X2"``, ``-1`` means no intercept model.

    :type formula: string

    :param depvar: If *data* contains a string, then *depvar* can be a:

        =========== ==============
           type         value
        =========== ==============
        string      name of dependent variable
        scalar      index of dependent variable. If scalar 0, the last column of the dataset will be used.
        =========== ==============

        If *data* is an empty string, name of dataframe, or 0:

        =========== ==============
           type         value
        =========== ==============
        Nx1 vector  the dependent variable.
        =========== ==============

    :param indvars: If *data* contains a string:

        ===================== ==============
           type                   value
        ===================== ==============
        Kx1 character vector  names of independent variables
        Kx1 numeric vector    indices of independent variables. These can be any size subset of the variables in the data
                              and can be in any order. If a scalar 0 is passed, all columns of the data will be used except
                              for the one used for the dependent variable.
        ===================== ==============

        If *data* is an empty string, dataframe, or 0:

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
                :``"hac"``: HAC robust sandwich estimator.

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

::

    Ordinary Least Squares
    ====================================================================================
    Valid cases:                        5          Dependent variable:                 Y
    Missing cases:                      0          Deletion method:                 None
    Total SS:                      23.200          Degrees of freedom:                 1
    R-squared:                      0.982          Rbar-squared:                   0.928
    Residual SS:                    0.417          Std. err of est:                0.646
    F(3,1):                        18.224          Probability of F:               0.170
    ====================================================================================
                                Standard                    Prob       Lower       Upper
    Variable        Estimate       Error     t-value        >|t|       Bound       Bound
    ------------------------------------------------------------------------------------
    CONSTANT          -3.149       1.322      -2.382       0.253      -5.740      -0.558 
    X1                 1.105       0.201       5.505       0.114       0.711       1.498 
    X2                 1.728       0.284       6.073       0.104       1.170       2.285 
    X3                -0.753       0.151      -4.986       0.126      -1.050      -0.457 
    ====================================================================================

Basic usage with a dataset and a formula string
++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Create string with the name and full file path of the dataset
    dataset = getGAUSSHome("examples/detroit.dta");

    // Create formula string specifying dependent and independent variables
    formula  = "homicide ~ unemployment + hourly_earn";

    // Perform estimation
    call olsmt(dataset, formula);

In this example, the dataset ``detroit.dta`` is used to compute a
regression. The dependent variable is *homicide*. The independent variables are: *unemployment* and *hourly_earn*. The output is:

::

    Ordinary Least Squares
    =====================================================================================
    Valid cases:                       13          Dependent variable:          homicide
    Missing cases:                      0          Deletion method:                 None
    Total SS:                    3221.790          Degrees of freedom:                10
    R-squared:                      0.834          Rbar-squared:                   0.801
    Residual SS:                  533.814          Std. err of est:                7.306
    F(2,10):                       25.177          Probability of F:               0.000
    =====================================================================================
                                Standard                    Prob       Lower       Upper
    Variable         Estimate       Error     t-value        >|t|       Bound       Bound
    -------------------------------------------------------------------------------------
    CONSTANT          -35.983       9.437      -3.813       0.003     -54.480     -17.486 
    unemployment       -0.005       0.919      -0.005       0.996      -1.806       1.796 
    hourly_earn        15.487       2.243       6.906       0.000      11.092      19.883 
    =====================================================================================

Basic usage with a dataframe and categorical variable
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Load data
    fname = getGAUSSHome("examples/auto2.dta");
    auto2 = loadd(fname);

    // Include the `rep78` categorical variable
    call olsmt(auto2, "price ~ mpg + rep78");

In this example, the dependent variable *price* is regressed on *mpg* and *rep78*. The categorical variable *rep78* will automatically be included in the OLS regression as a dummy variable with the base case excluded from the regression. The coefficients for the categories, *Fair, Average, Good, Excellent* are included in the printed output table. The *Poor* category is excluded from the regression, as it is the base case.

::

    Ordinary Least Squares
    =========================================================================================
    Valid cases:                         69          Dependent variable:               price
    Missing cases:                        5          Deletion method:               Listwise
    Total SS:                 576796958.870          Degrees of freedom:                  63
    R-squared:                        0.258          Rbar-squared:                     0.199
    Residual SS:              427776355.434          Std. err of est:               2605.782
    F(5,63):                          4.389          Probability of F:                 0.002
    =========================================================================================
                                    Standard                    Prob       Lower       Upper
    Variable             Estimate       Error     t-value        >|t|       Bound       Bound
    -----------------------------------------------------------------------------------------
    CONSTANT            10449.991    2251.041       4.642       0.000    6037.952   14862.031 
    mpg                  -280.261      61.577      -4.551       0.000    -400.952    -159.571 
    rep78: Fair           877.635    2063.285       0.425       0.672   -3166.403    4921.672 
    rep78: Average       1425.657    1905.438       0.748       0.457   -2309.001    5160.315 
    rep78: Good          1693.841    1942.669       0.872       0.387   -2113.791    5501.473 
    rep78: Excellent     3131.982    2041.049       1.534       0.130    -868.473    7132.438 
    =========================================================================================


Estimate a linear model for each subset of a categorical variable
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

In this example, we will regress *mpg* and *weight* on *price* for the case where *foreign* equals *"Domestic"* and for the case where *foreign* equals *"Foreign*", using the `by` keyword.

::

    // Load specific variables
    fname = getGAUSSHome("examples/auto2.dta");
    auto2 = loadd(fname, "price + mpg + weight + foreign");

    // Estimate a linear model for each value of `foreign`
    call olsmt(auto2, "price ~ mpg + weight + by(foreign)");


::

    Ordinary Least Squares
    ====================================================================================
    foreign: Domestic 
    ====================================================================================
    Valid cases:                       52          Dependent variable:             price
    Missing cases:                      0          Deletion method:                 None
    Total SS:               489194800.692          Degrees of freedom:                49
    R-squared:                      0.483          Rbar-squared:                   0.462
    Residual SS:            252934086.227          Std. err of est:             2271.986
    F(2,49):                       22.885          Probability of F:               0.000
    ====================================================================================
                                Standard                    Prob       Lower       Upper
    Variable        Estimate       Error     t-value        >|t|       Bound       Bound
    ------------------------------------------------------------------------------------
    CONSTANT      -13285.444    5726.031      -2.320       0.025  -24508.465   -2062.422 
    mpg              237.691     139.033       1.710       0.094     -34.815     510.196 
    weight             4.415       0.948       4.655       0.000       2.556       6.274 
    ====================================================================================

    Ordinary Least Squares
    ====================================================================================
    foreign: Foreign 
    ====================================================================================
    Valid cases:                       22          Dependent variable:             price
    Missing cases:                      0          Deletion method:                 None
    Total SS:               144363212.773          Degrees of freedom:                19
    R-squared:                      0.785          Rbar-squared:                   0.763
    Residual SS:             30967505.235          Std. err of est:             1276.663
    F(2,19):                       34.787          Probability of F:               0.000
    ====================================================================================
                                Standard                    Prob       Lower       Upper
    Variable        Estimate       Error     t-value        >|t|       Bound       Bound
    ------------------------------------------------------------------------------------
    CONSTANT       -5065.841    3202.514      -1.582       0.130  -11342.768    1211.087 
    mpg              -19.777      57.681      -0.343       0.735    -132.833      93.278 
    weight             5.156       0.881       5.854       0.000       3.430       6.882 
    ====================================================================================




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
    data = getGAUSSHome("examples/credit.dat");

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

::

  Ordinary Least Squares
  ====================================================================================
  Valid cases:                      400          Dependent variable:             Limit
  Missing cases:                      0          Deletion method:                 None
  Total SS:              2125784986.000          Degrees of freedom:               396
  R-squared:                      0.939          Rbar-squared:                   0.939
  Residual SS:            129727134.947          Std. err of est:              572.358
  F(3,396):                    2031.029          Probability of F:               0.000
  Durbin-Watson:                  1.953                                               
  ====================================================================================
                              Standard                    Prob       Lower       Upper
  Variable        Estimate       Error     t-value        >|t|       Bound       Bound
  ------------------------------------------------------------------------------------
  CONSTANT        1521.905     102.229      14.887       0.000    1321.536    1722.273 
  Balance            3.168       0.071      44.857       0.000       3.030       3.307 
  Income            32.567       0.936      34.797       0.000      30.733      34.401 
  Age                1.678       1.694       0.990       0.323      -1.643       4.999 
  ====================================================================================

Use a dataset and variable indices
+++++++++++++++++++++++++++++++++++

::

    // Set dataset name
    dataset = getGAUSSHome("examples/credit.dat");

    // Set the third variable in 'credit.dat', 'Rating'
    // to be the dependent variable
    depvar = 3;

    // Set the first, second and fifth variables in 'credit.dat'
    // to be the independent variables
    indepvar = { 1, 2, 5 };

    call olsmt(dataset, depvar, indepvar);

The above code will produce the following output:

::

    Ordinary Least Squares
    ====================================================================================
    Valid cases:                      400          Dependent variable:            Rating
    Missing cases:                      0          Deletion method:                 None
    Total SS:                 9551884.560          Degrees of freedom:               396
    R-squared:                      0.994          Rbar-squared:                   0.994
    Residual SS:                59390.952          Std. err of est:               12.247
    F(3,396):                   21097.644          Probability of F:               0.000
    ====================================================================================
                                Standard                    Prob       Lower       Upper
    Variable        Estimate       Error     t-value        >|t|       Bound       Bound
    ------------------------------------------------------------------------------------

    CONSTANT          37.676       2.416      15.596       0.000      32.941      42.410 
    Income             0.018       0.029       0.633       0.527      -0.038       0.075 
    Limit              0.067       0.000     152.718       0.000       0.066       0.067 
    Age                0.020       0.036       0.550       0.583      -0.051       0.091 
    ====================================================================================

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

  Ordinary Least Squares
  ====================================================================================
  Valid cases:                        7          Dependent variable:                 Y
  Missing cases:                      0          Deletion method:                 None
  Total SS:                     572.494          Degrees of freedom:                 5
  R-squared:                      0.852          Rbar-squared:                   0.823
  Residual SS:                    0.061          Std. err of est:                0.110
  F(1,5):                        28.812          Probability of F:               0.002
  ====================================================================================
                              Standard                    Prob       Lower       Upper
  Variable        Estimate       Error     t-value        >|t|       Bound       Bound
  ------------------------------------------------------------------------------------
  CONSTANT           0.128       0.007      18.787       0.000       0.115       0.141 
  X1                 0.205       0.038       5.368       0.003       0.130       0.280 
  ====================================================================================

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
