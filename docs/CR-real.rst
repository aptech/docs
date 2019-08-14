
real
==============================================

Purpose
----------------
Returns the real part of *x*.

Format
----------------
.. function:: zr = real(x)

    :param x: data
    :type x: NxK matrix or N-dimensional array

    :return zr: the real part of *x*.

    :type zr: NxK matrix or N-dimensional array

Remarks
-------

If *x* is not complex, *zr* will be equal to *x*.

Examples
----------------

::

    x = {  1 11+2i,
           7i 3,
         2+1i 1 };
    zr = real(x);

After the code above, *x* and *zr* are equal to:

::

        1+0i  11+2i       1 11
    x = 0+7i   3+0i  zr = 0  3
        2+1i   1+0i       2  1

.. seealso:: Functions :func:`complex`, :func:`imag`

