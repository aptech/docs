pcaTransform
====================

Purpose
----------------------
Reduces the dimension of a matrix using principal component vectors previously returned by :func:`pcaFit`.

Format
----------------------
.. function:: X_transform  = pcaTransform(X, mdl)

    :param X: The matrix to transform. This matrix must have the same number of columns as the matrix passed to :func:`pcaFit`.
    :type X: NxP matrix
    :param mdl: This must have been previously been filled in by a call to :func:`pcaFit`.
    :type mdl:  `pcaModel` structure

    :return X_transform:   The input matrix projected on the component vectors returned by a previous call to :func:`pcaFit`.
    :rtype X_transform: Nxn_components matrix

Examples
-------------

::

    new;
    library gml;
    
    // Get file name with full path
    fname = getGAUSSHome() $+ "pkgs/gml/examples/winequality.csv";
   
    // Load data
    X = loadd(fname, ". -quality");

    X_train = X[1:1000,.];
    X_test = X[1001:rows(X),.];
   
    n_components = 3;
   
    struct pcaModel mdl;
    mdl = pcaFit(X_train, n_components);

    X_transform = pcaTransform(X_test, mdl);

After the above code, the first 5 rows of *X_transform* will be:

::

       37.441282        1.2145282       -1.5416867 
      -2.0454164       -15.738950        1.0084994 
       21.315231       -2.4328631       0.15655108 
       41.776957        2.2901582       -2.2804431 
      0.73984770       -12.260074      -0.68265628


.. seealso:: :func:`pcaFit`, :func:`pcaTransformInv`
