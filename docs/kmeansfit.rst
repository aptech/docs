kmeansFit
====================

Purpose
----------------------
Partitions data into k clusters, using the kmeans algorithm.

Format
----------------------
.. function:: mdl = kmeansFit(X, clusters[, ctl])

    :param X: The training data.
    :type X: NxP matrix

    :param clusters: The number of clusters, or a matrix containing the initial centroids.
    :type clusters: Scalar

    :param ctl: Optional input, an instance of a :class:`kmeansControl` structure.

        .. csv-table::
            :widths: auto

                    "ctl.initMethod","Scalar specifying the algorithm used to create the initial centroids. Options include:

                                      * 0 -  kmeans++ (default).
                                      * 1 -  parallel k-means++
                                      * 2 -  k randomly selected observations."
                    "ctl.nStarts","Scalar, the number of times to run the kmeans algorithm with new starting centroids. Note: this input will be ignored if the *clusters* input is a starting centroid."
                    "ctl.seed","Seed for the random number generator which creates the initial centroids. Note: this input will be ignored if the *clusters* input is a starting centroid."
                    "ctl.tolerance","Scalar, the convergence tolerance for the kmeans algorithm."
                    "ctl.maxIters","Scalar, the maximum number of iterations to allow each of the *nStarts* to run before forcing convergence."

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
    
    
    // Get dataset with full name
    fname = getGAUSSHome() $+ "pkgs/gml/examples/iris.csv";
    
    // Load data
    X = loadd(fname, ". -species");
    
    // For repeatable sample
    rndseed 234234;
    
    // Split data into x_train and x_test
    { x_train, x_test } = splitData(X, 0.70);
    
    // Number of clusters
    n_clusters = 3;
    
    // Declare kmeansModel struct
    struct kmeansModel mdl;
    
    // Fit kmeans model
    mdl = kmeansFit(x_train , n_clusters);

    // Print the k centroids
    print mdl.centroids;
    

The above code will print the following:

::

    5.824 2.710 4.350 1.421
    5.009 3.406 1.475 0.250
    6.887 3.061 5.732 2.061


References
----------------

Parallel Kmeans++ initialization.
B. Bahmani, B. Moseley, A. Vattani, R. Kumar, S. Vassilvitskii. Scalable K-means++.
Proceedings of the VLDB Endowment, 2012.

.. seealso:: :func:`kmeansFit`, :func:`kmeansControlCreate`
