binaryClassMetrics
==============================================

Purpose 
-----------

Computes statistics to assess the quality of binary predictions and prints out a report.

Format 
-----------
.. function:: out = binaryClassMetrics(y_true, y_predict)

    :param y_true:  Nx1 vector of 0's and 1's, or strings that represent the true class labels.
    :param y_predict:  Nx1 vector of 0's and 1's, or strings that represent the predicted class labels.
        

    :return out:  An instance of a :class:`binaryClassQuality` structure. For an instance named *out*, the members are:

        .. csv-table::
            :widths: auto

            "out.confusionMatrix", "2x2 matrix, containing the computed confusion matrix."
            "out.accuracy", "Scalar, range 0-1, the accuracy of the predicted labels."
            "out.precision", "Scalar, (tp / (tp + fp))."
            "out.recall", "Scalar, (tp / (tp + fn))."
            "out.fScore", "Scalar, ((b^2 + 1) * tp) / ((b^2 + 1) * tp + b^2 * fn + fp) (b = 1) ."
            "out.specificity", "Scalar, (tp / (fp + tn))."
            "out.auc", "Scalar, 0.5 * ((tp / (tp + fn) + (tp / (fp + tn)).  Note: This is NOT the area under the roc curve, which requires requires predicted probabilities for its computation, rather than predicted class labels."

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

                 Confusion matrix
                 ----------------

         Class +        3       1 
         Class -        0       4 

        Accuracy            0.875 
       Precision             0.75 
          Recall                1 
         F-score           0.8571 
     Specificity              0.8 
             AUC              0.9

The interpretation of the confusion matrix is shown below:

::

                  Confusion matrix
                  ------------------------

         Class +  (True  Pos)  (False Neg) 
         Class -  (False Pos)  (True  Neg)


If you want to store the statistics computed by :func:`binaryClassMetrics`, you can assign them to a :class:`binaryClassQuality` structure like this:


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
   
   



Example 2: String class labels
++++++++++++++++++++++++++++++++++++++++++++++

::

    new;
    library gml;

    string true_label = { "cat", "cat", "dog", "cat", "dog", "dog", "dog", "cat" };
    string pred_label = { "cat", "cat", "dog", "cat", "dog", "cat", "dog", "cat" };

    call binaryClassMetrics(true_label, pred_label);

After the above code, the following report will be printed:

::

                 Confusion matrix
                 ----------------

             cat        4       0 
             dog        1       3 

        Accuracy            0.875 
       Precision                1 
          Recall              0.8 
         F-score           0.8889 
     Specificity                1 
             AUC              0.9

