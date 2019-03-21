
selif
==============================================

Purpose
----------------
Selects rows from a matrix. Those selected are the rows for which
there is a 1 in the corresponding row of  e.

Format
----------------
.. function:: selif(x, e)

    :param x: 
    :type x: NxK matrix or string array

    :param e: 
    :type e: Nx1 vector of 1's and 0's

    :returns: y (*TODO*), MxK matrix or string array consisting of the rows of x for
        which there is a 1 in the corresponding row of  e.

Examples
----------------

::

    y = selif(x,x[.,2] .gt 100);

This example selects all rows of x in which the second column is
greater than 100.

::

    let x[3,3] = 0 10 20
                30 40 50
                60 70 80;
    
    e =(x[.,1] .gt 0) .and (x[.,3] .lt 100);
    y = selif(x,e);

The resulting matrix y is:

::

    30 40 50
    60 70 80

All rows for which the element in column 1 is greater than 0 and the
element in column 3 is less than 100 are placed into the matrix y.

.. seealso:: Functions :func:`delif`, :func:`scalmiss`
