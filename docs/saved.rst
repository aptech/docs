
saved
==============================================

Purpose
----------------

Writes a matrix or dataframe in memory to a dataset in a specified format.

Format
----------------
.. function:: ret = saved(x, dataset [, vnames])

    :param x: data to save
    :type x: NxK matrix or dataframe

    :param dataset: name of dataset. The type of file to create is inferred from the file extension.
        Valid file extensions include CSV, GDAT, DAT, XLS, XLSX.
    :type dataset: string

    :param vnames: Optional input, names for the columns of the dataset. If ``vnames`` is not passed in:

                   - Dataframe variable names will be used.
                   - Matrix data will be saved with variable names *X1, X2...XP*.
    :type vnames: string or Kx1 string array.

    :return ret: 1 if successful, otherwise 0.

    :rtype ret: scalar


.. NOTE:: GDAT files are the new standard GAUSS dataset format. They allow you to save dataframes with string, category and date columns.

Examples
----------------

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

The return value of :func:`saved` can be used to check whether the dataset save was successful. The example below checks the return value and creates an error if the save fails.

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

**CSV**

-  The line endings for CSV files on Windows will be ``\r\n`` and ``\n`` on Linux and macOS.
-  Fifteen digits of precision will be written.
-  :func:`csvWriteM` can be used to write CSV data with options to specify the
   separator to be something other than a comma, to control the line
   endings, or the precision to write the data.

**DAT**

-  If *dataset* is null or 0, the dataset name will be :file:`temp.dat`.
-  If *vnames* is a null or 0, the variable names will begin with ``"X"`` and be numbered 1-K.
-  If *vnames* is a string or has fewer elements than *x* has columns, it will be expanded as explained under `create`.
-  The output data type is double precision.

Source
------

saveload.src

.. seealso:: Functions :func:`loadd`, :func:`writer`, `create`
