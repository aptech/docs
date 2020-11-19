Data Transformations
=============================

Normalizing and scaling data
------------------------------
The :func:`rescale` function provides 8 different scaling options and returns the rescaled along with the location and scale factors.

+--------------------+----------------------------+----------------------------------------------+
| Method             | Location                   | Scale Factor                                 |
+====================+============================+==============================================+
| “euclidean”        | 0                          |  Euclidean length                            |
+--------------------+----------------------------+----------------------------------------------+
| "mad"              | median                     |  Absolute deviation from median              |
+--------------------+----------------------------+----------------------------------------------+
| “maxabs”           | 0                          |  Maximum absolute value                      |
+--------------------+----------------------------+----------------------------------------------+
| “midrange”         | :math: `\frac{Max+Min}{2}` | :math: `\frac{Range}{2}`                     |
+--------------------+----------------------------+----------------------------------------------+
| “range”            | Minimum                    |  Range                                       |
+--------------------+----------------------------+----------------------------------------------+
| “standardize”      | Mean                       |  Standard deviation                          |
+--------------------+----------------------------+----------------------------------------------+
| “sum”              | 0                          |  Sum                                         |
+--------------------+----------------------------+----------------------------------------------+
| “ustd”             | 0                          |  Standard deviation around origin            |
+--------------------+----------------------------+----------------------------------------------+

Example: Specifying a scaling method
+++++++++++++++++++++++++++++++++++++

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
  location_s =        14.750000
  scale_factor_s =        4.2084948

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
  location_m =        15.000000
  scale_factor_m =        2.8500000

The :func:`rescale` function can also be used with a known location and scale factor to rescale data.

Example: Rescaling using known location and scaling factors
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

  // Additional observations
  x_new = { 9.3  964.1,
           10.9 1173.7,
           11.1 1232.0,
            9.1 1051.2,
           14.6 1124.1,
           18.4  815.3,
           20.2 1292.6,
           18.5  833.1 };

  // Rescale matrix above using
  // location and scale matrix
  // from above
  x_s2 = rescale(x_new, location_s, scale_factor_s);

After the code above:

::

    Standardized rescaling:
    x_s2 =
      -1.2949998
     -0.91481638
     -0.86729345
      -1.3425227
    -0.035642197
      0.86729345
       1.2949998
      0.89105492

The :func:`rescale` function can also be used to rescale multiple columns at time.

Example: Rescaling multiple columns
+++++++++++++++++++++++++++++++++++++++

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
  location =        14.750000        1029.8875
  scale_factor =        4.2084948        203.85740

Recoding and reclassifying
--------------------------------
GAUSS provides a variety of tools for recoding and reclassifying data.

+------------------------+--------------------------------------------------------------------------------+
| Function               |                                                                                |
+========================+================================================================================+
| :func:`reclassify`     | Replaces specified values of a matrix, array or string array.                  |
+------------------------+--------------------------------------------------------------------------------+
| :func:`reclassifycuts` | Replaces values of a matrix or array within specified ranges.                  |
+------------------------+--------------------------------------------------------------------------------+
| :func:`code`           | Allows a new variable to be created (coded) with different values              |
|                        | depending upon which one of a set of logical expressions is true.              |
+------------------------+--------------------------------------------------------------------------------+
| :func:`recode`         | Changes the values of an existing vector from a vector of                      |
|                        | new values.                                                                    |
+------------------------+--------------------------------------------------------------------------------+
| :func:`substute`       | Substitutes new values for old values in a matrix, depending on the            |
|                        | outcome of a logical expression.                                               |
+------------------------+--------------------------------------------------------------------------------+

**Coding new variables**

The :func:`code` procedure creates new variables from existing variables using conditional expressions.

Example:  Coding blood pressure data to create a new class variable
---------------------------------------------------------------------

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

**Recoding values of an existing vector**

While the :func:`code` procedure creates a new variable, the :func:`recode` procedure can be used to replace specific values of an existing vector with new values.
Some notes to remember about :func:`recode`:

*  There should be no more than a single 1 in any row of logical expression matrix.
*  For any given row of a data matrix and logical expression matrix, if the Kth column of the logical expression is 1, the Kth element of v will replace the original element of the data matrix.
*  If every column of logical expression matrix contains a 0, the original value of the data matrix will be unchanged.

Example: Recoding a vector of values based on ranges
-----------------------------------------------------

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
  e = e1~e2~e3~e4;

  v = { 1.2,
        2.4,
        3.1,
        4.6 };

  // Replace elements of 'x' with elements from 'v' based upon
  // the 0's and 1's in 'e'
  y = recode(x, e, v);

The above code assigns e and y as follows:

::

      0   0   0   0
      0   0   1   0
  e = 0   1   0   0
      0   0   0   0
      1   0   0   0

  // Since the third column of the second row of 'e' is equal
  // to 1, the second row of 'y' is set equal to the third
  // element of 'v', etc.
      20.000000
      3.1000000
  y = 2.4000000
      63.000000
      1.2000000
