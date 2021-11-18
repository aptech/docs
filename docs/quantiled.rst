
quantiled
==============================================

Purpose
----------------

Computes quantiles from data in a dataset, given specified probabilities.

Format
----------------
.. function:: y = quantiled(dataset, e, var)

    :param dataset: dataset name, or NxM matrix of data.
    :type dataset: string

    :param e: quantile levels or probabilities.
    :type e: Lx1 vector

    :param var: If Kx1, character vector of labels selected for analysis, or numeric vector of column numbers in dataset of variables selected for analysis.

        If *var* is scalar zero, all columns are selected.

        If *dataset* is a matrix *var* cannot be a character vector.

        If *dataset* includes variable names, then *var* could be a string array, e.g. ``"Height" $| "Weight"`` or formula string. e.g. ``"Height + Weight"``.

    :type var: Kx1 vector or scalar zero, string array, or formula string.

    :return y: quantiles.

    :rtype y: LxK matrix

Examples
----------------

Use dataset name
+++++++++++++++++

::

    // Create file name with full path
    file_name = getGAUSSHome() $+ "examples/fueleconomy.dat";

    // Set up quantile levels
    e = { .025, .5, .975 };

    // Choose all variables in the dataset
    var = 0;

    // Compute quantiles
    y = quantiled(file_name, e, var);

     print "medians";
     print y[2, .];
     print;
     print "95 percentiles";
     print y[1, .];
     print y[3, .];

produces:

::

    medians
    2.5000000        3.0000000

    95 percentiles
    1.5500000        1.4000000
    4.0500000        6.2550000

Use .csv file and variable index
++++++++++++++++++++++++++++++++

::

    // Create file name with full path
    file_name = getGAUSSHome() $+ "examples/binary.csv";

    // Set up quantile levels
    e = { .025, .5, .975 };

    // Set up variable index
    var = 2|3;

    // Compute quantiles
    y = quantiled(file_name, e, var);

     print "medians";
     print y[2, .];
     print;
     print "95 percentiles";
     print y[1, .];
     print y[3, .];

After the above code:

::

    medians
    580.00000        3.3900000

    95 percentiles
    360.00000        2.6300000
    800.00000        4.0000000

Use .xls file and formula string
++++++++++++++++++++++++++++++++

::

    // Create file name with full path
    file_name = getGAUSSHome() $+ "examples/nba_ht_wt.xls";

    // Set up quantile levels
    e = { .025, .5, .975 };

    // Set up formula string
    var = "Height + Weight" ;

    // Compute quantiles
    y = quantiled(file_name, e, var);
     print  "Height"$~"Weight";
     print  "medians";
     print y[2, .];
     print;
     print  "95 percentiles";
     print y[1, .];
     print y[3, .];

After the above code:

::

    medians
    220.00000        79.500000

    95 percentiles
    175.00000        72.000000
    270.00000        84.000000

Remarks
-------

- :func:`quantiled` will not succeed if ``N*minc(e)`` is less than 1, or ``N*maxc(e)`` is greater than :math:`N - 1`. In other words, to produce a quantile for a level of .001, the input matrix must have more than 1000 rows.

- The supported dataset types are CSV,	XLS, XLSX, HDF5, FMT, DAT.

- For HDF5 file, the dataset must include file schema and both file name and dataset name must be provided, e.g.

  ::

      quantiled("h5://C:/gauss22/examples/testdata.h5/mydata", 0.5, 0).

Source
------

quantile.src

.. seealso:: `Formula string`
