Data Transformations
=============================

Normalizing and scaling data
------------------------------
The :func:`rescale` function provides 8 different scaling options and returns the rescaled data along with the location and scale factors.

+--------------------+----------------------------+----------------------------------------------+
| Method             | Location                   | Scale Factor                                 |
+====================+============================+==============================================+
| ``“euclidean”``    | 0                          |  Euclidean length                            |
+--------------------+----------------------------+----------------------------------------------+
| ``"mad"``          | median                     |  Absolute deviation from median              |
+--------------------+----------------------------+----------------------------------------------+
| ``“maxabs"``       | 0                          |  Maximum absolute value                      |
+--------------------+----------------------------+----------------------------------------------+
| ``“midrange”``     | (Max+Min)/2                | Range/2                                      |
+--------------------+----------------------------+----------------------------------------------+
| ``“range”``        | Minimum                    |  Range                                       |
+--------------------+----------------------------+----------------------------------------------+
| ``“standardize”``  | Mean                       |  Standard deviation                          |
+--------------------+----------------------------+----------------------------------------------+
| ``“sum”``          | 0                          |  Sum                                         |
+--------------------+----------------------------+----------------------------------------------+
| ``“ustd”``         | 0                          |  Standard deviation around origin            |
+--------------------+----------------------------+----------------------------------------------+

Rescaling with a specified scaling method
+++++++++++++++++++++++++++++++++++++++++++

::

  // Create a column vector
  x = {   12.5,
    18.2,
    10.8,
    8.3,
    15.4,
    21.5,
    14.6,
    16.7 };

  // Standardize 'x' and return the location and scaling factors
  { x_s, location_s, scale_factor_s } = rescale(x, "standardize");

  // Rescale the `x` using the median
  { x_m, location_m, scale_factor_m } = rescale(x, "mad");

  print "Standardized rescaling:";
  print "x_s = " x_s;
  print "location_s = " location_s;
  print "scale_factor_s = " scale_factor_s;

  print "Median rescaling:";
  print "x_m = " x_m;
  print "location_m = " location_m;
  print "scale_factor_m = " scale_factor_m;

After the code above:

::

  Standardized rescaling:
  x_s =
     -0.53463295
      0.81977052
     -0.93857785
      -1.5326145
      0.15444952
       1.6038989
    -0.035642197
      0.46334856

  location_s =           14.75
  scale_factor_s =        4.21

  Median rescaling:
  x_m =
     -0.87719298
       1.1228070
      -1.4736842
      -2.3508772
      0.14035088
       2.2807018
     -0.14035088
      0.59649123

  location_m =           15.00
  scale_factor_m =        2.85

The :func:`rescale` function can also be used with a known location and scale factor to rescale data.

Rescaling using known location and scaling factors
++++++++++++++++++++++++++++++++++++++++++++++++++++

::

  // Additional observations
  x2    = { 9.3,
         10.9,
         11.1,
          9.1,
         14.6,
         18.4,
         20.2,
         18.5 };

  // Rescale matrix above using
  // location and scale matrix
  // from above
  x_s2 = rescale(x2, location_s, scale_factor_s);

After the code above *x_s2* is equal to:

::

      -1.2949998
     -0.91481638
     -0.86729345
      -1.3425227
    -0.035642197
      0.86729345
       1.2949998
      0.89105492

The :func:`rescale` function can also be used to rescale multiple columns at time.

Rescaling multiple columns
++++++++++++++++++++++++++++

::

  // Create a matrix with 2 columns
  x = {   12.5 1088.5,
          18.2  879.3,
          10.8 1232.0,
           8.3 1189.8,
          15.4  932.1,
          21.5 1009.2,
          14.6  656.7,
          16.7 1251.5 };

  // Standardize 'x' and return the location and scaling factors
  { x_s, location, scale_factor } = rescale(x, "standardize");

  print "x_s = " x_s;
  print "location = " location;
  print "scale_factor = " scale_factor;

::

  x_s =
     -0.53463295       0.28751716
      0.81977052      -0.73869039
     -0.93857785       0.99144060
      -1.5326145       0.78443315
      0.15444952      -0.47968581
       1.6038989      -0.10148025
    -0.035642197       -1.8306302
      0.46334856        1.0870957

  location =            14.750000        1029.8875
  scale_factor =        4.2084948        203.85740

Recoding and reclassifying
--------------------------------

GAUSS provides a variety of tools for recoding and reclassifying data. These functions can be divided into functions for numeric data and functions for categorical data.

