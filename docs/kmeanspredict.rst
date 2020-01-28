kmeansPredict
====================

Purpose
----------------------
Partitions data into *k* clusters, based upon *k* user supplied centroids.

Format
----------------------
.. function:: assignments = kmeansPredict(mdl, X)
              assignments = kmeansPredict(centroids, X)

          
    :param mdl: Instance of a :class:`kmeansModel` structure.
    :type mdl: struct

    :param centroids: Cluster centers.
    :type centroids: kxP matrix

    :param X: The data to partition.
    :type X: NxP matrix

    :return assignments: The cluster to which each corresponding index of *X* has been assigned. range = 1-k.
    :rtype assignments: Nx1 matrix


Examples
----------

Example 1: Basic example with a matrix of centroids.
++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    library gml;
    
    centroids = { 2  3,
                 -2 -3 };
                
    X = { 1  1,
          0 -2,
          2  0 };
    
    // Assign each row of 'X' to either cluster 1 or cluster 2
    assignments = kmeansPredict(centroids, X);
    
The above code will assign *assignments* equal to:

::

    1
    2
    1

because, the points (1,1) and (2,0) are closer (euclidean distance) to the first centroid at point (2,3), while the second row of *X* (0,-2) is closer to the second centroid (-2,-3).

    
Example 2: Use centroids from a kmeansModel structure
++++++++++++++++++++++++++++++++++++++++++++++++++++++

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
    
    // Assign test data to clusters
    test_clusters = kmeansPredict(mdl, x_test);
    
    print "The first three cluster assignments are: " test_clusters[1:3];

The above code will print the following:

::

    The first three cluster assignments are: 
      2
      2
      1

.. seealso:: :func:`kmeansFit`, :func:`kmeansControlCreate`
