nondiag
==============================================

Purpose
----------------
Gets the non-diagonal elements of a matrix in a column vector.

Format
----------------
.. function:: { w } = nondiag(r)

    :param r: Input matrix from which non-diagonal elements are to be extracted.
    :type r: KxK matrix

    :return w: Output column vector containing the non-diagonal elements of the input matrix. The size of the vector is (K^2-K) x 1, corresponding to the number of non-diagonal elements in a KxK matrix.
    :rtype w: (K^2-K) x 1 vector

Example
----------------

::

    // Define r as a matrix
    r = { 1 2 3,
          4 5 6,
          7 8 9 };

    // Extract non-diagonal elements
    w = nondiag(r);

After the above code, *w* equals:

::

    2
    3
    4
    6
    7
    8

.. seealso:: :func:`vecdup`, :func:`vecndup`, :func:`matdup`, :func:`matdupfull`, :func:`matndup`, :func:`matndupdiagzero`, :func:`matndupdiagzerofull`, :func:`matndupdiagone`, :func:`matndupdiagonefull`, :func:`matcholeskycor`

