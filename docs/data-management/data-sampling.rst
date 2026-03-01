Data Sampling
=============================

Sampling draws a subset of observations from a dataset. Common uses
include bootstrapping, Monte Carlo simulation, creating holdout sets
for validation, and working with datasets too large to fit in memory.

+---------------------------+---------------------------------------------------------------------+
| Function                  | Description                                                         |
+===========================+=====================================================================+
| :func:`sampleData`        | Sample rows from a matrix or dataframe, with or without             |
|                           | replacement.                                                        |
+---------------------------+---------------------------------------------------------------------+
| :func:`rndi`              | Generate random integers for custom index-based sampling.           |
+---------------------------+---------------------------------------------------------------------+


Sampling with Replacement
--------------------------------------------

Sampling **with replacement** means the same row can appear more than
once in the sample. This is the basis of bootstrap methods.

Using sampleData
+++++++++++++++++++++++++++++++++

:func:`sampleData` is the simplest way to draw a sample.
By default, it samples **without** replacement. Set the third argument
to ``1`` for sampling with replacement:

::

    sample = sampleData(x, n_rows, 1);

- *x* — matrix or dataframe to sample from.
- *n_rows* — number of rows to draw.
- The third argument: ``1`` = with replacement, ``0`` = without (default).

Example: Bootstrap sample
^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    rndseed 23423;

    x = { 1.2 1.8,
          2.7 2.1,
          3.0 3.3,
          4.8 4.1,
          5.1 5.4,
          6.0 2.8,
          7.2 3.9 };

    // Draw 5 rows with replacement
    sample = sampleData(x, 5, 1);
    print sample;

This prints:

::

    5.1    5.4
    3.0    3.3
    6.0    2.8
    4.8    4.1
    3.0    3.3

Row ``3.0  3.3`` appears twice because sampling with replacement can
select the same row more than once.


Using rndi for index-based sampling
++++++++++++++++++++++++++++++++++++

The :func:`rndi` function generates random integers in a specified
range. Using these as row indices lets you generate one index vector
and apply it to any number of variables — useful when you need to
keep *X*, *y*, and other variables aligned:

::

    // 1|rows(x) creates the 2x1 vector { 1, rows(x) }
    // using the vertical concatenation operator |
    idx = rndi(n_rows, 1, 1|rows(x));

- The third argument is a 2x1 vector giving the range:
  ``min_value | max_value``.

Example: Sampling aligned X and y
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    rndseed 73725;

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

    // Random integers from 1 to 5
    idx = rndi(5, 1, 1|5);

    // Index into both variables with the same indices
    y_s = y[idx];
    X_s = X[idx, .];

    print idx ~ y_s ~ X_s;

This prints:

::

       5.0000000        5.1000000        8.2000000        9.1000000
       4.0000000        4.4000000        3.9000000        4.2000000
       2.0000000        2.3000000        8.8000000        7.9000000
       3.0000000        6.7000000        2.4000000        1.9000000
       5.0000000        5.1000000        8.2000000        9.1000000

Each row is consistent across all variables because the same ``idx``
was used for both ``y`` and ``X``.

.. note::

    When sampling from a dataframe, the result preserves column names,
    types, and other metadata from the original.


Example: Sampling from a real dataset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    // Load data
    fname = getGAUSSHome("examples/fueleconomy.dat");
    fueleconomy = loadd(fname);

    // Draw 100 rows with replacement
    idx = rndi(100, 1, 1|rows(fueleconomy));
    fuel_sample = fueleconomy[idx, .];

    print "Original rows:" rows(fueleconomy);
    print "Sample rows:  " rows(fuel_sample);


Sampling without Replacement
--------------------------------------------

Sampling **without replacement** means each row can appear at most once.
This is the default behavior of :func:`sampleData` — when you omit the
third argument (or set it to ``0``), sampling is without replacement:

::

    sample = sampleData(x, n_rows);

The sample size must be less than or equal to the number of rows
in *x*.

Example: Draw a unique subset
+++++++++++++++++++++++++++++++++

::

    rndseed 23423;

    x = { 1,
          2,
          3,
          4,
          5,
          6,
          7 };

    // Draw 3 elements without replacement
    s = sampleData(x, 3);
    print s;

This prints:

::

       5.0000000
       3.0000000
       7.0000000

Every value appears exactly once.

.. tip::

    To **shuffle** the rows of a matrix, sample all rows without
    replacement::

        shuffled = sampleData(x, rows(x));


Setting Seeds for Reproducibility
--------------------------------------------

Sampling functions use the GAUSS random number generator. To get the
same sample every time, set the seed with :func:`rndseed` before
sampling:

::

    rndseed 12345;
    s1 = sampleData(x, 5, 1);

    rndseed 12345;
    s2 = sampleData(x, 5, 1);

    // s1 and s2 are identical
    print (s1 .== s2);

Every element prints ``1``, confirming the two samples match.


Choosing a Method
--------------------------------------------

.. list-table::
    :widths: 25 40 35
    :header-rows: 1

    * - Method
      - Best for
      - Notes

    * - :func:`sampleData`
      - General-purpose sampling from a matrix or dataframe
      - Simplest option; supports with and without replacement

    * - :func:`rndi`
      - Sampling aligned rows from multiple variables
      - Generate one index, apply to any number of variables

.. note::

    The GAUSS Machine Learning (GML) add-on provides additional
    functions for model evaluation workflows: :func:`trainTestSplit`
    for train/test splits, :func:`cvSplit` for k-fold cross-validation,
    and :func:`splitData` for splitting a single matrix.

.. seealso:: Functions :func:`sampleData`, :func:`rndi`, :func:`rndseed`
