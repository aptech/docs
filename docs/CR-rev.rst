
rev
==============================================

Purpose
----------------
Reverses the order of the rows in a matrix.

Format
----------------
.. function:: rev(x)

    :param x: 
    :type x: NxK matrix

    :returns: y (*NxK matrix*), containing the reversed rows of x.

Remarks
-------

The first row of y will be where the last row of x was and the last row
will be where the first was and so on. This can be used to put a sorted
matrix in descending order.


Examples
----------------

::

    // Set the rng seed for repeatable results               
    rndseed 345345;
    
    // Set print formatting to print 4 spaces for each column
    // and 0 numbers after the decimal
    format /rd 4,0
    
    // Create some random integers
    x = round(rndn(5,3)*10);
    
    // Reverse the order of the columns
    y = rev(x);
    
    print "x = " x;
    print "y = " y;

The code above produces the following output:

::

    x = 
      10  -14   -7 
       3   -1   -5 
      -7    4    2 
       1    1    1 
       7   -7    2 
    y = 
       7   -7    2 
       1    1    1 
      -7    4    2 
       3   -1   -5 
      10  -14   -7

.. seealso:: Functions :func:`sortc`
