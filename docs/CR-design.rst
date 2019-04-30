
design
==============================================

Purpose
----------------

Creates a design matrix of 0's and 1's from a column
vector of numbers specifying the columns in which
the 1's should be placed.

Format
----------------
.. function:: design(x)

    :param x: 
    :type x: Nx1 vector

    :returns: y (*NxK matrix*), where :math:`K = maxc(x)`; each row of *y*
        will contain a single 1, and the rest 0's. The
        one in the ith row will be in the :code:`round(x[i,1])`
        column.

Remarks
-------

Note that *x* does not have to contain integers: it will be rounded to
nearest if necessary.


Examples
----------------
This example uses design to interchange the rows of a matrix.

::

    // Suppress printing of digits after the decimal place
    format /rd 6,0;
    
    // Set the rng seed for repeatable random numbers
    rndseed 345425235;
    
    // Create a 4x4 matrix of random integers with a standard 
    // deviation of 10
    x = round(10*rndn(4,4));
    print x;

The code above returns:

::

    4     12     -1    -10 
     5     -3     12      8 
    12     -2     21    -21 
    -7    -13      0     -1

Contintuing on with the example:

::

    // The order of the rows we want
    rowOrder = { 3, 1, 4, 2 };
    
    // Create a permutation matrix from 'rowOrder'
    p = design(rowOrder);
    print p;

This section returns:

::

    0      0      1      0 
    1      0      0      0 
    0      0      0      1 
    0      1      0      0
    
    // Create a permuted version of 'x' with our preferred row 
    // order
    x2 = p*x;
    print x2;

This final section returns:

::

    12     -2     21    -21 
     4     12     -1    -10 
    -7    -13      0     -1 
     5     -3     12      8

This last print statement shows us that we have indeed changed the order of the rows. In *x* the row order is 1, 2, 3, 4. However, in *x2*, the row order is 3, 1, 4, 2 (i.e. the third row is now first, the first row is now second, etc.)

Source
------

design.src

.. seealso:: Functions :func:`cumprodc`, :func:`cumsumc`, :func:`recserrc`

