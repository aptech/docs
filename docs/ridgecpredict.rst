ridgeCPredict
====================

Purpose
----------------------
Predicts responses using the output from :func:`ridgeCFit` and matrix of independent variables.

Format
-------------------

.. function:: predictions = ridgeCPredict(mdl, x_test, [, y_test])

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

    :param y_test: Optional, the test target, or dependent variable. If included model diagnostics will be computed.
    :type y_test: Nx1 vector

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
    lambda = seqm(90, 0.8, 60);

    // Train the ridge classifier with default settings
    mdl = ridgeCFit(y_train, X_train, lambda);

    // Make predictions on the test set, from our trained model
    y_hat = ridgeCPredict(mdl, X_test, y_test);


The code above will print the following output:

::

                 Confusion matrix
                 ----------------

      Class +         40      34
      Class -         62      69

       Accuracy           0.5317
      Precision           0.5405
         Recall           0.3922
        F-score           0.4545
    Specificity           0.6699
            AUC            0.531


.. seealso:: :func:`ridgeCFit`, :func:`ridgeFit`