+------------------------+----------------------------------------------------------------------------+------------------------------------------+
| Numeric Functions      | Description                                                                | Recoding specifier                       |
+========================+============================================================================+==========================================+
| :func:`reclassify`     | Replaces specified values of a matrix, array or string array.              |  User-specified values.                  |
+------------------------+----------------------------------------------------------------------------+------------------------------------------+
| :func:`reclassifycuts` | Replaces values of a matrix or array within specified ranges.              |  User-specified values.                  |
+------------------------+----------------------------------------------------------------------------+------------------------------------------+
| :func:`code`           | Creates a new matrix based on recoding of an existing numeric vector.      |  Based on logical expression.            |
+------------------------+----------------------------------------------------------------------------+------------------------------------------+
| :func:`recode`         | Recodes the values of an existing vector of numeric data.                  |  Based on logical expression.            |
+------------------------+----------------------------------------------------------------------------+------------------------------------------+
| :func:`substute`       | Substitutes new values for old values in a matrix, depending on the        |  Based on logical expression.            |
|                        | outcome of a logical expression.                                           |                                          |
+------------------------+----------------------------------------------------------------------------+------------------------------------------+

+-------------------------+--------------------------------------------------------------------------------+
| Categorical Functions   |                                                                                |
+=========================+================================================================================+
| :func:`reorderCatLabels`| Changes relative order of categorical variable. This changes the key values    |
|                         | associated with the categorical labels.                                        |
+-------------------------+--------------------------------------------------------------------------------+
| :func:`recodeCatLabels` | Replaces the labels of categorical variables with new labels.                  |
+-------------------------+--------------------------------------------------------------------------------+

Recoding and reclassifying non-categorical data
+++++++++++++++++++++++++++++++++++++++++++++++++
Both the :func:`code` and :func:`recode` procedures can be used to recode data using conditional expressions.

The :func:`code` procedure:

* Creates a new matrix which splits existing data into classes.
* Uses *N* logical expressions to determine *N+1* classes.
* Works for vectors only.

Example:  Coding blood pressure data to create a new (binary) class variable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

  // Blood pressure data
  x = { 91,
       121,
        99,
       135,
       110,
       155 };

  // Values for the classes
  new_val = { 1, 2 };

  /*
  ** Create a vector containing a 1 for every element
  ** which is less than 120, or a 0 otherwise
  */
  logical = x .<  120;

  /*
  ** Create a new vector which contains the class
  ** assignment for each element in 'x'
  */
  x_class = code(logical, new_val);

The code above generates a new vector *x_class* which splits the original data into two
classes based on whether x is less than 120.

::

  x = 91   logical =  1   x_class = 1
     121              0             2
      99              1             1
     135              0             2
     110              1             1
     155              0             2

Example:  Coding blood pressure data to create a new multi-class variable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

  // Blood pressure data
  x = { 91,
       121,
        99,
       135,
       110,
       155 };

  // Values for the classes
  new_val = { 1,
              2,
              3 };

  // Create a vector containing a 1 for every element
  // which is less than 100, or a 0 otherwise
  logical_1 = x .<= 100;

  // Create a vector containing a 1 for every element
  // which is between 100 and 120, or a 0 otherwise
  logical_2 = x .> 100 .and x .<=  120;

  // Form a 2 column logical vector using
  // horizontal concatenation
  logical = logical_1 ~ logical_2;

  // Create a new vector which contains the class
  // assignment for each element in 'x'
  x_class = code(logical, new_val);

Now *x_class* splits the original data into three classes based on whether *x* is less than or equal to 100, falls between 100 and 120, or is greater 120.

::

  x =  91    logical = 1 0     x_class = 1
      121              0 0               3
       99              1 0               1
      135              0 0               3
      110              0 1               2
      155              0 0               3

.. note:: The :func:`setColLabels` function can be used to specify *x_class* as a categorical variable and to assign labels to the classes.

Recoding values of an existing vector
+++++++++++++++++++++++++++++++++++++

The :func:`recode` procedure :

* Replaces specific values of an existing vector with new values.
* Uses a logical expression to determine where and how to replace values.
* Is valid for vectors.

Some notes to remember about :func:`recode`:

*  There should be no more than a single 1 in any row of logical expression matrix.
*  For any given row of a data matrix and logical expression matrix, if a column of the logical expression is 1, the corresponding replacement values with replace the original element of the data matrix.
*  If every column of logical expression matrix contains a 0, the original value of the data matrix will be unchanged.

