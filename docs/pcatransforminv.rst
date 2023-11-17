pcaTransformInv
====================

Purpose
----------------------
Transforms a matrix back to the original feature space of the *X* which was input to :func:`pcaFit`.

Format
----------------------
.. function:: X_original  = pcaTransformInv(X_transform, mdl)

    :param X_transform: The matrix to transform to the original feature space. This matrix must have the same number of columns as the number of principal
                        component vectors in *mdl*.
    :type X_transform: Nxn_components matrix
    :param mdl: This must have been previously been filled in by a call to :func:`pcaFit`.
    :type mdl:  `pcaModel` structure

    :return X_original:   The input matrix projected back to the original feature space of the matrix input to :func:`pcaFit`.
    :rtype X_original: NxP matrix

Examples
-------------

::

    new;
    library gml;

    // Get file name with full path
    fname = getGAUSSHome("pkgs/gml/examples/winequality.csv");

    // Load data
    X = loadd(fname, ". -quality");

    X_train = X[1:1000,.];
    X_test = X[1001:rows(X), .];

    n_components = 3;

    struct pcaModel mdl;
    mdl = pcaFit(X_train, n_components);

    // Apply dimensionality reduction to 'X_test'
    X_transform = pcaTransform(X_test, mdl);

After the above code, the first 5 rows of *X_transform* will be:

::

          PC1              PC2              PC3
    37.441282        1.2145282       -1.5416867
   -2.0454164       -15.738950        1.0084994
    21.315231       -2.4328631       0.15655108
    41.776957        2.2901582       -2.2804431
   0.73984770       -12.260074      -0.68265628


Now we can use :func:`pcaTransformInv` to transform *X_transform* back to the original space of *X*, *X_train* and *X_test*.

::

    // Transform 'X_transform' back to the original feature space
    X_original = pcaTransformInv(X_transform, mdl);


After the above code, the first 5 rows of *X_original* will be:

::

    7.601  0.548  0.184  2.055  0.088  6.025 11.990  0.996  3.385  0.628 10.346
    9.593  0.464  0.343  2.918  0.086 30.986 46.993  0.998  3.290  0.699 10.615
    9.071  0.505  0.305  2.526  0.089 13.022 26.985  0.997  3.297  0.667 10.418
    6.932  0.568  0.130  1.866  0.087  4.050  7.976  0.996  3.425  0.613 10.312
    8.000  0.515  0.221  2.514  0.086 26.987 44.997  0.997  3.379  0.664 10.474


.. seealso:: :func:`pcaFit`, :func:`pcaTransform`
