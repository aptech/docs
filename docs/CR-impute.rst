
impute
==============================================

Purpose
----------------
Replaces missing values in the columns of a matrix by a specified imputation method.


Format
----------------
.. function:: X_full = impute(x[, method])

    :param x: data
    :type x: NxK matrix

    :param method: Optional input. Specifies which imputation method to use.

        **Valid options:**

        .. list-table::
            :widths: auto

            * - "mean"
              - Replace missing values with the mean of the column (default).
            * - "median"
              - Replace missing values with the median of the column.

    :type method: string

    :returns: **x_full** (*matrix*) - the input matrix with the missing values from each column filled in by the specified imputation method.

Examples
----------------

::

    // Create 3x3 matrix with a missing value
    x = { 1    2    3,
          4    .    5,
          7    8    9,
         10   11    . };

    // Replace missing values with column mean
    x_default = impute(x);

    // Replace missing values with column median
    x_median = impute(x, "median");

    // Replace missing values with column mean
    x_mean = impute(x, "mean");

The above code will make the following assignments:

::

                   1    2    3
    x_default =    4    7    5
                   7    8    9
                  10   11    5.67

                   1    2    3
    x_median  =    4    8    5
                   7    8    9
                  10   11    5

                   1    2    3
    x_mean    =    4    7    5
                   7    8    9
                  10   11    5.67

Remarks
-------

-  If all elements of a column passed to :func:`impute` are missing values,
   every element of the corresponding column returned will contain
   missing values.
-  To replace the missing values in each column with a constant value,
   use :func:`missrv`. It will allow you to specify one constant for the entire
   matrix, or a separate constant for each column.
-  Use the :func:`miss` function to replace specific values (for example 999)
   with GAUSS missing values.
-  The :func:`packr` function will remove all rows which contain one or more
   missing values (listwise deletion).

.. seealso:: Functions :func:`missrv`, :func:`miss`, :func:`reclassify`, :func:`packr`
