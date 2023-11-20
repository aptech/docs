
hasMetaData
==============================================

Purpose
----------------

Checks if a matrix has metadata, meaning it is a dataframe.

Format
----------------
.. function:: has_meta = hasMetaData(x)

    :param x: data.
    :type x: NxK matrix or dataframe.

    :return has_meta: Indicator variable representing whether a matrix has metadata.
    :rtype has_meta: Scalar


Examples
----------------

::

  // Load data
  fname = getGAUSSHome("examples/yarn.xlsx");
  yarn = loadd(fname, "cat(yarn_length) + cat(amplitude) + cat(load) + cycles");

  // Check for metadata
  has_meta = hasMetaData(yarn);

After the code above `has_meta=1` because *yarn* contains meta data.


::

    // Create numeric matrix
    x = rndn(10,3);

    // Check to see if 'x' is a dataframe
    is_df = hasMetaData(x);

After the code above `is_df=0` because *x* is a numeric matrix and does not contain meta data.

.. note:: Column (or variable) names are meta data, so a dataframe with all numeric variables will still have meta data. 


.. seealso:: Functions :func:`setcolmetadata`

