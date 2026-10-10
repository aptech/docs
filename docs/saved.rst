
saved
==============================================

Purpose
----------------

Writes a matrix or dataframe to a dataset. GDAT v2 also saves structures,
strings, and arrays, including dataframe metadata inside structures.

.. note::

    GDAT v2 is an unreleased development feature. The v2 behavior below
    requires a development build with GDAT v2 support.

Format
----------------
.. function:: ret = saved(x, dataset [, vnames [, gdat_version]])

    :param x: data to save. GDAT v2 supports the additional values listed
        under :ref:`saved-gdat-v2`.
    :type x: NxK matrix or dataframe, or a supported GAUSS value for GDAT v2

    :param dataset: name of dataset. The type of file to create is inferred from the file extension.
        Valid file extensions include CSV, GDAT, DAT, XLS, XLSX.
    :type dataset: string

    :param vnames: Optional input, names for the columns of the dataset.
        If ``vnames`` is not passed in:

        - Dataframe variable names will be used.
        - Matrix data will be saved with variable names *X1, X2...XP*.

        For GDAT, pass 0 to keep these defaults. Explicit column names apply
        only to real, nonempty matrices and dataframes.
    :type vnames: string, Kx1 string array, or 0

    :param gdat_version: Optional, GDAT version: 2 (default) or 1 for a legacy
        table file readable by older GAUSS releases. This argument applies
        only to filenames with a ``.gdat`` extension.
    :type gdat_version: scalar

    :return ret: 1 if successful, otherwise 0. GDAT v2 failures raise a
        GAUSS runtime error instead of returning 0.

    :rtype ret: scalar


Examples
----------------

Save a dataframe with its metadata
++++++++++++++++++++++++++++++++++

::

    auto_data = loadd(getGAUSSHome("examples/auto2.dta"),
                     "str(make) + price + cat(foreign)");
    call saved(auto_data, "auto.gdat");
    auto_restored = loadd("auto.gdat");

GDAT v2 preserves column names and types, date display formats, and the
codes and labels for string and category columns, including unused labels.

Save a structure and load it back
+++++++++++++++++++++++++++++++++

::

    struct savedFit {
        matrix coefficients;
        matrix training_data;
    };

    struct savedFit fit_out, fit_restored;
    fit_out.coefficients = { 1.5, 0.25 };
    fit_out.training_data = asdf({ 10 1, 20 2, 30 3 }, "y" $| "x");

    call saved(fit_out, "fit.gdat");
    fit_restored = loadd("fit.gdat");

The dataframe metadata in ``training_data`` is retained. When loading the
file in another session, define or include the same ``savedFit`` structure
before declaring ``fit_restored``. See :func:`loadd` for loading an individual
member without loading the whole structure.

Save a table for an older GAUSS release
+++++++++++++++++++++++++++++++++++++++

::

    legacy_data = asdf({ 10 1, 20 2, 30 3 }, "y" $| "x");

    // Keep column names and write a GDAT v1 table
    call saved(legacy_data, "legacy.gdat", 0, 1);

Older GAUSS releases cannot read GDAT v2. Version 1 supports tables;
it cannot store structures, standalone strings, or N-dimensional arrays.

Save a dataframe to a CSV file
++++++++++++++++++++++++++++++

::

    // Load data from Stata dataset to GAUSS dataframe
    fname = getGAUSSHome("examples/auto2.dta");
    auto = loadd(fname, "str(make) + price + cat(foreign)");

    // Print the first 5 observations of the dataframe
    print auto[1:5,.];

The above code will print the first 5 observations from the  ``auto`` dataframe as shown below:

::

            make            price          foreign 
     AMC Concord        4099.0000         Domestic 
       AMC Pacer        4749.0000         Domestic 
      AMC Spirit        3799.0000         Domestic 
   Buick Century        4816.0000         Domestic 
   Buick Electra        7827.0000         Domestic

Now we can save this data to a CSV file with the :func:`saved` command.

::

    // Save the data 
    call saved(auto, "my_auto.csv");

