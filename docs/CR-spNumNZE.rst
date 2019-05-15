
spNumNZE
==============================================

Purpose
----------------
Returns the number of non-zero elements in a sparse matrix.

Format
----------------
.. function:: spNumNZE(x)

    :param x: data
    :type x: MxN sparse matrix

    :returns: n (*scalar*), the number of non-zero elements in *x*.

Examples
----------------

::

    sparse matrix y;
    x = { 0 0 0 10,
          0 2 0  0,
          0 0 0  0,
          5 0 0  0,
          0 0 0  3 };
          
     y = denseToSp(x, 0);
     n = spNumNZE(y);
     print "The number of nonzeros is" n;

::

    4.00

.. seealso:: Functions :func:`spGetNZE`