Example: Recoding numeric values based on ranges
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

  x = { 20,
      45,
      32,
      63,
      29 };

  // Create 4 column vectors with a 1 where the statement
  // evaluates as 'true'

  // Check if 20 < x <= 30
  e1 = (20 .lt x) .and (x .le 30);

  // Check if 30 < x <= 40
  e2 = (30 .lt x) .and (x .le 40);

  // Check if 40 < x <= 50
  e3 = (40 .lt x) .and (x .le 50);

  // Check if 50 < x <= 60
  e4 = (50 .lt x) .and (x .le 60);

  // Horizontally concatenate the column vectors into a 5x4
  // matrix
  logical = e1~e2~e3~e4;

  v = { 1.2,
        2.4,
        3.1,
        4.6 };

  // Replace elements of 'x' with elements from 'v' based upon
  // the 0's and 1's in 'e'
  x_new = recode(x, logical, v);

Note that in this example *x_new* is as follows:

::

            0   0   0   0
            0   0   1   0
  logical = 0   1   0   0
            0   0   0   0
            1   0   0   0

  // Since the third column of the second row of 'e' is equal
  // to 1, the second row of 'y' is set equal to the third
  // element of 'v', etc.
          20.000000
          3.1000000
  x_new = 2.4000000
          63.000000
          1.2000000

Reclassifying data
+++++++++++++++++++

The :func:`reclassify` and :func:`reclassifyCuts` procedures can be used to reclassify existing values to new values.

The :func:`reclassify` procedure:

* Replaces values in a *from* input with values specified in a *to* input.
* Works for matrices, arrays, and string arrays.
* Can be used to reclassify matrices to string arrays and vice versa.

.. note:: The :func:`reclassify` function can reclassify matrices to string arrays but does not create a dataframe. To create a dataframe with a string labels from an existing matrix see :func:`asDF`.

Example: Change instances of 1, 2 and 3 to ‘low’, ‘medium’ and ‘high’.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

  // Vector to be changed
  x = { 2,
        3,
        2,
        1,
        2,
        3 };

  from = { 1,
           2,
           3 };

  // Create a 3x1 string array using
  // string vertical concatenation operator
  to = "low" $| "medium" $| "high";

  x_new = reclassify(x, from, to);
  print x_new;

After the code above, *x_new* is equal to:

::

  medium
  high
  medium
  low
  medium
  high

In this case, if the number of specified strings in *to* is less than the number of unique values in *x*, the unmapped values will be converted directly into strings.

::

  // Vector to be changed
  x = { 2,
        3,
        2,
        1,
        2,
        3 };

  from = { 1,
           2};

  // Create a 3x1 string array using
  // string vertical concatenation operator
  to = "low" $| "medium";

  x_new = reclassify(x, from, to);
  print x_new;

Now *x_new* is

::

          medium
               3
          medium
             low
          medium
               3

Example: Change instances of tea types: ‘black’, ‘green’, ‘oolong’ to 9.95, 11.95 and 10.50, respectively.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

  string orders  = { "green",
                 "green",
                 "oolong",
                 "green",
                 "green",
                 "green",
                 "black" };

  string tea_types   = { "black",
                       "green",
                       "oolong" };

  price = { 9.95, 11.95, 10.50 };

  order_prices = reclassify(orders, tea_types, price);
  print order_prices;

The vector *order_prices* is equal to:

::

  11.95
  11.95
  10.50
  11.95
  11.95
  11.95
  9.95

In this case, if the number of specified values in *to* is less than the number of unique strings in *x*, unmapped strings will be reclassified as missings:

::

  string orders  = { "green",
                   "green",
                   "oolong",
                   "green",
                   "green",
                   "green",
                   "black" };

  string tea_types   = { "black",
                         "green" };

  price = { 9.95, 11.95 };

  order_prices = reclassify(orders, tea_types, price);
  print order_prices;

Now *order_prices* is:

::

  11.950000
  11.950000
          .
  11.950000
  11.950000
  11.950000
  9.9500000

The :func:`reclassifyCuts` procedure:

  * Splits the data in *x* into classes based on specified cutoff values.
  * Works for matrices and arrays.
  * Cutoff points can be used to define the right endpoint of an interval or the starting points of the next interval. The default is to use the cutoff points as starting points of the next interval.

Example: Basic sequence
+++++++++++++++++++++++++++++++

::

  // Create column vector to place in categories
  x = {   0,
        0.1,
        0.2,
        0.3,
        0.4,
        0.5,
        0.6,
        0.7 };

  // Cut points for data in 'x'
  cut_pts = { 0.2,
              0.5 };

  // Class 0:       x <= 0.2
  // Class 1: 0.2 < x <= 0.5
  // Class 2: 0.5 < x
  r_open = reclassifyCuts(x, cut_pts);

  // Class 0:       x < 0.2
  // Class 1: 0.2 <= x < 0.5
  // Class 2: 0.5 <= x
  r_closed = reclassifyCuts(x, cut_pts, 1);

  print "x = " x;
  print;
  print "r_open = " r_open;
  print;
  print "r_closed = " r_closed;
  print;
  print "cut_pts = " cut_pts;

