
fgls
==============================================

Purpose
----------------

Computes a feasible generalized least squares (FGLS) regression.

Format
----------------
.. function:: out = fgls(data, formula, method, [, ctl])
              out = fgls(depvar, indvars, method, [, ctl])

    :param data: name of dataframe.
    :type data: dataframe

    :param formula: formula string of the model.
        E.g ``"y ~ X1 + X2"``, ``y`` is the name of dependent variable, ``X1`` and ``X2`` are names of independent variables;

        E.g ``"y ~ ."``, ``.`` means including all variables except dependent variable ``y``;

        E.g ``"y ~ -1 + X1 + X2"``, ``-1`` means no intercept model.

    :type formula: string

    :param depvar: Dependent variable. 
    :type depvar: Nx1 dataframe or matrix
    
    :param indvars: Independent variable(s).
    :type indvars: NxK matrix or dataframe
    
    :param method: Optional input, model for innovations covariance estimate.

        .. csv-table::
            :widths: auto

            ``"CLM"``, :math:`\omega_i = \frac{1}{df}\sum_{i=1}^T \epsilon_i^2`
            ``"AR"``,  Autoregressive with lags equal to ARlags. (Default).
            ``"HC0"``, :math:`\omega_i = \epsilon_i^2`
            ``"HC1"``, :math:`\omega_i = \frac{T}{df} \epsilon_i^2`
            ``"HC2"``, :math:`\omega_i = \frac{\epsilon_i^2}{1 - h_i}` 
            ``"HC3"``, :math:`\omega_i = \frac{\epsilon_i^2}{1 - h_i}^2`
            ``"HC4"``, :math:`\omega_i = \frac{\epsilon_i^2}{1 - h_i}^{d_i}`
       
    :type method: string

    :param ctl: Optional input, instance of an :class:`fglsControl` structure containing the following members:

        .. list-table::
            :widths: auto
        
            * - ctl.intercept
              - scalar, default 1.

                :1: a constant term will be added.
                :0: no constant term will be added.

            * - ctl.ARlags
              - scalar, number of lags to use for autoregressive computation of :math:`\hat{\omega}`. Default = 1.
            * - ctl.omega0
              - Matrix or vector, user-defined :math:`\hat{\omega}`, specified as a positive vector, positive semidefinite matrix, or a positive definite matrix. If provided, `method` is ignored and no data-driven :math:`\hat{\omega}` is computed.              
            * - ctl.miss
              - scalar, default 0.

                :0: Do not drop missing values. Will error if any missing values are detected.
                :1: listwise deletion, drop any cases in which missings occur. Generates warning message if missing values detected.
  
            * - ctl.scaleResiduals
              - scalar, default 0.

                :0: do not scale residuals.
                :1: Scale residuals to truncate values at the 1 first and ninety-ninth percentiles.

            * - ctl.mleAR
              - scalar, default 1.

                If 0, internally created variable names are not padded to the same length (e.g. ``X1, X2,..., X10``). If 1, they are padded with zeros to the same length (e.g., ``X01, X02,..., X10``).
            * - ctl.printOutput
              - scalar, default 1.

                :1: print the statistics.
                :0: do not print statistics.

    :type ctl: struct

    :return out: instance of :class:`fglsOut` struct containing the following members:

        .. list-table::
            :widths: auto

            * - out.beta_fgls
              - Dx1 vector, the feasible least squares estimates of parameters.
            * - out.sigma_fgls
              - DxD matrix, covariance matrix of estimated parameters.
            * - out.se_fgls
              - Dx1 vector, the standard errors of the estimated parameters.
            * - out.ci
              - Dx2 vector, the confidence interval of the estimated parameters. 
            * - out.t_stats
              - Dx1 vector, the t-statistics of the estimated parameters.
            * - out.pvt
              - Dx1 vector, the p-value the t-statistics of the estimated parameters.
            * - out.resid
              - residuals, :math:`out.resid = y -  x * out.beta_fgls`.
            * - out.df
              - Scalar, degrees of freedom.
            * - out.sse
              - Scalar, sum of squared errors.
            * - out.sst
              - Scalar, total sum of squares.
            * - out.std_est
              - scalar, standard deviation of residuals.
            * - out.fstat
              - Scalar, model F-stat.        
            * - out.pvf
              - Scalar, p-value of model F-stat. 
            * - out.rsq
              - scalar, R squared, coefficient of determination.
            * - out.rbsq
              - scalar, Rbar squared, coefficient of determination.
            * - out.dw
              - scalar, Durbin-Watson statistic.

    :rtype out: struct

Examples
----------------

Basic usage with matrices
+++++++++++++++++++++++++

::

    rndseed 907808;
    
    // Generate y matrix
    y = rndn(50, 1);

    //  Generate x matrix
    x = rndn(50, 3);

    // Perform fgls regression and print report to the screen
    call fgls(y, x);

Basic usage with a dataframe and a formula string
++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Create string with the name and full file path of the dataset
    dataset = getGAUSSHome() $+ "examples/df_returns.gdat";

    // Load dataset into dataframe
    data_df = loadd(dataset);
    
    // Create formula string specifying dependent and independent variables
    formula  = "rcoe ~ rcpi";

    // Perform estimation
    call fgls(dataset, formula);

In this example, the dataset ``df_returns.gdat`` is used to compute a
regression. The dependent variable is *rcoe*. The independent variable is *rcpi*. The output is:

::

    Valid cases:                    248              Dependent variable:            rcpi
    Total SS:                     0.027              Degrees of freedom:             245
    R-squared:                    0.110              Rbar-squared:                 0.103
    Residual SS:                  0.024              Std error of est:             0.010
    F(1,245)                     30.329              Probability of F:             0.000
    Dubin-Watson                  0.757                                                 


    ------------------------------------------------------------------------------------
                            Standard                    Prob                        
    Variable   Estimates       Error     t-value        >|t|  [95% Conf.   Interval]
    ------------------------------------------------------------------------------------

    Constant      0.0148     0.00122        12.1       0.000      0.0124      0.0172 
        rcoe       0.196      0.0685        2.86       0.005      0.0619        0.33 

Changing method of innovation covariance estimation and storing results
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    new;

    // Declare 'fgls_out' to be an fglsOut structure
    // to hold the results of the computations
    struct fglsOut fgls_out;

    // Create string with the name and full file path of the dataset
    dataset = getGAUSSHome() $+ "examples/credit.dat";
    
    // Load dataframe
    data_df = loadd(dataset);
    
    // Create a string with the name of the dependent variable
    formula = "Limit ~ Balance + Income + Age";

    // Specify method to be classic linear model
    method = "CLM";
    
    // Perform estimation, using CLM innovation covariance
    // and store the results in 'fgls_out'
    fgls_out = fgls(data_df, formula, method);

In this example, the dataset :file:`credit.dat` is used to compute a
regression using a classic linear model innovation covariance matrix. The dependent variable is *Limit*. The independent
variables are: *Balance*, *Income*, and *Age*. 

Source
------

fgls.src

.. seealso:: Functions :func:`glm`, :func:`gmmFitIV`, :func:`fglsControlCreate`, :func:`olsmt`
