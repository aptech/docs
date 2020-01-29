cvSplit
=========

Purpose
--------------------
Returns the test and training set for the *ith* of *k* cross validation splits for a given set of dependent and independent variables.

Format
--------------------
.. function::  { y_train, y_test, X_train, X_test } = cvSplit(y, X, k, i)

    :param y: The dependent variable(s).
    :type y:  Nx1 vector, or NxK matrix.

    :param X: The independent variable(s).
    :type X:  Nx1 vector, or NxK matrix

    :param k:  The number of folds.
    :type k:  Scalar

    :param i:  The fold number.
    :type i:  Scalar


    :return y_train:  The training target values for the *ith* CV split.

    :return y_test:  The test target values for the *ith* CV split

    :return X_train: The training predictor values for the *ith* CV split.
    :return X_test:  The test predictor values for the *ith* CV split.

Examples
------------

::

    y = { 7, 2, 5, 1, 3, 4 };
    
    X = { 1   3,
          9   6,
          6   1,
          8   4,
          9   5,
          1   8 };
          
    // Divide the dataset into 3 folds. Place the first
    // 1/3 of the observations in the test set and the remaining
    // observations in the training set.
    { y_train, y_test, X_train, X_test } = cvSplit(y, X, 3, 1);

After the above code:

::

   y_train = 5   X_train = 6    1 
             1             8    4 
             3             9    5 
             4             1    8 

  y_test  =  7  X_test  =  1    3 
             2             9    6 


Continuing with the same *y* and *X* from above, if we run:

::

    // Divide the dataset into 3 folds. Place the second
    // 1/3 of the observations in the test set and the remaining
    // observations in the training set.
    { y_train, y_test, X_train, X_test } = cvSplit(y, X, 3, 2);

This time, the variables are assigned as follows:
   
::

   y_train = 7   X_train = 1    3 
             2             9    6 
             3             9    5 
             4             1    8 

  y_test  =  5  X_test  =  6    1 
             1             8    4 


Remarks
--------------------
The observations from *X* and *y* are NOT randomly shuffled.

.. seealso:: Functions  :func:`rndi`, :func:`sampleData`, :func:`trainTestSplit`

