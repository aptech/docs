
Data Import and Export
===========================

General data loading
-------------------------

======================       ====================================================================================
:func:`loadd`                Loads data into a GAUSS dataframe. The supported dataset types are CSV, Excel (XLS, XLSX), HDF5, GAUSS Matrix (FMT), GAUSS Dataset (DAT), Stata (DTA) and SAS (SAS7BDAT, SAS7BCAT).
:func:`saved`                Writes a matrix or dataframe in memory to a dataset in a specified format.
======================       ====================================================================================


CSV and delimited text files
------------------------------

======================       ====================================================================================
:func:`csvReadM`             Reads numeric data from a CSV file into a GAUSS matrix.
:func:`csvReadSA`            Reads data from a CSV file into a GAUSS string array.
:func:`csvWriteM`            Write the contents of a GAUSS matrix to a CSV file.
======================       ====================================================================================


Spreadsheets (Excel files)
------------------------------


======================       ====================================================================================
:func:`xlsGetSheetCount`     Returns the number of sheets in an Excel® spreadsheet.
:func:`xlsGetSheetSize`      Returns the size (rows and columns) of a specified sheet in an Excel® spreadsheet.
:func:`xlsGetSheetTypes`     Gets the cell format types of a row in an Excel® spreadsheet.
:func:`xlsMakeRange`         Builds an Excel® range string from a row/column pair.
:func:`xlsReadM`             Reads from an Excel® spreadsheet into a GAUSS matrix.
:func:`xlsReadSA`            Reads from an Excel® spreadsheet into a GAUSS string array.
:func:`xlsWrite`             Writes a GAUSS matrix, string, or string array to an Excel® spreadsheet.
======================       ====================================================================================
