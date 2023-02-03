trainTestSplit
===================

Purpose
--------------------
Returns test and training splits for a given set of dependent and independent variables.

Format
--------------------
.. function::  { y_train, y_test, X_train, X_test } = trainTestSplit(y, X, train_pct [, shuffle])

    :param y:   The dependent variables.
    :type y:   Nx1 vector, or NxK matrix.

    :param X:  The independent variables.
    :type X: Nx1 vector, or NxP matrix.

    :param train_pct:  The percentage of observations to include in the training set.
    :type train_pct: Scalar

    :param shuffle:  Optional input, "True" (default) or "False". 
    :type shuffle: String


    :return y_train:  The (*train_pct* \* *N*) observations from the original *y* which correspond to the observations selected for *X_train*.
    :rtype y_train:

    :return y_test:  The remaining observations from the original *y* not selected for the training set.
    :return X_train: (*train_pct* \* *N*) x *P* matrix of independent variables.
    :return X_test:  The remaining observations from the original *X* which were not selected to be in the training set.

Examples
------------

Basic example
===================

::

    library gml;

    // Set seed for repeatable sampling
    rndseed 23324;
    
    y = { 7, 2, 5, 1, 3, 4 };
    
    X = { 1   3,
          9   6,
          6   1,
          8   4,
          9   5,
          1   8 };
          
    // Shuffle data and create training set with 2/3 of
    // the observations and 1/3 for the test set
    { y_train, y_test, X_train, X_test } = trainTestSplit(y, X, 0.67);

After the above code:

::

   y_train = 3   X_train = 9    5 
             7             1    3 
             1             8    4 
             4             1    8 

   y_test =  2   X_test =  9    6 
             5             6    1 


Example without shuffling
==========================

Sometimes, for example with time series data, you may not want to shuffle before creating your train and test splits.

::


    y = { 7, 2, 5, 1, 3, 4 };
    
    X = { 1   3,
          9   6,
          6   1,
          8   4,
          9   5,
          1   8 };
          
    // Create training set in the original order with 2/3 of
    // the observations and 1/3 for the test set
    { y_train, y_test, X_train, X_test } = trainTestSplit(y, X, 0.67, "False");

This time, the split data will be in the same order as the original data.

::

    
   y_train = 7   X_train = 1    3 
             2             9    6 
             5             6    1 
             1             8    4 

   y_test =  3   X_test =  9    5 
             4             1    8 




Remarks
--------------------

If ``shuffle`` is enabled, the observations from *X* and *y* are first randomly shuffled such that the corresponding rows of *X* and *y* are kept together. For repeatable shuffling, use the `rndseed` keyword before calling :func:`trainTestSplit`.

.. seealso:: Functions  :func:`cvSplit`, :func:`rndi`, :func:`sampleData`, :func:`splitData`

