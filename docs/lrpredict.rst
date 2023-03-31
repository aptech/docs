lrPredict
====================

Purpose
----------------------
Predict outcomes and computes MSE for test data from a linear Regression model.

Format
----------------------
.. function:: { predictions, mse_test } = lrPredict(mdl, X_test [, y_test])


    :param mdl: Instance of a :class:`lassoModel` or :class:`ridgeModel` structure.
    :type mdl: struct

    :param x_test: The test model features, or independent variables.
    :type x_test: NxP matrix

    :param y_test: Optional, the test target, or dependent variable. If included model diagnostics will be computed.
    :type y_test: Nx1 vector

    :return predictions: Contains one set of predictions for each lambda used for fitting the model.
    :rtype predictions: NxK matrix

    :return mse_test: The mse on the test set for each lambda used for fitting the model.
    :rtype mse_test: Kx1 vector


Examples
----------

::

    new;
    library gml;

    // Specify dataset with full path
    dataset = getGAUSSHome("pkgs/gml/examples/qsar_fish_toxicity.csv");

    // Split data into training sets without shuffling
    shuffle = "False";
    { y_train, y_test, x_train, x_test } = trainTestSplit(dataset, "LC50 ~ . ", 0.7, shuffle);

    // Declare 'mdl' to be an instance of a
    // lassoModel structure to hold the estimation results
    struct lassoModel mdl;

    // Provide lambda
    lambdas = {0, 0.01, 0.05, 0.15, 0.3};

    // Estimate the model with default settings
    mdl = lassoFit(y_train, X_train, lambdas);

    /*
    ** Prediction for test data
    */
    { y_hat, test_mse } = lrPredict(mdl, x_test, y_test);

The above code will print the following:

::

    ===========================================================================
    Model:                        Lasso     Target Variable:               LC50
    Number observations:            636     Number features:                  6
    ===========================================================================
    
    ======================================================================
                  Lamdba      0.00      0.01      0.05      0.15      0.30
    ======================================================================
    
                    CIC0    0.2609    0.2354    0.1331    0.0000    0.0000
                  SM1_DZ    1.2362    1.2020    1.0650    0.7872    0.4546
                  GATS1i   -0.6843   -0.6442   -0.4838   -0.1878    0.0000
                   NdsCH    0.4999    0.4822    0.4116    0.2328    0.0000
                   NdssC    0.0654    0.0616    0.0463    0.0000    0.0000
                   MLOGP    0.4032    0.4091    0.4323    0.4450    0.3820
                  CONST.    2.4544    2.4914    2.6394    2.8472    2.9904
    ======================================================================
                      DF         5         5         5         3         1
         # Non-zero Vars         6         6         6         4         2
            Training MSE     0.933     0.933     0.946     1.033     1.225
    ======================================================================
             Testing MSE     0.839     0.844     0.880     1.012     1.230


.. seealso:: :func:`lassoFit`, :func:`ridgeFit`, :func:`plotLR`
