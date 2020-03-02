splitData
===================

Purpose
--------------------
Returns test and training splits for a single matrix of variables.

Format
--------------------
.. function::  { X_train, X_test } = splitData(X, train_pct)

    :param X:  The matrix to split.
    :type X: Nx1 vector, or NxP matrix.

    :param train_pct:  The percentage of observations to include in the training set.
    :type train_pct: Scalar


    :return X_train: (*train_pct* \* *N*) x *P* matrix of independent variables.
    :return X_test:  The remaining observations from the original *X* which were not selected to be in the training set.

Examples
------------

::

    library gml;

    // Set seed for repeatable sampling
    rndseed 23324;
    
    X = { 1   3,
          9   6,
          6   1,
          8   4,
          9   5,
          1   8 };
          
    // Shuffle data and create training set with 2/3 of
    // the observations and 1/3 for the test set
    { X_train, X_test } = splitData(X, 0.67);

After the above code:

::

   X_train = 9    5 
             1    3 
             8    4 
             1    8 

   X_test =  9    6 
             6    1 



Remarks
--------------------

The observations (rows) of  *X* are kept together. For repeatable shuffling, use the `rndseed` keyword before calling :func:`splitData`.

.. seealso:: Functions  :func:`cvSplit`, :func:`rndi`, :func:`sampleData`, :func:`trainTestSplit`

