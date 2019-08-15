
saved
==============================================

Purpose
----------------

Writes a matrix in memory to a GAUSS data set in a specified format on disk.

Format
----------------
.. function:: ret = saved(x, dataset, vnames)

    :param x: data to save
    :type x: NxK matrix

    :param dataset: name of data set. The type of file to create is inferred from the file extension. 
        Valid file extensions include CSV, DAT, XLS, XLSX.
    :type dataset: string

    :param vnames: names for the columns of the data set.
    :type vnames: string or Kx1 character vector

    :return ret: 1 if successful, otherwise 0.

    :rtype ret: scalar

Remarks
-------

**CSV**

-  The line endings for CSV files on Windows will be '``\r\n``' and '``\n``' on Linux and macOS.
-  Fifteen digits of precision will be written.
-  :func:`csvWriteM` can be used to write CSV data with options to specify the
   separator to be something other than a comma, to control the line
   endings, or the precision to write the data.

**DAT**

-  If *dataset* is null or 0, the data set name will be *temp.dat*.
-  If *vnames* is a null or 0, the variable names will begin with "X" and be numbered 1-K.
-  If *vnames* is a string or has fewer elements than *x* has columns, it will be expanded as explained under `create`.
-  The output data type is double precision.

Examples
----------------

Save data to a GAUSS .dat file
++++++++++++++++++++++++++++++

::

    // Create some data to save
    x = rndn(100,3);
    
    // Create a 3x1 string array containing the variable names
    vnames = "GDP" $| "Imports" $| "Exports";
    
    // Create the GAUSS dataset, 'mydata.dat'
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

The return value of :func:`saved` can be used to check whether the data set save was successful. The example below checks the return value and creates an error if the save fails.

::

    x = rndn(100,2);
    dataset = "mydata.dat";
    
    // Create a 2x1 string array containing the variable names
    vnames = "Price" $| "Quantity";
     
    // Check to see if save is successful. If not, report an error and end the program
    if not saved(x,dataset,vnames);
       errorlog "saved failed to write: "$+dataset;
       end;
    endif;

Source
------

saveload.src

.. seealso:: Functions :func:`loadd`, :func:`writer`, `create`

