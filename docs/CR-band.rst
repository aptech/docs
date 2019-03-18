
band
==============================================

Purpose
----------------
Extracts bands from a symmetric banded matrix.

Format
----------------
.. function:: band(y,  n)

    :param y: KxK symmetric banded matrix.
    :type y: TODO

    :param n: number of subdiagonals.
    :type n: scalar

    :returns: a (*TODO*), Kx(N+1) matrix, 1 subdiagonal per column.

Examples
----------------

::

    x = { 1 2 0 0,
          2 8 1 0,
          0 1 5 2,
          0 0 2 3 };
    
    //Extract only the principal diagonal
    b0 = band(x,0);
    
    //Extract the principal diagonal and the first subdiagonal
    b1 = band(x,1);
    
    //Extract the principal diagonal and the first two subdiagonals
    b2 = band(x,2);

After the code above:

::

    1       0  1       0  0  1
    b0 = 8  b1 = 2  8  b2 = 0  2  8
         5       1  5       0  1  5
         3       2  3       0  2  3

.. seealso:: Functions :func:`bandchol`, :func:`bandcholsol`, :func:`bandltsol`, :func:`bandrv`, :func:`bandsolpd`

extracts bands from a symmetric banded matrix band sparse spdiags
