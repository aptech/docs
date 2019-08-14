
dstatmt
==============================================

Purpose
----------------

Compute descriptive statistics.

Format
----------------
.. function:: dout = dstatmt(dataset[, vars[, ctl]])

    :param dataset: name of dataset. If *dataset* is null or 0, *vars* will be assumed to be a matrix containing the data.
    :type dataset: string

    :param vars: the variables.

     If *dataset* contains the name of a dataset, *vars* will be interpreted as either:

         * A Kx1 character vector containing the names of variables.
         * A Kx1 numeric vector containing indices of variables. 
         * A `formula string`. e.g. :code:`"PAY + WT"` or :code:`". - sex"`

         These can be any size subset of the variables in the dataset and can be in any order. If a scalar 0 is passed, all columns of the dataset will be used.

     If *dataset* is null or 0, *vars* will be interpreted as a NxK matrix, the data on which to compute the descriptive statistics.

    :type vars: string or string array

    :param ctl: instance of a ``dstatmtControl`` structure containing the following members:

        .. list-table::
            :widths: auto

            * - *ctl.altnames*
              - Kx1 string array of alternate variable names to be used if a matrix in memory is analyzed (i.e., dataset is a null string or 0). Default = "".
            * - *ctl.maxbytes*
              - scalar, the maximum number of bytes to be read per iteration of the read loop. Default = 1e9.
            * - *ctl.vartype*
              - scalar, unused in dstatmt.
            * - *ctl.miss*
              - scalar, default 0.

                  :0: there are no missing values (fastest).
                  :1: listwise deletion, drop a row if any missings occur in it.
                  :2: pairwise deletion.

            * - *ctl.row*
              - scalar, the number of rows to read per iteration of the read loop.If 0, (default) the number of rows will be calculated using *ctl.maxbytes* and *maxvec*.
            * - *ctl.output*
              - scalar, controls output, default 1.

                  :1: print output table.
                  :0: do not print output.


    :type ctl: Optional input

    :return dout: instance of :class:`dstatmtOut` struct
        structure containing the following members:

        .. list-table::
            :widths: auto

            * - *dout.vnames*
              - Kx1 string array, the names of the variables used in the statistics.
            * - *dout.mean*
              - Kx1 vector, means.
            * - *dout.var*
              - Kx1 vector, variance.
            * - *dout.std*
              - Kx1 vector, standard deviation.
            * - *dout.min*
              - Kx1 vector, minima.
            * - *dout.max*
              - Kx1 vector, maxima.
            * - *dout.valid*
              - Kx1 vector, the number of valid cases.
            * - *dout.missing*
              - Kx1 vector, the number of missing cases.
            * - *dout.errcode*
              - scalar, error code, 0 if successful; otherwise, one of the following:

                  :2: Can't open file.
                  :7: Too many missings - no data left after packing.
                  :9: *altnames* member of :class:`dstatmtControl` structure wrong size.
                  :10: *vartype* member of :class:`dstatmtControl` structure wrong size.

    :type dout: struct

Examples
----------------

Computing statistics on a GAUSS dataset
+++++++++++++++++++++++++++++++++++++++

::

    // Create file name with full path
    file_name = getGAUSSHome() $+ "examples/fueleconomy.dat";

    /*
    ** Compute statistics for all variables in the dataset
    ** The 'call' keyword disregards return values from the function
    */
    call  dstatmt(file_name);

The above example will print the following report to the program input/output window:

::

    ----------------------------------------------------------------------------------------
    Variable               Mean     Std Dev    Variance   Minimum   Maximum  Valid   Missing
    ----------------------------------------------------------------------------------------

    annual_fuel_cost      2.537     0.6533      0.4267     1.05      5.70     978        0
    engine_displacement   3.233      1.376       1.892     1.00      8.40     978        0

The code below uses the second input, *vars*, to compute only the descriptive statistics for
the second variable.

::

    // Create file name with full path
    file_name = getGAUSSHome() $+ "examples/fueleconomy.dat";

    // Only calculate statistics on the second variable
    vars = 2;

    // Compute statistics for only the second variable in the dataset
    call  dstatmt(file_name, vars);

The following report is printed to the program input/output window.

::

    ----------------------------------------------------------------------------------------
    Variable                Mean    Std Dev   Variance   Minimum   Maximum   Valid   Missing
    ----------------------------------------------------------------------------------------
    engine_displacement    3.233      1.376     1.892          1       8.4     978         0

