
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
    Number of vars:            0                                       
    ===================================================================
                                      Standard                    Prob
    Variable               Estimate       Error     t-value        >|t|
    -------------------------------------------------------------------
    CONSTANT                  0.067       0.102       0.656       0.514 
    x1                       -0.027       0.097      -0.281       0.780 
    x2                       -0.107       0.091      -1.182       0.240 
    x3                        0.277       0.093       2.962       0.004 
    x4                        0.068       0.111       0.612       0.542 
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
    Deviance:            458.517           Link function:         logit
    Pearson Chi-square:  397.490           AIC:                 470.517
    Log likelihood:     -229.259           BIC:                 494.466
    Dispersion:                1           Iterations:              494
    Number of vars:            0                                       
    ===================================================================
                                      Standard                    Prob
    Variable               Estimate       Error     z-value        >|z|
    -------------------------------------------------------------------
    CONSTANT                 -3.990       1.140      -3.500       0.000 
    rank: 2                  -0.675       0.316      -2.134       0.033 
    rank: 3                  -1.340       0.345      -3.881       0.000 
    rank: 4                  -1.551       0.418      -3.713       0.000 
    gre                       0.002       0.001       2.070       0.038 
    gpa                       0.804       0.332       2.423       0.015 
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
    ===================================================================
    Valid cases:              68           Dependent variable: smoker: Yes
    Degrees of freedom:       64           Distribution        binomial
    Deviance:             85.787           Link function:         logit
    Pearson Chi-square:   67.797           AIC:                  93.787
    Log likelihood:      -42.893           BIC:                 102.665
    Dispersion:                1           Iterations:              102
    Number of vars:            0                                       
    ===================================================================
                                      Standard                    Prob
    Variable               Estimate       Error     z-value        >|z|
    -------------------------------------------------------------------
    CONSTANT                 -1.067       0.697      -1.531       0.126 
    total_bill               -0.024       0.057      -0.419       0.675 
    tip                       0.209       0.360       0.580       0.562 
    sex: Male                 0.464       0.522       0.889       0.374 
    ===================================================================

    Note: Dispersion parameter for BINOMIAL distribution taken to be 1 
    
    
    ====================================================================================
    time: Dinner
    ====================================================================================
    
    Generalized Linear Model
    ===================================================================
    Valid cases:             179           Dependent variable: smoker: Yes
    Degrees of freedom:      175           Distribution        binomial
    Deviance:            235.159           Link function:         logit
    Pearson Chi-square:  180.370           AIC:                 243.159
    Log likelihood:     -117.580           BIC:                 255.909
    Dispersion:                1           Iterations:              255
    Number of vars:            0                                       
    ===================================================================
                                      Standard                    Prob
    Variable               Estimate       Error     z-value        >|z|
    -------------------------------------------------------------------

    CONSTANT                 -0.511       0.460      -1.112       0.266 
    total_bill                0.043       0.023       1.922       0.055 
    tip                      -0.196       0.143      -1.367       0.172 
    sex: Male                -0.331       0.339      -0.975       0.330 
    ===================================================================

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
    Deviance:           1330.683           Link function:      identity
    Pearson Chi-square: 1330.683           AIC:                 429.817
    Log likelihood:     -211.909           BIC:                 436.729
    Dispersion:               18           Iterations:              436
    Number of vars:            0                                       
    ===================================================================
                                      Standard                    Prob
    Variable               Estimate       Error     t-value        >|t|
    -------------------------------------------------------------------
    weight                   -0.001       0.000      -3.235       0.002 
    gear_ratio                8.424       0.446      18.872       0.000 
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
    Deviance:            533.814           Link function:      identity
    Pearson Chi-square:  533.814           AIC:                  93.189
    Log likelihood:      -42.594           BIC:                  95.448
    Dispersion:               53           Iterations:               95
    Number of vars:            0                                       
    ===================================================================
                                      Standard                    Prob
    Variable               Estimate       Error     t-value        >|t|
    -------------------------------------------------------------------
    CONSTANT                -35.983       9.437      -3.813       0.003 
    unemployment             -0.005       0.919      -0.005       0.996 
    hourly_earn              15.487       2.243       6.906       0.000 
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
    Deviance:           66106798.130           Link function:      identity
    Pearson Chi-square: 66106798.130           AIC:                5951.278
    Log likelihood:     -2970.639           BIC:                5971.235
    Dispersion:           166936           Iterations:             5971
    Number of vars:            0                                       
    ===================================================================
                                      Standard                    Prob
    Variable               Estimate       Error     t-value        >|t|
    -------------------------------------------------------------------
    CONSTANT                246.185      46.535       5.290       0.000 
    Gender: 2                24.577      40.889       0.601       0.548 
    Married: 2              -21.279      41.963      -0.507       0.612 
    Income                    6.063       0.581      10.439       0.000 
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
  Deviance:           66106798.130           Link function:      identity
  Pearson Chi-square: 66106798.130           AIC:                5951.278
  Log likelihood:     -2970.639           BIC:                5971.235
  Dispersion:           166936           Iterations:             5971
  Number of vars:            0                                       
  ===================================================================
                                    Standard                    Prob
  Variable               Estimate       Error     t-value        >|t|
  -------------------------------------------------------------------
  CONSTANT                246.185      46.535       5.290       0.000 
  Gender: Female           24.577      40.889       0.601       0.548 
  Married: Married        -21.279      41.963      -0.507       0.612 
  Income                    6.063       0.581      10.439       0.000 
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

    Valid cases:                  400     Dependent Variable:                      admit
    Degrees of freedom:           394     Distribution:                         binomial
    Deviance:                   458.4     Link function:                          probit
    Pearson Chi-square:         397.7     AIC:                                     470.4
    Log likelihood:            -229.2     BIC:                                     494.4
    Dispersion:                     1     Iterations:                                  4

                                              Standard                              Prob
    Variable                 Estimate            Error          z-value             >|z|
    ----------------     ------------     ------------     ------------     ------------
    CONSTANT                  -2.3868          0.67395          -3.5416      0.000397733 
    rank: 2                   -0.4154          0.19498          -2.1305        0.0331297 
    rank: 3                  -0.81214          0.20836          -3.8978         < 0.0001 
    rank: 4                   -0.9359          0.24527          -3.8158      0.000135764 
    gre                     0.0013756       0.00065003           2.1162        0.0343292 
    gpa                       0.47773           0.1972           2.4226        0.0154097 

    // Note: Dispersion parameter for BINOMIAL distribution taken to be 1

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

    Valid cases:                  200     Dependent Variable:                  num_award
    Degrees of freedom:           196     Distribution:                          poisson
    Deviance:                   189.4     Link function:                              ln
    Pearson Chi-square:         212.1     AIC:                                     373.5
    Log likelihood:            -182.8     BIC:                                     386.7
    Dispersion:                     1     Iterations:                                  6

                                               Standard                              Prob
    Variable                  Estimate            Error          z-value             >|z|
    ----------------      ------------     ------------     ------------     ------------
    CONSTANT                   -5.2471          0.65845          -7.9689         < 0.0001
    prog            2           1.0839          0.35825           3.0254       0.00248303
                    3          0.36981          0.44107          0.83844         0.401786
    math                      0.070152         0.010599           6.6186         < 0.0001

    // Note: Dispersion parameter for POISSON distribution taken to be 1

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
