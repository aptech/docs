binaryClassMetrics
==============================================

Purpose 
-----------

Computes statistics to assess the quality of binary predictions and prints out a report.

Format 
-----------
.. function:: out = binaryClassMetrics(y_true, y_predict)

    :param y_true:  Nx1 vector of 0's and 1's, with the true class labels.
    :param y_predict:  Nx1 vector of 0's and 1's, with the predicted class labels.
        

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

::

    y_true = { 0, 0, 1, 0, 1, 1, 1, 0 };
    y_pred = { 0, 0, 1, 0, 1, 0, 1, 0 };

    call binaryClassMetrics(y_true, y_pred);

After the above code, the following report will be printed:

::

                 Confusion matrix
              -------------------

               3                0 
               1                4 

        Accuracy            0.875 
       Precision             0.75 
          Recall                1 
         F-score         0.857143 
     Specificity              0.8 
             AUC              0.9

