
Data Import and Export
===========================

General data loading
-------------------------

.. note:: :doc:`../loadd` and :doc:`../saved` are recommended for most cases when working with the following file types:

          * GAUSS, SAS, Stata and SPSS datasets.
          * CSV and Excel files with variable names in the first row.

======================       ====================================================================================
:doc:`../getheaders`            Returns the variable names from a dataset as a string array.
:doc:`../loadd`                 Loads data into a GAUSS dataframe. The supported dataset types are CSV, Excel (XLS, XLSX), HDF5, GAUSS Matrix (FMT), GAUSS Dataset (DAT), Stata (DTA) and SAS (SAS7BDAT, SAS7BCAT).
:doc:`../saved`                 Writes a matrix or dataframe in memory to a dataset in a specified format.
======================       ====================================================================================


CSV and delimited text files
------------------------------

======================       ====================================================================================
:doc:`../csvreadm`              Reads numeric data from a CSV file into a GAUSS matrix.
:doc:`../csvreadsa`             Reads data from a CSV file into a GAUSS string array.
:doc:`../csvwritem`             Write the contents of a GAUSS matrix to a CSV file.
======================       ====================================================================================


Spreadsheets (Excel files)
------------------------------

===========================       ====================================================================================
:doc:`../xlsgetsheetcount`        Returns the number of sheets in an Excel® spreadsheet.
:doc:`../xlsgetsheetsize`         Returns the size (rows and columns) of a specified sheet in an Excel® spreadsheet.
:doc:`../xlsgetsheettypes`        Gets the cell format types of a row in an Excel® spreadsheet.
:doc:`../xlsmakerange`            Builds an Excel® range string from a row/column pair.
:doc:`../xlsreadm`                Reads from an Excel® spreadsheet into a GAUSS matrix.
:doc:`../xlsreadsa`               Reads from an Excel® spreadsheet into a GAUSS string array.
:doc:`../xlswrite`                Writes a GAUSS matrix, string, or string array to an Excel® spreadsheet.
===========================       ====================================================================================

HDF 5 files
-------------------

==========================       ====================================================================================
:doc:`../h5create`                Create a HDF5 dataset (.h5).
:doc:`../h5open` 	                Open a HDF5 file.
:doc:`../h5read`                  Reads data from a HDF5 file (.h5) into a GAUSS matrix.
:doc:`../h5readattribute`         Read attributes from a HDF5 file into GAUSS.
:doc:`../h5write`                 Writes a GAUSS matrix to a HDF5 file.
==========================       ====================================================================================

GAUSS Data Sets
-------------------

These are the main functions to use for loading and saving GAUSS datasets.

======================       ====================================================================================
:doc:`../loadd`                  Loads a data set into a GAUSS dataframe.
:doc:`../saved`                  Saves matrices or dataframes to a variety of dataset types.
======================       ====================================================================================


The following functions use file handles which enable reading and writing partial chunks of a dataset.

======================       ====================================================================================
:doc:`../close`                  Closes an open data set (.dat file).
:doc:`../closeall`               Closes all open data sets.
:doc:`../datacreate`             Creates a file handle to a new, empty GAUSS data set.
:doc:`../dataopen`               Opens a file handle to a GAUSS data set.
:doc:`../eof`                    Tests for end of file.
:doc:`../getnr`                  Computes number of rows to read per iteration for a program that reads data from a disk file in a loop.
:doc:`../getnrmt`                Computes number of rows to read per iteration for a program that reads data from a disk file in a loop.
:doc:`../readr`                  Reads rows from open data set.
:doc:`../seekr`                  Moves pointer to specified location in open data set.
:doc:`../tempname`               Creates a temporary file with a unique name.
:doc:`../typef`                  Returns the element size (2, 4 or 8 bytes) of data in open data set.
:doc:`../writer`                 Writes matrix to a GAUSS dataset using open file handle.
======================       ====================================================================================



Databases
-------------

Database Setup
+++++++++++++++++++++++++++

