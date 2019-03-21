
spDiagRvMat
==============================================

Purpose
----------------
Inserts submatrices along the diagonal of a sparse matrix.

Format
----------------
.. function:: spDiagRvMat(x, inds, size, a)

    :param x: 
    :type x: MxN sparse matrix

    :param inds: row and column indices into x at which to place the
        corresponding submatrices in a.
    :type inds: Kx2 vector or scalar 0

    :param size: sizes of the corresponding submatrices in a.
    :type size: Kx2 vector or scalar 0

    :param a: containing the submatrices to insert into x.
    :type a: KxLxP array

    :returns: y (*MxN sparse matrix*), a copy of x containing the specified insertions.

Examples
----------------

::

    declare sparse matrix x,y;
    
    //Create a 10x10 sparse identity matrix
    x = spEye(10);
    
    sx1 = { 2 3, 5 8 };
    sx2 = { 8 2 3 4, 7 9 5 6, 3 2 8 4 };
    sx3 = { 4 7 2, 6 5 3 };
    sx4 = { 9, 3 };
    
    //Create a 4x3x4 dimensional array with every element set 
    //to 0
    a = arrayinit(4|3|4,0);
    
    //Set some of the array values
    a[1,1:2,1:2] = sx1;
    a[2,.,.] = sx2;
    a[3,1:2,1:3] = sx3;
    a[4,1:2,1] = sx4;

a

::

    Plane [1,.,.] 
    
        2.00000000    3.00000000    0.00000000    0.00000000 
        5.00000000    8.00000000    0.00000000    0.00000000 
        0.00000000    0.00000000    0.00000000    0.00000000 
    
    Plane [2,.,.] 
    
        8.00000000    2.00000000    3.00000000    4.00000000 
        7.00000000    9.00000000    5.00000000    6.00000000 
        3.00000000    2.00000000    8.00000000    4.00000000 
    
    Plane [3,.,.] 
    
        4.00000000    7.00000000    2.00000000    0.00000000 
        6.00000000    5.00000000    3.00000000    0.00000000 
        0.00000000    0.00000000    0.00000000    0.00000000 
    
    Plane [4,.,.] 
    
        9.00000000    0.00000000    0.00000000    0.00000000 
        3.00000000    0.00000000    0.00000000    0.00000000 
        0.00000000    0.00000000    0.00000000    0.00000000

::

    inds = 0;
    siz = { 2 2, 3 4, 2 3, 2 1 };
    
    y = spDiagRvMat(x,inds,siz,a);

The output, in variable y, is:

::

    2  3  0  0  0  0  0  0  0  0 
     5  8  0  0  0  0  0  0  0  0 
     0  0  8  2  3  4  0  0  0  0 
     0  0  7  9  5  6  0  0  0  0 
     0  0  3  2  8  4  0  0  0  0 
     0  0  0  0  0  1  4  7  2  0 
     0  0  0  0  0  0  6  5  3  0 
     0  0  0  0  0  0  0  1  0  9 
     0  0  0  0  0  0  0  0  1  3 
     0  0  0  0  0  0  0  0  0  1

