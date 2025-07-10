vectranspose
==============================================

Purpose
----------------
Creates an indicator vector to transform a matrix with respect to derivatives of the vectorization of the elements of a matrix A to derivatives with respect to the vectorization of the transpose elements of the matrix A.

Format
----------------
.. function:: w = vectranspose(r, c)

    :param r: Rows of matrix A.
    :type r: integer

    :param c: Columns of matrix A.
    :type c: integer

Output
----------------
    :return w: An rc*1 vector for re-ordering rows. This vector is used to transform derivatives with respect to the vectorization of the elements of matrix A (e.g., in matrix dvec(B)/dvec(A)) to derivatives with respect to the vectorization of the transpose elements of matrix A, by applying the transformation dvec(B)/dvec(A') = submat(dvec(B)/dvec(A), w, 0).
    :rtype w: vector

Example
----------------

Given a matrix A with dimensions `r = 3` and `c = 4`, to transform derivatives with respect to the vectorization of the elements of A to derivatives with respect to the vectorization of the transpose elements of A:

::

    // Define r and c for matrix A
    r = 3;
    c = 4;

    // Apply vectranspose to create w
    w = vectranspose(r, c);

After the above code is run, *w* equals:

::

       1
       5
       9
       2
       6
      10
       3
       7
      11
       4
       8
      12

To transform these derivatives to those with respect to the vectorization of the transpose of matrix A, apply the transformation:

::

    dvec(B)/dvec(A') = submat(dvec(B)/dvec(A), w, 0);

After applying the `vectranspose` function, the indicator vector *w* will be used to reorder the rows in the derivative matrix to match the transpose operation on matrix *A*.


.. seealso:: :func:`vecdup`, :func:`vecndup`

