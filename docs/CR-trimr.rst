
trimr
==============================================

Purpose
----------------
Trims rows from the top and/or bottom of a matrix.

Format
----------------
.. function:: trimr(x, t, b)

    :param x: 
    :type x: NxK matrix from which rows are to be trimmed

    :param t: 
    :type t: scalar containing the number of rows which are
        to be removed from the top of x

    :param b: 
    :type b: scalar containing the number of rows which are
        to be removed from the bottom of x

    :returns: y (*TODO*), RxK matrix where R=N-(t + b),
        containing the rows left after the trim.

Remarks
-------

If either t or b is zero, then no rows will be trimmed from that end of
the matrix.


Examples
----------------

::

    //Create a 5x3 matrix of random uniform numbers
    x = rndu(5,3);
    
    //Remove the top 2 rows of x and the bottom row
    y = trimr(x,2,1);

If x is equal to:

::

    0.780 0.922 0.864
    0.151 0.687 0.947
    0.271 0.014 0.060
    0.054 0.084 0.526
    0.880 0.278 0.199

then y will equal:

::

    0.271 0.014 0.060
    0.054 0.084 0.526

.. seealso:: Functions :func:`submat`, :func:`rotater`, :func:`shiftr`
