knnClassify
====================

Purpose
----------------------
Creates nearest neighbor predictions.

Format
----------------------
.. function:: y_hat = knnClassify(mdl, X)

    :param mdl: A :class:`knnModel` structure returned from a call to :func:`knnFit`.
    :type mdl: struct
    :param X: The training data.
    :type X: NxP matrix, or string array.

    :return y_hat:    The predicted classes.
    :rtype y_hat:     Nx1 vector, or string array. 

Examples
-------------

::

    new;
    library gml;
    
    // Get file name with full path
    fname = getGAUSSHome() $+ "pkgs/gml/examples/iris.csv";
    
    // Load numeric predictors
    X = loadd(fname, ". -Species");
    
    // Load string labels
    species = loaddSA(fname, "Species");
    
    // Set seed for repeatable train/test sampling
    rndseed 423432;
    
    // Split data into (70%) train and (30%) test sets
    { y_train, y_test, X_train, X_test } = trainTestSplit(species, X, 0.7);
    
    /*
    ** Train the model
    */
    
    k = 3;
    
    struct knnModel mdl;
    mdl = knnFit(y_train, X_train, k);
    
    /*
    ** Predictions on the test set
    */
    
    y_hat = knnClassify(mdl, X_test);
    
    print "First three predictions = " y_hat[1:3];
    print "";
    print "prediction accuracy = " meanc(y_hat .$== y_test);

The above code will print the following output:

::

    First three predictions = 
                    virginica 
                   versicolor 
                       setosa

    prediction accuracy = 0.956

.. seealso:: :func:`knnFit`