This results in:

::

  x =
  0.00
  0.10
  0.20
  0.30
  0.40
  0.50
  0.60
  0.70

  r_open =
  0.00
  0.00
  0.00
  1.0
  1.0
  1.0
  2.0
  2.0

  r_closed =
  0.00
  0.00
  1.0
  1.0
  1.0
  2.0
  2.0
  2.0

  cut_pts =
  0.20
  0.50

Example: Classifying blood pressure data
++++++++++++++++++++++++++++++++++++++++++

::

  // Create a column of blood pressure data
  bp = {  87,
         154,
         127,
         112,
         159,
          90,
         151,
         109,
         125,
         107 };

  // Assign cut points
  cut_pts = { 120, 140 };

  // Create categorical variable
  bp_category = reclassifyCuts(bp, cut_pts);

  print "bp = " bp;
  print;
  print "bp_category = " bp_category;
  print;
  print "cut_pts = " cut_pts;

This splits the data in *bp* into three categories: those that fall below 120, those that greater than or equal to 120 but less than 140, and those that are greater than or equal to 140:

::

       87
       154
       127
       112
  bp = 159
       90
       151
       109
       125
       107

                 0
                 2
                 1
                 0
  bp_category =  2
                 0
                 2
                 0
                 1
                 0

  cut_pts = 120
            140

Substituting values
----------------------------

The :func:`substute` function replaces values in a matrix based on the outcome of a logical expression.

Example: Setting very small values to zero
++++++++++++++++++++++++++++++++++++++++++++++

::

  // Create example vector
  x = { 3.8e-21,
        1.0,
        3.5,
    2.7e-18,
        0.5,
        3.0,
    1.1e-16,
        0.5,
        2.2,
        4.0 };

  // Substitute all values less than 2.2e-16 with a zero
  x_new = substute(x, x .< 2.25e-16, 0);

This results in *x_new* equal to:

::

  0.00000000
  1.0000000
  3.5000000
  0.00000000
  0.50000000
  3.0000000
  0.00000000
  0.50000000
  2.2000000
  4.0000000

Recoding categorical data
+++++++++++++++++++++++++++++
The :func:`recodeCatLabels` can be use to change the labels on categorical variables in a dataframe.

Example: Recoding categories in yarn dataset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

  // Load data
  fname = getGAUSSHome("examples/yarn.xlsx");
  yarn = loadd(fname, "cat(yarn_length) + cat(amplitude) + cat(load) + cycles");

  // Get column labels for yarn_length
  { labels, keyvalues } = getColLabels(yarn, "yarn_length");

  // Print results
  sprintf("%11s", "Key"$~"Labels");
  sprintf("%10.0f %10s", keyvalues, labels);

  // Recode yarn_length variable from
  // 'low', 'medium', and 'high'
  //  to 'sm', 'md', 'lg'
  yarn_recoded = recodecatlabels(yarn, "low"$|"med"$|"high", "sm"$|"md"$|"lg", "yarn_length");

  // Get column labels for yarn_length
  { labels, keyvalues } = getColLabels(yarn_recoded, "yarn_length");

  // Print results
  print "Yarn recoded labels";

  sprintf("%11s", "Key"$~"Labels");
  sprintf("%10.0f %10s", keyvalues, labels);


This prints the following:

::

  Yarn labels
  Key     Labels

       0       high
       1        low
       2        med

  Yarn recoded labels
      Key     Labels

       0         lg
       1         sm
       2         md

Reordering categorical data
+++++++++++++++++++++++++++++
The :func:`reorderCatLabels` can be use to change the key values associated with categorical labels.

::

  // Load data
  fname = getGAUSSHome("examples/yarn.xlsx");
  yarn = loadd(fname, "cat(yarn_length) + cat(amplitude) + cat(load) + cycles");

  // Get column labels for yarn_length
  { labels, keyvalues } = getColLabels(yarn, "yarn_length");

  // Print results
  print "Yarn labels";

  sprintf("%11s", "Key"$~"Labels");
  sprintf("%10.0f %10s", keyvalues, labels);

  // Order labels
  yarn_reordered = reordercatlabels(yarn, "med"$|"high"$|"low", "yarn_length");

  // Get column labels for yarn_length
  { labels, keyvalues } = getColLabels(yarn_reordered, "yarn_length");

  // Print results
  print "Reordered yarn labels";

  sprintf("%11s", "Key"$~"Labels");
  sprintf("%10.0f %10s", keyvalues, labels);

This prints the following:

::

  Yarn labels
        Key     Labels

         0       high
         1        low
         2        med

  Reordered yarn labels
        Key     Labels

         0        med
         1       high
         2        low

