
fgls
==============================================

Purpose
----------------

Computes a feasible generalized least squares (FGLS) regression.

Format
----------------
.. function:: out = fgls(data, formula [, method, ctl])
              out = fgls(depvar, indvars [, method, ctl])

    :param data: Name of dataframe.
    :type data: Dataframe

    :param formula: Formula string of the model.
        E.g ``"y ~ X1 + X2"``, ``y`` is the name of dependent variable, ``X1`` and ``X2`` are names of independent variables;

        E.g ``"y ~ ."``, ``.`` means including all variables except dependent variable ``y``;

        E.g ``"y ~ -1 + X1 + X2"``, ``-1`` means no intercept model.

    :type formula: String

    :param depvar: Dependent variable. 
    :type depvar: Nx1 dataframe or matrix
    
    :param indvars: Independent variable(s).
    :type indvars: NxK matrix or dataframe
    
    :param method: Optional input, model for innovations covariance estimate, :math:`\hat{\Omega}`.

        .. csv-table::
            :widths: auto

            ``"CLM"``, :math:`\omega_i = \frac{1}{df}\sum_{i=1}^T \epsilon_i^2`
            ``"AR"``,  :math:`AR(1)` model. (Default)
            ``"HC0"``, :math:`\omega_i = \epsilon_i^2`
            ``"HC1"``, :math:`\omega_i = \frac{T}{df} \epsilon_i^2`
            ``"HC2"``, :math:`\omega_i = \frac{\epsilon_i^2}{1 - h_i}` 
            ``"HC3"``, :math:`\omega_i = \frac{\epsilon_i^2}{1 - h_i}^2`
            ``"HC4"``, :math:`\omega_i = \frac{\epsilon_i^2}{1 - h_i}^{d_i}`
       
    :type method: String

    :param ctl: Optional input, instance of an :class:`fglsControl` structure containing the following members:

        .. list-table::
            :widths: auto
        
            * - ctl.intercept
              - Scalar, default 1.

                :1: a constant term will be added.
                :0: no constant term will be added.

            * - ctl.iters
              - Scalar, number of iterations, default is two-stage FGLS.              
            * - ctl.omega0
              - Matrix or vector, user-defined :math:`\hat{\Omega}`, specified as a positive vector, positive semidefinite matrix, or a positive definite matrix. If provided, *method* is ignored and no data-driven :math:`\hat{\omega}` is computed.              
            * - ctl.miss
              - Scalar, default 0.

                :0: Do not drop missing values. Will error if any missing values are detected.
                :1: listwise deletion, drop any cases in which missings occur. Generates warning message if missing values detected.
  
            * - ctl.scaleResiduals
              - Scalar, default 0.

                :0: do not scale residuals.
                :1: Scale residuals to truncate values at the first and ninety-ninth percentiles.

            * - ctl.mleAR
              - Scalar, default 1.

                :0: Use OLS estimate of autoregressive parameters in innovation covariance matrix estimation.
                :1: Use MLE estimate of autoregressive parameters in innovation covariance matrix estimation. 
 
                Valid only if using ``"AR"`` method for computing innovation covariance matrix. 
                    
            * - ctl.printOutput
              - Scalar, default 1.

                :0: do not print statistics.
                :1: print the statistics.
                

    :type ctl: Struct

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
              - Residuals, :math:`out.resid = y -  x * out.beta\_{fgls}`.
            * - out.df
              - Scalar, degrees of freedom.
            * - out.sse
              - Scalar, sum of squared errors.
            * - out.sst
              - Scalar, total sum of squares.
            * - out.std_est
              - Scalar, standard deviation of residuals.
            * - out.fstat
              - Scalar, model F-stat.        
            * - out.pvf
              - Scalar, p-value of model F-stat. 
            * - out.rsq
              - Scalar, R squared, coefficient of determination.
            * - out.rbsq
              - Scalar, Rbar squared, coefficient of determination.
            * - out.dw
              - Scalar, Durbin-Watson statistic.

    :rtype out: Struct

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

The output for data matrices includes default variable names:

::

    Valid cases:                     50              Dependent variable:             Y
    Total SS:                    48.078              Degrees of freedom:            46
    R-squared:                    0.019              Rbar-squared:              -0.045
    Residual SS:                 47.145              Std error of est:           1.012
    F(3,46)                       0.303              Probability of F:           0.874
    Durbin-Watson                 2.087                                                 


    ----------------------------------------------------------------------------------
                            Standard                    Prob                        
      Variable   Estimates       Error     t-value        >|t|  [95% Conf.   Interval]
    ----------------------------------------------------------------------------------

    Constant     -0.0699       0.146      -0.478       0.635      -0.356       0.217 
          X1       0.103       0.139       0.744       0.461      -0.169       0.376 
          X2       0.166       0.183       0.906       0.370      -0.193       0.524 
          X3     -0.0228       0.129      -0.177       0.860      -0.275       0.229
  
Basic usage with a dataframe and a formula string
++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Create string with the name and full file path of the dataset
    dataset = getGAUSSHome("examples/df_returns.gdat");

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
    Total SS:                     0.027              Degrees of freedom:             246
    R-squared:                    0.110              Rbar-squared:                 0.107
    Residual SS:                  0.024              Std error of est:             0.010
    F(1,245)                     30.453              Probability of F:             0.000
    Durbin-Watson                 0.757                                                 


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
    dataset = getGAUSSHome("examples/credit.dat");
    
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

::

   Valid cases:                    400              Dependent variable:         Balance
   Total SS:            2125784986.000              Degrees of freedom:             396
   R-squared:                    0.939              Rbar-squared:                 0.939
   Residual SS:          129727134.947              Std error of est:           572.358
   F(3,396)                   2031.029              Probability of F:             0.000
   Durbin-Watson                 1.953                                                 


   ------------------------------------------------------------------------------------
                            Standard                    Prob                        
    Variable   Estimates       Error     t-value        >|t|  [95% Conf.   Interval]
   ------------------------------------------------------------------------------------

    Constant    1.52e+03         102        14.9       0.000    1.32e+03    1.72e+03 
      Income        3.17      0.0706        44.9       0.000        3.03        3.31 
         Age        32.6       0.936        34.8       0.000        30.7        34.4 
       Limit        1.68        1.69        0.99       0.323       -1.64           5
       
Source
------

fgls.src

.. seealso:: Functions :func:`glm`, :func:`gmmFitIV`, :func:`fglsControlCreate`, :func:`olsmt`
