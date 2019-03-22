
dstatmt
==============================================

Purpose
----------------

Compute descriptive statistics.

Format
----------------
.. function:: dstatmt(dataset, vars, ctl)

    :param dataset: name of data set.
        
        If dataset is null or 0,
        vars will be assumed
        to be a matrix containing the data.
    :type dataset: string

    :param vars: the variables.
        
        If dataset contains the name of a
        data set, vars will be interpreted as:
        If dataset is null or 0, vars will be interpreted as:
    :type vars: Optional input

    .. csv-table::
        :widths: auto

        "Kx1 string array, names of variables."
        "- or -"
        "Kx1 numeric vector, indices of variables."
        "- or -"
        "formula string. e.g. "PAY + WT"  or ". - sex""

    :param ctl: instance of a dstatmtControl structure containing the following members:
    :type ctl: Optional input

    .. csv-table::
        :widths: auto

        "ctl.altnames", "Kx1 string array of alternate variable names to be used if a matrix in memory is analyzed (i.e., dataset is a null string or 0). Default = ""."
        "ctl.maxbytes", "scalar, the maximum numberof bytes to be read per iteration of the read loop. Default = 1e9."
        "ctl.vartype", "Scalar, unused in dstatmt."
        "ctl.miss", "scalar, default 0."
        "", "0", "there are no missing values (fastest)."
        "", "1", "listwise deletion, drop arow if any missings occur in it."
        "", "2", "pairwise deletion."
        "ctl.row", "scalar, the number of rows to readper iteration of the read loop.If 0, (default) the number of rows will becalculated using ctl.maxbytes andmaxvec."
        "ctl.output", "scalar, controls output, default 1."
        "", "1", "print output table."
        "", "0", "do not print output."
        "These can be any size subset of the variables inthe data set and can be in any order. If ascalar 0 is passed, all columns of the data setwill be used."
        "NxK matrix, the data on which to compute the descriptive"
        "statistics."

    :returns: dout (*struct*) instance of :class:`dstatmtOut` struct
        structure containing the following members:

    .. csv-table::
        :widths: auto

        "dout.vnames", "Kx1 string array, the names of the variablesused in the statistics."
        "dout.mean", "Kx1 vector, means."
        "dout.var", "Kx1 vector, variance."
        "dout.std", "Kx1 vector, standard deviation."
        "dout.min", "Kx1 vector, minima."
        "dout.max", "Kx1 vector, maxima."
        "dout.valid", "Kx1 vector, the number of valid cases."
        "dout.missing", "Kx1 vector, the number of missing cases."
        "dout.errcode", "scalar, error code, 0 if successful; otherwise, one of the following:"
        "", "2", "Can't open file."
        "", "7", "Too many missings - no data left after packing."
        "", "9", "altnames member ofdstatmtControl structure wrong size."
        "", "10", "vartype member ofdstatmtControl structure wrong size."

Examples
----------------

Computing statistics on a GAUSS dataset
+++++++++++++++++++++++++++++++++++++++

::

    //Create file name with full path
    file_name = getGAUSSHome() $+ "examples/fueleconomy.dat";
    
    //Compute statistics for all variables in the dataset
    //The 'call' keyword disregards return values from the function
    call  dstatmt(file_name);

The above example will print the following report to the program input/output window:

::

    -----------------------------------------------------------------------------------------------
    Variable                Mean     Std Dev     Variance     Minimum     Maximum   Valid   Missing
    -----------------------------------------------------------------------------------------------
    
    annual_fuel_cost      2.5371      0.6533       0.4267      1.0500      5.7000     978        0 
    engine_displacement   3.2333      1.3757       1.8925      1.0000      8.4000     978        0

The code below uses the second input, vars, to compute only the descriptive statistics for
the second variable.

::

    //Create file name with full path
    file_name = getGAUSSHome() $+ "examples/fueleconomy.dat";
    
    //Only calculate statistics on the second variable
    vars = 2;
    
    //Compute statistics for only the second variable in the dataset
    call  dstatmt(file_name, vars);

The following report is printed to the program input/output window.

::

    -----------------------------------------------------------------------------------------------
    Variable                 Mean     Std Dev    Variance     Minimum     Maximum   Valid   Missing
    -----------------------------------------------------------------------------------------------
    engine_displacement    3.2333      1.3757      1.8925      1.0000      8.4000     978         0

Computing statistics on a csv dataset with formula string
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    //Create file name with full path
    file_name = getGAUSSHome() $+ "examples/binary.csv";
    
    //Set up a formula string with variables "gre" and "gpa"
    vars = "gre + gpa"; 
    					
    //Compute statistics for all variables in the dataset
    //The 'call' keyword disregards return values from the function
    call  dstatmt(file_name, vars);

