
sortr, sortrc
==============================================

Purpose
----------------
Sorts the columns of a matrix of numeric or character data, with respect to a specified row.

Format
----------------
.. function:: sortrc(x, r)

    :param x: 
    :type x: NxK matrix

    :param r: row of x on which to sort.
    :type r: scalar

    :returns: y (*NxK matrix*) equal to x and sorted on row r.

Remarks
-------

These functions sort the columns of a matrix with respect to a specified
row. That is, they sort the elements of a row and arrange all rows of
the matrix in the same order as the sorted column.

sortr assumes the row on which to sort is numeric. sortrc assumes that
the row on which to sort contains character data.

The matrix may contain both character and numeric data, but the sort row
must be all of one type. Missing values will sort as if their value is
below -∞.

The sort will be in left to right ascending order. This function uses
the Quicksort algorithm. If you need to obtain the matrix sorted left to
right in descending order (i.e., ascending right to left), use:

::

   rev(sortr(x, r)')'


Examples
----------------

::

    // Create a 5 x 3 matrix of random integers
    // between 1 and 30
    x = ceil(30*rndu(5, 3));
    
    // Sort the columns based upon the first row 
    y = sortr(x,1);

Examine the variables after the code above. Notice that the columns remain the same, but their order has changed.

::

    10.000 21.000 18.000 
        11.000 30.000 20.000 
    x = 10.000 23.000  7.000 
         6.000  9.000 20.000 
         7.000  4.000 30.000 
         
        10.000 18.000 21.000 
        11.000 20.000 30.000 
    y = 10.000  7.000 23.000 
         6.000 20.000  9.000 
         7.000 30.000  4.000

If we were to use the same x, but sort on the 5th row:

::

    y2 = sortr(x, 5);

We get the following result:

::

    21.000 10.000 18.000 
         30.000 11.000 20.000 
    y2 = 23.000 10.000  7.000 
          9.000  6.000 20.000 
          4.000  7.000 30.000

