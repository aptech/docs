
innerJoin
==============================================

Purpose
----------------

			Joins two matrices based upon user-specified key columns,
			with non-matching rows removed.
		

Format
----------------
.. function:: innerJoin(A, ca, B, cb)

    :param A: 
    :type A: Matrix to join

    :param ca: or vector, key columns in 'A'
    :type ca: Scalar

    :param B: 
    :type B: Matrix to join with 'A'

    :param cb: key columns in 'B'
    :type cb: Scalar or vector

    :returns: C (*Matrix*), result of join of 'A' and 'B'

Remarks
-------

The first columns of the output matrix C will be the columns of A in the
same order as in A. The remaining columns of C will be the columns of B
with the key columns removed.


Examples
----------------

A = { 1 12 0.5,
      3 15 0.6,
      5 19 1.1,
      2 11 0.9 };

B = { 7 0.3 5,
      2 1.1 1,
      9 0.1 3 };

//Perform inner join on 'A' and 'B', based upon
//matches in column 1 of 'A' and column 3 of 'B'
C = innerJoin(A, 1, B, 3);
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

After the code above, C equals:

::

    1 12 0.5 2 1.1
    3 15 0.6 9 0.1
    5 19 1.1 7 0.3

A = { 1 3.1 12 0.5,
      3 1.2 15 0.6,
      5 4.4 19 1.1,
      2 6.9 11 0.9 };

B = { 7 20 0.3 5,
      2 12 1.1 1,
      9 15 0.1 3 };

a_keys = { 1, 3 };
b_keys = { 4, 2 };

//Perform inner join on A and B, based on matches
//from the 1st column of A with the 4th column of B
//and the 3rd column of A with the 2nd column of B 
C = innerJoin(A, a_keys, B, b_keys);
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

After the code above, C equals:

::

    1 3.1 12 0.5 2 1.1 
    3 1.2 15 0.6 9 0.1

.. seealso:: Functions :func:`outerJoin`