The above example will print the following report to the program input/output window:

::

    ----------------------------------------------------------------------------------------
    Variable        Mean     Std Dev      Variance     Minimum     Maximum     Valid Missing
    ----------------------------------------------------------------------------------------
    
    gre     587.7000    115.5165    13344.0702    220.0000    800.0000       400    0 
    gpa       3.3899      0.3806        0.1448      2.2600      4.0000       400    0

Using control and out structures
++++++++++++++++++++++++++++++++

::

    //Create file name with full path
    file_name = getGAUSSHome() $+ "examples/credit.dat";
    
    //Declare control structure and fill in with defaults
    struct dstatmtControl dctl;
    dctl = dstatmtControlCreate();
    
    //Do not print output to the screen
    dctl.output = 0;
    
    //Declare output structure
    struct dstatmtOut dout;
    
    //Calculate statistics on the 1st, 3rd and 6th variables
    vars = { 1, 3, 6 };
    
    //Calculate statistics, and place output in 'dout'
    dout = dstatmt(file_name, vars, dctl);
    
    //Print calculated means and variable names
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

    //Set random number seed for repeatable random numbers
    rndseed 32452;
    
    //Create a random matrix on which to compute statistics
    X = rndn(10,3);
    
    //The empty string as the second input tells GAUSS to
    //compute statistics on a matrix rather than a dataset
    call dstatmt("", X);

The code above will print out the following report:

::

    -----------------------------------------------------------------------------------
    Variable     Mean     Std Dev      Variance     Minimum     Maximum  Valid  Missing
    -----------------------------------------------------------------------------------
    
    X1         0.2348      0.8164        0.6664     -1.0736      1.4604     10       0 
    X2        -0.5062      1.1256        1.2669     -2.2231      1.2695     10       0 
    X3         0.5011      0.7758        0.6018     -0.6119      1.8235     10       0

Computing statistics on a matrix, using structures
++++++++++++++++++++++++++++++++++++++++++++++++++

::

    //Set random number seed for repeatable random numbers
    rndseed 32452;
    
    //Declare control structure and fill with default values
    struct dstatmtControl dctl;
    dctl = dstatmtControlCreate();
    
    //Variable names for printed output
    dctl.altnames = "Alpha"$|"Beta"$|"Gamma";
    
    //Declare structure to hold output values
    struct dstatmtOut dout;
    
    //Create a random matrix on which to compute statistics
    X = rndn(10,3);
    
    //The empty string as the second input tells GAUSS to
    //compute statistics on a matrix rather than a dataset
    dout = dstatmt("", X, dctl);

This time, the following output will be printed to the screen:

::

    -----------------------------------------------------------------------------------
    Variable     Mean     Std Dev      Variance     Minimum     Maximum  Valid  Missing
    -----------------------------------------------------------------------------------
    
    Alpha      0.2348      0.8164        0.6664     -1.0736      1.4604     10       0 
    Beta      -0.5062      1.1256        1.2669     -2.2231      1.2695     10       0 
    Gamma      0.5011      0.7758        0.6018     -0.6119      1.8235     10       0

Remarks
-------

-  If pairwise deletion is used, the minima and maxima will be the true
   values for the valid data. The means and standard deviations will be
   computed using the correct number of valid observations for each
   variable.
-  For backwards compatiblitity, the following format is still
   supported:

   ::

      dout = dstatmt(dctl, dataset, vars);

   However, all new code should use one of the formats listed at the top
   of this document.

-  The supported dataset types are
   ` <FIO.1-DelimitedTextFiles.html#data-source-csv>`__\ `CSV <FIO.1-DelimitedTextFiles.html#data-source-csv>`__,
   `Excel (XLS, XLSX) <FIO.3-Spreadsheets.html#data-source-excel>`__,
   `HDF5 <FIO.4-HDF5Files.html#data-source-hdf5>`__, `GAUSS Matrix
   (FMT) <FIO.6-GAUSSMatrixFiles.html#data-source-gauss-matrix>`__,
   `GAUSS Dataset
   (DAT) <FIO.5-GAUSSDatasets.html#data-source-gauss-dataset>`__, `Stata
   (DTA) and SAS (SAS7BDAT, SAS7BCAT) <FIO.4-SAS_STATADatasets.html>`__.
-  For HDF5 files, the dataset must include a `file
   schema <FIO.4-HDF5Files.html#schema-hdf5>`__ and both file name and
   data set name must be provided, e.g.
   dstatmt("h5://testdata.h5/mydata").

Source
------

dstatmt.src

.. seealso:: Functions :func:`dstatmtControlCreate`
`Formula String <LF.11-FormulaString.html#FormulaString>`__

descriptive statistics data handle
