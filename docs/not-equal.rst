Matrix Not Equal (!=)
==============================================

Purpose
----------------

Determines if all elements of two matrices, vectors, or scalars are different, returning a single boolean value indicating complete non-equivalence of operands.

Format
----------------
.. function:: flag = A != B

    :param A: first matrix, vector, or scalar.
    :type A: NxK matrix or scalar

    :param B: second matrix, vector, or scalar.
    :type B: LxM matrix or scalar

    :return flag: boolean value indicating complete non-equivalence.
    
    :rtype flag: scalar (1 for true, 0 for false)

Description
----------------

The `!=` operator checks if all corresponding elements between two operands, A and B, are different. For the result to be true, no elements should match. It evaluates overall content and does not result in true if there is any matching element between A and B.

Compatibility:
- Scalars can be compared with any matrix or vector.
- A row vector can be compared with any matrix that has the same number of columns.
- A column vector can be compared with any matrix that has the same number of rows.

Examples
----------------

Example 1: Matrix complete non-equivalence
+++++++++++++++++++++++++++++++++++++++++++++++


::

    // Create a 2x2 matrix A
    A = { 1 2,
          3 4 };

    // Create another 2x2 matrix B
    B = { 5 6,
          7 8 };

    flag = A != B;  // flag will be 1 (true) because no elements match

Example 2: Matrix with one element matching
++++++++++++++++++++++++++++++++++++++++++++++

::

    // Create a 2x2 matrix A
    A = { 1 2,
          3 4 };

    // Create another 2x2 matrix B
    B = { 1 5,
          6 7 };

    flag = A != B;  // flag will be 0 (false) because one element matches

Example 3: Scalar and matrix comparison with all elements different
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    // Create a 2x2 matrix A
    A = { 4 4,
          4 4 };

    // Create a scalar B
    B = 3;

    flag = A != B;  // flag will be 1 (true) because all elements are different

Notes
----------------

1. If comparing different data structures (e.g., scalar to matrix or vector to matrix), the comparison is made element-wise after possible expansion.
2. The operator returns true only if absolutely no elements are the same between A and B.

