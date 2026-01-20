
strrindx
==============================================

Purpose
----------------
Finds the index of one string within another string.
Searches from the end of the string to the beginning.

Format
----------------
.. function:: idx = strrindx(haystack, needle [, start])

    :param haystack: the string, string array or dataframe to be searched.
    :type haystack: string, scalar, string array, or dataframe where all column types are a string or category.

    :param needle: the substring to be searched for in *haystack*. Can be a scalar (applied to all elements), have the same number of rows as *haystack* (one-to-one matching), and can have one column or the same number of columns as *haystack*.
    :type needle: string, scalar, string array, or dataframe where all column types are a string or category.

    :param start: the starting point of the search in *haystack* for an occurrence of *needle*.
        *haystack* will be searched from this point backward for *needle*. Default is the end of the string
    :type start: scalar

    :return idx: contains the index of the last occurrence of *needle*, within *haystack*,
        which is less than or equal to *start*. If no occurrence is found, it will be 0.

    :rtype idx: scalar

Examples
-----------

::

    // Create a 3x1 string array
    state = "alaska" $|
            "alabama" $|
            "arkansas";

    // Find the first instance of the
    // letter 'a' starting from
    // the end of the string
    strrindx(state, "a");

Since the search starts from the back, the above code will print out:

::

       6.0000000
       7.0000000
       7.0000000

::

    // Find the first instance of the
    // letter 'a' starting from the
    // 5th character of the string
    strrindx(state, "a", 5);

This time, the search will start from the 5th character and continue searching towards the first character, resulting in:

::

       3.0000000
       5.0000000
       4.0000000


A negative value for *start* causes the search to begin at the end of the
string. An example of the use of :func:`strrindx` is extracting a file name from
a complete path specification:

::

   path = "/gauss/src/ols.src";
   ps = "/";
   pos = strrindx(path, ps, -1);
   if pos;
      name = strsect(path, pos+1, strlen(path)-pos);
   else;
      name = "";
   endif;

The above code makes the following assignments:

::

   pos = 11

   name = ols.src

Filtering files by extension
++++++++++++++++++++++++++++++

This example uses :func:`strrindx` with a dataframe to find which files have .csv or .dat extensions:

::

   // Create dataframe with filenames
   files = asDF("filename",
       "sales_data.csv" $|
       "backup.tar.gz" $|
       "prices.dat" $|
       "report.xlsx" $|
       "inventory.csv" $|
       "notes.txt");

   // Find position of last period in each filename
   dot_pos = strrindx(files[., "filename"], ".");

   // Extract file extension (everything after the last dot)
   extension = strsect(files[., "filename"], dot_pos + 1);

   // Find files that are .csv or .dat
   is_data_file = extension .$== "csv" .or extension .$== "dat";

   // Filter to only data files
   data_files = selif(files, is_data_file);
   print data_files;

The above code will print:

::

          filename
   sales_data.csv
       prices.dat
    inventory.csv

.. seealso:: Functions :func:`strindx`, :func:`strlen`, :func:`strsect`, :func:`strput`
