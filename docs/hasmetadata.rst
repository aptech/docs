
hasMetaData
==============================================

Purpose
----------------

Checks if a matrix has metadata.

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
  fname = getGAUSSHome() $+ "examples\\yarn.xlsx";
  yarn = loadd(fname, "cat(yarn_length) + cat(amplitude) + cat(load) + cycles");

  // Check for metadata
  has_meta = hasMetaData(yarn);

After the code above `has_meta=1` because *yarn* contains meta data.

.. seealso:: Functions :func:`setcolmetadata`
