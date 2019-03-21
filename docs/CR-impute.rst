
impute
==============================================

Purpose
----------------
Replaces missing values in the columns of a matrix by a specified imputation method.
		

Format
----------------
.. function:: impute(X, method)

    :param X: 
    :type X: NxK matrix

    :param method: specifying which imputation method to use.
        Valid options:"mean"String, replace missing values with the mean of the column (default)."median"String, replace missing values with the median of the column.
        "mean"
        String, replace missing values with the mean of the column (default).
        "median"
        String, replace missing values with the median of the column.
    :type method: Optional string

    :param "mean": replace missing values with the mean of the column (default).
    :type "mean": String

    :param "median": replace missing values with the median of the column.
    :type "median": String

    :returns: X_full (*Matrix*), the input matrix with the missing values from each column filled in by the specified imputation method.

Examples
----------------

// Create 3x3 matrix with a missing value
X = { 1    2    3,
      4    .    5,
      7    8    9,
     10   11    . };

// Replace missing values with column mean
X_default = impute(X);

// Replace missing values with column median
X_median = impute(X, "median");

// Replace missing values with column mean
X_mean = impute(X, "mean");
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The above code will make the following assignments:

::

    1    2    3
    X_default =    4    7    5
                   7    8    9
                  10   11    5.67
    
                   1    2    3
    X_median  =    4    8    5
                   7    8    9
                  10   11    5
    
                   1    2    3
    X_mean    =    4    7    5
                   7    8    9
                  10   11    5.67

Remarks
-------

-  If all elements of a column passed to impute are missing values,
   every element of the corresponding column returned will contain
   missing values.
-  To replace the missing values in each column with a constant value,
   use missrv. It will allow you to specify one constant for the entire
   matrix, or a separate constant for each column.
-  Use the miss function to replace specific values (for example 999)
   with GAUSS missing values.
-  The packr function will remove all rows which contain one or more
   missing values (listwise deletion).

.. seealso:: Functions :func:`missrv`, :func:`miss`, :func:`reclassify`, :func:`packr`
