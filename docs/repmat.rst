
repmat
==============================================

Purpose
----------------
Tiles (repeats) a matrix to create a larger matrix.

Format
----------------
.. function:: B = repmat(A, m, n)

    :param A: matrix to tile.
    :type A: RxC matrix

    :param m: number of times to tile vertically.
    :type m: scalar

    :param n: number of times to tile horizontally.
    :type n: scalar

    :return B: containing *m* x *n* copies of *A*.

    :rtype B: (R*m)x(C*n) matrix

Examples
----------------

Tile a matrix into a 2x3 grid
++++++++++++++++++++++++++++++++++++++++++++

::

    A = { 1 2,
          3 4 };

    B = repmat(A, 2, 3);

After the above code, ``B`` will equal:

::

    1 2 1 2 1 2
    3 4 3 4 3 4
    1 2 1 2 1 2
    3 4 3 4 3 4

Repeat a column vector across columns
++++++++++++++++++++++++++++++++++++++++++++

::

    v = { 10, 20, 30 };

    B = repmat(v, 1, 4);

After the above code, ``B`` will equal:

::

    10 10 10 10
    20 20 20 20
    30 30 30 30

Stack a row vector vertically
++++++++++++++++++++++++++++++++++++++++++++

::

    r = { 1 2 3 };

    B = repmat(r, 3, 1);

After the above code, ``B`` will equal:

::

    1 2 3
    1 2 3
    1 2 3

Remarks
-------

:func:`repmat` uses the Kronecker product to tile the input matrix. It is equivalent to::

    B = ones(m, n) .*. A;

.. seealso:: Functions :func:`reshape`, :func:`ones`, :func:`zeros`
