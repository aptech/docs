
glm
==============================================

Purpose
----------------

Solves the generalized linear model problems.

Format
----------------
.. function:: out = glm(y, x, family[, var_names[, categoryIdx[, link]]])
              out = glm(y, x, family[, ctl])
              out = glm(dataset_name, formula, family[, ctl])

    :param y: the dependent, or response, variable. *n* is the number of the observations used in the analysis.
    :type y: Nx1 vector

    :param x: the independent, or explanatory, variables. *k* is the number of the independent variables.
    :type x: NxK matrix

    :param dataset_name: the name of dataset or dataframe. E.g. :code:`"credit.dat"`, :code:`"example.fmt"`, or `binary`.
    :type dataset_name: string or dataframe

    :param formula: formula string of the model.
        E.g :code:`"y ~ X1 + X2"`, ``y`` is the name of dependent variable, ``X1`` and ``X2`` are names of independent variables;
        E.g :code:`"y ~ ."`, ``.`` means including all variables except dependent variable ``y``;
        E.g :code:`"y ~ -1 + X1 + X2"`, ``-1`` means no intercept model.
    :type formula: string

    :param family: the distribution of the dependent variable. Options include:

        - :code:`"binomial"`
        - :code:`"gamma"`
        - :code:`"normal"`
        - :code:`"poisson"`
        - :code:`"inverse gaussian"`

    :type family: string

    :param var_names: Optional argument, the names of the variables. The first element must be the name of the dependent variable.
        e.g., :code:`var_names = "admit" $| "gre" $| "gpa" $| "rank"`, then :code:`"admit"` will be the label of the response variable, :code:`"gre"`, :code:`"gpa"`, :code:`"rank"` are the labels of the independent variables corresponding to the order in the *X* matrix.
    :type var_names: (k+1)x1⁢ string array or character matrix


    :param categoryIdx: Optional argument, :math:`k_d \leq k`. :math:`k_d` is the categorical variable index of *X* matrix.
        *categoryIdx* specifies the categorical variable columns to be used in the analysis. GAUSS will automatically include
        dataframe categories as categorical variables. If *categoryIdx* is specified with a dataframe, the columns specified by
        *categoryIdx* will supercede the categories in the dataframe.

        e.g. If *categoryIdx* = 0, then it means the independent variable does not contain any categorical variables or categories are specified in the dataframe;
        if :math:`\text{categoryIdx} = \{ 1\ 4 \}`, then it means that column 1 and column 4 in the *X* matrix are categorical variables.

        .. NOTE:: The function :func:`glm` uses the smallest number as the reference category in each categorical variable.

    :type categoryIdx: 1 × k_d matrix

    :param link: the link function. Options include:

        - :code:`"identity"`
        - :code:`"inverse"`
        - :code:`"inverse squared"`
        - :code:`"ln"`
        - :code:`"logit"`
        - :code:`"probit"`
        - :code:`"cloglog"`
        - :code:`"canonical"`

        The default link of each distribution is the canonical link function:

        - Normal -- identity;
        - Binomial -- logit;
        - Gamma -- inverse;
        - Poisson -- nature log.

    :type link: string

    :param ctl: Optional argument. For an instance named *ct1*, the members are:

        .. list-table::
            :widths: auto

            * - *ctl.varNames*
              - :math:`(k+1) \times 1` string array or character matrix, the names of the variables. The first element must be the name of the dependent variable.

            * - *ctl.categoryIdx*
              - :math:`1 × k_d` matrix, :math:`k_d \leq k`. *ctl.categoryIdx* specifies the categorical variable columns to be used in the analysis.  GAUSS will automatically include
                dataframe categories as categorical variables. If *categoryIdx* is specified with a dataframe, the columns specified by
                *categoryIdx* will supercede the categories in the dataframe.

                e.g. If *ctl.categoryIdx* = 0, then it means no categorical variable or categories should be determined by dataframe types;
                if *ctl.categoryIdx* = :code:`{ 1 4 }`, then it means that column 1 and column 4 in *x* matrix are categorical variables.

                .. NOTE:: :func:`glm` function uses the smallest number as the reference category in each categorical variable.

            * - *ctl.link*
              - string, the link function. Options include:

                - :code:`"identity"`
                - :code:`"inverse"`
                - :code:`"inverse squared"`
                - :code:`"ln"`
                - :code:`"logit"`
                - :code:`"probit"`
                - :code:`"cloglog"`
                - :code:`"canonical"`

                The default link is the canonical link for each distribution.

            * - *ctl.constantFlag*
              - scalar, flag of constant term. The negative number means no intercept model, e.g. :code:`"-1"`. This member will be ignored if a formula string is used.
            * - *ctl.printFlag*
              - string, :code:`"Y"` or :code:`"N"`, flag of print to screen. The :code:`"N"` means no printing.
            * - *ctl.maxIters*
              - scalar, maximum iterations. The default *ctl.maxIters* is 25.
            * - *ctl.eps*
              - scalar, convergence precision. The default is 1e-8.

    :type ctl: an instance of a :class:`glmControl` structure

    :return out: instance of :class:`glmOut` struct structure. For an instance named *out*, the members are:

        .. list-table::
            :widths: auto

            * - *out.modelInfo*
              - An instance of a :class:`glmModelInfo` structure. The members are:

                :out.modelInfo.distribution: string, the distribution of dependent variable
                :out.modelInfo.link: string, the link function used in the procedure
                :out.modelInfo.yName: string, the label of dependent variable
                :out.modelInfo.xNames: string array, the label of independent variables with intercept and dummy variables for each categorical variable
                :out.modelInfo.varNames: string array, the label of variables
                :out.modelInfo.n: scalar, the number of valid cases used in the analysis
                :out.modelInfo.df: scalar, degree of freedom

            * - *out.modelSelect*
              - An instance of a :class:`glmModelSelection` structure. The members are:

                :out.modelSelect.deviance: scalar, the residual deviance from the fit model. The greater the deviance, the poorer the fit.
                :out.modelSelect.pearson: scalar, the Pearson Chi-square Statistics. Pearson statistic is an alternative to the deviance for testing the fitof certain GLMs.
                :out.modelSelect.LL: scalar, the log likelihood of the fit model
                :out.modelSelect.dispersion: scalar, the estimate of the dispersion parameter by Pearson statistic and degree of freedom. It is fixed at 1 when the distribution is "poisson" or "binomial".
                :out.modelSelect.aic: scalar, Akaike information criterion (AIC)
                :out.modelSelect.bic: scalar, Bayesian information criterion (BIC)

            * - *out.coef*
              - An instance of a :class:`glmParameters` structure. The members are:

                :out.coef.estimates: matrix, the estimate value of parameters
                :out.coef.se: matrix, the standard error of parameters
                :out.coef.testStat: matrix, the statistic value of parameters
                :out.coef.testStatName: string, the name of test statistic
                :out.coef.pvalue: scalar, the p_value of parameters
                
            * - *out.yhat*
              - scalar, the fitted mean values for response variable
            * - *out.residuals*
              - matrix, residuals on the linear predictor scale, equal to the adjusted response value minus the fitted linear predictors
            * - *out.covmat*
              - matrix, the covariance matrix for the parameters
            * - *out.corrmat*
              - matrix, the correlation matrix for the parameters
            * - *out.constantFlag*
              - string, flag of constant term.
            * - *out.iteration*
              - scalar, the number of iterations of IWLS used
            * - *out.maxIters*
              - scalar, the maximum iterations
            * - *out.eps*
              - scalar, convergence precision

    :rtype out: struct

