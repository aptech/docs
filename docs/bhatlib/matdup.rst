matdup
==============================================

Purpose
----------------
Takes a column vector and converts it into an upper diagonal matrix, including the diagonal of the matrix.

Format
----------------
.. function:: { w } = matdup(r)

    :param r: Input column vector to be converted into an upper diagonal matrix.
    :type r: Kx1 vector

    :return w: Output upper diagonal matrix derived from the input vector. The size of the matrix *P* is determined by the formula *P=(-1+sqrt(1+8*K))/2*, where *K* is the length of the input vector.
    :rtype w: PxP matrix

Example
----------------

::

    r =  1
         2
         3
         4
         5
         6

    w = matdup(r);

After the above code, *w* equals:

::

    { 1 2 3,
      0 4 5,
      0 0 6 }

.. seealso:: :func:`vecdup`, :func:`vecndup`, :func:`matdupfull`

