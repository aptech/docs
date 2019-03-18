
getHeaders
==============================================

Purpose
----------------

Returns the variable names in a dataset as a string array. 

Format
----------------
.. function:: getHeaders(fname)

    :param fname: the name of the data file.
    :type fname: String

    :returns: headers (*TODO*), Px1 string array containing the variable names in the file.

Examples
----------------

Excel Data
++++++++++

::

    //Get file name with full path
    fname = getGAUSSHome() $+ "examples/yarn.xlsx";
     
    //Read headers from the first row of the first
    //sheet of the XLSX file
    headers = getHeaders(fname);

After the above code, 'headers' will contain:

::

    yarn_length     
    amplitude   
    load   
    cycles

GAUSS dataset
+++++++++++++

::

    //Get file name with full path
    fname = getGAUSSHome() $+ "examples/fueleconomy.dat";
     
    //Read headers from the dataset
    headers = getHeaders(fname);

After the above code, 'headers' will contain:

::

    annual_fuel_cost 
    engine_displacement

Stata dataset
+++++++++++++

::

    //Get file name with full path
    fname = getGAUSSHome() $+ "examples/auto2.dta";
     
    //Read headers from the dataset
    headers = getHeaders(fname);

After the above code, 'headers' will contain:

::

    make
    price
    mpg
    rep78
    headroom
    trunk
    weight
    length
    turn
    displacement
    gear_ratio
    foreign

SAS dataset
+++++++++++

::

    //Get file name with full path
    fname = getGAUSSHome() $+ "examples/detroit.sas7bdat";
     
    //Read headers from the dataset
    headers = getHeaders(fname);

After the above code, 'headers' will contain:

::

    year
    ft_police
    unemployment
    manufacture_employ
    gun_license
    gun_registration
    homicide_clearance
    num_white_males
    non_manufacture_employ
    govt_employ
    hourly_earn
    weekly_earn
    homicide
    accident_death
    assault

` <FIO.1-DelimitedTextFiles.html#data-source-csv>`__
`CSV <FIO.1-DelimitedTextFiles.html#data-source-csv>`__, `Excel (XLS,
XLSX) <FIO.3-Spreadsheets.html#data-source-excel>`__,
`HDF5 <FIO.4-HDF5Files.html#data-source-hdf5>`__, `GAUSS Matrix
(FMT) <FIO.6-GAUSSMatrixFiles.html#data-source-gauss-matrix>`__, `GAUSS
Dataset (DAT) <FIO.5-GAUSSDatasets.html#data-source-gauss-dataset>`__,
`Stata (DTA) and SAS (SAS7BDAT,
SAS7BCAT) <FIO.4-SAS_STATADatasets.html>`__.

.. seealso:: Functions :func:`csvReadSA`, :func:`dataopen`, :func:`getnamef`, :func:`loadd`, :func:`xlsReadSA`