Time series transformations
--------------------------------------------
While data lags, leads, differences and recursive terms can always be computed using matrix operations, GAUSS also includes built-in tools for these transformations.

+------------------------+----------------------------------------------------------------------------+------------------------------------------+
| Function               | Description                                                                | Format                                   |
+========================+============================================================================+==========================================+
| :func:`lag1`           | Lags a matrix by one time period for time series analysis.                 |  ``y = lag1(x)``                         |
+------------------------+----------------------------------------------------------------------------+------------------------------------------+
| :func:`lagn`           | Lags or leads a matrix a specified number of time periods. Use negative    |   ``y = lagn(x, t)``                     |
|                        | input *t* to indicate leads.                                               |                                          |
+------------------------+----------------------------------------------------------------------------+------------------------------------------+
| :func:`lagTrim`        | Lags or leads a matrix a specified number of time periods and removes      |  ``y = lagTrim(y, t)``                   |
|                        | the incomplete rows. Use negative input *t* to indicate leads.             |                                          |
+------------------------+----------------------------------------------------------------------------+------------------------------------------+
| :func:`shiftc`         | Shifts the columns of a matrix, or dataframe.                              |  ``y = shiftc(x, s, fill)``              |
+------------------------+----------------------------------------------------------------------------+------------------------------------------+
| :func:`recserar`       | Computes a vector of autoregressive recursive series.                      |  ``y = recserar(x, y0, rho)``            |
+------------------------+----------------------------------------------------------------------------+------------------------------------------+
| :func:`recserVAR`      | Computes a vector autoregressive recursive (VAR) series.                   |  ``y = recserVAR(x, y0, pi_)``           |
+------------------------+----------------------------------------------------------------------------+------------------------------------------+

Lagging data with the `lagn` or `lag1` procedures
+++++++++++++++++++++++++++++++++++++++++++++++++++
The :func:`lagn` and :func:`lag1` procedures are used to lag data without removing or replacing the missing values. These procedures accepts *M x T* data matrices, *x*, and the :func:`lagn` and procedure accepts an *ExE* conformable vector of lags.

The ExE conformability requirement means that :func:`lagn` can be used to compute:

* The same lag of every column of a data matrix.
* Specific lags for each column of a data matrix.
* Multiple lags of a single vector of data.

Because missing values are not removed by the :func:`lagn` and :func:`lag1` procedures, the returns from these procedures will always have the same number of rows as the input, *x*.

Computing a single lag of a matrix with `lagn`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In this example the *PPI* matrix contains two variables:

*  A date column named, *date*
*  Observed PPI data column named, *PPIACO*

To compute the same number of lags of each column of the data, a scalar lag input, *t* can be used:

::

  // Load PPIACO series
  // from FRED database
  PPI = fred_load("PPIACO");

  // Lag the PPI data
  // using lagn
  PPI_lag_1 = lagn(PPI, 1);

  // Preview PPI_lag_1 data
  head(PPI_lag_1);

Our preview shows that the first element of the *PPI_lag* vector is a missing value:

::

           date           PPIACO
              .                .
     1913-01-01        12.100000
     1913-02-01        12.000000
     1913-03-01        12.000000
     1913-04-01        12.000000

Computing a different lags of each column of a matrix with ``lagn``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To compute different lags of each column of data at the same time, a vector input of lags specifying a separate lag for each column of data can be used. Note that the lag vector must have the same number of elements as the number of columns in the matrix being lagged:

::

  // Load multiple series
  // from FRED
  data = fred_load("PPIACO + T10Y2Y");

  // Lags vectors
  lags = 1|2;

  // Compute Lags
  data_lag_12 = lagn(data["PPIACO" "T10Y2Y"], lags);

  // Preview the lagged data
  head(data_lag_12)

This computes the first lag of the *PPIACO* variable and the second lag of the *T10Y2Y* series:

::


Computing a different lags of vector of data using ``lagn``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

  // Load PPIACO series
  // from FRED database
  PPI = fred_load("PPIACO");

  // Specify lags vector
  lags = 1|2|3;

  // Lag just the observations
  // of the PPI data
  // using lagn
  PPI_lag_123 = lagn(PPI[., "PPIACO"], lags);

  // Preview PPI_lag_1 data
  head(PPI_lag_123);

This computes the first, second, and third lag of the *PPIACO* variable. Note that in this case, new variables names, *PPIACO_2* and *PPIACO_3* variables are created for first and second columns.

::

    PPIACO         PPIACO_2          PPIACO_3
          .               .                 .
  12.100000               .                 .
  12.000000        12.100000                .
  12.000000        12.000000        12.100000
  12.000000        12.000000        12.000000

