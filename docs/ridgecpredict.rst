ridgeCPredict
====================

Purpose
----------------------
Predicts responses using the output from :func:`ridgeCFit` and matrix of independent variables.

Format
-------------------

.. function:: predictions = ridgeCPredict(mdl, x_test)

    :return mdl: An instance of a :class:`ridgeModel` structure. An instance named *mdl* will have the following members:

        .. csv-table::
            :widths: auto

            "mdl.alpha_hat","(*1 x nlambdas vector*) The estimated value for the intercept for each provided *lambda*."
            "mdl.beta_hat","(*P x nlambdas matrix*) The estimated parameter values for each provided *lambda*."
            "mdl.mse_train","(*nlambdas x 1 vector*) The mean squared error for each set of parameters, computed on the training set."
            "mdl.lambda","(*nlambdas x 1 vector*) The *lambda* values used in the estimation."

    :rtype mdl: struct

    :param x_test: The independent variables.
    :type x_test: NxP matrix

    :return predictions: The predictions.
    :rtype predictions: Nx1 numeric or string vector

Examples
-------------

::

    new;
    library gml;

    rndseed 23423;

    // Create file name with full path
    fname = getGAUSSHome("pkgs/gml/examples/breastcancer.csv");

    // Load all variables from dataset, except for 'ID'
    X = loadd(fname, ". -ID");

    // Remove rows with a missing value
    X = packr(X);

    // Separate dependent and independent variables
    y = X[., "class"];
    X = delcols(X, "class");

    // Split data into 70% training and 30% test set
    { X_train, X_test, y_train, y_test } = trainTestSplit(X, y, 0.7);

    // Declare 'mdl' to be an 'ridgeModel' structure
    // to hold the trained model
    struct ridgeModel mdl;

    // Set lambda vector
    lambda = seqm(90, 0.4, 5);

    // Train the ridge classifier with default settings
    mdl = ridgeCFit(y_train, X_train, lambda);

    // Make predictions on the test set, from our trained model
    y_hat = ridgeCPredict(mdl, X_test);

    // Assess model quality
    print "";
    print "Classification metrics for lambda = "$+ntos(lambda[2]);
    call classificationMetrics(y_test, y_hat[.,2]);
   
    print "";
    print "Classification metrics for lambda = "$+ntos(lambda[4]);
    call classificationMetrics(y_test, y_hat[.,4]);

The code above will print the following output:

::

    ===========================================================================
    Model:                        Ridge     Target Variable:              class
    Number observations:            478     Number features:                  9
    ===========================================================================
    
    ======================================================================
                  Lambda   90.0000   36.0000   14.4000    5.7600    2.3040
    ======================================================================
    
             clump_thick    0.0026    0.0059    0.0124    0.0225    0.0344
             c_size_unif    0.0027    0.0061    0.0127    0.0219    0.0306
            c_shape_unif    0.0028    0.0063    0.0131    0.0228    0.0323
           marg_adhesion    0.0024    0.0055    0.0113    0.0192    0.0258
         single_epi_size    0.0032    0.0073    0.0149    0.0252    0.0337
             bare_nuclei    0.0023    0.0053    0.0112    0.0208    0.0332
         bland_chromatin    0.0031    0.0071    0.0147    0.0257    0.0369
        normal_nulcleoli    0.0024    0.0055    0.0113    0.0195    0.0275
                 mitosis    0.0023    0.0052    0.0102    0.0159    0.0175
                  CONST.   -0.3833   -0.4783   -0.6586   -0.9190   -1.1786
    ======================================================================
            Training MSE     0.818     0.714     0.542     0.349     0.221
    
    Classification metrics for lambda = 36
    ===================================================
                                 Classification metrics
    ===================================================
           Class   Precision  Recall  F1-score  Support
    
               0        0.65    1.00      0.79      131
               1        1.00    0.04      0.08       74
    
       Macro avg        0.82    0.52      0.43      205
    Weighted avg        0.78    0.65      0.53      205
    
        Accuracy                          0.65      205
    
    Classification metrics for lambda = 5.76
    ===================================================
                                 Classification metrics
    ===================================================
           Class   Precision  Recall  F1-score  Support
    
               0        0.92    0.98      0.95      131
               1        0.97    0.85      0.91       74
    
       Macro avg        0.95    0.92      0.93      205
    Weighted avg        0.94    0.94      0.94      205
    
        Accuracy                          0.94      205

.. seealso:: :func:`ridgecfit`, :func:`ridgeFit`
