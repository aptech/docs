pcaFit
====================

Purpose
----------------------
Performs principal component dimension reduction.

Format
----------------------
.. function:: mdl = pcaFit(X, n_components)

    :param X: Independent variables.
    :type X: NxP matrix
    :param n_components: The number of principal component vectors to return. :math:`1 \le n\_components \le P`
    :type n_components:  Scalar

    :return mdl:   An instance of a  :class:`pcaModel` structure. For an instance named *mdl*, the members will be:

        .. csv-table::
            :widths: auto

            "mdl.singular_values", "*n_components x 1* vector, containing the largest singular values of *X*."
            "mdl.components", "*P x n_components* matrix, containing the principal component vectors which represent the directions of greatest variance."
            "mdl.explained_variance_ratio",  "*n_components x 1* vector, the percentage of variance explained by each of the returned component vectors."
            "mdl.explained_variance",  "*n_components x 1* vector, the variance explained by each of the returned component vectors."
            "mdl.mean", "*1 x P* vector, the means for each column of the input matrix *X*."
            "mdl.n_components", "Scalar, the number of component vectors returned."
            "mdl.n_samples", "Scalar, the number of rows of the input matrix *X*."

    :rtype mdl: struct

Examples
-------------

::

    new;
    library gml;
    
    // Get file name with full path
    fname = getGAUSSHome() $+ "pkgs/gml/examples/winequality.csv";
    
    // Load data
    X = loadd(fname, ". -quality");
    
    n_components = 3;
    
    struct pcaModel mdl;
    mdl = pcaFit(X, n_components);

    print mdl.explained_variance_ratio;
    
The above code will print the following output, which shows us that the first principal component
accounts for nearly 95% of the variance.

::

    0.9466 
    0.0484 
    0.0026

We can now transform the input data to the new 3-dimensional space with :func:`pcaTransform`:

::

    X_transform = pcaTransform(X, mdl);

After the above code, the first 5 rows of *X_transform* will be:

::

     13.2249  -2.0239   1.1268 
    -22.0377   4.4083   0.3104 
     -7.1627  -2.5015   0.5819 
    -13.4301  -1.9511  -2.6340 
     13.2249  -2.0239   1.1268


.. seealso:: :func:`pcaTransform`
