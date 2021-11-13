
dfname
==============================================

Purpose
----------------

Set column variable names.

Format
----------------
.. function:: x_meta = dfname(x, varnames [, columns])

    :param X: data.
    :type X: NxK matrix or dataframe

    :param varnames: Names to apply to columns specified in *columns*.
    :type varnames: Mx1 vector

    :param columns: Optional argument, indices of columns in *X* to be assigned names. Default = all columns.
    :type columns: Mx1 vector

    :return x_meta: Data with column names in *varnames* assigned to the columns in *columns*.
    :rtype x_meta: NxK dataframe


Examples
----------------

Example 1: Convert a matrix to a dataframe and set variable names
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

  x = { 1  15  15,
        5  19   8,
       16  14   4,
        7  19   6 };

  // Create new dataframe x_meta with the specified variable names
  df_x = dfname(x, "Planes"$|"Trains"$|"Automobiles");

  print df_x;


The above code will print out:

::

     Planes  Trains  Automobiles
          1      15           15
          5      19            8
         16      14            4
          7      19            6


Below we change the name of an existing variable.

::

  // Change variable name of first column of x_meta
  df_x = dfname(df_x, "Airplanes", "Planes");


::

     Airplanes  Trains  Automobiles
             1      15           15
             5      19            8
            16      14            4
             7      19            6


Example 2: Convert a string array to a dataframe and set variable names
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

  // Create a 3x1 string array
  apples = "Gala" $| "Fuji" $| "Rome";

  // Create new dataframe
  apples = dfname(apples, "Variety");
  print apples;

The above code will print out:

::

   Variety
      Gala
      Fuji
      Rome
    

Now that ``apples`` is a dataframe, we can use the concatenation operators to combine it with a numeric variable.

::

    // Create a 3x1 vector
    n = { 437, 672, 231 };

    // Add a name to 'n' and combine with 'apples'
    apples = apples ~ dfname(n, "count");
    print apples;

::


   Variety    count
      Gala      437
      Fuji      672
      Rome      231



Remarks
-------

- :func:`dfname` will automatically convert string arrays to categorical variables matrices to datframes with numeric columns.
- To convert date strings to date variables, use :func:`asDate`.
- :func:`asdf` will also convert strings and numeric data to dataframes with the option to set the variable names.


.. seealso:: Functions :func:`getColNames`, :func:`asdf`, :func:`dfType`