Examples
----------------

Ordinary linear regression with simulated data matrices.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Set random number seed for repeatable random numbers
    rndseed 86;

    // Simulate data using rndn function
    x = rndn(100, 4);
    y = rndn(100, 1);

    // Call glm function with the minimum inputs
    call glm(y, x, "normal");

This example will compute a least squares regression of *y* on *x*. The results will be shown in the program input / output window. The return values are discarded by using a `call` statement.

::

    Generalized Linear Model
    ===================================================================
    Valid cases:             100           Dependent variable:        y
    Degrees of freedom:       95           Distribution          normal
    Deviance:             99.370           Link function:      identity
    Pearson Chi-square:   99.370           AIC:                 295.156
    Log likelihood:     -141.578           BIC:                 310.787
    Dispersion:                1           Iterations:              310
    Number of vars:            5                                       
    ===================================================================
                                       Standard                    Prob
    Variable               Estimate       Error     t-value        >|t|
    -------------------------------------------------------------------

    Constant               0.067084     0.10233     0.65556     0.51369 
    x1                    -0.027278    0.097162    -0.28074     0.77952 
    x2                     -0.10747    0.090888     -1.1825     0.23996 
    x3                      0.27659    0.093397      2.9615    0.003867 
    x4                     0.067915     0.11099      0.6119     0.54206 
    ===================================================================

