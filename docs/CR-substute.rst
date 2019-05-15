
substute
==============================================

Purpose
----------------

Substitutes new values for old values in a matrix, depending on the outcome of a logical expression.

Format
----------------
.. function:: substute(x, e, v)

    :param x: the data to be changed
    :type x: NxK matrix

    :param e: ExE conformable with *x* containing 1's and 0's.
    :type e: LxM matrix

    :param v: ExE conformable with *x* and *e*, containing the values to be substituted 
        for the original values of *x* when the corresponding element of *e* is 1.
    :type v: PxQ matrix

    :returns: y (*max(N,L,P) by max(K,M,Q) matrix*)

Remarks
-------

The *e* matrix is usually the result of an expression or set of expressions using dot conditional and boolean operators.

Examples
----------------

Example 1
+++++++++

Set all elements between 0 and 2.25e-16 equal to 0.

::

    // Create example vector
    x = { 3.8e-21, 
              1.0, 
              3.5, 
          2.7e-18, 
              0.5, 
              3.0, 
          1.1e-16, 
              0.5, 
              2.2, 
              4.0 }; 
    
    // Substitute all values less than 2.2e-16 with a zero
    x = substute(x, x .< 2.25e-16, 0);

After the code above, *x* is equal to:

::

    0.0 
    1.0 
    3.5 
    0.0 
    0.5 
    3.0 
    0.0 
    0.5 
    2.2 
    4.0


Example 2
+++++++++

::

    //Create a matrix with character elements 
    //in the first column
    x = { Y 55 30,
          N 57 18,
          Y 24 3,
          N 63 38,
          Y 55 32,
          N 37 11 };
    
    //Create a rows(x) by 1 vector with a '1' for each row
    // that:
    //  1) The first element is a Y
    //  2) The second element is greater than or equal to 55
    //  3) The third element is greater than or equal to 30
    //If the row does not meet ALL of these conditions a 0 will 
    //be returned.
    e = (x[.,1] .$== "Y") .and (x[.,2] .>= 55) .and (x[.,3] .>= 30);
    
    //Substitute an 'R' for the first element in every row that
    //meets the conditions specified in the assignment to 'e'
    x[.,1] = substute(x[.,1],e, "R");

The vector *e* is equal to:

::

    1
    0
    0
    0
    1
    0

Here is what *x* looks like after substitution:

::

    R 55 30
    N 57 18
    Y 24  3
    N 63 38
    R 55 32
    N 37 11

Source
------

datatran.src

.. seealso:: Functions `code`, :func:`recode`, :func:`reclassifyCuts`, :func:`reclassify`, :func:`rescale`

