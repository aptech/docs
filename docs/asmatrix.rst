
asMatrix
==============================================

Purpose
----------------

Strips metadata from dataframe and returns matrix.

Format
----------------
.. function:: x_mat = asMatrix(x_meta)

    :param x_meta: data.
    :type x_meta: NxK matrix or dataframe.

    :return x_mat: data matrix.
    :rtype x_mat: NxK matrix


Examples
----------------

::

  // Load data
  fname = getGAUSSHome() $+ "examples/yarn.xlsx";
  yarn = loadd(fname, "cat(yarn_length) + cat(amplitude) + cat(load) + cycles");

  // Strip metadata from 'yarn' to return a matrix
  yarn_mat = asMatrix(yarn);

After the above code, the first five rows of *yarn* are equal to:

::

     yarn_length     amplitude        load     cycles
             low           low         low        674
             low           low         med        370
             low           low        high        292
             low           med         low        338
             low           med         med        266

while the first five rows of *yarn_mat* are equal to:

::

               1             1           1        674
               1             1           2        370
               1             1           0        292
               1             2           1        338
               1             2           2        266


The matrix does not have variable (column names) and the string category labels have been replaced by the integer key values for the labels in the original dataframe.

Remarks
--------------

* Date variables will be in Posix time (seconds since Jan 1, 1970).
* Categorical and string variables will be returned as the integer keys for the corresponding category.
* Numeric variables will be unchanged.
* Variable names will be removed.

.. seealso:: Functions :func:`asdf`, :func:`setcolnames`, :func:`setcoltypes`
