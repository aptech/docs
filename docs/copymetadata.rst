
copyMetadata
==============================================

Purpose
----------------

Copies metadata from dataframe to dataset.

Format
----------------
.. function:: x_meta = copyMetadata(X, src, [, columns])

    :param X: data.
    :type X:  NxK matrix

    :param src: Source of metadata.
    :type src:  MxJ matrix

    :param columns: The names or indices of columns to copy metadata from. Default = all.
    :type columns:  Lx1 vector or string array

    :return x_meta: Data in *X* with metadata from the specified *columns* in *src* attached.
    :rtype x_meta:  NxK dataframe


Examples
----------------

::

  // Set random seed for replication
  rndseed 80970;

  // Load data with metadata
  fname = getGAUSSHome $+ "examples/auto2.dta";
  auto2 = loadd(fname, "cat(rep78) + str(make)");

  // Generate random data
  X = rndi(150, 1, 1|5);

  // Copy metadata from 'rep78' in 'auto2' to 'X'
  X = copymetadata(X, auto2, "rep78");

The code above copies the metadata from the categorical variable *rep78* to the matrix *X*. After the code the first five rows of *x* look like:

::
  
                  Average
                  Poor
    X[1:5, .] =   Poor
                  Good
                  Fair


.. seealso:: Functions :func:`setColNames`, :func:`setColLabels`, :func:`setColtypes`, :func:`setColDateFormats`