Logistic regression using a formula string to reference data in a CSV file containing categorical variables.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Create string with fully pathed file name
    fname = getGAUSShome("examples/binary.csv");
    
    // Load data and specify rank and admit as
    // categorical variables
    data = loadd(fname, "cat(admit) + cat(rank) + gre + gpa");
    
    /*
    ** Call glm function with formula string
    */
    call glm(data, "admit ~ rank + gre + gpa", "binomial");

The code above will produce the following output. Note that :math:`rank = 1` is used as the base case.

::

    Generalized Linear Model
    ===================================================================
    Valid cases:             400           Dependent variable:    admit
    Degrees of freedom:      394           Distribution        binomial
    Deviance:                459           Link function:         logit
    Pearson Chi-square:      397           AIC:                 470.517
    Log likelihood:         -229           BIC:                 494.466
    Dispersion:                1           Iterations:              494
    Number of vars:            6                                       
    ===================================================================
                                       Standard                    Prob
    Variable               Estimate       Error     z-value        >|z|
    -------------------------------------------------------------------

    CONSTANT                  -3.99        1.14     -3.5001  0.00046503 
    rank: 2                -0.67544     0.31649     -2.1342    0.032829 
    rank: 3                 -1.3402     0.34531     -3.8812  0.00010394 
    rank: 4                 -1.5515     0.41783     -3.7131  0.00020471 
    gre                   0.0022644    0.001094      2.0699    0.038465 
    gpa                     0.80404     0.33182      2.4231    0.015388 
    ===================================================================

    Note: Dispersion parameter for BINOMIAL distribution taken to be 1 


Logistic regression for each subset of a categorical variable
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

In the example below, we will estimate a logistic regression model for the case where *time* equals *"Lunch"* and another where *time* equals *"Dinner"*, using the `by` keyword.

::

    // Load all variables from the dataset
    tips = loadd(getGAUSShome("examples/tips2.dta"));
    
    // Estimate a logistic regression model for:
    //     time = Lunch
    //     time = Dinner
    call glm(tips, "smoker ~ total_bill + tip + sex + by(time)", "binomial");

::

    ====================================================================================
    time: Lunch
    ====================================================================================
    
    Generalized Linear Model
    ======================================================================
    Valid cases:              68           Dependent variable: smoker: Yes
    Degrees of freedom:       64           Distribution           binomial
    Deviance:               85.8           Link function:            logit
    Pearson Chi-square:     67.8           AIC:                     93.787
    Log likelihood:        -42.9           BIC:                    102.665
    Dispersion:                1           Iterations:                 102
    Number of vars:            4                                       
    =====================================================================
                                         Standard                    Prob
    Variable               Estimate         Error     z-value        >|z|
    ---------------------------------------------------------------------

    CONSTANT                -1.0674      0.69733      -1.5307     0.12583 
    total_bill            -0.023941     0.057074     -0.41947     0.67487 
    tip                     0.20882      0.35988      0.58025     0.56175 
    sex: Male               0.46393      0.52191      0.88891     0.37405 
    =====================================================================

    Note: Dispersion parameter for BINOMIAL distribution taken to be 1  
    
    
    ====================================================================================
    time: Dinner
    ====================================================================================
    
    Generalized Linear Model
    ======================================================================
    Valid cases:             179           Dependent variable: smoker: Yes
    Degrees of freedom:      175           Distribution           binomial
    Deviance:                235           Link function:            logit
    Pearson Chi-square:      180           AIC:                    243.159
    Log likelihood:         -118           BIC:                    255.909
    Dispersion:                1           Iterations:                 255
    Number of vars:            4                                       
    ======================================================================
                                           Standard                   Prob
    Variable                Estimate          Error     z-value       >|z|
    ----------------------------------------------------------------------

    CONSTANT                 -0.5111       0.4596        -1.112    0.26612 
    total_bill              0.043252     0.022504         1.922    0.05461 
    tip                     -0.19582      0.14327       -1.3668     0.1717 
    sex: Male               -0.33096       0.3395      -0.97485    0.32964 
    ======================================================================

    Note: Dispersion parameter for BINOMIAL distribution taken to be 1 

