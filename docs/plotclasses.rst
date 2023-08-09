
plotClasses
==============================================

Purpose
----------------

Plots classes after classification.

Format
----------------
.. function:: plotClasses(data, label [, myplot]);

    :param data: First column is x-axis, the second is y-axis.
    :type data: Nx2 matrix

    :param label: The corresponding label for each row.
    :type label: Nx1 vector

    :param myplot: An instance of the :class:`plotControl` structure used for formatting the plot.
    :type myplot: Structure


Examples
----------------

::

  new;
  library gml;
  rndseed 234234;

  /*
  ** Load data and prepare data
  */
  fname = getGAUSSHome("pkgs/gml/examples/iris.csv");
  X = loadd(fname, ". - species");

  // Split data into X_train and X_test
  { X_train, X_test } = splitData(X, 0.70);

  /*
  ** Train model
  */
  // Number of clusters
  n_clusters = 3;

  // Declare kmeansModel struct to
  // hold the results from 'kmeansFit'
  struct kmeansModel mdl;

  // Fit kmeans model to training set
  mdl = kmeansFit(X_train , n_clusters);

 /*
 ** Test model
 */
 test_clusters = kmeansPredict(mdl, X_test);

 /*
 ** Plot Classes
 */
 plotClasses(X_test[., 1:2], test_clusters);

This results in the following plot:

 .. figure:: _static/images/plotscatter.png
     :scale: 50%


.. seealso:: Functions :func:`plotScatter`
