
aggregate
==============================================

Purpose
----------------
Aggregates the data in the columns of a matrix based upon a column containing group ids with a choice of method.


Format
----------------
.. function:: x_agg = aggregate(x, method [, column , fast])

    :param x: data, if *column* is not specified, the first column must contain the ids for the groups on which to aggregate.
    :type x: NxK matrix or dataframe

    :param method: Specifies which aggregation method to use.

        **Valid options:**

        .. list-table::
            :widths: auto

            * - "mean"
            * - "median"
            * - "mode"
            * - "min"
            * - "max"
            * - "sd" (sample standard deviation)
            * - "sum"
            * - "variance" (sample variance)

    :type method: string

    :param column: Optional, specifies which variable contains the groups on which to aggregate.
    :type column: string

    :param fast: Optional, specifies fast computation that does not check for missing values. Set to 1 to use fast method.
    :type fast: scalar

    :return x_agg: the input aggregated by the group id, using the specified method.
    :rtype x_agg: NGROUPSxK matrix

Examples
----------------

Example 1
+++++++++++++

This example aggregates a matrix with one group id column and one column of data by mean and then by minimum.

::

    // Create a matrix where the first
    // column is the group id
    X = { 1002  7,
          1001  2,
          1004  9,
          1001  8,
          1004  6,
          1003  3,
          1002  5,
          1001  4 };

    agg_mean = aggregate(X, "mean");

    agg_min = aggregate(X, "min");

The above code will make the following assignments:

::

               1001   4.66667
    agg_mean = 1002         6
               1003         3
               1004       7.5

               1001         2
    agg_min  = 1002         5
               1003         3
               1004         6


Example 2
++++++++++++

This example aggregates the data from a matrix with one group id column and two data columns first by sample standard deviation and then by variance.

::

    // Create a matrix where the first
    // column is the group id
    X = { 1002   18  -5.1,
          1001   22   0.0,
          1001   47   3.3,
          1001   94   5.6,
          1001   17  -0.5,
          1001   72   7.5,
          1002   89   4.8,
          1001   67   2.3,
          1002   54   6.6,
          1002   61  -6.8,
          1002    7   1.3,
          1002   40   -2.1 };

    // aggregate by standard deviation
    agg_sd = aggregate(X, "sd");

    agg_var = aggregate(X, "variance");


The above code will make the following assignments:

::

    agg_sd  = 1001    30.10     3.13
              1002    29.90     5.38

    agg_var = 1001   906.17     9.77
              1002   894.17    28.93

Example 3
++++++++++++

This example specifies the column name to be used for aggregation.

::

  // Load data
  auto2 = loadd(getGAUSSHome $+ "examples/auto2.dta");

  // Aggregate data using
  // foreign column as group
  aggregate(auto2[., "price" "mpg" "foreign"], "mean", "foreign");

::

The above code will make the following table

::

  foreign     price      mpg
  Domestic  6072.423   19.827
  Foreign   6384.682   24.773



.. seealso:: Functions :func:`meanc`, :func:`modec`, :func:`selif`