Running a no intercept model from a STATA DTA file.
++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    new;
    cls;

    // File name with full path
    fname = getGAUSShome("examples/auto2.dta");

    // Load all variables in the auto2 dataset
    data = loadd(fname);
        
    // Declare 'fit' to be a glmOut structure
    struct glmOut fit;

    // Call 'glm' with no intercept model
    fit = glm(data, "mpg ~ -1 + weight + gear_ratio",  "normal");

After running the code above, the output is :

::

    Generalized Linear Model
    ===================================================================
    Valid cases:              74           Dependent variable:      mpg
    Degrees of freedom:       72           Distribution          normal
    Deviance:           1.33e+03           Link function:      identity
    Pearson Chi-square: 1.33e+03           AIC:                 429.817
    Log likelihood:         -212           BIC:                 436.729
    Dispersion:               18           Iterations:              436
    Number of vars:            2                                       
    ===================================================================
                                       Standard                    Prob
    Variable               Estimate       Error     t-value        >|t|
    -------------------------------------------------------------------

    weight               -0.0014124  0.00043663     -3.2348   0.0018396 
    gear_ratio               8.4236     0.44635      18.872  1.3699e-29 
    ===================================================================

Running a no intercept model from a SAS sas7bdat file.
++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    new;
    cls;

    // File name with full path
    fname = getGAUSSHome("examples/detroit.dta");

    // Load dataset
    data = loadd(fname);
    
    // Declare 'fit' to be a glmOut structure
    struct glmOut fit;

    // Call 'glm' with no intercept model
    fit = glm(data, "homicide ~ unemployment + hourly_earn",  "normal");

After running the code above, the output is :

::

    Generalized Linear Model
    ===================================================================
    Valid cases:              13           Dependent variable: homicide
    Degrees of freedom:       10           Distribution          normal
    Deviance:                534           Link function:      identity
    Pearson Chi-square:      534           AIC:                  93.189
    Log likelihood:        -42.6           BIC:                  95.448
    Dispersion:               53           Iterations:               95
    Number of vars:            3                                       
    ===================================================================
                                       Standard                    Prob
    Variable               Estimate       Error     t-value        >|t|
    -------------------------------------------------------------------

    CONSTANT                -35.983      9.4372     -3.8128   0.0034133 
    unemployment         -0.0049983     0.91882  -0.0054399     0.99577 
    hourly_earn              15.487      2.2427      6.9057  4.1653e-05 
    ===================================================================

Ordinary linear regression with categorical variables in a matrix.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Sometimes it is necessary or preferable to reference model variables by index rather than name. This example illustrates the use of numeric indexing of model variables and how to specify categorical variables in a matrix.

::

    new;
    cls;

    // Create filename with full path
    dataset = getGAUSSHome("examples/credit.dat");

    // Import all data from the dataset
    data = loadd(dataset);

    // Select the independent variables by index
    x = data[., 1 7 9] ;

    // Select the dependent variable by index
    y = data[., 11];

    // Get the names of the variables in the dataset
    label = getColNames(data, 11|1|7|9);

    // Specify that the 2nd and 3rd columns in 'x' are categorical variables
    categoryIdx = { 2 3 };

    // Call glm function with three necessary inputs and two optional inputs
    call glm(y, x, "normal", label, categoryIdx);

*label* is a string array containing all of the variable names from :file:`credit.dat` returned from the :func:`getColNames` function. The first element must be the label of the dependent variable, followed by the labels for the independent variables corresponding to the order in the *x* matrix.
:code:`"Gender"` and :code:`"Married"` are categorical variables. The :func:`glm` chooses the smallest number(1) as the base category in each categorical variable. The following shows the output:

