
aconcat
==============================================

Purpose
----------------

Concatenates conformable matrices and arrays in a user-specified dimension.

Format
----------------
.. function:: aconcat(a,  b,  dim)

    :param a: matrix or N-dimensional array.
    :type a: TODO

    :param b: matrix or K-dimensional array, conformable with  a.
    :type b: TODO

    :param dim: dimension in which to concatenate.
    :type dim: scalar

    :returns: y (*TODO*), M-dimensional array, the result of the concatenation.

Examples
----------------

::

    //Create a 2x3x4 array with each element set to 0
    a = arrayinit(2|3|4,0);
    
    //Create a 3x4 matrix with each element set to 3
    b = 3*ones(3,4);
    y = aconcat(a,b,3);

y will be a 3x3x4 array, where [1,1,1]
through [2,3,4] are zeros and [3,1,1] through [3,2,4] are threes.

::

    //Create an additive sequence from 1-20 and 'reshape' it
    //into a 4x5 matrix
    a = reshape(seqa(1,1,20),4,5);
    
    b = zeros(4,5);
    y = aconcat(a,b,3);

y will be a 2x4x5 array, where [1,1,1] through [1,4,5]
are sequential integers beginning with 1, and [2,1,1] through
[2,4,5] are zeros.

::

    //The pipe operator '|' causes vertical concatenation so
    //that the statement 2|3|4 creates a 3x1 column vector
    //equal to { 2, 3, 4 }
    a = arrayinit(2|3|4,0);
    b = seqa(1,1,24);
    
    //'Reshape' the vector 'b' into a 2x3x4 dimensional array
    b = areshape(b,2|3|4);
    y = aconcat(a,b,5);

y will be a 2x1x2x3x4 array,
where [1,1,1,1,1] through [1,1,2,3,4] are zeros, and [2,1,1,1,1]
through [2,1,2,3,4] are sequential integers beginning with 1.

::

    a = arrayinit(2|3|4,0);
    b = seqa(1,1,6);
    b = areshape(b,2|3|1);
    y = aconcat(a,b,1);
    print "y = " y;

y will be a 2x3x5 array:

::

    y = 
    
    Plane [1,.,.] 
    
    0.00     0.00     0.00     0.00      1.0 
    0.00     0.00     0.00     0.00      2.0 
    0.00     0.00     0.00     0.00      3.0 
    
    Plane [2,.,.] 
    
    0.00     0.00     0.00     0.00      4.0 
    0.00     0.00     0.00     0.00      5.0 
    0.00     0.00     0.00     0.00      6.0

.. seealso:: Functions :func:`areshape`

| 
