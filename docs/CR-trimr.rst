
trimr
==============================================

Purpose
----------------
Trims rows from the top and/or bottom of a matrix.

Format
----------------
.. function:: trimr(x,  t,  b)

    :param x: NxK matrix from which rows are to be trimmed.
    :type x: TODO

    :param t: scalar containing the number of rows which are
        to be removed from the top of x.
    :type t: TODO

    :param b: scalar containing the number of rows which are
        to be removed from the bottom of x.
    :type b: TODO

    :returns: y (*TODO*), RxK matrix where R=N-(t + b),
        containing the rows left after the trim.

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