::

    Generalized Linear Model
    ===================================================================
    Valid cases:             400           Dependent variable:  Balance
    Degrees of freedom:      396           Distribution          normal
    Deviance:           6.61e+07           Link function:      identity
    Pearson Chi-square: 6.61e+07           AIC:                5951.278
    Log likelihood:    -2.97e+03           BIC:                5971.235
    Dispersion:           166936           Iterations:             5971
    Number of vars:            4                                       
    ===================================================================
                                       Standard                    Prob
    Variable               Estimate       Error     t-value        >|t|
    -------------------------------------------------------------------

    Constant                 246.19      46.535      5.2903  2.0256e-07 
    Gender: 2                24.577      40.889     0.60108     0.54813 
    Married: 2              -21.279      41.963    -0.50708     0.61238 
    Income                   6.0626     0.58077      10.439  1.0685e-22 
    ===================================================================

Ordinary linear regression with categorical variables in a dataframe.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

  new;
  cls;

  // Import data as dataframe
  // with `Gender` and `Married` as
  // categorical variables
  fname = getGAUSSHome("examples/credit.dat");
  credit = loadd(fname, "Income + cat(Gender) + cat(Married) + Balance");

  // Relabel categories for `Gender`
  credit = setcollabels(move(credit), "Male"$|"Female", 0|1, "Gender");

  // Relabel categories for `Married`
  credit = setcollabels(move(credit), "Single"$|"Married", 0|1, "Married");

  // Call glm
  call glm(credit, "Balance ~ Gender + Married + Income", "normal");

The categorical variables code:`"Gender"` and code:`"Married"` are now automatically detected by GAUSS, based on their dataframe types. In addition, the variable names are automatically detected.

::

  Generalized Linear Model
  ===================================================================
  Valid cases:             400           Dependent variable:  Balance
  Degrees of freedom:      396           Distribution          normal
  Deviance:           6.61e+07           Link function:      identity
  Pearson Chi-square: 6.61e+07           AIC:                5951.278
  Log likelihood:    -2.97e+03           BIC:                5971.235
  Dispersion:           166936           Iterations:             5971
  Number of vars:            4                                       
  ===================================================================
                                     Standard                    Prob
  Variable               Estimate       Error     t-value        >|t|
  -------------------------------------------------------------------

  CONSTANT                 246.19      46.535      5.2903  2.0256e-07 
  Gender: Female           24.577      40.889     0.60108     0.54813 
  Married: Married        -21.279      41.963    -0.50708     0.61238 
  Income                   6.0626     0.58077      10.439  1.0685e-22 
  ===================================================================

Using a control structure
+++++++++++++++++++++++++

Use a :class:`glmControl` structure to control the link function and a :class:`glmOut` structure to store the reuslts for a Probit regression with categorical variables.

::

    new;

    // Create file name with full path
    fname = getGAUSShome("examples/binary.csv");
    
    // Load data and specify rank and admit as
    // categorical variables
    data = loadd(fname, "cat(admit) + cat(rank) + gre + gpa");
    
    // Declare 'binary_ctl' as a glmControl structure
    struct glmControl binary_ctl;

    // Specify the link function
    binary_ctl.link = "probit";

    // Save out the results in glmOut structure
    struct glmOut out1;
    out1 = glm(data, "admit ~ factor(rank) + gre + gpa", "binomial", binary_ctl);

After running above code, the model estimates and diagnostic information will be stored in the *out1* structure and the following output report will be displayed.

::

    Generalized Linear Model
    ===================================================================
    Valid cases:             400           Dependent variable:    admit
    Degrees of freedom:      394           Distribution        binomial
    Deviance:                458           Link function:        probit
    Pearson Chi-square:      398           AIC:                 470.413
    Log likelihood:         -229           BIC:                 494.362
    Dispersion:                1           Iterations:              494
    Number of vars:            6                                       
    ===================================================================
                                       Standard                    Prob
    Variable               Estimate       Error     z-value        >|z|
    -------------------------------------------------------------------

    CONSTANT                -2.3868     0.67395     -3.5416  0.00039773 
    rank: 2                 -0.4154     0.19498     -2.1305     0.03313 
    rank: 3                -0.81214     0.20836     -3.8978  9.7067e-05 
    rank: 4                 -0.9359     0.24527     -3.8158  0.00013576 
    gre                   0.0013756  0.00065003      2.1162    0.034329 
    gpa                     0.47773      0.1972      2.4226     0.01541 
    ===================================================================

    Note: Dispersion parameter for BINOMIAL distribution taken to be 1 

