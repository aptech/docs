
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

  // Strip metadata
  yarn_mat = asMatrix(yarn);

.. seealso:: Functions :func:`setcolmetadata`
