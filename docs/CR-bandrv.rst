
bandrv
==============================================

Purpose
----------------
Creates a symmetric banded matrix, given its compact form.

Format
----------------
.. function:: bandrv(a)

    :param a: KxN compact form matrix.
    :type a: TODO

    :returns: y (*TODO*), KxK symmetrix banded matrix.

Examples
----------------

::

    x = { 1 2 0 0,
          2 8 1 0,
          0 1 5 2,
          0 0 2 3 };
     
    //Create a version of 'x' in band format
    xBand = band(x,1);
     
    //Expand the banded version of 'x' back to a full matrix
    xNew = bandrv(xBand);

After the code above:

::

    0   1       1   2   0   0          1   2   0   0 
    xBand =  2   8   x = 2   8   1   0   xNew = 2   8   1   0 
             1   5       0   1   5   2          0   1   5   2 
             2   3       0   0   2   3          0   0   2   3

.. seealso:: Functions :func:`band`, :func:`bandchol`, :func:`bandcholsol`, :func:`bandltsol`, :func:`bandsolpd`

create symmetric banded matrix compact form
