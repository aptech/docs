
spTrTDense
==============================================

Purpose
----------------
Multiplies a sparse matrix transposed by a dense matrix.

Format
----------------
.. function:: y = spTrTDense(s, d)

    :param s: data
    :type s: NxM sparse matrix

    :param d: data
    :type d: NxL dense matrix

    :return y: the result of :math:`s'\*d`.

    :type y: MxL dense matrix

Remarks
-------

This may also be accomplished by the following code:

::

   y = s'*d;

However, :func:`spTrTDense` will be more efficient.

.. seealso:: Functions :func:`spTScalar`