Lagging data with the `lagTrim` procedure
++++++++++++++++++++++++++++++++++++++++++
The :func:`lagTrim` procedure removes resulting missing values from lagging the data. Like the :func:`lagn` procedure, the :func:`lagTrim` procedure accepts a *M x T* data matrices, *x*, and an *ExE* conformable vector of lags.

The return from the :func:`lagTrim` procedure will have a number of rows equal to the number of rows of the input *x* minus the maximum number of lags specified in *t*.

Computing multiple lags without missing values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

  // Create file name with full path
  fname = getGAUSSHome("examples/beef_prices.csv");

  // Load all observations of all variables
  beef = loadd(fname);

  // Create lag vector
  lags = 1|2|3;

  // Compute lags using lagTrim
  beef_lagTrim = lagTrim(beef[., 2], lags);

  // Preview lagged data
  head(beef_lagTrim);

  // Compare number of rows
  print "Rows in original data:";
  rows(beef);

  print "Rows in lagged data:";
  rows(beef_lagTrim);

The *beef_lagTrim* matrix has 282 rows, 3 less than the input data *beef*:

::

  111.11000        114.49000        116.64000
  108.17000        111.11000        114.49000
  107.76000        108.17000        111.11000
  105.90000        107.76000        108.17000
  106.43000        105.90000        107.76000

  Rows in original data:
  285.00000

  Rows in lagged data:
  282.00000

Shifting data with the ``shiftc`` procedure
+++++++++++++++++++++++++++++++++++++++++++++++
The :func:`shiftc` procedure shifts columns of a data matrix and requires three inputs:

* A N x K matrix of data.
* A scalar or 1 x N input specifying the magnitude of the shift.
* A scalar or 1 x N input specifying the value to fill in the shifted rows.

The return from the :func:`shiftc` procedure will have a number of rows equal to the number of rows of the data input. The :func:`shiftc` procedure can be used to fill the shifted rows with values other than missing values.

Shifting columns of a data matrix
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

  // Create file name with full path
 fname = getGAUSSHome("examples/beef_prices.csv");

 // Load all observations of all variables
 beef = loadd(fname);

 // Trim data to make smaller example set
 beef = beef[1:5,.];

 // Shift all columns of beef forward 2 rows
 // filling the extra rows with a missing value
 beef_lag = shiftc(beef, 2, miss());

After the above code:

::

  beef_lag =   date       beef_price
                  .                .
                  .                .
             199201        116.64000
             199202        114.49000
             199203        111.11000

Using the *beef* dataframe from the first example:

::

  // Shift all columns of beef forward 2 rows
  // filling the extra rows with a missing value
  beef_lag_0 = shiftc(beef, 2, 0);

After the above code:

::

  beef_lag_0 =   date       beef_price
                    0                0
                    0                0
               199201        116.64000
               199202        114.49000
               199203        111.11000



Panel data transformations
---------------------------
The :func:`dfLonger` and :func:`dfWider` functions provide intuitive and comprehensive tools for converting between long-form and wide-form panel data. Both procedures work with g

The ``dfLonger`` procedure 
+++++++++++++++++++++++++++
The :func:`dfLonger` procedure transform wide-form GAUSS dataframes to long-form GAUSS dataframes. Setting up the :func:`dfLonger` procedure requires four basic steps:

1. Identify the variables contained in the wide-form dataset. 
2. Identify the columns to convert. 
3. Name the new columns created in the long-form data for storing names.
4. Name the new columns created in the long-form data for storing values. 

Basic pivoting
^^^^^^^^^^^^^^^
Some wide-form datasets are easy to convert and can be done using the default settings. Consider the data in the *tiny_car_panel.csv* file. 

::

    // Load data
    file_name = getGAUSSHome("examples/tiny_car_panel.csv");
    df_wide = loadd(file_name);

    print df_wide;

This function is a wide-form panel dataset:

::

         Years     Cars_compact       Cars_truck         Cars_SUV
    1973-01-01        5.0000000                .        3.0000000
    1974-01-01        2.0000000        1.0000000        9.0000000

This dataset contains counts of different car types across different years. In terms of our four step process:

1. The variable contained in the wide-form dataset is car-types *count*.
2. The columns to convert are *Cars_compact*, *Cars_trucks*, and *Cars_SUV*.
3. We will create a *Car Class* column to store car type names. 
4. We will create a *counts* column to store counts of car types. 

::

    // Get all column names and remove the first column name, 'Years'
    columns = getcolnames(df_wide);
    columns = trimr(columns, 1, 0);
    
    // Specify the new column to store names
    names_to = "Class";
    
    // Specify the new column to store values
    values_to = "Count";

    // Convert data using 'dfLonger'
    df_long = dfLonger(df_wide, columns, names_to, values_to);

    print df_long;

