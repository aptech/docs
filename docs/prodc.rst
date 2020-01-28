
prodc
==============================================

Purpose
----------------

Computes the products of all elements in each column of a matrix.

Format
----------------
.. function:: y = prodc(x)

    :param x: data
    :type x: NxK matrix

    :return y: contains the products of all elements in each column of *x*.

    :rtype y: Kx1 matrix

Examples
----------------

::

    x = { 1 2 3,
          4 5 6,
          7 8 9 };

    y = prodc(x);

The code above assigns *y* to be equal to:

::

         28
    y =  80
        162

Remarks
-------

To find the products of the elements in each row of a matrix, transpose
before applying :func:`prodc`. If *x* is complex, use the bookkeeping transpose
(``.'``).

To find the products of all of the elements in a matrix, use the :func:`vecr`
function before applying :func:`prodc`.


.. seealso:: Functions :func:`sumc`, :func:`meanc`, :func:`stdc`
