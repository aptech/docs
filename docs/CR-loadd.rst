
loadd
==============================================

Purpose
----------------
Loads data from a dataset. The supported dataset types are CSV, Excel (XLS, XLSX), HDF5, GAUSS Matrix (FMT), GAUSS Dataset (DAT), Stata (DTA) and SAS (SAS7BDAT, SAS7BCAT).

Format
----------------
.. function:: loadd(dataset) 
			  loadd(dataset, varnames)

    :param dataset: name of dataset.
    :type dataset: string

    :param varnames: indicating which variable names to load from the data set
        E.g ".", include all variables;
        E.g.  "Income + Limit ", include "Income" and "Limit";
        E.g ". - Cards", '-' means exclude "Cards".
    :type varnames: Formula string

    :returns: y (*TODO*), NxK matrix of data.

Examples
----------------

Load all contents of a GAUSS data set
+++++++++++++++++++++++++++++++++++++

::

    //Create file name with full path
    file = getGAUSShome() $+ "examples/credit.dat";				
    
    //Load all rows from all columns of the dataset
    y = loadd(file);
    
    //Print the first three rows of 'y'
    print y[1:3,.];

After the above code, the following ouptut should be printed to the program input/output window.

::

    14.8910      3606.00      283.000      2.00000      34.0000 
    106.025      6645.00      483.000      3.00000      82.0000 
    104.593      7075.00      514.000      4.00000      71.0000

Load specified variables from a dataset
+++++++++++++++++++++++++++++++++++++++

::

    //Load all variables with a formula string
    dat1 = loadd(file, "." );
    
    //Load all observations of 'Balance' and 'Limit'
    dat2 = loadd(file, "Balance + Limit" );
    
    //Load all variables EXCEPT for 'Cards'
    dat3 = loadd(file, ". - Cards" );
    
    //Print first three rows of each matrix
    print  "All variables: " dat1[1:3,.];
    print  "Balance and Limit: " dat2[1:3,.];
    print  "All except Cards: " dat3[1:3,.];

After the above code,

::

    All variables: 
    
    14.891    3606.00    283.00    2.0000    34.000    11.000    1.0000    1.0000    2.0000    3.0000    333.000
    106.03    6645.00    483.00    3.0000    82.000    15.000    2.0000    2.0000    2.0000    2.0000    903.000
    104.59    7075.00    514.00    4.0000    71.000    11.000    1.0000    1.0000    1.0000    2.0000    580.000
    		
    Balance and Limit:
    
    333.000      3606.00 
    903.000      6645.00 
    580.000      7075.00 
    
    All except Cards: 
    
    14.8910    3606.00    283.00    34.000    11.000    1.0000    1.0000    2.0000    3.0000    333.000 
    106.025    6645.00    483.00    82.000    15.000    2.0000    2.0000    2.0000    2.0000    903.000 
    104.593    7075.00    514.00    71.000    11.000    1.0000    1.0000    1.0000    2.0000    580.000

Load all columns of a GAUSS matrix file, .fmt. No variable names are stored in .fmt files. GAUSS allows the use of 'X1, X2, X2...XP' to reference variables in a .fmt file.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    //Create a matrix
    x = rndn(10, 4);
    
    //Save to a matrix file, 'x.fmt'
    save x;
    
    //Load all columns of 'x.fmt'
    x_2 = loadd("x.fmt");

Load specified columns of a GAUSS matrix file, .fmt.
++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    //Create a matrix
    x = rndn(10, 4);
    
    //Save to a matrix file, 'x.fmt'
    save x;
    
    //Load columns 2 and 4 from 'x.fmt'
    x_2 = loadd("x.fmt", "X2 + X4");

Load three specified variables from a SAS dataset, .sas7bdat.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    new;
    cls;
    
    dataset = getGAUSSHome() $+ "examples/detroit.sas7bdat";
    
    //Create formula string specifying dependent and independent variables
    formula  = "homicide + unemployment + hourly_earn";
    
    y = loadd(dataset, formula);
    
    print "The dataset use is ";; dataset;
    print "The number of variables equals: ";; cols(y);
    print "The number of observations equals: ";; rows(y);

After the above code,

::

    The dataset use is C:\gauss18\examples\detroit.sas7bdat
    The number of variables equals:        3.0000000 
    The number of observations equals:        13.000000

Load a string date from a .csv file and automatically convert it to a Posix date/time (seconds since Jan 1, 1970).
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    dataset = getGAUSSHome() $+ "examples/yellowstone.csv";
    
    //Create formula string specifying that the column 'Date'
    //from 'yellowstone.csv' is a string column (by using $) and
    //that it should be loaded as a date with the 'date' keyword
    formula  = "date($Date)";
    
    //Load the date and convert to Posix date/time format
    dt_pos = loadd(dataset, formula);
    
    //Convert the first 5 dates to a string 'Month day, Year'
    //and print them
    print posixToStrc(dt_pos[1:5], "%B %d, %Y");

After the above code,

::

    January 01, 2016 
    January 01, 2015 
    January 01, 2014 
    January 01, 2013 
    January 01, 2012

Remarks
+++++++

-  Since loadd will load the entire dataset at once, the data set must
   be small enough to fit in memory. To read chunks of a dataset in an
   iterative manner, use dataopen and readr.
-  If dataset is a null string or 0, the data set temp.dat will be
   loaded.
-  To load a matrix file, use an .fmt extension on dataset.
-  The supported dataset types are
   ` <FIO.1-DelimitedTextFiles.html#data-source-csv>`__\ `CSV <FIO.1-DelimitedTextFiles.html#data-source-csv>`__,
   `Excel (XLS, XLSX) <FIO.3-Spreadsheets.html#data-source-excel>`__,
   `HDF5 <FIO.4-HDF5Files.html#data-source-hdf5>`__, `GAUSS Matrix
   (FMT) <FIO.6-GAUSSMatrixFiles.html#data-source-gauss-matrix>`__,
   `GAUSS Dataset
   (DAT) <FIO.5-GAUSSDatasets.html#data-source-gauss-dataset>`__, `Stata
   (DTA) and SAS (SAS7BDAT, SAS7BCAT) <FIO.4-SAS_STATADatasets.html>`__.
-  For HDF5 file, the dataset must include `file
   schema <FIO.4-HDF5Files.html#schema-hdf5>`__ and both file name and
   data set name must be provided, e.g.
   loadd("h5://C:/gauss17/examples/testdata.h5/mydata").

Source
++++++

saveload.src

See also
++++++++

`Formula
String <LF.11-FormulaString.html#FormulaString>`__\,\ `dataopen <CR-dataopen.html#dataopen>`__\,\ `getHeaders <CR-getHeaders.html#getHeaders>`__\,\ `readr <CR-readr.html#readr>`__\,\ `saved <CR-saved.html#saved>`__

Globals
+++++++

\__maxvec

.. raw:: html

   </div>
