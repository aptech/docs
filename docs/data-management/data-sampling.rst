Data Sampling
=============================

Sampling with replacement from a matrix or dataframe
--------------------------------------------------------
There are two ways to sample with replacement from a matrix or dataframe:

*  The :func:`sampleData` procedure.
*  The :func:`rndi` procedure.

The :func:`sampleData` procedure directly returns a sample from a matrix or dataframe. The final argument is an indicator for replacement and should be set to 1 to indicate sampling with replacement.

Example: Sampling with replacement from a matrix
++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Set seed for repeatable random draws
    rndseed  23423;

    // Create a 7x2 vector
    x  = { 1.2 1.8,
           2.7 2.1,
           3.0 3.3,
           4.8 4.1,
           5.1 5.4,
           6.0 2.8,
           7.2 3.9 };

    replace = 1;

    // Take a sample of 5 rows of 'x' with replacement
    sample = sampleData(x, 5, replace);

After the code above, *s* is equal to:

::

    5.1    5.4
    3.0    3.3
    6.0    2.8
    4.8    4.1
    3.0    3.3

Repeated observations of ``3.0`` and ``3.3`` occur because the sampling takes place with replacement.

The :func:`rndi` function returns random integers from a uniform distribution with the option to specify a range. These can be used as indices for sampling, enabling you to easily draw corresponding rows from two or more variables.

.. note:: Sampling with random indices maintains the metadata from the original dataframe and will contain variable names, types, etc.

Example: Sampling with replacement from multiple matrices
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Set seed for repeatable random draws
    rndseed  73725;

    y = { 9.1,
          2.3,
          6.7,
          4.4,
          5.1 };

    X = { 8.3 8.2,
          8.8 7.9,
          2.4 1.9,
          3.9 4.2,
          8.2 9.1 };


    // Create a random sample of
    // integers from 1 to 5
    idx = rndi(5, 1, 1|5);

    // Use 'idx' to draw corresponding rows from 'y' and 'X'
    y_s = y[idx];
    X_s = X[idx,.];

After the code above:

::

    idx = 5    y_s = 5.1    X_s = 8.2    9.1
          4          4.4          3.9    4.2
          2          2.3          8.8    7.9
          3          6.7          2.4    1.9
          5          5.1          8.2    9.1

Example: Generating indices to sample from a matrix
++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

      // Load data from the 'fueleconomy' dataset
      // in the GAUSS examples directory
      file_name = getGAUSSHome() $+ "examples/fueleconomy.dat";
      fueleconomy = loadd(file_name);

      // Create a 100x1 vector of random
      // integers between 1 and 100
      range_start = 1;
      range_end = rows(fueleconomy);
      idx = rndi(100, 1, range_start | range_end);

      // Draw a 100 observation sample from 'fueleconomy'
      fuel_sample = fueleconomy[idx, .];

Sampling without replacement from a matrix
--------------------------------------------
The :func:`sampleData` procedure can also be used to sample from a matrix or dataframe without replaced.  In this case, the final argument should be set to 0 to indicate sampling without replacement.

Example: Sampling without replacement
+++++++++++++++++++++++++++++++++++++++++

::

  // Set seed for repeatable random draws
  rndseed  23423;

  // Create a 7x1 vector
  x  = { 1,
         2,
         3,
         4,
         5,
         6,
         7 };

  // Take a sample of 3 elements without replacement
  s  = sampleData(x, 3);

.. note:: Setting the :func:`rndseed` before using :func:`sampleData` should be done if you want to replicate the same sample each draw.

Drawing a random sample from a dataset
------------------------------------------
The :func:`exctSmpl` procedure draws a sample with replacement from an existing data file and saves the result as a new data file. Neither the data file drawn from nor the new sample created are saved in the GAUSS workspace.

The :func:`exctSmpl` procedure returns the number of rows in the new data file OR an error code.  Specific error code details are available in Command Reference listing for :func:`exctSmpl`.

Example: Sample from data file
+++++++++++++++++++++++++++++++++++++++++++

::

  // Create file name with full path
  fname = getGAUSSHome()$+ "examples/credit.dat";

  // Randomly sample 30% of the rows from 'credit.dat'
  // and write them to a new dataset in the
  // GAUSS working directory, named 'sample.dat'
  n_rows = exctsmpl(fname, "sample.dat", 30);

After the code above,

::
  
  n_rows = 120
