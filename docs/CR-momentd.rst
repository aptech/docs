
momentd
==============================================

Purpose
----------------

Computes a moment (x'x) matrix from a GAUSS data set.

Format
----------------
.. function:: momentd(dataset, vars)

    :param dataset: name of data set.
    :type dataset: string

    :param vars: names of variables
        
        - or -Kx1 numeric vector, indices of columns.- or -Formula String. e.g. "PAY + WT"  or ". - 1"(include all variables besides intercept)These can be any size subset of the variables in the data set, and can be in any order. If a
        scalar 0 is passed, all columns of the data set will be used.
    :type vars: Kx1 string array

    :returns: m (*MxM matrix*), where M = K + __con, the moment matrix
        constructed by calculating X'X where X is the data, with or without a constant vector of ones.
        Error handling is controlled by the low order bit of the trap flag.

    .. csv-table::
        :widths: auto

        "trap 0    terminate with error message"
        "trap 1    return scalar error code in  m"
        "33   too many missings"
        "34   file not found"

Examples
----------------

Using indices of columns
++++++++++++++++++++++++

::

    fname = getGAUSShome() $+ "examples/freqdata.dat";	
    							
    //Calculate statistics on variables in dataset: PAY and WT
    //Specify the index of PAY and WT
    vars = 2|4;				
    m = momentd(fname, vars);
    
    print  m;

After the above code,

::

    400.00000        787.00000        587.98000 
    787.00000        1805.0000        1161.1400 
    587.98000        1161.1400        900.38540

Using names of variables
++++++++++++++++++++++++

::

    fname = getGAUSShome() $+ "examples/freqdata.dat";				
    //Calculate statistics on variables in dataset: PAY and WT
    //Define the names string array of PAY and WT				
    string vars = {"PAY", "WT"};				
    m = momentd(fname, vars );
    print  m;

After the above code,

::

    400.00000        787.00000        587.98000 
    787.00000        1805.0000        1161.1400 
    587.98000        1161.1400        900.38540

Using formula string
++++++++++++++++++++

::

    fname = getGAUSShome() $+ "examples/freqdata.dat";	
    //Define the formula for PAY and WT, remove the intercept (use - 1 )				
    formula_str = "-1 + PAY + WT";	
    										
    //Calculate statistics on variables in dataset: PAY and WT
    m = momentd(fname, formula_str);
    print  m;

After the above code,

::

    1805.0000        1161.1400 
    1161.1400        900.38540

Remarks
+++++++

-  The supported dataset types are
   ` <FIO.1-DelimitedTextFiles.html#data-source-csv>`__\ `CSV <FIO.1-DelimitedTextFiles.html#data-source-csv>`__,
   `Excel (XLS, XLSX) <FIO.3-Spreadsheets.html#data-source-excel>`__,
   `HDF5 <FIO.4-HDF5Files.html#data-source-hdf5>`__, `GAUSS Matrix
   (FMT) <FIO.6-GAUSSMatrixFiles.html#data-source-gauss-matrix>`__,
   `GAUSS Dataset
   (DAT) <FIO.5-GAUSSDatasets.html#data-source-gauss-dataset>`__, `Stata
   (DTA) and SAS (SAS7BDAT, SAS7BCAT) <FIO.4-SAS_STATADatasets.html>`__.
-  Character vectors are supported for backward compatibility, but it
   has been deprecated.

See also
++++++++

`Formula String <LF.11-FormulaString.html#FormulaString>`__

Source
------

momentd.src

dataset moment matrix
