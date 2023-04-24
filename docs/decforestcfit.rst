decForestCFit
======================

Purpose
--------------------
Fit a decision forest classification model.

Format
--------------------
.. function::  dfm = decForestCFit(y_train, x_train[, dfc])

    :param y_train: The target, or dependent variable.
    :type y_train: Nx1 vector

    :param X_train: The model features, or independent variables.
    :type X_train: NxP matrix

    :param dfc: Optional input, an instance of the :class:`dfControl` structure. For an instance named, *dfc* the members are:

        .. csv-table::
            :widths: auto

            "dfc.numTrees", "Scalar, number of trees (must be integer). Default = 100."
            "dfc.pctObsPerTree", "Scalar, the percentage of observations selected for each tree (sampling with replacement). Valid range: 0.0 < ``pctObsPerTree`` <= 1.0. Default = 1.0."
            "dfc.featuresPerSplit", "Scalar integer value, number of features considered as a possible split at each node. Default = sqrt(nvars)."
            "dfc.maxTreeDepth", "Scalar integer value, maximum tree depth. Default = 0 = unlimited."
            "dfc.maxLeafNodes", "Scalar integer value, maximum number of leaves in each tree. Setting this to a positive integer value will cause the tree to be built by making the best possible splits first, instead of growing the trees in a depth first fashion.  Default = 0 = unlimited."
            "dfc.minObsLeaf", "Scalar integer value, minimum observations per leaf node.  Default = 1."
            "dfc.impurityThreshold", "Scalar, if the impurity value at a particular node is below this value, it will no longer be split. Default = 0.0."
            "dfc.oobError", "Scalar, 1 to compute OOB error, 0 otherwise. Default = 0."
            "dfc.variableImportanceMethod", "Scalar, method of calculating variable importance.

                                           * 0 = none,
                                           * 1 = mean decrease in impurity (Gini importance)
                                           * 2 = mean decrease in accuracy (MDA),
                                           * 3 = scaled MDA.

                                           Default = 0."

    :type dfc: struct

    :return dfm: An instance of the dfModel structure. An instance named *dfm* will have the following members:

        .. csv-table::
            :widths: auto

                 "dfm.variableImportance","Matrix, 1 x p, variable importance measure if computation of variable importance is specified, zero otherwise."
                 "dfm.oobError","Scalar, out-of-bag error if OOB error computation is specified, zero otherwise."
                 "dfm.numClasses","Scalar, number of classes if classification model, zero otherwise."

    :rtype dfm: struct

Examples
-----------------

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
    { y_train, y_test, x_train, x_test } = trainTestSplit(y, X, 0.7);

    // Declare 'df_mdl' to be an 'dfModel' structure
    // to hold the trained model
    struct dfModel df_mdl;

    // Train the decision forest classifier with default settings
    df_mdl = decForestCFit(y_train, X_train);

    // Make predictions on the test set, from our trained model
    y_hat = decForestPredict(df_mdl, X_test);

    // Print classification quality report
    call classificationMetrics(y_hat, y_test);

The code above will print the following output:

::

    ======================================================================
    Model:              Decision Forest         Target variable:     class
    Number Observations:            489         Number features:         9
    Number of trees:                100           Obs. per Tree:      100%
    Min. Obs. Per Node:               1     Impurity Threshhold:         0
    ======================================================================
   
   
    ========================================================================
    Prediction Model:      DF Classification     Target variable:     class
    Number Predictions:                  210     Number features:         9
    ========================================================================
   
    ===================================================
                                 Classification metrics
    ===================================================
           Class   Precision  Recall  F1-score  Support
   
               0        0.99    0.99      0.99      155
               1        0.96    0.98      0.97       55
   
       Macro avg        0.98    0.98      0.98      210
    Weighted avg        0.99    0.99      0.99      210
   
        Accuracy                          0.99      210


Remarks
--------------------
The :class:`dfModel` structure contains a fourth, internally used member, `opaqueModel`, which contains model details used by :func:`decForestPredict`.

.. seealso:: Functions  :func:`decForestPredict`, :func:`decForestRFit`
