
conj
==============================================

Purpose
----------------

Returns the complex conjugate of a matrix.

Format
----------------
.. function:: conj(x)

    :param x: 
    :type x: NxK matrix

    :returns: y (*NxK matrix*), the complex conjugate of *x*.

Remarks
-------

Compare :func:`conj` with the transpose (``'``) operator.

Examples
----------------

::

    x = { 1+9i   2,
          4+4i   5i,
            7i 8-2i };
    y = conj(x);

::

    1 + 9i 2            1 - 9i 2
    x = 4 + 4i 0 + 5i   y = 4 - 4i 0 - 5i
        0 + 7i 8 - 2i       0 - 7i 8 + 2i

