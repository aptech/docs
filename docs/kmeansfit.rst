kmeansFit
====================

Purpose
----------------------
Partitions data into k clusters, using the kmeans algorithm.

Format
----------------------
.. function:: mdl = kmeansFit(X, clusters[, ctl])

    :param X_train: The training features.
    :type X_train: NxP matrix

    :param clusters: The number of clusters, or a matrix containing the initial centroids.
    :type clusters: Scalar

    :param ctl: Optional input, an instance of a :class:`kmeansControl` structure.

        .. list-table::
            :widths: auto

            * - ctl.initMethod
              - Scalar specifying the algorithm used to create the initial centroids. Options include:

                === ===========================================
                0   kmeans++ (default).
                1   parallel k-means++
                2   :math:`k` randomly-selected observations.
                === ===========================================

            * - ctl.nStarts
              - Scalar, the number of times to run the kmeans algorithm with new starting centroids. Note: this input will be ignored if the *clusters* input is a starting centroid.
            * - ctl.seed
              - Seed for the random number generator which creates the initial centroids. Note: this input will be ignored if the *clusters* input is a starting centroid.
            * - ctl.tolerance
              - Scalar, the convergence tolerance for the kmeans algorithm.
            * - ctl.maxIters
              - Scalar, the maximum number of iterations to allow each of the *nStarts* to run before forcing convergence.

    :return mdl: An instance of a :class:`kmeansModel` structure.

        .. csv-table::
            :widths: auto

                    "mdl.centroids","kxP matrix, containing the centroids with the lowest intra-cluster sum of squares."
                    "mdl.assignments","Nx1 matrix, containing the centroid assignment for the corresponding observation of the input matrix."
                    "mdl.clusterSS","Scalar, sum of squared differences between each observation and its assigned centroid."
                    "mdl.elapsedIters","Scalar, the number of iterations taken by the *start* with the lowest *clusterSS*."

    :rtype mdl: struct

Examples
------------

::

    new;
    library gml;


    // For repeatable sample
    rndseed 234234;

    // Get dataset with full name
    fname = getGAUSSHome("pkgs/gml/examples/iris.csv");

    // Load data
    X = loadd(fname, ". -species");

    // Split data into x_train and x_test
    { x_train, x_test } = splitData(X, 0.70);

    // Number of clusters
    n_clusters = 3;

    // Declare kmeansModel struct
    struct kmeansModel mdl;

    // Fit kmeans model
    mdl = kmeansFit(x_train , n_clusters);

The above code will print the following:

::

  =================================================================
  Model:                      K-Means         Number clusters:    3
  Number observations:            105         Number features:    4
  Init method:              K-means++           Number starts:    3
  Tolerance:                   0.0001
  =================================================================

  K-means fit performance statistics:

  ============================================================
  Total sum of squares:                                477.576
  Between group sum of squares:                      419.05229
  Within group sum of squares:                        58.52371
  The ratio of BSS/TSS:                             0.87745676
  ============================================================
  Centroids:
  ====================================================================
    SepalLength       SepalWidth      PetalLength       PetalWidth

        5.82381          2.70952             4.35          1.42143
        5.00937          3.40625            1.475             0.25
         6.8871          3.06129          5.73226          2.06129
  ====================================================================


References
----------------

Parallel Kmeans++ initialization.
B. Bahmani, B. Moseley, A. Vattani, R. Kumar, S. Vassilvitskii. Scalable K-means++.
Proceedings of the VLDB Endowment, 2012.

.. seealso:: :func:`kmeansPredict`, :func:`kmeansControlCreate`