The *df_long* dataframe now contains the stacked panel data, with three variables, *Years*, *Class*, and *Count*.

::

           Years            Class            Count 
      1973-01-01     Cars_compact        5.0000000 
      1973-01-01       Cars_truck                . 
      1973-01-01         Cars_SUV        3.0000000 
      1974-01-01     Cars_compact        2.0000000 
      1974-01-01       Cars_truck        1.0000000 
      1974-01-01         Cars_SUV        9.0000000

Advanced pivoting
^^^^^^^^^^^^^^^^^^
The optional ``pivotControl`` structure allows you to control pivoting specifications using the following members:

+------------------------+----------------------------------------------------------------------------+
| Member                 | Purpose                                                                    |
+========================+============================================================================+
| *names_prefix*         | A string input which specifies which characters, if any, should be stripped|
|                        | from the front of the wide variable names before they are assigned to a    |
|                        | long column.                                                               |
+------------------------+----------------------------------------------------------------------------+
| *names_sep_split*      | A string input which specifies which characters, if any, mark where the    |
|                        | *names_to* names should be broken up.                                                             |
+------------------------+----------------------------------------------------------------------------+
| *names_pattern_split*  | A string input containing a regular expression specifying group(s) in      |
|                        | *names_to* names which should be broken up.                                |
+------------------------+----------------------------------------------------------------------------+
| *names_types*          | A string input specifying data types for the names_to variable.            |
+------------------------+----------------------------------------------------------------------------+
| *values_drop_missing*  | Scalar, is set to 1 all rows with missing values will be removed.          |
+------------------------+----------------------------------------------------------------------------+

Consider a more advanced case using the *olympic_vault_wide.csv* data file.

::

    // Load the data
    df_wide = loadd(getGAUSSHome("examples/olympic_vault_wide.csv"));
    print df_wide;

This wide dataset looks like:

::

          Country     vault_2012_f     vault_2012_m     vault_2016_f     vault_2016_m
    United States        48.100000        46.600000        46.900000        45.900000
           Russia        46.400000        46.900000        45.700000        46.000000
            China        44.300000        48.300000        44.300000        45.000000

In terms of the four-step pivoting process:

1. The variable contained in the wide-form dataframe is scores. 
2. The columns to convert are all columns with the exception of the first column. 
3. The names of the columns in the wide data contain information about the *event*, the *year*, and the *sex* of the athlete. 
4. We will create a *scores* column to store the values in the long-form dataframe.

Because of the more advanced structure of the names in the wide-form dataframe, a ``pivotControl`` structure should be used. 

::

    // Get the list of variables to pivot
    // and remove the first column name, 'Country'
    columns =  getcolnames(df_wide);
    columns = trimr(columns, 1, 0);

    // Declare 'pctl' to be a pivotControl structure
    // and fill with default settings
    struct pivotControl pctl;
    pctl = pivotControlCreate();

    // Split the variable names from 'columns', i.e. vault_2012_f, etc
    // every time an underscore is encountered
    pctl.names_sep_split = "_";

    // Set variable names for the new columns
    names_to = "event" $| "year" $| "gender";

    // Set name of value column
    values_to = "score";

    // Convert 'year' to be a date variable.
    pctl.names_types = { "year" "date" };

    df_long = dfLonger(df_wide, columns, names_to, values_to, pctl);
    print df_long;

The *df_long* dataframe looks like:

::

          Country            event             year           gender            score
    United States            vault             2012                f        48.100000
    United States            vault             2012                m        46.600000
    United States            vault             2016                f        46.900000
    United States            vault             2016                m        45.900000
           Russia            vault             2012                f        46.400000
           Russia            vault             2012                m        46.900000
           Russia            vault             2016                f        45.700000
           Russia            vault             2016                m        46.000000
            China            vault             2012                f        44.300000
            China            vault             2012                m        48.300000
            China            vault             2016                f        44.300000
            China            vault             2016                m        45.000000
            
Dummy variables
-------------------------

Automatic treatment of categorical variables in estimation
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Categorical variables in dataframes will automatically be treated as dummy variables in GAUSS estimation routines. This means no extra steps are necessary to include categorical variables in regression.

Example: Include a categorical variable in OLS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

  // Load data
  fname = getGAUSSHome("examples/auto2.dta");

  // Include the `rep78`
  // categorical variable in
  // ols estimation
  call olsmt(fname, "price ~ mpg + rep78");

The categorical variable *rep78* will automatically be included in the OLS regression as a dummy variable with the base case excluded from the regression. In addition, the category labels will be displayed in the printed output table.

