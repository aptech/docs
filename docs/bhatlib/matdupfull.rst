matdupfull
==============================================

Purpose
----------------
Takes a column vector of upper diagonal elements (including the diagonal) and converts it into a full symmetric matrix, including the diagonal of the matrix.

Format
----------------
.. function:: { w } = matdupfull(r)

    :param r: Input column vector containing the upper diagonal elements of a matrix, including the diagonal.
    :type r: Kx1 vector

    :return w: Output full symmetric matrix derived from the input vector. The size of the matrix *P* is determined by the formula *P=(-1+sqrt(1+8*K))/2*, where *K* is the length of the input vector.
    :rtype w: PxP matrix

Example
----------------

::

    // Define r as a column vector
    r = { 1, 2, 3, 4, 5, 6 };

    w = matdupfull(r);

After the above code, *w* equals:

::

    1 2 3
    2 4 5
    3 5 6

.. seealso:: :func:`vecdup`, :func:`vecndup`, :func:`matdup`