A Poisson regression model with categorical variables, using matrix inputs.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    new;
    cls;

    // Load all data from the .fmt matrix file
    fname = getGAUSShome() $+ "examples/poisson_sim.fmt";
    data = loadd(fname);

    // Index dependent variable, 'num_award'
    y = data[., 2];

    // Index independent variable, 'prog' and 'math'
    x = data[., 3 4];

    /*
    ** Specify the variable names
    ** since the matrices do not contain variable names
    */
    string var_names = { "num_award", "prog", "math" };

    /*
    ** Indicate that the first variable in 'x'
    ** is a categorical variable
    */
    category_idx = 1;

    // specify the link function, 'ln'
    link = "ln";

    /*
    ** Declare the glmOut structure
    ** All the results are saved in the out_poi
    */
    struct glmOut out_poi;
    out_poi = glm(y, x, "poisson", var_names, category_idx, link);

After running above code, the output is:

::

    Generalized Linear Model
    ====================================================================
    Valid cases:             200           Dependent variable: num_award
    Degrees of freedom:      196           Distribution          poisson
    Deviance:                189           Link function:             ln
    Pearson Chi-square:      212           AIC:                  373.505
    Log likelihood:         -183           BIC:                  386.698
    Dispersion:                1           Iterations:               386
    Number of vars:            4                                       
    ====================================================================
                                      Standard                      Prob
    Variable               Estimate       Error     z-value         >|z|
    --------------------------------------------------------------------

    CONSTANT                -5.2471     0.65845     -7.9689   1.6014e-15 
    prog: 2                  1.0839     0.35825      3.0254     0.002483 
    prog: 3                 0.36981     0.44107     0.83844      0.40179 
    math                   0.070152    0.010599      6.6186    3.625e-11 
    ====================================================================

    Note: Dispersion parameter for POISSON distribution taken to be 1 

Using a :class:`glmOut` structure to save result for a Gamma regression with categorical variables.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    new;
    cls;

    // File name with full path
    file = getGAUSShome("examples/yarn.xlsx");

    // Read 4th column as a numeric matrix
    y = xlsReadM(file, "D2:D28");

    // Read columns 1, 2 and 3 as character data
    x = xlsReadSA(file, "A2:C28");

    // Find unique categorical levels
    from = uniquesa(x[., 1]);

    // Numeric categorical levels
    to = { 1, -1, 0 };

    // Reclassify the character to number
    x = reclassify(x, from, to);

    // Declare 'ctl_gamma' as a glmControl struct
    struct glmControl ctl_gamma;

    /*
    ** Read variable names and transpose
    ** to a column vector
    */
    ctl_gamma.varNames = xlsReadSA(file, "A1:D1")';

    // Specify categorical columns
    ctl_gamma.categoryIdx = { 1 2 3 };

    // Specify link function
    ctl_gamma.link = "ln";

    // Declare 'out_gamma' to be a glmOut structure
    struct glmOut out_gamma;

    // Call 'glm' and fill 'out_gamma' with results
    out_gamma = glm(y, x, "gamma", ctl_gamma);

In this example, the dataset :file:`yarn.xlsx` is used to perform a Gamma regression.
After running the code above, the output is :

::

    Generalized Linear Model

    Valid cases:                   27     Dependent Variable:                yarn_length
    Degrees of freedom:            20     Distribution:                            gamma
    Deviance:                  0.7089     Link function:                              ln
    Pearson Chi-square:        0.6917     AIC:                                     336.5
    Log likelihood:            -160.3     BIC:                                     346.9
    Dispersion:               0.03458     Iterations:                                  5

                                               Standard                              Prob
    Variable                  Estimate            Error          t-value             >|t|
    ----------------      ------------     ------------     ------------     ------------
    CONSTANT                    6.4841          0.09469           68.477         < 0.0001
    amplitude       0           0.9136         0.087666           10.421         < 0.0001
                    1           1.6791         0.087666           19.153         < 0.0001
    load            0         -0.64738         0.087666          -7.3846         < 0.0001
                    1          -1.2654         0.087666          -14.435         < 0.0001
    cycles          0         -0.31872         0.087666          -3.6356       0.00164628
                    1          -0.7701         0.087666          -8.7844         < 0.0001

