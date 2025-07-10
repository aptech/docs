matcholeskycor
==============================================

Purpose
----------------
Takes a column vector and converts it into a matrix that corresponds to the Cholesky decomposition of a correlation matrix, with the input column vector being the Cholesky elements of the correlation matrix.

Format
----------------
.. function:: { w } = matcholeskycor(r)

    :param r: Input column vector of Cholesky elements.
    :type r: Kx1 vector

    :return w: Output matrix derived from the input vector. The size of the matrix *P* is determined by the formula *P=(1+sqrt(1+8*K))/2*, where *K* is the length of the input vector. The matrix represents the Cholesky decomposition of a correlation matrix, with diagonal elements calculated to maintain the property of a correlation matrix.
    :rtype w: PxP matrix

Example
----------------

::

    // Define r as a column vector
    r = { 0.6, 0.5, 0.4 };

    w = matcholeskycor(r);

After the above code, *w* equals:

::

    1            0.6           0.5
    0   sqrt(1-0.6^2)          0.4
    0            0.0  sqrt(1-0.5^2-0.4^2)

.. seealso:: :func:`vecdup`, :func:`vecndup`, :func:`matdup`, :func:`matdupfull`, :func:`matndup`, :func:`matndupdiagzero`, :func:`matndupdiagzerofull`, :func:`matndupdiagone`, :func:`matndupdiagonefull`

