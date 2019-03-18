
denseToSpRE
==============================================

Purpose
----------------

Converts a dense matrix to a sparse matrix, using a relative epsilon.

Format
----------------
.. function:: denseToSpRE(x,  reps)

    :param x: MxN dense matrix.
    :type x: TODO

    :param reps: relative epsilon. Elements of x will be treated as
        zero if their absolute values are less than or equal to  reps
        multiplied by the mean of the absolute values of the non-zero values in
        x.
    :type reps: scalar

    :returns: y (*TODO*), MxN sparse matrix.

Examples
----------------

::

    sparse matrix y;
    x = { -9   0   0    1,
           0   4   0    0,
           5   0   0    7,
           0   0  -2  2.2 };
    
    y = denseToSpRE(x,0.5);
    d = spToDense(y);

After the code above, d is equal to:

::

    -9.00   0.00   0.00   0.00 
      0.00   4.00   0.00   0.00 
      5.00   0.00   0.00   7.00 
      0.00   0.00   0.00   2.20

You can calculate the mean of the non-zero elements of x like this:

::

    //Create a matrix of 1's and 0's with a 1 where the
    //corresponding element in 'x' is not equal to 0
    mask = x ./= 0;
    
    //Calculate the sum of 'mask', this is the number of 
    //non-zeros in 'x'
    nnz = sumc(sumc(mask));
    
    //Divide the sum of the absolute value of 'x' by the number
    //of non-zeros
    nzmean = sumc(sumc(abs(x)))/nnz;

::

    nnz =       7
    nzmean = 4.31

The call to denseToSpRE towards the start of this example, removed all non-zeros less than 0.5*nzmean, or approximately 2.16.

.. seealso:: Functions :func:`denseToSp`, :func:`spCreate`, :func:`spToDense`
