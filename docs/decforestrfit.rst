decForestRFit
======================

Purpose
--------------------
Fit a decision forest regression model.

Format
--------------------
.. function::  dfm = decForestRFit(y_train, x_train[, dfc])

    :param y_train: The dependent variable.
    :type y_train: Nx1 vector

    :param x_train: The independent variables.
    :type x_train: NxP matrix.

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
     
    /*
    ** Load and transform data
    */
     
    // Load hitters dataset
    dataset = getGAUSSHome $+ "pkgs/gml/examples/hitters.xlsx";
     
    // Load salary and perform natural log transform
    y = loadd(dataset, "ln(salary)");
     
    // Load all variables except 'salary'
    X = loadd(dataset, ". - salary");
     
    /*
    ** Split into test and training sets
    */
     
    // Set seed for repeatable sampling
    rndseed 234234;
     
    // Split data into training and test sets
    { y_train, y_test, X_train, X_test } = trainTestSplit(y, X, 0.7);
     
    /*
    ** Estimate decision forest model
    */
     
    // Declare 'dfc' to be a dfControl structure
    // and fill with default settings.
    struct dfControl dfc;
    dfc = dfControlCreate();
     
    // Turn on variable importance
    dfc.variableImportanceMethod = 1;
     
    // Turn on OOB error
    dfc.oobError = 1;
     
    // Structure to hold model results
    struct dfModel mdl;
     
    // Fit training data using decision forest
    mdl = decForestRFit(y_train, X_train, dfc);
     
    // OOB Error
    print "Out-of-bag error:" mdl.oobError;
    
The code above will print the following output:

::

    random forest test MSE:      0.23044959


Remarks
--------------------
The :class:`dfModel` structure contains a fourth, internally used member, `opaqueModel`, which contains model details used by :func:`decForestPredict`.

.. seealso:: Functions  :func:`decForestPredict`, :func:`decForestCFit`

