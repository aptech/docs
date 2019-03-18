
croutp
==============================================

Purpose
----------------

Computes the Crout decomposition of a square matrix with partial (row) pivoting.

Format
----------------
.. function:: croutp(x)

    :param x: NxN square nonsingular matrix.
    :type x: TODO

    :returns: y (*TODO*), (N+1)xN matrix containing the lower (L) and upper
        (U) matrices of the Crout decomposition of a
        permuted x. The N+1 row of the matrix y gives
        the row order of the y matrix. The matrix must be
        reordered prior to extracting the  L and
        U matrices. Use lowmat and
        upmat1 to extract the  L and  U matrices from the
        reordered y matrix.

Examples
----------------
This example illustrates a procedure for extracting
L and U of the permuted x matrix. It continues
by sorting the result of LU to compare with the
original matrix x.

::

    X = { 1 2 -1,
          2 3 -2,
          1 -2 1 };
     
    y = croutp(x);

If we view 'y', we will see:

::

    1.0000       0.50000       0.28571 
    y = 2.0000        1.5000       -1.0000 
        1.0000       -3.5000      -0.57142 
        2.0000        3.0000        1.0000

::

    //This bottom row is the permutation index vector
    //Calculate how many rows in 'y'
    r = rows(y);
    
    //Extract the index row and transpose it into a column 
    //vector
    index = y[r,.]';

Viewing 'indx' will reveal:

::

    2 
    index = 3 
            1

::

    //Rearrange the rows of 'y' based upon the index vector
    z = y[index,.];
    
    // obtain L and U of permuted matrix X
    L = lowmat(z); 
    U = upmat1(z);
    
    //Horizontally concatenate the index vector and the product
    //of L*U then pass that result into the 'sortc' function 
    //which will sort this result based upon the first column 
    //(which is the index vector)
    q = sortc(index~(L*U),1);
    
    //Remove the index vector, which we added by way of
    //horizontal concatenation in the statement just above
    x2 = q[.,2:cols(q)];

Now at the end of this example, x2 is equal to x.

.. seealso:: Functions :func:`crout`, :func:`chol`, :func:`lowmat`, :func:`lowmat1`, :func:`upmat`, :func:`upmat1`

computes crout decomposition row pivoting real matrices
