Data Sampling
=============================

Sampling with replacement from a matrix
------------------------------------------
Use :func:`sampleData` procedure to obtain a sample from a data matrix or dataframe. The final argument is an indicator for replacement, and should be set to 1 to indicate sampling with replacement.

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

After the code above, s is equal to:

~~~
5.1    5.4
3.0    3.3
6.0    2.8
4.8    4.1
3.0    3.3
~~~

Repeated observations of 3.0 and 3.3 occur because the sampling takes place with replacement.

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
The :func:`exctSmple` procedure draws a sample with replacement from an existing data file and saves the result as a new data file. Neither the data file drawn from nor the new sample created are saved in the GAUSS workspace.

The :func:`exctSmple` procedure has returns the number of rows in the new data file OR an error code.

Example: Sample from credit.dat data file
+++++++++++++++++++++++++++++++++++++++++++

::

  // Create file name with full path
  fname = getGAUSSHome()$+ "examples/credit.dat";

  // Randomly sample 30% of the rows from 'credit.dat'
  // and write them to a new dataset in the
  // GAUSS working directory, named 'sample.dat'
  n_rows = exctsmpl(fname, "sample.dat", 30);
