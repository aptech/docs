vecsymmetry
==============================================

Purpose
----------------
Transforms a given scalar input into a symmetric matrix representation, applying symmetry operations to produce a structured matrix.

Format
----------------
.. function:: w = vecsymmetry(r)

    :param r: Dimension of square matrix to be rolled out.
    :type r: scalar

Output
----------------
    :return w: Resulting matrix after applying symmetry operations. The matrix is of size [(K X (K+1)/2] X K^2, where K is derived from the input scalar. This matrix represents a specific symmetry pattern or structure.
    :rtype w: matrix

Example
----------------

::

    // Define r
    r = 4;

    // Apply vecsymmetry to create w
    w = vecsymmetry(r);

After the above code, *w* equals:

::

    1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0
    0 0 1 0 0 0 0 0 1 0 0 0 0 0 0 0
    0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0
    0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
    0 0 0 0 0 0 1 0 0 1 0 0 0 0 0 0
    0 0 0 0 0 0 0 1 0 0 0 0 0 1 0 0
    0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0
    0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0
    0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1

.. seealso:: :func:`vecdup`, :func:`vecndup`, :func:`matdup`, :func:`matdupfull`, :func:`matndup`, :func:`matndupdiagzero`, :func:`matndupdiagzerofull`, :func:`matndupdiagone`, :func:`matndupdiagonefull`, :func:`matcholeskycor`, :func:`nondiag`

