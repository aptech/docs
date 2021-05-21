
setcolmetadata
==============================================

Purpose
----------------

Set columns in a matrix to have variable names and types.

Format
----------------
.. function:: x_meta = setColMetadata(X, varnames, types)

    :param X: data.
    :type X: NxK matrix

    :param varnames: Names to apply to column in *X*.
    :type varnames: Kx1 string array

    :param types: Specifies types to be assigned to names in *varnames*. Valid options include: 0: string, 1: number, 2: categorical 3: date.
    :type types: Kx1 vector

    :return x_meta: Data with column names in *varnames* and types in *types* assigned to the columns.
    :rtype x_meta: NxK dataframe


Note
---------

The following variables are equal to their corresponding values in the description of *types* above:

* META_TYPE_STRING
* META_TYPE_NUMBER
* META_TYPE_CATEGORY
* META_TYPE_DATE

They may be used as shown in the example below.


Examples
----------------

::

  // We will interpret the first column as a posix date
  // meaning the number of seconds since Jan 1, 1970
  x = { 1e6 23,
        1e7 19 };

  // Specify types
  types = META_TYPE_DATE | META_TYPE_NUMBER;

  // Specify variable names
  varnames = "Departure"$|"Age";

  // Assign variable names to all three columns
  // and create new matrix x_meta
  x_meta = setColMetadata(x, varnames, types);

  print x_meta;


The above code will print:

::

       Departure    Age
      1970-01-12     23
      1970-04-26     19



.. seealso:: Functions :func:`setColNames`, :func:`setColLabels`, :func:`setColTypes`, :func:`setColDateFormats`
