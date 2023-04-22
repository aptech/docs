classificationMetrics
==============================================

Purpose
-----------

Computes statistics to assess the quality of classification predictions and prints out a report.

Format
-----------
.. function:: out = classificationMetrics(y_true, y_predict)

    :param y_true: That represents the true class labels.
    :type y_true:  Nx1 vector, or dataframe.

    :param y_predict:  That represents the predicted class labels.
    :type y_predict: Nx1 vector, or dataframe.

    :return out:  An instance of a :class:`classQuality` structure. For an instance named *out*, the members are:

        .. csv-table::
            :widths: auto

            "out.confusionMatrix", ":math:`kxk` matrix, containing the computed confusion matrix."
            "out.precision", ":math:`kx1` dataframe, where each row contains precision for corresponding class :math:`\frac{tp}{tp + fp}`."
            "out.recall", ":math:`kx1` dataframe, where each row contains recall for the corresponding class, :math:`\frac{tp}{tp + fn}`"
            "out.fScore", ":math:`kx1` dataframe, where each row contains the F1-score for the corresponding class, :math:`\frac{(b^2 + 1) * tp}{(b^2 + 1) * tp + b^2 * fn + fp)}` (b = 1) ."
            "out.support", ":math:`kx1` dataframe, where each row contains the number of observations for the corresponding class."
            "out.macroPrecision", "Scalar, the unweighted average of the precision for each class."
            "out.macroRecall", "Scalar, the unweighted average of the recall for each class."
            "out.macroFScore", "Scalar, the unweighted average of the F1-score for each class."
            "out.macroSupport", "Scalar, the total number of observations."
            "out.accuracy", "Scalar, range 0-1, the accuracy of the predicted labels for all classes."
            "out.classLabels", ":math:`kx1` string array, containing the labels for each class."
            "out.classes", ":math:`kx1` dataframe, containing the numeric keys and label names if given for each class."

    :rtype out: struct


Example
-----------

Example 1: Basic use with binary labels

Example
-----------

Example 1: Basic use with binary labels
++++++++++++++++++++++++++++++++++++++++

::

    new;
    library gml;

    y_true = { 0, 0, 1, 0, 1, 1, 1, 0 };
    y_pred = { 0, 0, 1, 0, 1, 0, 1, 0 };

    call classificationMetrics(y_true, y_pred);

After the above code, the following report will be printed:

::

    ===================================================
                                 Classification metrics
    ===================================================
           Class   Precision  Recall  F1-score  Support
    
               0        0.80    1.00      0.89        4
               1        1.00    0.75      0.86        4
    
       Macro avg        0.90    0.88      0.87        8
    Weighted avg        0.90    0.88      0.87        8
    
        Accuracy                          0.88        8


Example 2: Dataframe inputs
++++++++++++++++++++++++++++++++++++++++++++++

::

      new;
      library gml;

      // Strings
      string true_label = { "cat", "cat", "zebra", "zebra", "dog", "dog", "dog", "cat", "cat" };
      string pred_label = { "cat", "cat", "zebra", "cat", "zebra", "cat", "dog", "cat", "dog" };

      // Create dataframes
      df_true = asDF(true_label, "Observed");
      df_pred = asDF(pred_label, "Prediction");

      call classificationMetrics(df_true, df_pred);

After the above code, the following report will be printed:

::

    ===================================================
                                 Classification metrics
    ===================================================
           Class   Precision  Recall  F1-score  Support
    
             cat        0.60    0.75      0.67        4 
             dog        0.50    0.33      0.40        3 
           zebra        0.50    0.50      0.50        2 
    
       Macro avg        0.53    0.53      0.52        9 
    Weighted avg        0.54    0.56      0.54        9 
    
        Accuracy                          0.56        9

Example 3: KNN classification model assessment
++++++++++++++++++++++++++++++++++++++++++++++++++

::

    new;
    library gml;
    rndseed 790837;
    
    /*
    ** Load data and prepare data
    */
    // Get file name with full path
    fname = getGAUSSHome("pkgs/gml/examples/iris.csv");
    
    // Get predictors
    X = loadd(fname, ". -Species");
    
    // Load labels
    species = loadd(fname, "Species");
    
    // Split data into (70%) train and (30%) test sets
    { y_train, y_test, x_train, x_test } = trainTestSplit(species, x, 0.7);
    
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
    
    // Declare 'q' to be a classQuality structure
    // to hold the statistics
    struct classQuality q;

    // Print diagnostic report
    q = classificationMetrics(y_test, y_hat); 

After the code above and the knn training printouts,  we see the following report:

::

    ===================================================
                                 Classification metrics
    ===================================================
           Class   Precision  Recall  F1-score  Support
    
          setosa        1.00    1.00      1.00       13 
      versicolor        0.94    1.00      0.97       15 
       virginica        1.00    0.94      0.97       17 
    
       Macro avg        0.98    0.98      0.98       45 
    Weighted avg        0.98    0.98      0.98       45 
    
        Accuracy                          0.98       45


We can access any of the structure members from the ``classQuality`` structure using the dot operator:

::

    print "Macro precision for each class =";
    print q.macroPrecision;

::

    Macro precision for each class =
          0.97916667


::

    print (q.classes ~ q.precision);

::

           Class        Precision 
          setosa        1.0000000 
      versicolor       0.93750000 
       virginica        1.0000000

