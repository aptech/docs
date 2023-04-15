classificationReport
==============================================

Purpose
-----------

Computes statistics to assess the quality of classification predictions and prints out a report.

Format
-----------
.. function:: classificationReport(y_true, y_predict)

    :param y_true: That represents the true class labels.
    :type y_true:  Nx1 vector, or dataframe.

    :param y_predict:  That represents the predicted class labels.
    :type y_predict: Nx1 vector, or dataframe.


Example
-----------

Example 1: Basic use with binary labels
++++++++++++++++++++++++++++++++++++++++

::

    new;
    library gml;

    y_true = { 0, 0, 1, 0, 1, 1, 1, 0 };
    y_pred = { 0, 0, 1, 0, 1, 0, 1, 0 };

    call classificationReport(y_true, y_pred);

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

      call classificationReport(df_true, df_pred);

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
    
    // Print diagnostic report
    classificationReport(y_test, y_hat); 

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

