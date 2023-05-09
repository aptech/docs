binaryClassMetrics
==============================================

Purpose
-----------

Computes statistics to assess the quality of binary predictions and prints out a report.

Format
-----------
.. function:: out = binaryClassMetrics(y_true, y_predict)
              out = binaryClassMetrics(df_true, df_predict, classes)

    :param y_true: That represents the true class labels.
    :type y_true:  Nx1 binary vector.

    :param y_predict:  That represents the predicted class labels.
    :type y_true: Nx1 binary vector.

    :param df_true: That represents the true class labels.
    :type df_true:  Nx1 dataframe, or string array.

    :param y_predict:  That represents the predicted class labels.
    :type y_true: Nx1 dataframe, or string array.

    :param classes:  The first element of ``classes`` indicates which class should be treated as the positive case. This input is required if the ``true`` and ``predict`` inputs are string arrays or categorical dataframes.
    :type classes: String, 1x1 or 2x1 categorical dataframe, or string array.

    :return out:  An instance of a :class:`binaryClassQuality` structure. For an instance named *out*, the members are:

        .. csv-table::
            :widths: auto

            "out.confusionMatrix", "2x2 matrix, containing the computed confusion matrix."
            "out.accuracy", "Scalar, range 0-1, the accuracy of the predicted labels."
            "out.precision", "Scalar, :math:`\frac{tp}{tp + fp}`."
            "out.recall", "Scalar, :math:`\frac{tp}{tp + fn}`"
            "out.fScore", "Scalar, :math:`\frac{(b^2 + 1) * tp}{(b^2 + 1) * tp + b^2 * fn + fp)}` (b = 1) ."
            "out.specificity", "Scalar, :math:`\frac{tp}{fp + tn}`)."
            "out.balancedAccuracy", "Scalar, :math:`0.5 * (\frac{tp}{tp + fn} + \frac{tn}{tn + fp}`)."

    :rtype out: struct


Example
-----------

Example 1: Basic use with binary labels
++++++++++++++++++++++++++++++++++++++++

::

    new;
    library gml;

    y_true = { 0, 0, 1, 0, 1, 1, 1, 0 };
    y_pred = { 0, 0, 1, 0, 1, 0, 1, 0 };

    call binaryClassMetrics(y_true, y_pred);

After the above code, the following report will be printed:

::

    ==================================
                      Confusion matrix
    ==================================
                       Predicted class
                       ---------------
                             +       -
           True class
           ----------
                1 (+)        3       1
                0 (-)        0       4
   
             Accuracy            0.875
            Precision                1
               Recall             0.75
              F-score           0.8571
          Specificity                1
    Balanced Accuracy            0.875

The interpretation of the confusion matrix is shown below:

::

    ========================================
                            Confusion matrix
    ========================================
                             Predicted class
                      ----------------------
                         +            -
       True class
       ----------
        Class (+)    (True Pos)  (False Neg)
        Class (-)   (False Pos)   (True Neg)


You can store the statistics computed by :func:`binaryClassMetrics`, using a :class:`binaryClassQuality` structure like this:


::

   /*
   ** Continuing with y_true and y_pred created above
   */

   // Declare bqs to be a binaryClassQuality structure
   struct binaryClassQuality bqs;

   // Compute metrics and assign to struct
   bqs = binaryClassMetrics(y_true, y_pred);

   // Print some members
   print "Accuracy = " bqs.accuracy;
   print "F-score  = " bqs.fscore;


which will print the following output in addition to the standard report:

::

    Accuracy =       0.87500000
    F-score  =       0.85714287


Example 2: Dataframe inputs
++++++++++++++++++++++++++++++++++++++++++++++

::

      new;
      library gml;

      // Strings
      string true_label = { "cat", "cat", "dog", "cat", "dog", "dog", "dog", "cat" };
      string pred_label = { "cat", "cat", "dog", "cat", "dog", "cat", "dog", "cat" };

      // Create dataframes
      df_true = asDF(true_label, "Observed");
      df_pred = asDF(pred_label, "Prediction");

      call binaryClassMetrics(df_true, df_pred, "cat");

After the above code, the following report will be printed:

::

    ==================================
                      Confusion matrix
    ==================================
                       Predicted class
                       ---------------
                             +       -
           True class
           ----------
              cat (+)        4       0
              dog (-)        1       3
  
             Accuracy            0.875
            Precision              0.8
               Recall                1
              F-score           0.8889
          Specificity             0.75
    Balanced Accuracy            0.875


Example 3: String class labels
++++++++++++++++++++++++++++++++++++++++++++++

::

    new;
    library gml;

    string true_label = { "cat", "cat", "dog", "cat", "dog", "dog", "dog", "cat" };
    string pred_label = { "cat", "cat", "dog", "cat", "dog", "cat", "dog", "cat" };

    call binaryClassMetrics(true_label, pred_label, "dog");

After the above code, the following report will be printed:

::

    ==================================
                      Confusion matrix
    ==================================
                       Predicted class
                       ---------------
                             +       -
           True class
           ----------
              dog (+)        3       1
              cat (-)        0       4
  
             Accuracy            0.875
            Precision                1
               Recall             0.75
              F-score           0.8571
          Specificity                1
    Balanced Accuracy            0.875