==============================       ====================================================================================
:doc:`../dbadddatabase`              Adds a database to the list of database connections using the driver type or a connection URL.
:doc:`../dbgetdrivers`               Returns a list of available database drivers.
:doc:`../dbisdriveravailable`        Returns 1 if a specified database driver is available.
:doc:`../dbremovedatabase`           Removes a database connection from the list of open database connections. Frees all related resources.
==============================       ====================================================================================

Database Properties
+++++++++++++++++++++++++++

===================================       ====================================================================================
:doc:`../dbgetconnectoptions`              Returns the connection options string used for a database connection.
:doc:`../dbgetdatabasename`                Returns the name of the database.
:doc:`../dbgetdrivername`                  Returns the name of the connection's database driver.
:doc:`../dbgethostname`                    Returns the database connection's host name.
:doc:`../dbgetpassword`                    Returns a connection's password.
:doc:`../dbgetnumericalprecpolicy`         Returns the default numerical precision policy for a specified database connection.
:doc:`../dbgetport`                        Returns the database connection's port number if it has been set.
:doc:`../dbisopen`                         Reports whether a specified database connection is open.
:doc:`../dbisvalid`                        Reports whether a specified database connection has a valid driver.
:doc:`../dbsetconnectoptions`              Sets database-specific options.
:doc:`../dbsetdatabasename`                Sets the connection's database name to name.
:doc:`../dbsethostname`                    Sets the specified database connection's host name.
:doc:`../dbsetnumericalprecpolicy`         Sets the default numerical precision policy used by queries created on this database connection.
:doc:`../dbsetpassword`                    Sets the database connection's password.
:doc:`../dbsetport`                        Sets the specified database connection's port number.
===================================       ====================================================================================

Database Information
+++++++++++++++++++++++++++

=============================       ====================================================================================
:doc:`../dbgetprimaryindex`          Returns the primary index for the specified table.
:doc:`../dbgettableheaders`          Returns a string array populated with the names of all the fields in a specified table (or view).
:doc:`../dbgettables`                Returns the database's tables, system tables and views.
:doc:`../dbhasfeature`               Returns a 1 if the database supports the specified feature.
=============================       ====================================================================================

Database Errors
+++++++++++++++++++++++++++

===================================       ====================================================================================
:doc:`../dbgetlasterrornum`                Returns numerical information about the last error that occurred on the database.
:doc:`../dbgetlasterrortext`               Returns text information about the last error that occurred on the database.
:doc:`../dbisopenerror`                    Reports whether an error occurred while attempting to open the database connection.
:doc:`../dbquerygetlasterrornum`           Returns numerical error information about the last error that occurred (if any) with the last executed query.
:doc:`../dbquerygetlasterrortext`          Returns text error information about the last error that occurred (if any) with the last executed query.
===================================       ====================================================================================

Database Connect
+++++++++++++++++++++++++++

===========================       ====================================================================================
:doc:`../dbclose`                    Closes a database connection and destroys any remaining queries.
:doc:`../dbopen`                     Opens a specified database connection using the current connection values.
===========================       ====================================================================================

Database Transaction
+++++++++++++++++++++++++++

===========================       ====================================================================================
:doc:`../dbcommit`                   Commits a transaction to the database if the driver supports transactions and a dbTransaction() has been started.
:doc:`../dbcreatequery`              Process an SQL statement and prepare a query.
:doc:`../dbexecquery`                Executes an SQL statement and creates a query.
:doc:`../dbrollback`                 Rolls back a transaction on the database.
:doc:`../dbtransaction`              Begins a transaction on the database.
===========================       ====================================================================================

Query Building
+++++++++++++++++++++++++++

===============================       ====================================================================================
:doc:`../dbquerybindvalue`            Set the placeholder placeholder to be bound to value val in the prepared statement.
:doc:`../dbquerygetboundvalue`        Returns the value for a placeholder in a query.
:doc:`../dbquerygetboundvalues`       Returns an Nx2 string array containing the placeholders and their corresponding values in a query.
:doc:`../dbqueryexecprepared`         Executes a previously created and prepared query.
:doc:`../dbqueryprepare`              Prepares a SQL query for execution.
===============================       ====================================================================================

Query Manipulation
+++++++++++++++++++++++++++

