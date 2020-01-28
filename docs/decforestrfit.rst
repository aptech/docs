decForestRFit
======================

Purpose
--------------------
Fit a decision forest regression model.

Format
--------------------
.. function::  dfm = decForestRFit(y_train, x_train)
               dfm = decForestRFit(y_train, x_train, dfc)

    :param y_train: The dependent variable.
    :type y_train: Nx1 vector

    :param x_train:  The independent variables.
    :type x_train:  NxP matrix.

    :param dfc:  Optional input, an instance of the :class:`dfControl` structure. For an instance named, *dfc* the members are:

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

    :return dfm:       An instance of the dfModel structure. An instance named *dfm* will have the following members:

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
    struct dfModel df_mdl;
    
    // Train the decision forest classifier with default settings
    df_mdl = decForestCFit(y_train, X_train);
    
    // Make predictions on the test set, from our trained model
    y_hat = decForestPredict(df_mdl, X_test);
    
    // Print out model quality evaluation statistics
    call binaryClassMetrics(y_test, y_hat);

The code above will print the following output:

::

              Confusion matrix
              -------------------

              54                1 
               2              153 

        Accuracy         0.985714 
       Precision         0.964286 
          Recall         0.981818 
         F-score         0.972973 
     Specificity         0.987097 
             AUC         0.984457 



Remarks
--------------------
The :class:`dfModel` structure contains a fourth, internally used member, `opaqueModel`, which contains model details used by :func:`decForestPredict`.

.. seealso:: Functions  :func:`decForestPredict`, :func:`decForestCFit`

