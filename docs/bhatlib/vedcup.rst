vecdup
==============================================

Purpose
----------------
Picks out upper diagonal elements of a matrix (including the diagonal) and converts them into a column vector.

Format
----------------
.. function:: w  = vecdup(r)

    :param r: Input matrix from which upper diagonal (including diagonal) elements are to be extracted.
    :type r: KxK matrix

    :return w: Column vector containing the upper diagonal elements of the input matrix.
    :rtype w: Kx1 vector

Example
----------------

::

    r = { 1 2 3,
          2 4 5,
          3 5 6 };

    w = vecdup(r);

After the above code, *w* equals:

::

    1
    2
    3
    4
    5
    6

.. seealso:: :func:`vecndup`

