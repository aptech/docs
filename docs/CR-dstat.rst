
dstat
==============================================

Purpose
----------------

Computes descriptive statistics.

Format
----------------
.. function:: dstat(dataset, vars)

    :param dataset: name of data set.
        
        If  dataset is null or 0, vars will be assumed
        to be a matrix containing the data.
    :type dataset: string

    :param vars: 
        
        If  dataset contains the name of a  data set,vars will be interpreted as:
    :type vars: the variables

    .. csv-table::
        :widths: auto

        "Kx1 character vector, names of variables."
        "- or -"
        "Kx1 numeric vector, indices of variables."
        "- or -"
        "formula string. e.g. "PAY + WT"  or ". - sex""
        "These can be any size subset of the variables in the data set and can be in any order. If a scalar 0 is passed, all columns of the data set will be used.    If  dataset is null or 0, vars will be interpreted as:"
        "NxK matrix, the data on which to compute the descriptive statistics."

    :returns: vnam (*Kx1 character vector*), the names of the variables
        used in the statistics.

    :returns: mean (*Kx1 vector*), means.

    :returns: var (*Kx1 vector*), variance.

    :returns: std (*Kx1 vector*), standard deviation.

    :returns: min (*Kx1 vector*), minima.

    :returns: max (*Kx1 vector*), maxima.

    :returns: valid (*Kx1 vector*), the number of valid cases.

    :returns: mis (*Kx1 vector*), the number of missing cases.

Examples
----------------

Calculate statistics on all variables in dataset
++++++++++++++++++++++++++++++++++++++++++++++++

::

    file = getGAUSShome() $+ "examples/freqdata.dat";				
    //Calculate statistics on all variables in dataset: AGE, PAY, sex and WT
    vars = 0;
    { vnam, mean, var, std, min, max, valid, mis } = dstat(file, vars);

After the above code,

::

    -------------------------------------------------------------------------------
    Variable       Mean   Std Dev    Variance   Minimum   Maximum     Valid Missing
    -------------------------------------------------------------------------------
    AGE           -----     -----       -----    1.0000   10.0000       400    0
    PAY          1.9675    0.8019      0.6431    1.0000    3.0000       400    0
    sex           -----     -----       -----     -----     -----       400    0
    WT           1.4699    0.3007      0.0904    1.0000    1.9900       400    0

//Calculate statistics on just AGE and PAY
vars = { AGE, PAY };
{ vnam, mean, var, std, min, max, valid, mis } = dstat(file, vars);
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

After the above code,

::

    -------------------------------------------------------------------------------
    Variable       Mean   Std Dev    Variance   Minimum   Maximum     Valid Missing
    -------------------------------------------------------------------------------
    AGE           -----     -----       -----    1.0000   10.0000       400    0
    PAY          1.9675    0.8019      0.6431    1.0000    3.0000       400    0

//Calculate statistics on just AGE and PAY using numerical indices
vars = { 1, 2 }; 
{ vnam, mean, var, std, min, max, valid, mis } = dstat(file, vars);
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

After the above code,

::

    -------------------------------------------------------------------------------
    Variable       Mean   Std Dev    Variance   Minimum   Maximum     Valid Missing
    -------------------------------------------------------------------------------
    AGE           -----     -----       -----    1.0000   10.0000       400    0
    PAY          1.9675    0.8019      0.6431    1.0000    3.0000       400    0

//Calculate statistics on just AGE and PAY using __miss
vars = { 1, 2 }; 
//Drop rows with missing values				
__miss = 1;
{ vnam, mean, var, std, min, max, valid, mis } = dstat(file, vars);
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

After the above code,

::

    -------------------------------------------------------------------------------
    Variable       Mean   Std Dev    Variance   Minimum   Maximum     Valid	 Missing
    -------------------------------------------------------------------------------
    AGE          5.6784    2.9932      8.9593    1.0000   10.0000       398    2
    PAY          1.9623    0.8006      0.6409    1.0000    3.0000       398    2

//Calculate statistics using formula string and  __miss
//Set up a formula string with all variables exclude "sex"
vars = ". - sex"; 
//Drop rows with missing values				
__miss = 1;
{ vnam, mean, var, std, min, max, valid, mis } = dstat(file, vars);
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

After the above code,

::

    -------------------------------------------------------------------------------
    Variable       Mean   Std Dev    Variance   Minimum   Maximum     Valid Missing
    -------------------------------------------------------------------------------
    AGE          5.6784    2.9932      8.9593    1.0000   10.0000       398    2
    PAY          1.9623    0.8006      0.6409    1.0000    3.0000       398    2
    WT           1.4713    0.3009      0.0906    1.0000    1.9900       398    2

Remarks
-------

1. If pairwise deletion is used, the minima and maxima will be the true
values for the valid data. The means and standard deviations will be
computed using the correct number of valid observations for each
variable.

2. The supported data set types are
`CSV <FIO.1-DelimitedTextFiles.html#data-source-csv>`__,
`XLS <FIO.3-Spreadsheets.html#data-source-excel>`__,
`XLSX <FIO.3-Spreadsheets.html#data-source-excel>`__,
`HDF5 <FIO.4-HDF5Files.html#data-source-hdf5>`__,
`FMT <FIO.6-GAUSSMatrixFiles.html#data-source-gauss-matrix>`__,
`DAT <FIO.5-GAUSSDatasets.html#data-source-gauss-dataset>`__.

For HDF5 file, the dataset must include `file
schema <FIO.4-HDF5Files.html#schema-hdf5>`__ and both file name and data
set name must be provided, e.g.
dstat("h5://C:/gauss17/examples/testdata.h5/mydata", formula).

See also
++++++++

`Formula String <LF.11-FormulaString.html#FormulaString>`__

Source
------

dstat.src



Global Input
------------

\__altnam



matrix, default 0.

This can be a Kx1 character vector of alternate variable names for the
output.

\__maxbytes

scalar, the maximum number of bytes to be read per iteration of the read
loop. Default = 1e9.

\__maxvec

scalar, the largest number of elements allowed in any one matrix.
Default = 20000.

\__miss

scalar, default 0.

 

0

there are no missing values (fastest).

 

1

listwise deletion, drop a row if any missings occur in it.

 

2

pairwise deletion.

\__row

scalar, the number of rows to read per iteration of the read loop.

if 0, (default) the number of rows will be calculated using \__maxbytes
and \__maxvec.

\__output

scalar, controls output, default 1.

 

1

print output table.

 

0

do not print output.