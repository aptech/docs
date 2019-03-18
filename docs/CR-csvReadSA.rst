
csvReadSA
==============================================

Purpose
----------------
Reads data from CSV file into a GAUSS string array.

Format
----------------
.. function:: csvReadSA(file,  row_range,  col_range, delimiter)

    :param file: name of CSV file.
    :type file: string

    .. csv-table::
        :widths: auto

        ""

    :param row_range: Optional input: scalar, or 2x1 matrix. The first element of row_range will specify the first row of the file to read. If there is a second element in row_range, it will specify the last row to read from the file. If there is no second element in row_range, GAUSS will read to the end of the file. If row_range is not passed in, all rows will be read from the file. Default = 1.
    :type row_range: TODO

    .. csv-table::
        :widths: auto

        ""

    :param col_range: Optional input: scalar, or 2x1 matrix. The first element of col_range will specify the first column of the file to read. If there is a second element in col_range, it will specify the last column to read from the file. If there is no second element in col_range, GAUSS will read to the end of the file. If col_range is not passed in, all columns will be read from the file. Default = 1.
    :type col_range: TODO

    .. csv-table::
        :widths: auto

        ""

    :param delimiter: Optional input: string. The character used to separate elements in the file. Examples include:
        space " "tab "\t"semi-colon ";"comma "," (Default)
    :type delimiter: TODO

    :returns: s (*string array*), data read from the CSV file.

    .. csv-table::
        :widths: auto

        ""

    :returns: row_range (*TODO*), Optional input: scalar, or 2x1 matrix. The first element of row_range will specify the first row of the file to read. If there is a second element in row_range, it will specify the last row to read from the file. If there is no second element in row_range, GAUSS will read to the end of the file. If row_range is not passed in, all rows will be read from the file. Default = 1.

    .. csv-table::
        :widths: auto

        ""

    :returns: col_range (*TODO*), Optional input: scalar, or 2x1 matrix. The first element of col_range will specify the first column of the file to read. If there is a second element in col_range, it will specify the last column to read from the file. If there is no second element in col_range, GAUSS will read to the end of the file. If col_range is not passed in, all columns will be read from the file. Default = 1.

    .. csv-table::
        :widths: auto

        ""

    :returns: delimiter (*TODO*), Optional input: string. The character used to separate elements in the file. Examples include:
        space " tab "\t"semi-colon ";"comma "," (Default)

Examples
----------------

Basic Example
+++++++++++++

Read all contents from the file myfile.csv located in your current GAUSS working directory.

::

    s = csvReadSA("myfile.csv");

Read From a Row Range
+++++++++++++++++++++

::

    //Row range will be from line 1 to line 25
    row_range = { 1, 25 };
    
    //Load the data from rows 1 to 25 into 's'
    s = csvReadSA("myfile.csv", row_range);

Read all rows from a range of columns
+++++++++++++++++++++++++++++++++++++

::

    //Row range from the first line to the end of the file
    row_range = 1;
    
    //Read only columns 2 though 7
    col_range = { 2, 7 };
    
    //Load the data from columns 2 through 7 into 's'
    s = csvReadSA("myfile.csv", row_range, col_range);

Read all rows from one column
+++++++++++++++++++++++++++++

::

    //Row range from the first line to the end of the file
    row_range = 1;
    
    //Read only column 4
    col_range = { 4, 4 };
    
    //Load the data from column 4 into 's'
    s = csvReadSA("myfile.csv", row_range, col_range);

Specify full path to file
+++++++++++++++++++++++++

Windows: Notice that double backslashes are needed inside of a string.

::

    s = csvReadSA("C:\\mydata\\myfile.csv");

Mac

::

    s = csvReadSA("/Users/MyUserName/myfile.csv");

Linux

::

    s = csvReadSA("/home/my_user/myfile.csv");

Remarks
+++++++

The standard input stream (stdin) can be read with csvReadSA by passing
in \__STDIN as the filename input. Note that \__STDIN should not be
passed in as a string. Corrrect usage is shown below:

::

   x = csvReadSA(__STDIN);

.. seealso:: Functions :func:`csvReadM`, :func:`getHeaders`, :func:`xlsReadM`, :func:`xlsReadSA`, :func:`xlsWrite`
