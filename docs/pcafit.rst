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

    /*
    ** Load data and prepare
    */
    // Get file name with full path
    fname = getGAUSSHome("pkgs/gml/examples/winequality.csv");

    // Load data
    X = loadd(fname, ". -quality");

    /*
    ** Train the model
    */
    // Number of components
    n_components = 3;

    struct pcaModel mdl;
    mdl = pcaFit(X, n_components);


The above code will print the following output, which shows us that the first principal component
accounts for nearly 95% of the variance.

::

  ==================================================
  Model:                                         PCA
  Number observations:                          1599
  Number variables:                               11
  Number components:                               3
  ==================================================

  Component                Proportion     Cumulative
                          Of Variance     Proportion
  PC1                           0.947          0.947
  PC2                           0.048          0.995
  PC3                           0.003          0.998

  ==================================================
  Principal components       PC1       PC2       PC3
  ==================================================
  fixed acidity           0.0061   -0.0239   -0.9531
  volatile acidity       -0.0004   -0.0020    0.0251
  citric acid            -0.0002   -0.0030   -0.0737
  residual sugar         -0.0086    0.0111   -0.2809
  chlorides              -0.0001   -0.0002   -0.0029
  free sulfur dioxide    -0.2189    0.9753   -0.0209
  total sulfur dioxide   -0.9757   -0.2189    0.0015
  density                -0.0000   -0.0000   -0.0008
  pH                      0.0003    0.0033    0.0586
  sulphates              -0.0002    0.0006   -0.0175
  alcohol                 0.0064    0.0146    0.0486

We can now transform the input data to the new 3-dimensional space with :func:`pcaTransform`:

::

  X_transform = pcaTransform(X, mdl);

After the above code, the first 5 rows of *X_transform* will be:

::

            PC1              PC2              PC3 
      13.224905       -2.0238998        1.1268205
     -22.037724        4.4083216       0.31037799
     -7.1626733       -2.5014609       0.58186830
     -13.430063       -1.9511222       -2.6340395
      13.224905       -2.0238998        1.1268205


.. seealso:: :func:`pcaTransform`
