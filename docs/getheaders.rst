
getHeaders
==============================================

Purpose
----------------

Returns the variable names in a dataset as a string array.

Format
----------------
.. function:: headers = getHeaders(fname)

    :param fname: the name of the data file.
    :type fname: string

    :return headers: contains the variable names in the file.

    :rtype headers: Px1 string array

Examples
----------------

Excel Data
++++++++++

::

    // Get file name with full path
    fname = getGAUSSHome() $+ "examples/yarn.xlsx";

    /*
    ** Read headers from the first row of the first
    ** sheet of the XLSX file
    */
    headers = getHeaders(fname);

After the above code, *headers* will contain:

::

    yarn_length
    amplitude
    load
    cycles

GAUSS dataset
+++++++++++++

::

    // Get file name with full path
    fname = getGAUSSHome() $+ "examples/fueleconomy.dat";

    // Read headers from the dataset
    headers = getHeaders(fname);

After the above code, *headers* will contain:

::

    annual_fuel_cost
    engine_displacement

Stata dataset
+++++++++++++

::

    // Get file name with full path
    fname = getGAUSSHome() $+ "examples/auto2.dta";

    // Read headers from the dataset
    headers = getHeaders(fname);

After the above code, *headers* will contain:

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

    // Get file name with full path
    fname = getGAUSSHome() $+ "examples/detroit.sas7bdat";

    // Read headers from the dataset
    headers = getHeaders(fname);

After the above code, *headers* will contain:

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

The supported dataset types are `CSV <FIO.1-DelimitedTextFiles.html>`_, `Excel (XLS, XLSX) <FIO.3-Spreadsheets.html>`_, `HDF5 <FIO.4-HDF5Files.html>`_ , `GAUSS Matrix (FMT) <FIO.6-GAUSSMatrixFiles.html>`_ , `GAUSS Dataset (DAT) <FIO.5-GAUSSDatasets.html>`_, `Stata (DTA) and SAS (SAS7BDAT, SAS7BCAT) <FIO.4-SAS_STATADatasets.html>`_.

Remarks
-------

For convenience, :func:`getHeaders` will try to read variable names from Excel
and CSV files. However, since these file types do not have a standard
method specification for variable names, the first row of the file will
be returned.

CSV file names with a file extension other than :file:`.csv` will need to start
with the schema ``csv://``.

HDF5 file names must start with the schema ``h5://``


.. seealso:: Functions :func:`csvReadSA`, :func:`dataopen`, :func:`getnamef`, :func:`loadd`, :func:`xlsReadSA`
