Element-by-element Less Than or Equal To (.<=)
===============================================

Purpose
-------

Performs element-by-element comparisons to determine if elements of the first matrix, vector, or dataframe are less than or equal to those of the second matrix, vector, or dataframe.

Format
------

.. function:: c = a .<= b

    :param a: first matrix, vector, or dataframe.
    :type a: NxK matrix

    :param b: second matrix, vector, or dataframe ExE compatible with *a*.
    :type b: LxM matrix

    :return c: matrix of 1's (true) and 0's (false), where each element of *c* is 1 if the corresponding element of *a* is less than or equal to the corresponding element of *b*, otherwise 0.
    :rtype c: max(N, L) by max(K, M)

Examples
--------

Example 1: Matrices of the same size
++++++++++++++++++++++++++++++++++++

::

    // Create a 2x2 matrix
    a = { 4 5,
          6 7 };

    // Create another 2x2 matrix
    b = { 5 5,
          6 8 };

    c = a .<= b;

After the above code, *c* will equal:

::

    c = 1 1
        1 1


Example 2: Matrix vs vector comparison
++++++++++++++++++++++++++++++++++++++

If matrices are not the same size, they must be ExE conformable on one of the dimensions.

::

    // Create a 2x3 matrix
    a = { 4 5 6,
          7 8 9 };

    // Create a 1x3 vector
    b = { 4 7 6 };

    c = a .<= b;

After the above code, *c* will equal:

::

    c = 1 1 1
        0 0 0

Example 3: Row vector vs column vector comparison
++++++++++++++++++++++++++++++++++++++++++++++++++

Row vectors and column vectors can be compared by expanding one to match the dimensions of the other through broadcasting.

::

    // Create a 1x4 vector
    a = { 4 5 6 7 };

    // Create a 3x1 vector
    b = { 5,
          6,
          7 };

    c = a .<= b;

After the above code, *c* will equal:

::

    c = 1 1 0 0
        1 1 1 0
        1 1 1 1

GAUSS internally expands the vectors to match each other. The above example is equivalent to comparing:

::

    // Expanded 3x4 matrix from vector 'a'
    a = { 4 5 6 7,
          4 5 6 7,
          4 5 6 7 };

    // Expanded 3x4 matrix from vector 'b'
    b = { 5 5 5 5,
          6 6 6 6,
          7 7 7 7 };

    c = a .<= b;

This will set *c* equal to:

::

    c = 1 1 0 0
        1 1 1 0
        1 1 1 1

