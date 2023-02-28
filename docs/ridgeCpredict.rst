decForestPredict
====================

Purpose
----------------------
Predicts responses using the output from :func:`decForestCFit` or :func:`decForestRFit` and matrix of independent variables.

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
    fname = getGAUSSHome() $+ "pkgs/gml/examples/breastcancer.csv";

    // Load all variables from dataset, except for 'ID'
    X = loadd(fname, ". -ID");

    // Separate dependent and independent variables
    y = X[.,cols(X)];
    X = delcols(X, cols(X));

    // Split data into 70% training and 30% test set
    { X_train, X_test, y_train, y_test } = trainTestSplit(X, y, 0.7);

    // Declare 'df_mdl' to be an 'dfModel' structure
    // to hold the trained model
    struct ridgeModel mdl;

    // Set lambda vector
    lambda = seqm(90, 0.8, 60);

    // Train the decision forest classifier with default settings
    mdl = ridgeCFit(y_train, X_train, lambda);

    // Make predictions on the test set, from our trained model
    y_hat = ridgeCPredict(mdl, y_test, x_test);


The code above will print the following output:

::

                 Confusion matrix
                 ----------------

         Class +       54       2
         Class -        1     153

        Accuracy           0.9857
       Precision           0.9643
          Recall           0.9818
         F-score            0.973
     Specificity           0.9871
             AUC           0.9845


.. seealso:: :func:`decForestRFit`, :func:`decForestCFit`
