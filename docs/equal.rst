Matrix Equality (==)
==============================================

Purpose
----------------

Evaluates the equality of matrices, vectors, or scalars, returning a single boolean value indicating if the operands are considered equivalent based on their contents and dimension compatibility.

Format
----------------
.. function:: flag = A == B

    :param A: first matrix, vector, or scalar.
    :type A: NxK matrix or scalar

    :param B: second matrix, vector, or scalar.
    :type B: LxM matrix or scalar

    :return flag: boolean value indicating overall equality.
    
    :rtype flag: scalar (1 for true, 0 for false)

Description
----------------

The `==` operator checks if two operands are equivalent. For matrices and vectors, this means all corresponding elements must match. Scalars are compared directly, and scalars can be compared with matrices or vectors by implicitly matching the scalar with each element of the matrix or vector.

Compatibility:
- Scalars can be compared with any matrix or vector.
- A row vector can be compared with any matrix that has the same number of columns.
- A column vector can be compared with any matrix that has the same number of rows.

Examples
----------------

Example 1: Complete matrix equality
++++++++++++++++++++++++++++++++++++++++

::

    // Create a 2x2 matrix A
    A = { 1 2,
          3 4 };

    // Create another 2x2 matrix B
    B = { 1 2,
          3 4 };

    flag = A == B;  // flag will be 1 (true)

Example 2: Matrix and scalar comparison
++++++++++++++++++++++++++++++++++++++++

::

    // Create a 2x2 matrix A
    A = { 5 5,
          5 5 };

    // Create a scalar B
    B = 5;

    flag = A == B;  // flag will be 1 (true)

Example 3: Row vector and matrix comparison
++++++++++++++++++++++++++++++++++++++++

::

    // Create a row vector A
    A = { 4 4 4 };

    // Create a 3x3 matrix B
    B = { 4 4 4,
          4 4 4,
          4 4 4 };

    flag = A == B;  // flag will be 1 (true)

Example 4: Matrix inequality due to different elements
++++++++++++++++++++++++++++++++++++++++

::

    // Create a 2x2 matrix A
    A = { 1 2,
          3 4 };

    // Create another 2x2 matrix B
    B = { 2 2,
          3 5 };

    flag = A == B;  // flag will be 0 (false)

Example 5: Scalar and matrix comparison where elements differ
++++++++++++++++++++++++++++++++++++++++

::

    // Create a 2x2 matrix A
    A = { 5 6,
          7 8 };

    // Create a scalar B
    B = 5;

    flag = A == B;  // flag will be 0 (false)

Example 6: Row vector and matrix comparison with differing elements
++++++++++++++++++++++++++++++++++++++++

::

    // Create a row vector A
    A = { 4 4 4 };

    // Create a 3x3 matrix B
    B = { 4 4 4,
          1 1 1,
          2 2 2 };

    flag = A == B;  // flag will be 0 (false)

Notes
----------------

1. If comparing different data structures (e.g., scalar to matrix or vector to matrix), GAUSS automatically conforms the smaller dimensioned operand to the larger for comparison purposes.
2. The result is true only if all comparisons are equal across the conformed dimensions.

