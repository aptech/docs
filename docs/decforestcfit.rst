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

            "dfc.numTrees", "Scalar, number of trees (must be integer). Default = 100"
            "dfc.obsPerTree", "Scalar, observations per a tree. Default = 1.0."
            "dfc.featurePerNode", "Scalar, number of features considered at a node. Default = nvars/3."
            "dfc.maxTreeDepth", "Scalar, maximum tree depth. Default = unlimited."
            "dfc.minObsNode", "Scalar, minimum observations per node.  Default = 1."
            "dfc.impurityThreshold", "Scalar, impurity threshold. Default = 0."
            "dfc.oobError", "Scalar, 1 to compute OOB error, 0 otherwise. Default = 0."
            "dfc.variableImpurityMethod", "Scalar, method of calculating variable importance.

                                           * 0 = none,
                                           * 1 = mean decrease in impurity
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
    y = data[., cols(data)];
    X = delcols(data, cols(data));

    // Split data into 70% training and 30% test set
    { y_train, y_test, x_train, x_test } = trainTestSplit(y, X, 0.7);

    // Declare 'df_mdl' to be an 'dfModel' structure
    // to hold the trained model
    struct dfModel df_mdl;

    // Train the decision forest classifier with default settings
    df_mdl = decForestCFit(y_train, X_train);

    // Make predictions on the test set, from our trained model
    // Note that the y_test is optional
    y_hat = decForestPredict(df_mdl, X_test, y_test);

The code above will print the following output:

::

  ======================================================================
  Model:              Decision Forest         Target variable:     class
  Number Observations:            489         Number features:         9
  Number of trees:                100           Obs. per Tree:       100%
  Min. Obs. Per Node:               1     Impurity Threshhold:         0
  ======================================================================

  ========================================================================
  Prediction Model:      DF Classification     Target variable:     class
  Number Predictions:                  210     Number features:         9
  ========================================================================

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

Remarks
--------------------
The :class:`dfModel` structure contains a fourth, internally used member, `opaqueModel`, which contains model details used by :func:`decForestPredict`.

.. seealso:: Functions  :func:`decForestPredict`, :func:`decForestRFit`
