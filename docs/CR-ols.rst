
ols
==============================================

Purpose
----------------

Computes a least squares regression.

Format
----------------
.. function:: { vnam, m, b, stb, vc, stderr, sigma, cx, rsq, resid, dwstat } = ols(dataset, depvar, indvars)
              { vnam, m, b, stb, vc, stderr, sigma, cx, rsq, resid, dwstat } = ols(dataset, formula)

    :param dataset: name of data set or null string.

        If *dataset* is a null string, the procedure assumes that the actual data has been passed in the next two arguments.

    :type dataset: string

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

    :type depvar: string or scalar or Nx1 vector

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

    :param formula: formula string of the model.

        E.g ``"y ~ X1 + X2"``, 'y' is the name of dependent variable, '``X1``' and '``X2``' are names of independent variables;

        E.g ``"y ~ ."``, '.' means including all variables except dependent variable 'y';

        E.g ``"y ~ -1 + X1 + X2"``, '-1' means no intercept model.

    :type formula: string

    :return vnam: the variable
        names used in the regression. If a constant term is
        used, this vector will be :math:`(K+2)x1`, and the first
        name will be "CONSTANT". The last name will be the
        name of the dependent variable.

    :type vnam: (K+2)x1 or (K+1)x1 character vector

    :return m: where :math:`M = K+2`, the moment matrix constructed by calculating
        :math:`x'x` where *x* is a matrix containing all useable observations and having columns in the order:

        .. csv-table::
            :widths: auto
    
            "1.0", "indvars", "depvar"
            "(constant)", "(independent variables)", "(dependent variable)"

        A constant term is always used in computing *m*.

    :type m: MxM matrix

    :return b: the least squares estimates of parameters

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

        The system can become underdetermined if you use listwise deletion and have missing values. In that case, it is possible to skip so many cases that there are fewer useable rows than columns in the data set.

    :type b: Dx1 vector

    :return stb: the standardized coefficients.

    :type stb: Kx1 vector

    :return vc: the variance-covariance matrix of estimates.

    :type vc: DxD matrix

    :return stderr: the standard errors of the estimated parameters.

    :type stderr: Dx1 vector

    :return sigma: standard deviation of residual.

    :type sigma: scalar

    :return cx: correlation matrix of variables with the dependent variable as the last column.

    :type cx: (K+1)x(K+1) matrix

    :return rsq: R square, coefficient of determination.

    :type rsq: scalar

    :return resid: :math:`resid = y - x * b`.

        If *_olsres* = 1, the residuals will be computed.

        If the data is taken from a data set, a new data set will be created for the residuals, using the
        name in the global string variable *_olsrnam*. The residuals will be saved in this data set as an Nx1 column. 
        The *resid* return value will be a string containing the name of the new data set containing the residuals.
        If the data is passed in as a matrix, the *resid* return value will be the Nx1 vector of residuals.

    :type resid: residuals

    :return dwstat: Durbin-Watson statistic.

    :type dwstat: scalar

.. DANGER:: Fix equations

Global Input
------------

Defaults are provided for the following global input variables, so they
can be ignored unless you need control over the other options provided
by this procedure.

:__altnam: (*character vector*), default 0.

    This can be a :math:`(K+1)x1` or :math:`(K+2)x1` character vector of alternate variable
    names for the output. If *__con* is 1, this must be :math:`(K+2)x1`. The name of the dependent variable is the last element.

:__con: (*scalar*), default 1.

    === ===============
    1   a constant term will be added, :math:`D = K+1.`
    0   no constant term will be added, :math:`D = K.`
    === ===============

    A constant term will always be used in constructing the moment matrix *m*.

:__miss: (*scalar*), default 0.

    === ===============
    0   there are no missing values (fastest).
    1   listwise deletion, drop any cases in which missings occur.
    2   pairwise deletion, this is equivalent to setting missings to 0 when
        calculating *m*. The number of cases computed is equal to the total number
        of cases in the data set.
    === ===============

:__olsalg: (*string*), default "cholup". Selects the algorithm used for computing the
    parameter estimates. The default Cholesky update method is more
    computationally efficient; however, accuracy can suffer for poorly
    conditioned data. For higher accuracy, set *__olsalg* to either ``qr`` or ``svd``.

    === ===============
    qr  Solves for the parameter estimates using a qr decomposition.
    svd Solves for the paramer estimates using a singular value decomposition.
    === ===============

:__output: (*scalar*), default 1.

    === ===============
    1   print the statistics.
    0   do not print statistics.
    === ===============

