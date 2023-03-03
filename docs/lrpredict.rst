lrPredict
====================

Purpose
----------------------
Predict outcomes and computes MSE for test data from a linear Regression model.

Format
----------------------
.. function:: { predictions, mse_test } = kmeansPredict(mdl, X_test [, y_test])


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
    lambda = {0, 0.25, 5, 0.75, 1};

    // Estimate the model with default settings
    mdl = lassoFit(y_train, X_train);

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
              Lamdba      0.00      0.25      5.00      0.75      1.00
 ======================================================================

                CIC0    0.2609    0.0000    0.0000    0.0000    0.0000
              SM1_DZ    1.2362    0.5584    0.0000    0.0000    0.0000
              GATS1i   -0.6843   -0.0249    0.0000    0.0000    0.0000
               NdsCH    0.4999    0.0355    0.0000    0.0000    0.0000
               NdssC    0.0654    0.0000    0.0000    0.0000    0.0000
               MLOGP    0.4032    0.4080    0.0000    0.0940    0.0000
              CONST.    2.4544    2.8962    4.0735    3.8775    4.0735
 ======================================================================
                  DF         5         3         0         0         0
     # Non-zero Vars         6         4         0         1         0
        Training MSE     0.933     1.164     2.051     1.831     2.051
 ======================================================================
         Testing MSE     0.839     1.156     2.270     1.994     2.270

.. seealso:: :func:`lassoFit`, :func:`ridgeFit`, :func:`plotLR`
