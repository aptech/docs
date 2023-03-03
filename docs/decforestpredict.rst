decForestPredict
====================

Purpose
----------------------
Predicts responses using the output from :func:`decForestCFit` or :func:`decForestRFit` and matrix of independent variables.

Format
-------------------

.. function:: predictions = decForestPredict(dfm, x_test [, y_test])

    :param dfm: An instance of the :class:`dfModel` structure filled by :func:`decForestRFit` or :func:`decForestCFit` and containing the following relevant members:

        .. csv-table::
            :widths: auto

                 "dfm.variableImportance","Matrix, 1 x p, variable importance measure if computation of variable importance is specified, zero otherwise."
                 "dfm.oobError","Scalar, out-of-bag error if OOB error computation is specified, zero otherwise."
                 "dfm.numClasses","Scalar, number of classes if classification model, zero otherwise."
                 "dfm.opaqueModel","Matrix, contains model details for internal use only."
    :type dfm: struct

    :param x_test: The test model features, or independent variables.
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
    data = loadd(fname, ". -ID");

    // Separate dependent and independent variables
    y = data[., cols(X)];
    X = delcols(X, cols(X));

    // Split data into 70% training and 30% test set
    { y_train, y_test, x_train, x_test } = trainTestSplit(y, x, 0.7);

    // Declare 'df_mdl' to be an 'dfModel' structure
    // to hold the trained model
    struct dfModel df_mdl;

    // Train the decision forest classifier with default settings
    df_mdl = decForestCFit(y_train, X_train);

    // Make predictions on the test set, from our trained model
    y_hat = decForestPredict(df_mdl, X_test, y_test);


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
