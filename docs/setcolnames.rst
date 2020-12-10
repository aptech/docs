
setcolnames
==============================================

Purpose
----------------

Set column variable names.

Format
----------------
.. function:: x_meta = setColNames(X, varnames [, columns])

    :param X: data.
    :type X: NxK matrix or dataframe

    :param varnames: Names to apply to columns specified in *index*.
    :type varnames: Mx1 vector

    :param columns: Optional argument, indices of columns in *X* to be assigned names. Default = all columns.
    :type columns: Mx1 vector

    :return x_meta: Data with column names in *varnames* assigned to the columns in *columns*.
    :rtype x_meta: NxK dataframe


Examples
----------------

::

  x = { 1  15  15,
        5  19   8,
       16  14   4,
        7  19   6 };

  // Create new dataframe x_meta with the specified variable names
  x_meta = setColNames(x, "Planes"$|"Trains"$|"Automobiles");

  print x_meta;


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
  x_meta = setColNames(x_meta, "Airplanes", "Planes");


:: 

     Airplanes  Trains  Automobiles
             1      15           15
             5      19            8
            16      14            4
             7      19            6



.. seealso:: Functions :func:`getColNames`, :func:`setColMetadata`
