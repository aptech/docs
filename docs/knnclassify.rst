knnClassify
====================

Purpose
----------------------
Creates nearest neighbor predictions.

Format
----------------------
.. function:: y_hat = knnClassify(mdl, X)

    :param mdl: A :class:`knnModel` structure returned from a call to :func:`knnFit`.
    :type mdl: struct

    :param X_train: The training features.
    :type X: NxP matrix, or string array.

    :return y_hat: The predicted classes.
    :rtype y_hat:  Nx1 vector, or string array.

Examples
-------------

::

    new;
    library gml;

    // Set seed for repeatable train/test sampling
    rndseed 423432;

    // Get file name with full path
    fname = getGAUSSHome("pkgs/gml/examples/iris.csv");

    // Get predictors
    X = loadd(fname, ". -Species");

    // Load labels
    species = loadd(fname, "Species");

    // Split data into (70%) train and (30%) test sets
    { y_train, y_test, X_train, X_test } = trainTestSplit(species, X, 0.7);

    /*
    ** Train the model
    */
    // Specify number of neighbors
    k = 3;

    struct knnModel mdl;
    mdl = knnFit(y_train, X_train, k);

    /*
    ** Predictions on the test set
    */
    y_hat = knnClassify(mdl, X_test);


    /*
    ** Model assessment
    */
    call classificationMetrics(y_test, y_hat);


The above code will print the following output:

::

    ===========================================================================
    Model:                          KNN     Target Variable:            Species
    Number observations:            105     Number features:                  4
    Num. Neighbors:                   3     Number of Classes:                3
    ===========================================================================
   
    KNN Classification Prediction Frequencies:
    =============================================
   
         Label      Count   Total %    Cum. %
        setosa         14     31.11     31.11
    versicolor         19     42.22     73.33
     virginica         12     26.67       100
         Total         45       100          
   
    =============================================
   
    Observed Test Data Frequencies:
    =============================================
   
         Label      Count   Total %    Cum. %
        setosa         14     31.11     31.11
    versicolor         19     42.22     73.33
     virginica         12     26.67       100
         Total         45       100          
   
    =============================================
   
    ===================================================
                                 Classification metrics
    ===================================================
           Class   Precision  Recall  F1-score  Support
   
          setosa        1.00    1.00      1.00       14
      versicolor        0.95    0.95      0.95       19
       virginica        0.92    0.92      0.92       12
   
       Macro avg        0.95    0.95      0.95       45
    Weighted avg        0.96    0.96      0.96       45
   
        Accuracy                          0.96       45

.. seealso:: :func:`knnFit`, :func:`plotClasses`
