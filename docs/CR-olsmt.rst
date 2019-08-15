
olsmt
==============================================

Purpose
----------------

Computes a least squares regression.

Format
----------------
.. function:: oout = olsmt(dataset, formula[, oc0])
              oout = olsmt(dataset, depvar, indvars[, oc0])

    :param dataset: name of data set or null string.
        If *dataset* is a null string, the procedure assumes that the actual data has been passed in the next two arguments.
    :type dataset: string

    :param formula: formula string of the model.
        E.g ``"y ~ X1 + X2"``, 'y' is the name of dependent variable, '``X1``' and '``X2``' are names of independent variables;

        E.g ``"y ~ ."``, '.' means including all variables except dependent variable 'y';

        E.g ``"y ~ -1 + X1 + X2"``, '-1' means no intercept model.

    :type formula: string

    :param depvar: If *dataset* contains a string, then *depvar* can be a:

        =========== ==============
           type         value
        =========== ==============
        string      name of dependent variable
        scalar      index of dependent variable. If scalar 0, the last column of the data set will be used.
        =========== ==============

        If *dataset* is a null string or 0:

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
        Kx1 numeric vector    indices of independent variables. These can be any size subset of the variables in the data set 
                              and can be in any order. If a scalar 0 is passed, all columns of the data set will be used except 
                              for the one used for the dependent variable.
        ===================== ==============

        If *dataset* is a null string or 0:

        =========== ==============
           type         value
        =========== ==============
        NxK matrix  the independent variables
        =========== ==============

    :type indvars: Kx1 vector or NxK matrix

    :param oc0: Optional input. instance of an :class:`olsmtControl` structure containing the following members:

        .. DANGER:: Fix equations

        .. list-table::
            :widths: auto
    
            * - oc0.altnam
              - character vector, default 0.
                
                This can be a :math:`(K+1)x1` or :math:`(K+2)x1` character vector of alternate variable names for the output. 
                If *oc0.con* is 1, this must be :math:`(K+2)x1`. The name of the dependent variable is the last element.

            * - oc0.con
              - scalar, default 1.

                :1: a constant term will be added, :math:`D = K+1`.
                :0: no constant term will be added, :math:`D = K`.

                A constant term will always be used in constructing the moment matrix *m*.

            * - oc0.cov
              - string, set covariance type. Default = "iid".

                :"iid": Error terms assumed to be identical independently distrbuted.
                :"robust": Huber/White/sandwich estimator.
                :"cluster": Clustered sandwich estimator. Must specify cluster variable identifier.

            * - oc0.clusterID
              - Matrix, vector of categorical group variable used for computer cluster robust standard errors.
            * - oc0.clusterVar
              - String, name of cluster group variable. Only valid if dataset and formula specified.
            * - oc0.miss
              - scalar, default 0.

                :0: there are no missing values (fastest).
                :1: listwise deletion, drop any cases in which missings occur.
                :2: pairwise deletion, this is equivalent to setting missings to 0 when calculating *m*. The number of cases computed is equal to the total number of cases in the data set.

            * - oc0.row
              - scalar, the number of rows to read per iteration of the read loop. Default 0.
                
                If 0, the number of rows will be calculated internally. If you get an *Insufficient memory* error message while 
                executing :func:`olsmt`, you can supply a value for oc0.row that works on your system.
                
                The answers may vary slightly due to rounding error differences when a different number of rows is read per iteration. 
                You can use oc0.row to control this if you want to get exactly the same rounding effects between several runs.
            * - oc0.vpad
              - scalar, default 1. 
                
                If 0, internally created variable names are not padded to the same length (e.g. "X1, X2,..., X10"). If 1, they are padded with zeros to the same length (e.g., "X01, X02,..., X10").
            * - oc0.output
              - scalar, default 1.

                :1: print the statistics.
                :0: do not print statistics.

            * - oc0.res
              - scalar, default 0.

                :1: compute residuals (resid) and Durbin-Watson statistic (dwstat.)
                :0: oout.resid = 0, oout.dwstat = 0.

            * - oc0.rnam
              - string, default "_olsmtres".
                
              
                If the data is taken from a data set, a new data set will be created for the residuals, using the name in oc0.rnam.
            * - oc0.maxvec
              - scalar, default 20000.
                
                The largest number of elements allowed in any one matrix.
            * - oc0.fcmptol
              - scalar, default 1e-12.
                
                Tolerance used to fuzz the comparison operations to allow for round off error.
            * - oc0.alg
              - string, default "cholup".
                
                Selects the algorithm used for computing the parameter estimates. The default Cholesky update method is more computationally efficient. However, accuracy can suffer for poorly conditioned data. For higher accuracy set oc0.alg to either  qr or  svd.

                :"qr": Solves for the parameter estimates using a  qr decomposition.
                :"svd": Solves for the paramer estimates using a singular value decomposition.

    :type oc0: struct

    :return oout: instance of :class:`olsmtOut` struct containing the following members:

        .. list-table::
            :widths: auto
    
            * - oout.vnam
              - :math:`(K+2)x1` or :math:`(K+1)x1` character vector, the variable names used in the regression. If a constant term is used, this vector will be :math:`(K+2)x1`, and the first name will be "CONSTANT". The last name will be the name of the dependent variable.
            * - oout.m
              - MxM matrix, where :math:`M = K+2`, the moment matrix constructed by calculating ``X'X`` where *X* is a matrix containing all useable observations and having columns in the order:

                .. csv-table::
                    :widths: auto
    
                    "1.0", "indvars", "depvar"
                    "(constant)", "(independent variables)", "(dependent variable)"

                A constant term is always used in computing *m*.

            * - oout.b
              - Dx1 vector, the least squares estimates of parameters.,

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

                The system can become underdetermined if you use listwise deletion and have missing values.In that case, it is possible to skip so many cases that there are fewer usable rows than columns in the data set.

            * - oout.stb
              - Kx1 vector, the standardized coefficients.
            * - oout.vc
              - DxD matrix, the variance-covariance matrix of estimates.
            * - oout.stderr
              - Dx1 vector, the standard errors of the estimated parameters.
            * - oout.sigma
              - scalar, standard deviation of residual.
            * - oout.cx
              - :math:`(K+1)x(K+1)` matrix, correlation matrix of variables with the dependent variable as the last column.
            * - oout.rsq
              - scalar, R square, coefficient of determination.
            * - oout.resid
              - residuals, :math:`oout.resid = y -  x * oout.b`.

                If *oc0.olsres* = 1, the residuals will be computed.
                
                If the data is taken from a data set, a new data set will be created for the residuals, using the name in oc0.rnam. 
                The residuals will be saved in this data set as an Nx1 column. The oout.resid return value will be a string 
                containing the name of the new data set containing the residuals. If the data is passed in as a matrix, 
                the oout.resid return value will be the Nx1 vector of residuals.
            * - oout.dwstat
              - scalar, Durbin-Watson statistic.

    :rtype oout: struct

