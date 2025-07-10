matndup
==============================================

Purpose
----------------
Takes a column vector of upper diagonal elements and converts it into a matrix, with diagonal elements being the square root of (1 minus the sum of the squares of non-diagonal elements in each column).

Format
----------------
.. function:: { w } = matndup(r)

    :param r: Input column vector containing the upper diagonal elements of a matrix.
    :type r: Kx1 vector

    :return w: Output matrix derived from the input vector. The size of the matrix *P* is determined by the formula *P=(1+sqrt(1+8*K))/2*, where *K* is the length of the input vector. Diagonal elements are calculated as the square root of (1 minus the sum of the squares of non-diagonal elements in each column).
    :rtype w: PxP matrix

Example
----------------

::

    // Define r as a column vector
    r = { 0.6, 0.5, 0.5 };

    w = matndup(r);

After the above code, *w* equals:

::

    1 0.6 0.5
    0 0.8 0.5
    0 0.0 0.7071

The resulting matrix *w* such that *w'w* is a correlation matrix.

.. seealso:: :func:`vecdup`, :func:`vecndup`, :func:`matdup`, :func:`matdupfull`

