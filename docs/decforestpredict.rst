decForestPredict
====================

Purpose
----------------------
Predicts responses using the output from :func:`decForestCFit` or :func:`decForestRFit` and matrix of independent variables.

Format
-------------------

.. function:: predictions = decForestPredict(dfm, x_test)

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
    y = data[., "class"];
    X = delcols(data, "class");

    // Split data into 70% training and 30% test set
    { y_train, y_test, x_train, x_test } = trainTestSplit(y, x, 0.7);

    // Declare 'df_mdl' to be an 'dfModel' structure
    // to hold the trained model
    struct dfModel df_mdl;

    // Train the decision forest classifier with default settings
    df_mdl = decForestCFit(y_train, X_train);

    // Make predictions on the test set, from our trained model
    y_hat = decForestPredict(df_mdl, X_test);

    // Print diagnostic report
    call classificationMetrics(y_test, y_hat);


The code above will print the following output:

::

    ======================================================================
    Model:              Decision Forest         Target variable:     class
    Number Observations:            489         Number features:         9
    Number of trees:                100           Obs. per Tree:      100%
    Min. Obs. Per Node:               1     Impurity Threshhold:         0
    ======================================================================
   
   
    ======================================================================
    Prediction Model:     DF Classification     Target variable:     class
    Number Predictions:                 210     Number features:         9
    ======================================================================
   
    ===================================================
                                 Classification metrics
    ===================================================
           Class   Precision  Recall  F1-score  Support
   
               0        0.99    0.99      0.99      154
               1        0.98    0.96      0.97       56
   
       Macro avg        0.98    0.98      0.98      210
    Weighted avg        0.99    0.99      0.99      210

        Accuracy                          0.99      210


.. seealso:: :func:`decForestRFit`, :func:`decForestCFit`