Computing statistics on a csv dataset with formula string
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Create file name with full path
    file_name = getGAUSSHome() $+ "examples/binary.csv";

    // Set up a formula string with variables "gre" and "gpa"
    vars = "gre + gpa";

    /*
    ** Compute statistics for all variables in the dataset
    ** The 'call' keyword disregards return values from the function
    */
    call  dstatmt(file_name, vars);

The above example will print the following report to the program input/output window:

::

    --------------------------------------------------------------------------------
    Variable     Mean   Std Dev    Variance    Minimum     Maximum   Valid   Missing
    --------------------------------------------------------------------------------

    gre         587.7     115.5    1334e+04        220        800     400      0
    gpa          3.39    0.3806      0.1448       2.26          4     400      0

Using control and out structures
++++++++++++++++++++++++++++++++

::

    // Create file name with full path
    file_name = getGAUSSHome() $+ "examples/credit.dat";

    // Declare control structure and fill in with defaults
    struct dstatmtControl dctl;
    dctl = dstatmtControlCreate();

    // Do not print output to the screen
    dctl.output = 0;

    // Declare output structure
    struct dstatmtOut dout;

    // Calculate statistics on the 1st, 3rd and 6th variables
    vars = { 1, 3, 6 };

    // Calculate statistics, and place output in 'dout'
    dout = dstatmt(file_name, vars, dctl);

    // Print calculated means and variable names
    print dout.mean;
    print dout.vnames;

The code above should print the following output:

::

    45.218885
    354.94000
    13.450000

       Income
       Rating
    Education

Computing statistics on a matrix
++++++++++++++++++++++++++++++++

::

    // Set random number seed for repeatable random numbers
    rndseed 32452;

    // Create a random matrix on which to compute statistics
    X = rndn(10, 3);

    /*
    ** The empty string as the second input tells GAUSS to
    ** compute statistics on a matrix rather than a dataset
    */
    call dstatmt("", X);

The code above will print out the following report:

::

    -------------------------------------------------------------------------------
    Variable    Mean    Std Dev     Variance     Minimum    Maximum  Valid  Missing
    -------------------------------------------------------------------------------

    X1        0.2348     0.8164       0.6664     -1.0736      1.46     10       0
    X2       -0.5062      1.126        1.267      -2.223      1.269    10       0
    X3        0.5011     0.7758       0.6018     -0.6119      1.823    10       0

Computing statistics on a matrix, using structures
++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Set random number seed for repeatable random numbers
    rndseed 32452;

    // Declare control structure and fill with default values
    struct dstatmtControl dctl;
    dctl = dstatmtControlCreate();

    // Variable names for printed output
    dctl.altnames = "Alpha"$|"Beta"$|"Gamma";

    // Declare structure to hold output values
    struct dstatmtOut dout;

    // Create a random matrix on which to compute statistics
    X = rndn(10, 3);

    /*
    ** The empty string as the second input tells GAUSS to
    ** compute statistics on a matrix rather than a dataset
    */
    dout = dstatmt("", X, dctl);

This time, the following output will be printed to the screen:

::

    ------------------------------------------------------------------------------
    Variable     Mean    Std Dev    Variance    Minimum    Maximum  Valid  Missing
    ------------------------------------------------------------------------------

    Alpha      0.2348     0.8164      0.6664     -1.074      1.46      10       0
    Beta      -0.5062     1.1256       1.267     -2.223     1.269      10       0
    Gamma      0.5011     0.7758      0.6018    -0.6119     1.823      10       0

Remarks
-------

1. If pairwise deletion is used, the minima and maxima will be the true
   values for the valid data. The means and standard deviations will be
   computed using the correct number of valid observations for each
   variable.

2. For backwards compatiblitity, the following format is still
   supported:

   ::

      dout = dstatmt(dctl, dataset, vars);

   However, all new code should use one of the formats listed at the top
   of this document.

3. The supported dataset types are `CSV`, `XLS`, `XLSX`, `HDF5`, `FMT`, `DAT`, `DTA`


4. For `HDF5` files, the dataset must include a `file schema` and both file name and dataset name must be provided, e.g.
   :code:`dstatmt("h5://testdata.h5/mydata")`.

Source
------

dstatmt.src

.. seealso:: Functions :func:`dstatmtControlCreate`, `formula string`
