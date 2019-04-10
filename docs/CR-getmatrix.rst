
getmatrix
==============================================

Purpose
----------------

Gets a contiguous matrix from an N-dimensional array.

Format
----------------
.. function:: getmatrix(a, loc)

    :param a: data
    :type a: N-dimensional array

    :param loc: indices into the array to locate the matrix of interest where *M* equals *N*, N-1 or N-2.
    :type loc: Mx1 vector

    :returns: y (*KxL or 1xL matrix or scalar*), where *L* is the
        size of the fastest moving dimension of the array and *K* is the size
        of the second fastest moving dimension.

Remarks
-------

Inputting an Nx1 locator vector will return a scalar, an (N-1)x1 locator
vector will return a 1xL matrix, and an (N-2)x1 locator vector will
return a KxL matrix.


Examples
----------------

::

    //Create the sequence 1, 2, 3...20
    a = seqa(1, 1, 20);
    
    //Reshape the column vector 'a' into a 3x3x2 dimensional 
    //array
    a = areshape(a, 3|3|2);
    
    //Extract the second 3x2 array
    mat = getmatrix(a, 2);

After code above *a* is equal to:

::

    Plane [1,.,.]
    
           1.0000000        2.0000000
           3.0000000        4.0000000
           5.0000000        6.0000000
    
    Plane [2,.,.]
    
           7.0000000        8.0000000
           9.0000000        10.000000
           11.000000        12.000000
    
    Plane [3,.,.]
    
           13.000000        14.000000
           15.000000        16.000000
           17.000000        18.000000

and *mat* is equal to:

::

           7.0000000        8.0000000
           9.0000000        10.000000
           11.000000        12.000000

.. seealso:: Functions :func:`getarray`, :func:`getmatrix4D`