::

  Standard                                                  Prob   Standardized  Cor with
  Variable             Estimate      Error      t-value     >|t|     Estimate    Dep Var
  ---------------------------------------------------------------------------------------

  CONSTANT                10450     2251.04     4.64229     0.000       ---         ---
  mpg                  -280.261     61.5767    -4.55142     0.000   -0.564519   -0.455949
  rep78: Fair           877.635     2063.28    0.425358     0.672   0.0971824  -0.0223477
  rep78: Average        1425.66     1905.44    0.748204     0.457     0.24444   0.0859051
  rep78: Good           1693.84     1942.67    0.871914     0.387    0.257252   -0.015317
  rep78: Excellent      3131.98     2041.05      1.5345     0.130    0.396546   -0.035102

The categories of *rep78*, ``"Fair"``, ``"Average"``, ``"Good"``, and ``"Excellent"``, are included as dummy variables in the regression. The ``"Poor"`` category is excluded from the regression, as it is the base case.

Example: Include a categorical variable in GLM estimation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

  // Load data
  fname = getGAUSSHome("examples/auto2.dta");

  // Loadd data and remove missing values
  data = packr(loadd(fname, "price + mpg + rep78"));

  // Include the `rep78`
  // categorical variable in
  // linear regression using glm
  call glm(data, "price ~ mpg + rep78", "normal");

::

  Standard                                                                        Prob
  Variable                 Estimate            Error          t-value             >|t|
  ----------------     ------------     ------------     ------------     ------------
  CONSTANT                    10450             2251           4.6423         < 0.0001
  mpg                       -280.26           61.577          -4.5514         < 0.0001
  rep78: Fair                877.63           2063.3          0.42536         0.672025
  rep78: Average             1425.7           1905.4           0.7482         0.457121
  rep78: Good                1693.8           1942.7          0.87191         0.386566
  rep78: Excellent             3132             2041           1.5345         0.129915


Generating dummy variables outside of estimation
+++++++++++++++++++++++++++++++++++++++++++++++++

Outside of estimation, dummy variables can be created using a number of procedures:

+------------------------+----------------------------------------------------------------------------+
| Functions              | Description                                                                |
+========================+============================================================================+
| :func:`design`         | Creates dummy variables from discrete data that is split into classes.     |
+------------------------+----------------------------------------------------------------------------+
| :func:`dummybr`        | Creates dummy variables from continuous data based on break points.        |
|                        | The highest (rightmost) category is bounded on the right.                  |
+------------------------+----------------------------------------------------------------------------+
| :func:`dummydn`        | Creates dummy variables from continuous data based on break points.        |
|                        | The highest (rightmost) category is unbounded on the right, and a          |
|                        | specified column of dummies is dropped.                                    |
+------------------------+----------------------------------------------------------------------------+
| :func:`dummy`          | Creates dummy variables from continuous data based on break points.        |
|                        | The highest (rightmost) category is unbounded on the right.                |
+------------------------+----------------------------------------------------------------------------+


Example: Create dummy variables based on BP classes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This example builds on an earlier example, in which BP data was split into 3 classes using :func:`reclassify`.

::

  // Classified BP data
  bp_class = { 1,
             3,
             1,
             3,
             2,
             3 };

  // Create matrix of dummy
  // variables using design
  dv_bp_classes = design(bp_class);

After this code *dv_bp_classes* is equal to:

::

  dv_bp_classes;

       1      0      0
       0      0      1
       1      0      0
       0      0      1
       0      1      0
       0      0      1

Example: Create dummy variables from continuous BP data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :func:`dummybr` variable can be used to generate dummy variables from the ranges of
original BP data.

::

  // Create a column of blood pressure data
  bp = { 91,
       121,
        99,
       135,
       110,
       155 };

  // Create breakpoints
  v = { 100, 120 };

  // Create dummy variables
  dv_bp = dummy(bp, v);

Note that *dv_bp* is the same as *dv_bp_classes* from the first example:

::

  1      0      0
  0      0      1
  1      0      0
  0      0      1
  0      1      0
  0      0      1

Example: Create dummy variables from continuous BP data and drop first column
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The :func:`dummydn` variable can be used to generate dummy variables from the ranges of
original BP data.

::

  // Create a column of blood pressure data
  bp = { 91,
       121,
        99,
       135,
       110,
       155 };

  // Create breakpoints
  v = { 100, 120 };

  // Create dummy variables
  dv_bp_drop = dummydn(bp, v, 1);

Now the *dv_bp_drop* matrix is the same as the second and third columns of *dv_bp* and *dv_bp_classes*:

::

  0      0
  0      1
  0      0
  0      1
  1      0
  0      1
