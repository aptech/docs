
getHeaders
==============================================

Purpose
----------------

Returns the variable names in a dataset as a string array. 

Format
----------------
.. function:: getHeaders(fname)

    :param fname: the name of the data file.
    :type fname: string

    :returns: headers (*Px1 string array*) containing the variable names in the file.

Remarks
-------

For convenience, :func:`getHeaders` will try to read variable names from Excel
and CSV files. However, since these file types do not have a standard
method specification for variable names, the first row of the file will
be returned.

CSV file names with a file extension other than ``.csv`` will need to start
with the schema ``csv://``.

HDF5 file names must start with the schema ``h5://``


Examples
----------------

Excel Data
++++++++++

::

    // Get file name with full path
    fname = getGAUSSHome() $+ "examples/yarn.xlsx";
     
    // Read headers from the first row of the first
    // sheet of the XLSX file
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

The supported dataset types are CSV, Excel (XLS, XLSX), HDF5, GAUSS Matrix (FMT), GAUSS Dataset (DAT), Stata (DTA) and SAS (SAS7BDAT, SAS7BCAT).

.. DANGER:: Link up references

.. seealso:: Functions :func:`csvReadSA`, :func:`dataopen`, :func:`getnamef`, :func:`loadd`, :func:`xlsReadSA`

