
floor
==============================================

Purpose
----------------

Round down toward -∞.

Format
----------------
.. function:: floor(x)

    :param x: 
    :type x: NxK matrix or N-dimensional array

    :returns: y (*NxK matrix or N-dimensional array*) containing the elements of x rounded down.

Remarks
-------

This rounds every element in x down to the nearest integer.


Examples
----------------

::

    //Set the seed for repeatable random numbers
    rndseed 9072345;
    
    //Create random normal numbers with a standard 
    //deviation of 100
    x = 100*rndn(2,2);
    
    //Round the numbers down
    f = floor(x);
    
    //Format so numbers will print in decimal form rather than
    //scientific notation) and will show 2 digits after the 
    //decimal point
    format /rd 8,2;
    
    print "************************"; 
    print "After running this code:"; 
    print "************************\n"; 
    print "x = " x;
    print "";
    print "and, f = " f;

produces:

::

    ************************
    After running this code:
    ************************
    
    x = 
        0.11   314.05 
      -80.87   103.73 
    
    and, f = 
        0.00   314.00 
      -81.00   103.00

Notice in the code above, how the \n at the end of the statement printing the line of asterisks, inserts a newline.

.. seealso:: Functions :func:`ceil`, :func:`round`, :func:`trunc`
