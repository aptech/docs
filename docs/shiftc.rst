
shiftc
==============================================

Purpose
----------------
Shifts the columns of a matrix, or dataframe.

Format
----------------
.. function:: y = shiftc(x, s, f)

    :param x: data to be shifted
    :type x: NxK matrix or dataframe

    :param s: specifies the magnitude of the shift
    :type s: scalar or Nx1 vector

    :param f: specifies the value to fill in
    :type f: scalar or 1xN vector

    :return y: shifted matrix
    :rtype y: NxK matrix

Examples
----------------

Example 1: Basic lag
+++++++++++++++++++++++

::

    // Create file name with full path
    fname = getGAUSSHome() $+ "examples/beef_prices.csv";
    
    // Load all observations of all variables
    beef = loadd(fname);

    // Trim data to make smaller example set
    beef = beef[1:5,.];

    // Shift all columns of beef forward 2 rows
    // filling the extra rows with a missing value
    beef_lag = shiftc(beef, 2, miss());

After the above code:

::

    beef =   date beef_price 
           199201     116.64 
           199202     114.49 
           199203     111.11 
           199204     108.17 
           199205     107.76 

::

    // Data matrix
    x = { 1 2,
          3 4 };

    // Amount of shift
    s = { 1,
         -1 };

    // Value to fill in
    f = { 99,
         999 };

    // Shift the matrix
    y = shiftc(x, s, f);

Now *y* is equal to:

::

    99   1
    4  999

::

    // Data 
    x = { 1 2 3,
          4 5 6,
          7 8 9 };

    // Amount to shift
    s = { 0,
          1,
          2 };

    // Value to fill in
    f = 0;

    // Shift the matrix
    y2 = shiftc(x, s, f);

Now *y2* is equal to:

::

    1  2  3
    0  4  5
    0  0  7

Remarks
-------

The shift is performed within each column of the matrix, vertically. If
the shift value is positive, the elements in the column will be moved
down. A negative shift value causes the elements to be moved up.
The elements that are pushed off the end of the column are lost, and
the fill value will be used for the new elements on the other end.

.. seealso:: Functions :func:`lagn`, :func:`shiftr`
