meanSquaredError
====================

Purpose
--------------------
Returns the mean squared error between two input vectors, or sets of vectors.

Format
--------------------
.. function::  mse = meanSquaredError(y_true, y_pred)

    :param y_true: The true values.
    :type y_true:  Nx1 vector, or NxK matrix.

    :param y_pred: The predicted values.
    :type y_pred:  Nx1 vector, or NxK matrix

    :return mse:  The mean squared error between the column(s) in ``y_true`` and the column(s) in ``y_pred``.

Examples
------------

Basic example
+++++++++++++++

::

    y_true = { 7.3, 2.1, 5.9, 1.1, 3.3, 4.4 };
   
    y_pred = { 6.9, 1.5, 5.7, 1.3, 3.2, 4.7 };
         
    mse = meanSquaredError(y_true, y_pred);

After the above code:

::

    mse = 0.11666667

MSE for multiple Lasso predictions
+++++++++++++++++++++++++++++++++++++++

::

    new;
    library gml;
   
    /*
    ** Load data and prepare data
    */
    // Get file name with full path to
    // the location of this file
    fname = getGAUSSHome("pkgs/gml/examples/pcancer.csv");
   
    // Load dependent variables
    X = loadd(fname, ". -lpsa");
   
    // Load independent variable
    lpsa = loadd(fname, "lpsa");
   
    // Split into 80% test and train sets
    { lpsa_train, lpsa_test, X_train, X_test } = trainTestSplit(lpsa, X, 0.8);
   
    /*
    ** Train 3 models with 3 different lambda values
    */
   
    struct lassoControl ctl;
    ctl.lambdas  = { 0.9, 0.6, 0.3 };
   
    // Declare model structure to
    // store results
    struct lassoModel mdl;
    mdl = lassoFit(lpsa_train, X_train, ctl);
   
    lpsa_pred = lrPredict(mdl, X_test);
   
    test_mse = meanSquaredError(lpsa_test, lpsa_pred);
   
    print "lambda values: "; mdl.lambda;
    print "test_mse: "; test_mse;


::

    lambda values:

      0.90000000
      0.60000000
      0.30000000

    test_mse:

       1.2019214
      0.89992338
      0.70390474


.. seealso:: Functions  :func:`classMetrics`

