knnFit
====================

Purpose
----------------------
Creates a K-D tree model from training data for efficient KNN predictions.

Format
----------------------
.. function:: mdl = knnFit(y, X, k)

    :param y:   The dependent, or target, variable.
    :type y:   Nx1 vector or string array

    :param X: The independent, or features, variables.
    :type X: NxP matrix

    :param k: The number of neighbors.
    :type k:  Scalar

    :return mdl:   An instance of a  :class:`knnModel` structure. For an instance named *mdl*, the members will be:

        .. csv-table::
            :widths: auto

            "mdl.opaqueModel", "Column vector, containing the K-D tree in opaque form."
            "mdl.classIndices", "*Px1* matrix, where *P* is the number of classes in the target vector *y*."
            "mdl.classNames",  "*Px1* string array, where *P* is the number of classes in the target vector *y*, containing the class names if the target vector was a string array."
            "mdl.k", "Scalar, the number of neighbors to search."

    :rtype mdl: struct

    Examples
    -------------

    ::

        new;
        library gml;

        // Set seed for repeatable train/test sampling
        rndseed 423432;

        /*
        ** Load data and prepare
        */
        // Get file name with full path
        fname = getGAUSSHome("pkgs/gml/examples/iris.csv");

        // Get predictors
        X = loadd(fname, ". -Species");

        // Load labels
        species = loadd(fname, "Species");

        // Split data into (70%) train and (30%) test sets
        { y_train, y_test, X_train, X_test } = trainTestSplit(species, X, 0.7);

        /*
        ** Train the model
        */
        // Specify number of neighbors
        k = 3;

        struct knnModel mdl;
        mdl = knnFit(y_train, X_train, k);

        /*
        ** Predictions on the test set
        */
        y_hat = knnClassify(mdl, X_test, y_test);


    The above code will print the following output:

    ::

      ===========================================================================
      Model:                          KNN     Target Variable:            Species
      Number observations:            105     Number features:                  4
      Num. Neighbors:                   3     Number of Classes:                3
      ===========================================================================

      KNN Classification Prediction Frequencies:
      =============================================
           Label      Count   Total %    Cum. %
          setosa         14     31.11     31.11
      versicolor         19     42.22     73.33
       virginica         12     26.67       100
          Total         45       100
      =============================================

      Observed Test Data Frequencies:
      =============================================
           Label      Count   Total %    Cum. %
          setosa         14     31.11     31.11
      versicolor         19     42.22     73.33
       virginica         12     26.67       100
           Total         45       100
      =============================================

      Prediction accuracy:      0.95555556

.. seealso:: :func:`knnClassify`, func:`plotClasses`
