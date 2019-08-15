
csvReadM
==============================================

Purpose
----------------
Reads data from CSV file into a GAUSS matrix.

Format
----------------
.. function:: mat = csvReadM(file[, row_range[, col_range[, delimiter]]])

    :param file: name of CSV file.
    :type file: string

    :param row_range: Optional input: The first element of *row_range* will specify the
        first row of the file to read. If there is a second element in *row_range*,
        it will specify the last row to read from the file. If there is no second
        element in *row_range*, GAUSS will read to the end of the file. If *row_range*
        is not passed in, all rows will be read from the file. Default = 1.
    :type row_range: scalar or 2x1 matrix

    :param col_range: Optional input. The first element of *col_range* will specify the
        first column of the file to read. If there is a second element in *col_range*,
        it will specify the last column to read from the file. If there is no second
        element in *col_range*, GAUSS will read to the end of the file. If *col_range*
        is not passed in, all columns will be read from the file. Default = 1.
    :type col_range: scalar or 2x1 matrix

    :param delimiter: Optional input. The character used to separate elements in the file. Examples include:

        - space ``" "``
        - tab ``"\t"``
        - semi-colon ``";"``
        - comma ``","`` (Default)

    :type delimiter: string

    :return mat: data read from the CSV file.

    :rtype mat: matrix

Remarks
------------

The standard input stream (stdin) can be read with :func:`csvReadM` by passing
in `__STDIN` as the filename input. Note that `__STDIN` should not be
passed as a string, surrounded by quotes. Correct usage is shown below:

::

   x = csvReadM(__STDIN);

Examples
----------------

Basic Example
+++++++++++++

Read all contents from the file :file:`housing.csv` located in your GAUSS examples directory.

::

    // Get file name with full path
    file = getGAUSSHome() $+ "examples/housing.csv";

    // Read entire contents of 'housing.csv'
    housing = csvReadM(file);

    // Print the first 5 rows of all columns
    print housing[1:5, .];

The code above will produce the following output. Notice that the first row contains all missing values.
This is because the first row of the file :file:`housing.csv` contains a header. :func:`csvReadM` reads in textual
data as missing values by default. You can easily remove any rows that contain all missing values with
the function :func:`packr` (which stands for "pack rows").

::

          .          .          .          .          .          .
    3104.00       4.00       2.00       0.00     279.90    2048.00
    1173.00       2.00       1.00       0.00     146.50     912.00
    3076.00       4.00       2.00       0.00     237.70    1654.00
    1608.00       3.00       2.00       0.00     200.00    2068.00

Skip the header
+++++++++++++++

In the previous example, we read the header in as numeric data and got missing values.
In this example, we will skip the first row to avoid reading the header as numeric data.

::

    // Create file name with full path
    file = getGAUSSHome() $+ "examples/housing.csv";

    /*
    ** Row range will be from line 2 to the end of the file
    ** since no end to the range is specified.
    */
    row_range = 2;

    // Load the data from row 2 to the end of the file into 'housing'
    housing = csvReadM(file, row_range);

    // Print the first 5 rows of all columns
    print housing[1:5, .];

After the code above, housing should equal:

::

    3104.00       4.00       2.00       0.00     279.90    2048.00
    1173.00       2.00       1.00       0.00     146.50     912.00
    3076.00       4.00       2.00       0.00     237.70    1654.00
    1608.00       3.00       2.00       0.00     200.00    2068.00
    1454.00       3.00       3.00       0.00     159.90    1477.00

Read from a row range
+++++++++++++++++++++

::

    // Create file name with full path
    file = getGAUSSHome() $+ "examples/housing.csv";

    // Row range will be from line 3 to line 5
    row_range = { 3, 5 };

    // Load the data from rows 3 to 5 of the file into 'housing'
    housing = csvReadM(file, row_range);

    // Print the entire contents of the variable 'housing'
    print housing;

After the code above, housing should equal:

::

    1173.00       2.00       1.00       0.00     146.50     912.00
    3076.00       4.00       2.00       0.00     237.70    1654.00
    1608.00       3.00       2.00       0.00     200.00    2068.00

Read all rows of a range of columns
+++++++++++++++++++++++++++++++++++

::

    // Create file name with full path
    file = getGAUSSHome() $+ "examples/housing.csv";

    // Row range from the first line to the end of the file
    row_range = 1;

    // Read only columns 2 through 4
    col_range = { 2, 4 };

    // Load the data from columns 2 through 4 into 'x'
    x = csvReadM(file, row_range, col_range);

Read all rows of one specific column
++++++++++++++++++++++++++++++++++++

::

    // Create file name with full path
    file = getGAUSSHome() $+ "examples/housing.csv";

    // Row range from the first line to the end of the file
    row_range = 1;

    // Read only the 3rd column
    col_range = { 3, 3 };

    // Load the data from the 3rd column into 'x'
    x = csvReadM(file, row_range, col_range);

Read all rows and all cols, with specified delimiter
++++++++++++++++++++++++++++++++++++++++++++++++++++

Enter 1 for the *row_range* and *col_range* if you want to read all contents of a file, but need to specify the field delimiter.

::

    x = csvReadM("myfile.csv", 1, 1, ";");

Specify full path to file
+++++++++++++++++++++++++

Windows

::

    x = csvReadM("C:\\mydata\\myfile.csv");

.. NOTE:: Notice that double backslashes are needed inside of a string on Windows

macOS

::

    x = csvReadM("/Users/MyUserName/myfile.csv");

Linux

::

    x = csvReadM("/home/my_user/myfile.csv");

.. seealso:: Functions :func:`csvReadSA`, :func:`xlsWrite`, :func:`xlsWriteM`, :func:`xlsWriteSA`, :func:`xlsGetSheetCount`, :func:`xlsGetSheetSize`, :func:`xlsGetSheetTypes`, :func:`xlsMakeRange`
