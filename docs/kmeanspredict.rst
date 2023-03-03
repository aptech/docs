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

    // Assign test data to clusters
    test_clusters = kmeansPredict(mdl, x_test);


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

  K-Means Prediction Clusters Frequencies:
  =============================================
  Label      Count   Total %    Cum. %
      1         19     42.22     42.22
      2         18        40     82.22
      3          8     17.78       100
  Total         45       100
  =============================================

.. seealso:: :func:`kmeansFit`, :func:`kmeansControlCreate`, :func:`plotClasses`
