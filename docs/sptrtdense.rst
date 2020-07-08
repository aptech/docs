
spTrTDense
==============================================

Purpose
----------------
Multiplies a sparse matrix transposed by a dense matrix.

Format
----------------
.. function:: y = spTrTDense(s, d)

    :param s: sparse data matrix.
    :type s: NxM sparse matrix

    :param d: dense data matrix.
    :type d: NxL dense matrix

    :return y: the result of :math:`s\*d`.

    :rtype y: MxL dense matrix


Examples
---------

::

  sparse matrix s;

  // Create a 4x4 sparse identity matrix
  s = spEye(4);

  // Create dense matrix
  d = rndn(4, 4);

  y =  spTrTDense(s, d);

Remarks
----------
This may also be accomplished by the following code:

::

    y = s'*d;

However, :func:`spTrTDense` will be more efficient.

.. seealso:: Functions :func:`spTScalar`