:__row: (*scalar*), the number of rows to read per iteration of the read loop. Default 0.

    If 0, the number of rows will be calculated internally. If you get an
    Insufficient memory error while executing :func:`ols`, you can supply a value
    for *__row* that works on your system.
    
    The answers may vary slightly due to rounding error differences when a
    different number of rows is read per iteration. You can use *__row* to
    control this if you want to get exactly the same rounding effects
    between several runs.

:_olsres: (*scalar*), default 0.

    === ===============
    1   compute residuals (*resid*) and Durbin-Watson statistic (*dwstat*).
    0   *resid* = 0, *dwstat* = 0.
    === ===============

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
  file before calling :func:`ols`.
- The supported data set types are CSV, XLS, XLSX, HDF5, FMT, DAT
- For HDF5 file, the dataset must include `file schema` and both file name and
  data set name must be provided, e.g.

  ::

        ols("h5://C:/gauss/examples/testdata.h5/mydata", formula).

Examples
--------

Example 1
+++++++++

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
     
    output file = ols.out reset;
    call ols(0,y,x);
    output off;

In this example, the output from :func:`ols` is put into a file called *ols.out*
as well as being printed to the window. This example will compute a
least squares regression of *y* on *x*. The return values are discarded by
using a `call` statement.

::

    data = "olsdat";
    depvar = { score };
    indvars = { region, age, marstat };
    _olsres = 1;
    output file = lpt1 on;
    { nam, m, b, stb, vc, std, sig, cx, rsq, resid, dbw } = ols(data, depvar, indvars);
    output off;

In this example, the data set *olsdat.dat* is used to compute a
regression. The dependent variable is *score*. The independent variables
are: *region*, *age*, and *marstat*. The residuals and Durbin-Watson statistic
will be computed. The output will be sent to the printer as well as the
window and the returned values are assigned to variables.

Example 2
+++++++++

Pass in a data set name and variable names

::

    fname = getGAUSShome() $+ "examples/credit.dat"; 
    // Specify the formula, Limit is dependent variable and Balance, Income and Age are independent variables 
    dep = "Limit";
    string indep = {"Balance", "Income", "Age"};
 
    call ols(fname, dep, indep);

After the above code,

::


    Valid cases:                   400      Dependent variable:               Limit
    Missing cases:                   0      Deletion method:                   None
    Total SS:           2125784986.000      Degrees of freedom:                 396
    R-squared:                   0.939      Rbar-squared:                     0.939
    Residual SS:         129727134.947      Std error of est:               572.358
    F(3,396):                 2031.029      Probability of F:                 0.000
 
    Standard                 Prob   Standardized  Cor with
    Variable     Estimate      Error      t-value     >|t|     Estimate    Dep Var
    -------------------------------------------------------------------------------
    CONSTANT  1521.904666  102.228802   14.887240     0.000       ---         ---  
    Balance      3.168467    0.070635   44.856923     0.000    0.631111    0.861697
    Income      32.566995    0.935925   34.796581     0.000    0.497271    0.792088
    Age          1.677855    1.694288    0.990301     0.323    0.012539    0.100888             

Example 3
+++++++++

Pass in a data set name and a `Formula string`

::

    fname = getGAUSShome() $+ "examples/credit.dat"; 
                    
    // Specify the formula, 'Limit' is dependent variable and 'Balance', 'Income' and 'Age' are independent variables, '-1' means remove the intercept in the model 
    formula = "Limit ~ - 1 + Balance + Income + Age ";
                    
    call ols(fname, formula);

After the above code,

::

    Valid cases:                   400      Dependent variable:               Limit
    Missing cases:                   0      Deletion method:                   None
    Total SS:          11096147930.000      Degrees of freedom:                 397
    R-squared:                   0.982      Rbar-squared:                     0.982
    Residual SS:         202331711.222      Std error of est:               713.899
    F(3,397):                 7125.008      Probability of F:                 0.000
 
    Standard                 Prob   Standardized  Cor with
    Variable     Estimate      Error      t-value     >|t|     Estimate    Dep Var
    -------------------------------------------------------------------------------
    Balance      3.429796    0.085339   40.190438     0.000    0.451757    0.923618
    Income      33.447531    1.165041   28.709327     0.000    0.363912    0.922459
    Age         23.718127    1.027629   23.080436     0.000    0.262414    0.871984 

Source
------

ols.src

.. seealso:: Functions :func:`olsqr`, `Formula string`

