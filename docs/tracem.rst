
tracem
==============================================

Purpose
----------------

Returns the trace of a matrix or multi-dimensional array.

Format
----------------
.. function:: t = tracem(A)

    :param A: data
    :type A: NxM matrix, or multidimensional array.

    :return t: the trace of the matrix.

    :rtype t: scalar, or multidimensional array.

Examples
----------------

::

    A = { 1 2,
          3 4 };

    // Compute the trace of the matrix
    t = tracem(A);

After the code above:

::

    t = 5

::

    // Create a 2x3x3 array
    A = areshape(seqa(1,1,18), 2|3|3);
    print A;

::

    Plane [1,.,.]

         1              2              3
         4              5              6
         7              8              9

    Plane [2,.,.]

        10             11             12
        13             14             15
        16             17             18

::

    t = tracem(A);
    print t;


::

    Plane [1,.,.] 
        15 

    Plane [2,.,.] 
        42

.. seealso:: Functions :func:`norm`, :func:`powerm`
