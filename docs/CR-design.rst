
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

    :param x: Vector specifying the columns in which 1's for the design matrix should be placed.
    :type x: Nx1 vector

    :returns: **y** (*NxK matrix*) - each row of *y*
        will contain a single 1, and the rest 0's. The
        one in the ith row will be in the :code:`round(x[i, 1])` column. The dimension *K* is such that :code:`K = maxc(x)`.

Remarks
-------

Note that *x* does not have to contain integers: it will be rounded to
nearest integer if necessary.


Examples
----------------

Example 1: Create dummy variables
+++++++++++++++++++++++++++++++++

:func:`design` makes it easy to create dummy variables from a vector of integers.

::

    // Vector of classes
    c = { 3, 1, 1, 3, 2 };

   // Create dummy variable
   d = design(c);

After the above code:

::

    d = 0 0 1
        1 0 0
        1 0 0
        0 0 1
        0 1 0


Example 2: Create a permutation matrix
++++++++++++++++++++++++++++++++++++++

This example uses design to interchange the rows of a matrix.

::

    // Suppress printing of digits after the decimal place
    format /rd 6,0;

    // Set the rng seed for repeatable random numbers
    rndseed 345425235;

    /*
    ** Create a 4x4 matrix of random integers with a standard
    ** deviation of 10
    */
    x = round(10*rndn(4, 4));
    print x;

The code above returns:

::

     4     12     -1    -10
     5     -3     12      8
    12     -2     21    -21
    -7    -13      0     -1

Continuing with the example:

::

    // The order of the rows we want
    row_order = { 3, 1, 4, 2 };

    // Create a permutation matrix from 'row_order'
    p = design(row_order);
    print p;

This section returns:

::

    0      0      1      0
    1      0      0      0
    0      0      0      1
    0      1      0      0

We can use ``p`` to permutate the matrix  ``x``

::

    /*
    ** Create a permuted version of 'x' with our preferred row
    ** order
    */
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