The first four rows of the ``my_auto.csv`` will look like this:

::

    make,price,foreign
    AMC Concord,4099,Domestic
    AMC Pacer,4749,Domestic
    AMC Spirit,3799,Domestic


Save a matrix to a GAUSS .dat file with default variable names
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Create some data to save
    x = rndn(100, 3);

    // Create the GAUSS dataset, 'mydata.dat'
    // using default variable names X1, X2 and X3
    call saved(x, "mydata.dat");


Save a matrix to a GAUSS .dat file with specified variable names
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Continuing with the matrix created above, we can specify the variable names in the dataset as shown below:

::

    // Create a 3x1 string array containing the variable names
    vnames = "GDP" $| "Imports" $| "Exports";

    // Create the GAUSS dataset, 'mydata.dat'
    // with variable names GDP, Imports and Exports
    call saved(x, "mydata.dat", vnames);


Save data to a .xlsx file
+++++++++++++++++++++++++

To save the data to an Excel file, all we have to change is the file extension. Continuing with the data from the example above:

::

    // Create an Excel dataset, 'mydata.xlsx'
    call saved(x, "mydata.xlsx", vnames);

The variable names will be written as strings along the first row of the Excel file and the data will start in cell A2.

Save data to a .csv file
++++++++++++++++++++++++

To save the data to as a comma separated text file, all we have to change is the file extension. Continuing with the data from our first example:

::

    // Create a CSV dataset, 'mydata.csv'
    call saved(x, "mydata.csv", vnames);

Error checking
++++++++++++++

For formats that return 0 on failure, the return value can be checked as
shown below. GDAT v2 instead raises a runtime error if saving fails.

::

    x = rndn(100, 2);
    dataset = "mydata.dat";

    // Create a 2x1 string array containing the variable names
    vnames = "Price" $| "Quantity";

    // Check to see if save is successful. If not, report an error and end the program
    if not saved(x, dataset, vnames);
       errorlog "saved failed to write: "$+dataset;
       end;
    endif;

Remarks
-------

-  You can add variable names to a matrix with :func:`dfname`.
-  Use an explicit ``.gdat`` extension to select GDAT. A filename without an
   extension continues to select the legacy ``.dat`` format.

.. _saved-gdat-v2:

GDAT v2
+++++++

-  Supported values are structures and structure arrays (including nested
   structures), scalars, real or complex matrices and N-dimensional arrays,
   strings, string arrays, and real, nonempty dataframes.
-  A real, nonempty matrix saved as the top-level value is stored as a
   dataframe with column names. A scalar becomes a 1x1 dataframe. Matrix
   members inside structures retain their original metadata, if any.
-  Sparse matrices, complex or empty dataframes, and empty N-dimensional
   arrays are not supported. Empty matrices are supported.
-  Text must be valid UTF-8 without embedded NUL characters. Structure type
   and member names must use ASCII characters.
-  Saving replaces the whole file. An existing file is replaced only after
   the new file has been written successfully. In-place append and update
   through :func:`dataopen` are not supported for v2.
-  :func:`loadd` detects v1 and v2 automatically. Reading a v1 file does not
   convert it to v2; saving to ``.gdat`` uses v2 unless version 1 is specified.

CSV
+++

-  The line endings for CSV files on Windows will be ``\r\n`` and ``\n`` on Linux and macOS.
-  Fifteen digits of precision will be written.
-  :func:`csvWriteM` can be used to write CSV data with options to specify the
   separator to be something other than a comma, to control the line
   endings, or the precision to write the data.

DAT
+++

-  If *dataset* is null or 0, the dataset name will be :file:`temp.dat`.
-  If *vnames* is a null or 0, the variable names will begin with ``"X"`` and be numbered 1-K.
-  If *vnames* is a string or has fewer elements than *x* has columns, it will be expanded as explained under `create`.
-  The output data type is double precision.

Source
------

saveload.src

.. seealso:: Functions :func:`loadd`, :func:`writer`, `create`
