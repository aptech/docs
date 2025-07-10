matndupdiagone
==============================================

Purpose
----------------
Takes a column vector and converts it into a matrix, with diagonal elements being ones and lower diagonal elements being zeros.

Format
----------------
.. function:: { w } = matndupdiagone(r)

    :param r: Input column vector.
    :type r: Kx1 vector

    :return w: Output matrix derived from the input vector. The size of the matrix *P* is determined by the formula *P=(1+sqrt(1+8*K))/2*, where *K* is the length of the input vector. Diagonal elements are set to ones, and lower diagonal elements are set to zeros.
    :rtype w: PxP matrix

Example
----------------

::

    // Define r as a column vector
    r = { 0.6, 0.5, 0.5 };

    w = matndupdiagone(r);

After the above code, *w* equals:

::

    1 0.6 0.5
    0 1.0 0.5
    0 0.0 1.0

.. seealso:: :func:`vecdup`, :func:`vecndup`, :func:`matdup`, :func:`matdupfull`, :func:`matndup`, :func:`matndupdiagzero`, :func:`matndupdiagzerofull`