Using a "\*.dat" file directly in :func:`glm` for a Inverse Gaussian distribution.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    new;
    cls;

    // File name with full path
    fname = getGAUSShome("examples/clotting_time.dat");

    // Load plasma and lot1 variables
    data = loadd(fname, "plasma + lot1");
    
    // Declare 'fit_inv' to be a glmOut structure
    struct glmOut fit_inv;

    // Call 'glm' and fill 'fit_inv' with results
    fit_inv = glm(data, "plasma ~ lot1",  "inverse gaussian");

After running the code above, the output is:

::

    Generalized Linear Model

    Valid cases:                    9     Dependent Variable:                     plasma
    Degrees of freedom:             7     Distribution:                 inverse gaussian
    Deviance:                 0.03557     Link function:                 inverse squared
    Pearson Chi-square:       0.03511     AIC:                                      71.1
    Log likelihood:            -32.55     BIC:                                     71.69
    Dispersion:              0.005016     Iterations:                                  6


                                              Standard                              Prob
    Variable                 Estimate            Error          t-value             >|t|
    ----------------     ------------     ------------     ------------     ------------
    CONSTANT               -0.0034177       0.00074729          -4.5735       0.00256355
    lot1                   0.00019223       4.0768e-05           4.7154       0.00216923

Running a linear regression model using data transformations with HDF5 file.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    new;
    cls;

    // Give a fully pathed HDF5 file name
    file_name = getGAUSShome("examples/nba_data.h5");

    /*
    ** Add the file schema "h5://" to the front
    ** Given a dataset name in above file
    ** and the dataset name "/nba_data" to the back
    */
    dataset = "h5://" $+ file_name $+ "/nba_data";

    // Load 'Weight', 'Height', and  'Age' data
    data = loadd(dataset, "Weight + Height + Age");
    
    /*
    ** Define the formula for the linear model,
    ** using 'ln' data transformation
    */
    formula = "ln(Weight) ~ ln(Height) + Age";

    // Call 'glm'
    call glm(data, formula,  "normal");

After running the code above, the output is :

::

    Generalized Linear Model

    Valid cases:                  505     Dependent Variable:                 ln(Weight)
    Degrees of freedom:           502     Distribution:                           normal
    Deviance:                   2.268     Link function:                        identity
    Pearson Chi-square:         2.268     AIC:                                     -1289
    Log likelihood:             648.4     BIC:                                     -1272
    Dispersion:              0.004517     Iterations:                                  2


                                              Standard                              Prob
    Variable                 Estimate            Error          t-value             >|t|
    ----------------     ------------     ------------     ------------     ------------
    CONSTANT                  -4.6683          0.29683          -15.727         < 0.0001
    ln(Height)                 2.2842         0.067824           33.678         < 0.0001
    Age                     0.0029575       0.00069211           4.2731         < 0.0001

Remarks
-------

#. The :class:`glmControl` structure stores the user defined options.
#. The :class:`glmOut` structure stores all the results after running :func:`glm` function.
#. For the categorical variables, :func:`glm` chooses the smallest value as the
   base category. You can change the base category by using the
   reclassify or recode functions to change the base category with the
   smallest value in the variable.
#. The *dispersion* parameter is calculated based on Pearson Chi-square Statistics.
#. The :func:`glm` function cannot handle missing values. You can use :func:`packr`
   function to delete the rows of a matrix that contain any missing values.
#. The weights for each observation are equal.
#. The supported dataset types are CSV, Excel (XLS, XLSX), HDF5, GAUSS Matrix (FMT), GAUSS Dataset (DAT), Stata (DTA) and SAS (SAS7BDAT, SAS7BCAT).

For HDF5 files, the dataset must include file schema and both file name and dataset name must be provided, e.g. :code:`glm("h5://C:/gauss23/examples/testdata.h5/mydata", formula, family)`

Source
------

glm.src

.. seealso:: Functions :func:`ols`, :func:`olsmt`, :func:`reclassify`, :func:`packr`
