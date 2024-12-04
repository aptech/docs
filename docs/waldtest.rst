waldTest
==============================================

Purpose
----------------
Performs a Wald test of joint hypothesis on model parameters.

Format
----------------
.. function:: { waldTest, p_value } = waldTest(out [, R, q, tau, joint])
              { waldTest, p_value } = waldTest(sigma, params [, R, q, df_residuals, varnames])  

    :param out: Post-estimation filled output structure. Valid structure types include: :class:`olsmtOut`,  :class:`gmmOut`, :class:`glmOut`, and :class:`qfitOut`.
    :type out: Struct

    :param sigma: Parameter variance-covariance estimation.
    :type sigma: Matrix

    :param params: Parameter estimates.
    :type params: Vector
    
    :param R: Optional, LHS of the null hypothesis. Should be specified in terms of the model variables, with a separate row for each hypothesis. The function accepts linear combinations of the model variables.  If using matrix inputs and no variable names are specified, variables labeled by default ``"X1", "X2", "X3", ...``. 

        e.g to test the hypothesis ``"X1 - X4 = 0"`` jointly with the hypothesis that ``"2*X3 - X2 = 0"``. The R matrix input will be:

        ::      

            // Specify R matrix
            R_sa = "X1 - X4"$|"2*X3 - X2";

        To include all individual variables use "all". Default is to test the joint hypothesis of all variables. 
    :type R: String Array

    :param q: Optional, RHS of the null hypothesis. Must be numeric vector. Default is to set RHS of all hypothesis to zero.
    
        e.g to test the hypothesis ``"X1 - X4 = 2"`` jointly with the hypothesis that ``"2*X3 - X2 = 0"`` The q matrix input will be:

        ::             
        
            // Specify R matrix
            R_sa = "X1 - X4"$|"2*X3 - X2";

            // Specify q matrix
            q = 2|0;

    :type q: Vector

    :param tau: Optional, tau level corresponding to the testing hypothesis. Default is to jointly tests across all tau values. To include all tau levels use ``"all"``. Only valid for the :class:`qfitOut` structure.
    :type tau: Vector

    :param joint:  Optional, specification to test :func:`quantileFit` hypotheses jointly across all coefficients for the :class:`qfitOut` structure. Default = 1.
    :type joint: Scalar
    
    :param df_residuals: Optional, model degrees of freedom for the F-test. Default = 500.
    :type df_residuals: Scalar
    
    :param varnames: Optional, variable names.
    :type varnames: String array
    
    :return waldTest: The statistic for testing the null joint hypothesis specified by the R and q inputs.
    :rtype waldTest: Vector

    :return p_value: The p-value associated with the Wald statistic.
    :rtype p_value: Vector

Examples
----------------

Basic test with estimation output structure
++++++++++++++++++++++++++++++++++++++++++++
The default settings of the :func:`waldTest` procedure test the joint hypotheses that all variables equal zero. 

::

    // Run ols estimation
    // Load data
    fname = getGAUSSHome("examples/auto2.dta");

    // Run OLS estimation
    struct olsmtOut out;
    out = olsmt(auto2, "price ~ mpg + rep78");

The OLS results are:

::

    Valid cases:                    69      Dependent variable:               price
    Missing cases:                   5      Deletion method:               Listwise
    Total SS:            576796958.870      Degrees of freedom:                  63
    R-squared:                   0.258      Rbar-squared:                     0.199
    Residual SS:         427776355.434      Std error of est:              2605.782
    F(5,63):                     4.389      Probability of F:                 0.002

                                     Standard                 Prob   Standardized  Cor with
    Variable             Estimate      Error      t-value     >|t|     Estimate    Dep Var
    ---------------------------------------------------------------------------------------
    CONSTANT                10450     2251.04     4.64229     0.000       ---         ---   
    mpg                  -280.261     61.5767    -4.55142     0.000   -0.564519   -0.455949 
    rep78: Fair           877.635     2063.28    0.425358     0.672   0.0971824  -0.0223477 
    rep78: Average        1425.66     1905.44    0.748204     0.457     0.24444   0.0859051 
    rep78: Good           1693.84     1942.67    0.871914     0.387    0.257252   -0.015317 
    rep78: Excellent      3131.98     2041.05      1.5345     0.130    0.396546   -0.035102 

    // Call waldTest 
    call waldTest(out);

The code above will print a test summary.

::

    ===================================
    Wald test of null joint hypothesis:

    CONSTANT         =  0 
    mpg              =  0 
    rep78: Fair      =  0 
    rep78: Average   =  0 
    rep78: Good      =  0 
    rep78: Excellent =  0 
    -----------------------------------
    F( 6, 63 ):                 67.6332 
    Prob > F :                   0.0000 
    ===================================

Example One: Testing that all variables equal zero
++++++++++++++++++++++++++++++++++++++++++++++++++
The default settings of the :func:`waldTest` procedure test the joint hypotheses that all variables equal zero. 

::

    // Run ols estimation
    // Load data
    fname = getGAUSSHome("examples/auto2.dta");

    // Run OLS estimation
    struct olsmtOut out;
    out = olsmt(auto2, "price ~ mpg + rep78");
    
    // Call waldTest 
    call waldTest(out);

The code above will print a test summary.

::

    ===================================
    Wald test of null joint hypothesis:

    CONSTANT         =  0 
    mpg              =  0 
    rep78: Fair      =  0 
    rep78: Average   =  0 
    rep78: Good      =  0 
    rep78: Excellent =  0 
    -----------------------------------
    F( 6, 63 ):                 67.6332 
    Prob > F :                   0.0000 
    ===================================

Example Two: Testing that subset of variables equal zero
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
In the first example we tested all variables. Now suppose we wish to test all variable except the constant. This is done by specifying a hypothesis matrix, ``R``.

::

    // Specify hypotheses
    R = "mpg"$|"rep78: Fair"$|"rep78: Average"$|"rep78: Good"$|"rep78: Excellent";

    // Call waldTest to test joint hypotheses that
    // mpg = 0
    // rep78: Fair = 0
    // rep78: Average = 0
    // rep78: Good = 0
    // rep78: Excellent = 0 
    call waldTest(out, R);

Note that this is the same as the F-test reported from the OLS estimation:

::

    ===================================
    Wald test of null joint hypothesis:

    mpg              =  0 
    rep78: Fair      =  0 
    rep78: Average   =  0 
    rep78: Good      =  0 
    rep78: Excellent =  0 
    -----------------------------------
    F( 5, 63 ):                  4.3893 
    Prob > F :                   0.0017 
    ===================================

Example Three: Testing the equality of variables
+++++++++++++++++++++++++++++++++++++++++++++++++
The true usefulness of the :func:`waldTest` procedure is the ability to more than if variables are equal to zero. For example, suppose we want to test if the coefficients for the *rep78: Average* and *rep78: Good* categories are equal. We can do this by testing the hypothesis that ``rep78: Average - rep78: Good = 0``.

::  

    // Specify R matrix
    R = "rep78: Good - rep78: Average";

    // Call waldTest 
    call waldTest(out, R);

::

    ===================================
    Wald test of null joint hypothesis:
    rep78: Good - rep78: Average =  0
    -----------------------------------
    F( 1, 63 ):                  0.1155 
    Prob > F :                   0.7351 
    ===================================

    In this case, we cannot reject the null hypothesis. 

.. seealso:: :func:`qFitSlopeTest`