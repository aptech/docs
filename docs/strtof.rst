
strtof
==============================================

Purpose
----------------
Converts a string array to a numeric matrix, or a categorical / string column of a dataframe to a numeric column.

Format
----------------
.. function:: x = strtof(sa)

    :param sa: numeric data.
    :type sa: NxK string array

    :return x: converted string array.

    :rtype x: NxK matrix

Examples
----------------


Example 1: Convert a string dataframe column to a numeric variable
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Our first step will be to create a dataframe with one variable that contains numbers inside of strings. 

::

    // Create a 3x1 string array
    sa = "0.9" $| "2.3" $| "1.7"; 

    // Convert the string array to a dataframe
    // with one variable named "GDP"
    df_sa = asdf(sa, "GDP"); 

    print df_sa;

The above code will print:

::

             GDP 
             0.9 
             2.3 
             1.7 

Our next step will be to convert the string labels in this dataframe to real numbers with :func:`strtof`:

::

    // Convert the strings to real numbers
    df_num = strtof(df_sa[.,"GDP"]);

    print df_num;

The above code will print the following output, showing us that the data is now numeric.

::

             GDP
      0.90000000
       2.3000000
       1.7000000


Example 2: Convert a string array to a numeric matrix
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Create a string array
    string sa = { "1.1" "2.2" "3.3",
                  "4.4" "5.5" "6.6" };
    num = strtof(sa);

After the code above, ``num`` is a numeric matrix with the following values:

::

    1.100  2.200 3.300
    4.400  5.500 6.600

Remarks
-------

Elements with more than one numerical character separated by a delimiter
such as a comma or a space will be interpreted as complex data. For
example, the string:
::

   "1.2 1.9"

will be converted into the number:

::

   1.2 + 1.9i

Parentheses surrounding the numerical elements in the string will be
ignored as will be a following *i*. The following strings will be
interpreted as the same by :func:`strtof`.

::

   "(2.31 4.72)""2.31 4.73""2.31,4.73i"

.. seealso:: Functions :func:`strtofcplx`, :func:`ftostrC`
