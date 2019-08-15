
subvec
==============================================

Purpose
----------------
Extracts an Nx1 vector of elements from an NxK matrix.

Format
----------------
.. function:: y = subvec(x, ci)

    :param x: data
    :type x: NxK matrix

    :param ci: column indices
    :type ci: Nx1 vector

    :return y: containing the elements in *x* indicated by *ci*.

    :rtype y: Nx1 vector

Remarks
-------

Each element of *y* is from the corresponding row of *x* and the column set
by the corresponding row of *ci*. In other words, :math:`y[i] = x[i, ci[i]]`.

Examples
----------------

::

    // Create an additive sequence from 1-12, i.e. 1, 2, 3,...12
    x = seqa(1, 1, 12);
    
    // Reshape the sequential vector 'x' into a 4x3 matrix
    x = reshape(x,4,3);
    
    // The column indices (one per row of 'x') indicating which
    // values to extract from 'x'
    ci = { 2, 3, 1, 3 };
    
    // Extract subvector from 'x' and assign it to 'y'
    y = subvec(x,ci);

After the above code, *x* and *y* are equal to:

::

         1  2  3
    x =  4  5  6
         7  8  9
        10 11 12
    
         2
     y = 6
         7
        12

