
outerJoin
==============================================

Purpose
----------------
Performs an outer join on two matrices based upon user-specified key columns.
		

Format
----------------
.. function:: outerJoin(A, ca, B, cb)

    :param A: 
    :type A: Matrix to join

    :param ca: or vector, key columns in 'A'
    :type ca: Scalar

    :param B: 
    :type B: Matrix to join with 'A'

    :param cb: key columns in 'B'
    :type cb: Scalar or vector

    :returns: C (*Matrix*), result of join of 'A' and 'B'

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
    
    //Perform left outer-join, using the first
    //columns of 'A' and 'B' as key columns
    C = outerJoin(A, 1, B, 1);

After the code above, C equals:

::

    1.0 1.1 9.0 
    2.0 2.2   .
    3.0 3.3  27

A = { 1 3.1 12 0.5,
      3 1.2 15 0.6,
      5 4.4 19 1.1,
      2 6.9 11 0.9 };

B = { 7 20 0.3 5,
      2 12 1.1 1,
      9 15 0.1 3 };

a_keys = { 1, 3 };
b_keys = { 4, 2 };

//Perform a left-outer join on A and B, based on matches
//from the 1st column of A with the 4th column of B
//and the 3rd column of A with the 2nd column of B 
C = outerJoin(A, a_keys, B, b_keys);
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

After the code above, C equals:

::

    1 3.1 12 0.5 2 1.1 
    3 1.2 15 0.6 9 0.1
    5 4.4 19 1.1 .   .
    2 6.9 11 0.9 .   .

.. seealso:: Functions :func:`innerJoin`
