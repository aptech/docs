ridgeCFit
======================

Purpose
--------------------
Fit a binary classification model using with an L2 penalty.

Format
--------------------
.. function::  mdl = ridgeCFit(y_train, X_train, lambda)

    :param y_train: The dependent variable.
    :type y_train: Nx1 vector

    :param x_train: The independent variables.
    :type x_train: NxP matrix.

    :param lambda: The L2 penalty parameter(s).
    :type lambda: Scalar, or Kx1 vector

    :return mdl: An instance of a :class:`ridgeModel` structure. An instance named *mdl* will have the following members:

        .. csv-table::
            :widths: auto

            "mdl.alpha_hat","(*1 x nlambdas vector*) The estimated value for the intercept for each provided *lambda*."
            "mdl.beta_hat","(*P x nlambdas matrix*) The estimated parameter values for each provided *lambda*."
            "mdl.mse_train","(*nlambdas x 1 vector*) The mean squared error for each set of parameters, computed on the training set."
            "mdl.lambda","(*nlambdas x 1 vector*) The *lambda* values used in the estimation."

    :rtype mdl: struct

Examples
-----------------

::

    new;
    library gml;

    rndseed 23423;

    // Create file name with full path
    fname = getGAUSSHome() $+ "pkgs/gml/examples/breastcancer.csv";

    // Load all variables from dataset, except for 'ID'
    X = packr(loadd(fname, ". -ID"));

    // Separate dependent and independent variables
    y = X[., "class"];
    X = delcols(X, "class");

    // Split data into 70% training and 30% test set
    { X_train, X_test, y_train, y_test } = trainTestSplit(X, y, 0.7);

    // Declare 'mdl' to be an 'ridgeModel' structure
    // to hold the trained model
    struct ridgeModel mdl;

    // Set lambda vector
    lambda = { 90, 36, 14 };

    // Train the decision forest classifier with default settings
    mdl = ridgeCFit(y_train, X_train, lambda);

    // Make predictions on the test set, from our trained model
    y_hat = ridgeCPredict(mdl, X_test);
   
    print "";
    fmt = "Classification report for lambda = %.2f";
    sprintf(fmt, lambda[1]);
    call classificationMetrics(y_test, y_hat[.,1]);
   
    print "";
    sprintf(fmt, lambda[3]);
    call classificationMetrics(y_test, y_hat[.,3]);

The code above will print the following output:

::

    Classification report for lambda = 90.00
    ===================================================
                                 Classification metrics
    ===================================================
           Class   Precision  Recall  F1-score  Support
    
               0        0.64    1.00      0.78      131
               1        0.00    0.00      0.00       74
    
       Macro avg        0.32    0.50      0.39      205
    Weighted avg        0.41    0.64      0.50      205
    
        Accuracy                          0.64      205
    
    Classification report for lambda = 14.00
    ===================================================
                                 Classification metrics
    ===================================================
           Class   Precision  Recall  F1-score  Support
    
               0        0.82    1.00      0.90      131
               1        1.00    0.61      0.76       74
    
       Macro avg        0.91    0.80      0.83      205
    Weighted avg        0.88    0.86      0.85      205
    
        Accuracy                          0.86      205

.. seealso:: Functions  :func:`ridgeCPredict`, :func:`ridgeFit`