===========================       ====================================================================================
:doc:`../dbqueryclear`               Clears the result set and releases any resources held by the query. Sets the query state to inactive.
:doc:`../dbqueryfinish`              Instructs the database driver that no more data will be fetched from this query until it is re-executed.
===========================       ====================================================================================

Query Information
+++++++++++++++++++++++++++

===================================       ====================================================================================
:doc:`../dbquerycols`                      Returns the number of fields in the record.
:doc:`../dbquerygetlastinsertid`           Returns the object ID of the most recent inserted row if supported by the database.
:doc:`../dbquerygetlastquery`              Returns the text of the current query being used.
:doc:`../dbquerygetnumrowsaffected`        Reports the number of rows affected by the result's SQL statement.
:doc:`../dbqueryisactive`                  Returns 1 if the query is active.
:doc:`../dbqueryisforwardonly`             Reports whether you can only scroll forward through a result set.
:doc:`../dbqueryisnull`                    Reports whether the current field pointed at by an active query positioned on a valid record is NULL.
:doc:`../dbqueryisselect`                  Reports whether the specified query is a SELECT statement.
:doc:`../dbqueryisvalid`                   Reports whether the specified query is positioned on a valid record.
:doc:`../dbqueryrows`                      Returns the size of the result (number of rows returned), or -1 if the size cannot be determined or if the database does not support reporting information about query sizes.
:doc:`../dbquerysetforwardonly`            Sets forward only mode to forward. If forward is true, only :doc:`../dbQuerySeekNext` and :doc:`../dbQuerySeek` with positive values, are allowed for navigating the results.
===================================       ====================================================================================

Query Iteration
+++++++++++++++++++++++++++

==============================       ====================================================================================
:doc:`../dbquerygetposition`         Returns the current internal position of the query.
:doc:`../dbqueryseek`                Retrieves the record at a specified position, if available, and positions the query on the retrieved record.
:doc:`../dbqueryseekfirst`           Retrieves the first record in the result, if available, and positions the query on the retrieved record.
:doc:`../dbqueryseeklast`            Retrieves the last record in the result, if available, and positions the query on the retrieved record.
:doc:`../dbqueryseeknext`            Retrieves the next record in the result, if available, and positions the query on the retrieved record.
:doc:`../dbqueryseekprevious`        Retrieves the previous record in the result, if available, and positions the query on the retrieved record.
==============================       ====================================================================================

Query Data Retrieval
+++++++++++++++++++++++++++

=============================       ====================================================================================
:doc:`../dbqueryfetchallm`           Returns the result set for the current query as a matrix.
:doc:`../dbqueryfetchallsa`          Returns the result set for the current query as a string array.
:doc:`../dbqueryfetchonem`           Returns a single row as an Nx1 matrix where N is the column count of the SELECT statement.
:doc:`../dbqueryfetchonesa`          Returns a single row as a string vector containing the field information for the current query.
:doc:`../dbquerygetfield`            Returns the value of a specified field in the current record.
=============================       ====================================================================================


General text file manipulation
-----------------------------------

To read and write data from CSV and delimited text files, see the earlier section.

====================       ====================================================================================
:doc:`../fcheckerr`           Gets the error status of a file.
:doc:`../fclearerr`           Gets the error status of a file, then clears it.
:doc:`../fflush`              Flushes a file's output buffer.
:doc:`../fgets`               Reads a line of text from a file.
:doc:`../fgetsa`              Reads lines of text from a file into a string array.
:doc:`../fgetsat`             Reads lines of text from a file into a string array without retaining newlines.
:doc:`../fgetst`              Reads a line of text from a file without retaining the newline.
:doc:`../fopen`               Opens a file.
:doc:`../fputs`               Writes strings to a file.
:doc:`../fputst`              Writes strings followed by a newline to a file.
:doc:`../fseek`               Positions the file pointer in a file.
:doc:`../fstrerror`           Returns an error message explaining the cause of the most recent file I/O error.
:doc:`../ftell`               Gets the position of the file pointer in a file.
:doc:`../getf`                Loads an ASCII or binary file into a string.
:doc:`../putf`                Writes the contents of a string to a file.
====================       ====================================================================================
