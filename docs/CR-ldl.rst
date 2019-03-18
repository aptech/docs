
ldl
==============================================

Purpose
----------------

Returns the L and D factors of the LDL' (or LDLT) factorization of a real symmetric matrix.

Format
----------------
.. function:: ldl(A)

    :param A: NxN real symmetric matrix.
    :type A: TODO

    :returns: L (*NxN permuted*), lower triangular matrix, containing the factor L.

    :returns: D (*NxN block diagonal matrix*), containing the factor D.

Examples
----------------

A = { 5   9   3   4, 
      9  -6   8   1, 
      3   8   2   3, 
      4   1   3   9 };

//Factorize matrix 'A'
{ L, D } = ldl(A);

A_new = L * D *  L';
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    -1.50     1.00     0.00     0.00 
    L =     1.00     0.00     0.00     0.00 
           -1.33     0.81     1.00     0.00 
           -0.17     0.30    -0.25     1.00     
        
           -6.00     0.00     0.00     0.00 
    D =     0.00    18.50     0.00     0.00 
            0.00     0.00     0.50     0.00 
            0.00     0.00     0.00     7.50  
               
            5.00     9.00     3.00     4.00 
    A_new = 9.00    -6.00     8.00     1.00 
            3.00     8.00     2.00     3.00 
            4.00     1.00     3.00     9.00

Permuted L matrix
+++++++++++++++++

::

    // Create 5x5 matrix
    A = { 8.2990  -2.7560   2.3840   3.4980   0.7520, 
         -2.7560   2.2370  -2.7400   1.2930  -1.2740, 
          2.3840  -2.7400   6.7890  -0.9610   0.1600, 
          3.4980   1.2930  -0.9610   9.3570  -2.3780, 
          0.7520  -1.2740   0.1600  -2.3780   2.2210 };
    
    // Perform LDL decomposition 
    { L, D } = ldl(A);

After the code above, the permuted L and diagonal D equal:

::

    1        0        0        0        0 
         -0.3321   0.3114  -0.2380        1        0 
    L =   0.2873  -0.2494        1        0        0 
          0.4215        1        0        0        0 
          0.0906  -0.3419  -0.1297  -1.4970        1 
    
          8.2990        0        0        0        0 
          0        7.8826        0        0        0 
    D =   0             0   5.6139        0        0 
          0             0        0   0.2394        0 
          0             0        0        0   0.6006

.. seealso:: Functions :func:`ldlp`, :func:`ldlsol`, :func:`chol`, :func:`solpd`

Cholesky L D factor decomposition ldl factorization symmetric matrix
