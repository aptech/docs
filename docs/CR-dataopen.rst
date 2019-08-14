
dataopen
==============================================

Purpose
----------------

Opens a data set.

Format
----------------
.. function:: fh = dataopen(filename, mode)

    :param filename: name of data file.
    :type filename: string

    :param mode: containing one of the following:

        .. csv-table::
            :widths: auto

            "read", "Open file for read only."
            "append", "Open file for append. The file pointer will start at the end of the file to add new rows."
            "update", "Open file for update. Allows reading and writing. The file pointer will start at the first row."

    :type mode: string

    :returns: **fh** (*scalar*) - file handle.

Remarks
-------

1. The **file must exist before it can be opened** with the :func:`dataopen`
command (to create a new file, see :func:`datacreate` or :func:`datasave`).

2. The file handle returned by :func:`dataopen` is a scalar containing a
positive integer value that uniquely identifies each file. This value is
assigned by GAUSS when the `create`, :func:`datacreate`, :func:`datacreatecomplex`, `open`
or :func:`dataopen` commands are executed. The file handle is used to reference
the file in the commands :func:`readr` and :func:`writer`. If :func:`dataopen` fails, it returns
a -1.

3. A file can be opened simultaneously under more than one handle. If
the value that is in the file handle when the :func:`dataopen` command begins to
execute matches that of an already open file, the process will be
aborted and a ``File already open`` error message will be given. This gives
you some protection against opening a second file with the same handle
as a currently open file. If this happens, you would no longer be able
to access the first file.

4. It is important to set unused file handles to zero because both
:func:`dataopen` and :func:`datacreate` check the value that is in a file handle to see
if it matches that of an open file before they proceed with the process
of opening a file. You may set unused file handles to zero with the
`close` or :func:`closeall` commands.

5. If filename does not have an extension, :func:`dataopen` appends a .dat
extension before searching for the file. If the file is an ``.fmt`` matrix
file, the extension must be explicitly given. If no path information is
included, then :func:`dataopen` searches for the file in the current directory.

6. Files opened in read mode cannot be written to. The pointer is set to
the beginning of the file and the :func:`writer` function is disabled for files
opened in this way. This is the only mode available for matrix files
(``.fmt``), which are always written in one piece with the `save` command.

7. Files opened in append mode cannot be read. The pointer is set to the
end of the file so that a subsequent write to the file with the :func:`writer`
function will add data to the end of the file without overwriting any of
the existing data in the file. The :func:`readr` function is disabled for files
opened in this way. This mode is used to add additional rows to the end
of a file.

8. Files opened in update mode can be read from and written to. The
pointer is set to the beginning of the file. This mode is used to make
changes in a file.

9. The supported data set types are ``.dat``, ``.h5``, ``.fmt``.

For HDF5 files, the dataset must include schema and both file name and
data set name must be provided, e.g.

::

    glm("h5://C:/gauss/examples/testdata.h5/mydata").

Examples
----------------

Read from a GAUSS dataset
+++++++++++++++++++++++++

::

    // Create a file name with full path
    file_name = getGAUSSHome() $+ "examples/credit.dat";

    // Open file handle to dataset and assign it to 'fh'
    fh = dataopen(file_name, "read");

    // Read 100 rows from the dataset into the variable 'y'
    y = readr(fh, 100);

    // Close file handle
    ret = close(fh);


Write to a GAUSS dataset
++++++++++++++++++++++++

::

   // Create variable names for dataset
   var_names = "alpha" $| "beta";

   // Create dataset containing 2 variables with 5 observations all equal to 1
   x = ones(5, 2);
   call saved(x, "my_ones.dat", var_names);

   // Open file handle to dataset and assign it to 'fh'
   fh = dataopen("my_ones.dat", "update");

   // Write to the first row
   y = { 17 21 };
   call writer(fh, y);

   // Close file handle
   ret = close(fh);

   // Load all contents of dataset
   new_x = loadd("my_ones.dat");

After the code above, *new_x* should be equal to:

::

   17 21
    1  1
    1  1
    1  1
    1  1

Source
------

datafile.src

.. seealso:: Functions `open`, :func:`datacreate`, :func:`getHeaders`, :func:`writer`, :func:`readr`
