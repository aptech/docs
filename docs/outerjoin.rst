
outerJoin
==============================================

Purpose
----------------
Performs a left outer join on two matrices based upon user-specified key columns.
		

Format
----------------
.. function:: C = outerJoin(A, ca, B, cb)

    :param A: data to join
    :type A: matrix or dataframe

    :param ca: key column indices or names from *A*
    :type ca: scalar, vector or string

    :param B: matrix to join with *A*
    :type B: matrix

    :param cb: key column indices or names from *B*
    :type cb: scalar, vector or string

    :return C: result of join of *A* and *B*

    :rtype C: matrix or dataframe

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


Join dataframes based on a date variable
++++++++++++++++++++++++++++++++++++++++++++++

::

    // Load Tbill and US recession data
    tbill_3mo = loadd(getGAUSSHome() $+ "examples/tbill_3mo.xlsx", "date($obs_date) + tbill_3m");
    USREC = loadd(getGAUSSHome() $+ "examples/USREC.csv",  "date($DATE) + USREC");
    
    // Perform left outer-join
    tbill_rec = outerJoin(tbill_3mo, "obs_date", USREC, "DATE");
    
    print tbill_rec[1:12,.];

will print out:

::

        obs_date         tbill_3m            USREC 
      1982-01-01        12.920000        1.0000000 
      1982-02-01        14.280000        1.0000000 
      1982-03-01        13.310000        1.0000000 
      1982-04-01        13.340000        1.0000000 
      1982-05-01        12.710000        1.0000000 
      1982-06-01        13.080000        1.0000000 
      1982-07-01        11.860000        1.0000000 
      1982-08-01        9.0000000        1.0000000 
      1982-09-01        8.1900000        1.0000000 
      1982-10-01        7.9700000        1.0000000 
      1982-11-01        8.3500000        1.0000000 
      1982-12-01        8.2000000        0.0000000


Remarks
-------

By default, :func:`outerJoin` performs a left outer-join, retaining only the key
columns from the first input matrix.

The first columns of the output matrix *C* will be the columns of *A* in the
same order as in *A*. The remaining columns of *C* will be the columns of *B*
with the key columns removed.

.. seealso:: Functions :func:`innerJoin`

