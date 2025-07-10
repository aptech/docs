vecndup
==============================================

Purpose
----------------
Picks out upper diagonal elements of a matrix (excluding the diagonal) and converts them into a column vector.

Format
----------------
.. function:: w = vecndup(r)

    :param r: Input matrix from which upper diagonal (excluding diagonal) elements are to be extracted.
    :type r: KxK matrix

    :return w: Column vector containing the upper diagonal elements of the input matrix, excluding the diagonal elements themselves.
    :rtype w: Kx1 vector

Example
----------------

::

    r = { 1 2 3,
          2 6 5,
          3 5 7 };

    w = vecndup(r);

After the above code, *w* equals:

::

    2
    3
    5

.. seealso:: :func:`vecdup`
