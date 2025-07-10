matndupdiagzerofull
==============================================

Purpose
----------------
Takes a column vector of upper diagonal elements and converts it into a matrix, with diagonal elements being zero and upper diagonal elements filling the lower diagonal based on symmetry.

Format
----------------
.. function:: { w } = matndupdiagzerofull(r)

    :param r: Input column vector containing the upper diagonal elements of a matrix.
    :type r: Kx1 vector

    :return w: Output matrix derived from the input vector. The size of the matrix *P* is determined by the formula *P=(1+sqrt(1+8*K))/2*, where *K* is the length of the input vector. Diagonal elements are set to zero, and the matrix is symmetrical with respect to the diagonal.
    :rtype w: PxP matrix

Example
----------------

::

    // Define r as a column vector
    r = { 0.6, 0.5, 0.5 };

    w = matndupdiagzerofull(r);

After the above code, *w* equals:

::

    0.0 0.6 0.5
    0.6 0.0 0.5
    0.5 0.5 0.0

.. seealso:: :func:`vecdup`, :func:`vecndup`, :func:`matdup`, :func:`matdupfull`, :func:`matndup`, :func:`matndupdiagzero`

