
outerJoin
==============================================

Purpose
----------------
Performs an outer join on two matrices based upon user-specified key columns.
		

Format
----------------
.. function:: C = outerJoin(A, ca, B, cb)

    :param A: matrix to join
    :type A: matrix

    :param ca: key columns in *A*
    :type ca: scalar or vector

    :param B: matrix to join with *A*
    :type B: matrix

    :param cb: key columns in *B*
    :type cb: scalar or vector

    :return C: result of join of *A* and *B*

    :type C: matrix

Remarks
-------

By default, :func:`outerJoin` performs a left outer-join, retaining only the key
columns from the first input matrix.

The first columns of the output matrix *C* will be the columns of *A* in the
same order as in *A*. The remaining columns of *C* will be the columns of *B*
with the key columns removed.

Examples
----------------

Basic example
+++++++++++++

::

    A = { 1 1.1,
          2 2.2,
          3 3.3 };
        
    B = { 1  9,
          3 27 };
    
    // Perform left outer-join, using the first
    // columns of 'A' and 'B' as key columns
    C = outerJoin(A, 1, B, 1);

After the code above, *C* equals:

::

    1.0 1.1 9.0 
    2.0 2.2   .
    3.0 3.3  27

Join on two columns
+++++++++++++++++++

::

    A = { 1 3.1 12 0.5,
          3 1.2 15 0.6,
          5 4.4 19 1.1,
          2 6.9 11 0.9 };
    
    B = { 7 20 0.3 5,
          2 12 1.1 1,
          9 15 0.1 3 };
    
    a_keys = { 1, 3 };
    b_keys = { 4, 2 };
    
    // Perform a left-outer join on A and B, based on matches
    // from the 1st column of A with the 4th column of B
    // and the 3rd column of A with the 2nd column of B 
    C = outerJoin(A, a_keys, B, b_keys);

After the code above, *C* equals:

::

    1 3.1 12 0.5 2 1.1 
    3 1.2 15 0.6 9 0.1
    5 4.4 19 1.1 .   .
    2 6.9 11 0.9 .   .

.. seealso:: Functions :func:`innerJoin`

