
vech
==============================================

Purpose
----------------
Vectorizes a symmetric matrix by retaining only the lower triangular portion of the matrix.

Format
----------------
.. function:: vech(x)

    :param x: 
    :type x: NxN symmetric matrix

    :returns: v (*(N*(N+1)/2)x1 vector*) , the lower triangular portion of the matrix x.

Remarks
-------

As you can see from the example below, vech will not check to see if x
is symmetric. It just packs the lower trangular portion of the matrix
into a column vector in row-wise order.


Examples
----------------

::

    //Add a 3x1 column vector containing 10, 20, 30 to a 1x3 
    //row vector containing 1, 2, 3, to create a 3x3 matrix
    x = seqa(10,10,3) + seqa(1,1,3)';
    
    //Turn the lower triangular portion of 'x' into a column 
    //vector in 'v'
    v = vech(x);
    
    //Expand the vector 'v' into a symmetric matrix in 'sx'
    sx = xpnd(v);

After the code above:

::

    11
        11 12 13       21       11 21 31
    x = 21 22 23   v = 22  sx = 21 22 32
        31 32 33       31       31 32 33
                       32
                       33

.. seealso:: Functions :func:`xpnd`