Remarks
-------

- For poorly conditioned data the default setting for *__olsalg*, using
  the Cholesky update, may produce only four or five digits of accuracy
  for the parameter estimates and standard error. For greater accuracy,
  use either the *qr* or singular value decomposition algorithm by
  setting *__olsalg* to ``qr`` or ``svd``. If you are unsure of the condition of
  your data, set *__olsalg* to ``qr``.
- No output file is modified, opened, or closed by this procedure. If
  you want output to be placed in a file, you need to open an output
  file before calling :func:`olsmt`.
- The supported data set types are CSV, XLS, XLSX, HDF5, FMT, DAT
- For HDF5 file, the dataset must include `file schema` and both file name and
  data set name must be provided, e.g.

  ::

      ols("h5://C:/gauss/examples/testdata.h5/mydata", formula).

Examples
----------------

Basic usage with matrices
+++++++++++++++++++++++++

::

    y = { 2,
          3,
          1,
          7,
          5 };
    
    x = { 1 3 2,
          2 3 1,
          7 1 7,
          5 3 1,
          3 5 5 };
    
    // Perform least squares regression and print report to the screen
    // The empty string, "" indicates that no dataset is used
    call olsmt("",y,x);

Basic usage with a data set and a formula string
++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Create string with the name and full file path of the dataset
    dataset = getGAUSSHome() $+ "examples/detroit.sas7bdat";
    
    // Create formula string specifying dependent and independent variables
    formula  = "homicide ~ unemployment + hourly_earn";
    
    // Perform estimation
    call olsmt(dataset, formula);

In this example, the data set "detroit.sas7bdat" is used to compute a
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

Use a data set, a list of variable names plus a control and output structure.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

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

In this example, the data set "credit.dat" is used to compute a
regression. The dependent variable is *Limit*. The independent
variables are: *Balance*, *Income*, and *Age*. The residuals and Durbin-Watson statistic will be computed.

Use a data set and variable indices
+++++++++++++++++++++++++++++++++++

::

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

Source
------

olsmt.src

.. seealso:: Functions :func:`glm`, :func:`gmmFitIV`, :func:`olsmtControlCreate`, :func:`olsqrmt`, `Formula string`, :func:`clusterSE`, :func:`robustSE`

