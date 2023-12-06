logisticRegFit
===================

Purpose
----------------
Fit a logistic regression model with an optional L1 and/or L2 penalty.

Format
------------
.. function:: mdl = logisticRegFit(y, X [, ctl])

    :param y: The target, or dependent variable.
    :type y: Nx1 vector

    :param X: The model features, or independent variables.
    :type X: NxP matrix

    :param lambda: Optional L1 penalties. The model will be estimated for each lambda value. If not provided and *ctl.lambdas* is an empty matrix, {}, :func:`lassoFit` will create a vector of decreasing values. Default = {}.
    :type lambda: Scalar, or Kx1 vector

    :param ctl: Optional input, an instance of a :class:`logisticRegControl` structure. An instance named *ctl* will have the following members:

        .. csv-table::
            :widths: auto

                "ctl.l1","Scalar, the L1 regulariazation penalty. Default = 0."
                "ctl.l2","Scalar, the L2 regulariazation penalty. Default = 0."
                "ctl.intercept","Scalar, indicator to include constant. Set to 1 to include constant, 0 otherwise. Default = 1."
                "ctl.tolerance","Scalar, the tolerance for convergence of the coordinant descent optimization for each lambda value. Default = 1e-4."
                "ctl.batch_size","Scalar, size of batch to include in model. Default = 0 (all observations)."
                "ctl.max_iters","The maximum number of iterations for the coordinate descent optimization for each provided *lambda*. Default = 1000."
                "ctl.solver_type","Solver to use for otpimization. Default = lbfgs."

    :type ctl: struct

    :return mdl: An instance of a :class:`logisticRegModel` structure. An instance named *mdl* will have the following members:

        .. csv-table::
            :widths: auto

                "mdl.alpha_hat","(*1 x nlambdas vector*) The estimated value for the intercept for each provided *lambda*."
                "mdl.beta_hat","(*P x nlambdas matrix*) The estimated parameter values for each provided *lambda*."
                "mdl.l1","Scalar, the L1 regulariazation penalty."
                "mdl.l2","Scalar, the L2 regulariazation penalty."
                "mdl.nobs","Scalar, the number of observations."
                "mdl.nvars","Scalar, the number of variables."

    :rtype mdl: struct

Examples
-----------

Example 1: Basic Logistic Regression
+++++++++++++++++++++++++++++++++++++++++++++

::

    new;
    library gml;
    rndseed 23423;

    /*
    ** Load data and prepare data
    */

    // Load wine quality dataset
    dataset = loadd(getGAUSSHome("pkgs/gml/examples/winequality.csv"));

    // Separate target variable from predictive features
    X = delcols(dataset, "quality");
    y = dataset[.,"quality"];

    // Split data into (80%) training and (20%) test sets
    { y_train, y_test, X_train, X_test } = trainTestSplit(y, X, 0.8);

    // Scale training features
    { X_train, mu, sd } = rescale(X_train, "standardize");

    /*
    ** Train model
    */
    // The logisticRegModel structure holds the trained model
    struct logisticRegModel lrm;

    // Fit training data, using default options
    lrm = logisticRegFit(y_train, X_train);

Continuing with our example, we can make test predictions like this:

::

  /*
  ** Test model
  */

  // Apply training scale parameters to test data
  X_test = rescale(X_test, mu, sd);

  // Make predictions using test data
  predictions = lmPredict(lrm, X_test);

  call classificationMetrics(y_test, predictions);

This prints the following evaluation metrics:

::

   ===================================================
                                Classification metrics
   ===================================================
          Class   Precision  Recall  F1-score  Support

              3        0.00    0.00      0.00        2
              4        0.00    0.00      0.00       12
              5        0.67    0.77      0.72      137
              6        0.56    0.63      0.60      131
              7        0.47    0.22      0.30       36
              8        0.00    0.00      0.00        2

      Macro avg        0.28    0.27      0.27      320
   Weighted avg        0.57    0.61      0.59      320

       Accuracy                          0.61      320

Example 2: Basic Logistic Regression with Regulariazation
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

      new;
      library gml;

      /*
      ** Load data and prepare data
      */
      // Load all variables from dataset, except for 'ID'
      fname = getGAUSSHome("pkgs/gml/examples/breastcancer.csv");
      data = loadd(fname, ". -ID");

      // Remove any rows with missing values
      data = packr(data);

      // Extract target variable and set class names
      // for more informative reporting
      y = data[., "class"];
      y = setcollabels(y, "Positive"$|"Negative", 1|0);

      // Remove target variable to create feature dataframe
      X = delcols(data, "class");

      // Split data into 70% training and 30% test set
      { y_train, y_test, X_train, X_test } = trainTestSplit(y, X, 0.7);

      /*
      ** Train model
      */
      // Declare 'lr_mdl' to be an 'logisticRegModel' structure
      // to hold the trained model
      struct logisticRegModel lr_mdl;

      // Declare 'lrc' to be a logisticRegControl
      // structure and fill with default settings
      struct logisticRegControl lrc;
      lrc = logisticRegControlCreate();

      // Set regularization parameters
      lrc.l1 = 0.3;
      lrc.l2 = 0.9;

      // Train the logistic regression classifier
      lr_mdl = logisticRegFit(y_train, X_train, lrc);

Continuing with our example, we can make test predictions like this:

::

  /*
  ** Test model
  */
  // Make predictions on the test set, from our trained model
  y_hat = lmPredict(lr_mdl, X_test);

  call classificationMetrics(y_test, y_hat);

This prints the following evaluation metrics:

::

  ===================================================
                               Classification metrics
  ===================================================
         Class   Precision  Recall  F1-score  Support

      Negative        0.98    0.97      0.97      131
      Positive        0.95    0.96      0.95       74

     Macro avg        0.96    0.96      0.96      205
  Weighted avg        0.97    0.97      0.97      205

      Accuracy                          0.97      205



.. seealso:: :func:`ridgeFit`, :func:`lassoFit`, :func:`lmPredict`
