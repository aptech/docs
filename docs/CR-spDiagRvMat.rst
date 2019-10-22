
spDiagRvMat
==============================================

Purpose
----------------
Inserts submatrices along the diagonal of a sparse matrix.

Format
----------------
.. function:: y = spDiagRvMat(x, inds, size, a)

    :param x: data
    :type x: MxN sparse matrix

    :param inds: row and column indices into *x* at which to place the corresponding submatrices in *a*.
    :type inds: Kx2 vector or scalar 0

    :param size: sizes of the corresponding submatrices in *a*.
    :type size: Kx2 vector or scalar 0

    :param a: containing the submatrices to insert into *x*.
    :type a: KxLxP array

    :return y: a copy of *x* containing the specified insertions.

    :rtype y: MxN sparse matrix

Examples
----------------

::

    declare sparse matrix x,y;
    
    // Create a 10x10 sparse identity matrix
    x = spEye(10);
    
    sx1 = { 2 3, 5 8 };
    sx2 = { 8 2 3 4, 7 9 5 6, 3 2 8 4 };
    sx3 = { 4 7 2, 6 5 3 };
    sx4 = { 9, 3 };
    
    // Create a 4x3x4 dimensional array with every element set 
    // to 0
    a = arrayinit(4|3|4,0);
    
    // Set some of the array values
    a[1,1:2,1:2] = sx1;
    a[2,.,.] = sx2;
    a[3,1:2,1:3] = sx3;
    a[4,1:2,1] = sx4;

The value of *a* is now:

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
    
    y = spDiagRvMat(x, inds, siz, a);

The output, in variable *y*, is:

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

Remarks
-------

Each row of *inds* must contain the row and column indices, respectively,
that form the starting point for the insertion of the corresponding
submatrix in *a*. If *inds* is a scalar 0, the starting point for the
insertion of each submatrix will be one row and one column past the
ending point of the previous insertion. The first insertion will begin
at the :math:`[1,1]` element.

Each row of size must contain the number of rows and columns in the
corresponding submatrix in *a*. This allows you to insert submatrices of
different sizes :math:`L_i \times P_i` by inserting them into the
planes of an array that is :math:`KxMAX(L)xMAX(P)` and padding the submatrices
with zeros to :math:`MAX(L)xMAX(P)`. For each plane in *a*, :func:`spDiagRvMat` extracts
the submatrix ``a[i,1:size[i,1], 1:size[i,2]]`` and inserts that into *x* at
the location indicated by the corresponding row of *inds*. If *size* is a
scalar 0, then each LxP plane of *a* is inserted into *x* as is.

