
schur
==============================================

Purpose
----------------
Computes the real or complex Schur form of a square matrix with the option to sort the eigenvalues.

Format
----------------
.. function:: { S, Z } = schur(A[, flag[, sort_type]])

    :param A: data
    :type A: KxK matrix

    :param flag: Optional input, to control whether output should be in real or complex Schur form. Valid options include: 

        - "complex"
        - "real"

    :type flag: string

    :param sort_type: Optional input, specifying how to sort the eigenvalues. Options include:

        === ====== ===========================================================
        1   "udi"  Absolute value of the eigenvalue less than 1.0. (Unit disk inside)
        2   "udo"  Absolute value of the eigenvalue greater than or equal to 1.0. (Unit disk outside)
        3   "lhp"  Value of the real portion of the eigenvalue less than 0. (Left hand plane)
        4   "rhp"  Value of the real portion of the eigenvalue greater than 0. (Right hand plane)
        5   "ref"  Real eigenvalues first. (Complex portion less than imagtol see remarks section)
        6   "cef"  Complex eigenvalues first. (Complex portion greater than imagtol see remarks section)
        === ====== ===========================================================

    :type sort_type: string 

    :return S: Schur form.

    :rtype S: KxK matrix

    :return Z: transformation matrix.

    :rtype Z: KxK matrix

Examples
----------------

Real matrix with all real eigenvalues
+++++++++++++++++++++++++++++++++++++

::

    // Create a 2 x 2 matrix
    A = { 7 -2, 
         12 -5 };
    
    // Calculate eigenvalues of 'A'
    lambda = eig(A);

After the code above, *lambda* should equal:

::

     4.4641
    -2.4641

::

    // Continuing with 'A' from above
    { S, Z } = schur(A);

Now *S* and *Z* should equal:

::

    S = 4.4641   -14.000  Z =  0.6193   -0.7852 
             0   -2.4641       0.7852    0.6193

Real matrix with some complex eigenvalues
+++++++++++++++++++++++++++++++++++++++++

::

    // Create a 3 x 3 matrix
    A = {  1  -4  -1, 
           3  -1   9, 
          -9   1  -2 };
    
    // Calculate real schur form, with complex eigenvalues
    // stored as 2 x 2 blocks on the diagonal
    { S_r, Z_r } = schur(A, "real");
    
    // Calculate complex schur form
    { S_c, Z_c } = schur(A, "complex");

After the code above:

::

    S_r = -7.2208   8.6875   -1.7726
          -4.4007  -1.1773    1.5989 
                0        0    6.3981
    
    Z_r = -0.1304  0.7105 -0.6915 
           0.6913  0.5651  0.4502 
          -0.7107  0.4193  0.5649
    
    S_c = -4.1991+5.3945i  -2.5084+6.9720i   1.0168-0.7763i 
                     0+0i  -4.1991-5.3945i   1.9825-0.3630i 
                     0+0i             0+0i        6.3981+0i 
    
    Z_c =  0.3275 -   0.1759i   0.5326 +   0.3160i  -0.6915             
           0.1102 -   0.7700i   0.0023 +   0.4385i   0.4502             
           0.3132 +   0.3984i   0.6502 +   0.0373i   0.5649

Complex matrix with sorted eigenvalues
++++++++++++++++++++++++++++++++++++++

::

    // Create a 3 x 3 complex matrix
    A = { -1.9615 + 0.4382i   0.0655 + 0.6913i  -1.1424 + 0.1997i, 
           0.1244 + 0.3783i  -0.2821 + 0.0588i   0.4854 + 0.4700i, 
           1.1271 + 0.7045i  -1.5245 - 0.9966i   1.4969 + 0.4450i };
    
    // Place eigenvalues in unit circle at top-left
    { S, Z } = schur(A, "complex", "udi");

After the code above:

::

         -0.3548 +   0.8005i   2.4873 -   0.4942i  -1.3144 +   0.7286i 
    S =   0.0000               1.0504 -   0.5581i   0.1763 +   0.7846i 
          0.0000               0.0000              -1.4423 +   0.6996i 
    
          0.3692 -   0.2393i  -0.0144 +   0.2838i   0.5890 -   0.6155i 
    Z =  -0.3907 +   0.2625i   0.5407 -   0.5251i   0.4161 -   0.1930i 
         -0.7530 -   0.1336i  -0.5813 +   0.1154i   0.2225 -   0.1201i

Remarks
-------

If a real matrix is passed in without a flag variable, the real Schur
form will be returned. If a complex matrix is passed in without a flag
variable, GAUSS will check to see if any of the imaginary elements are
greater than *imagtol* (2.23e-16 by default). If any imaginary elements
are greater than *imagtol*, the complex Schur form will be calculated,
otherwise the real Schur form will be returned. If a real flag is passed
in with a complex matrix, the flag will be ignored and the complex Schur
factorization will be returned.

The real Schur form is an upper quasi-triangular matrix, that is, it is
block triangular where the blocks are 2x2 submatrices which correspond
to complex eigenvalues of *A*. If *A* has no complex eigenvalues, *S* will be
strictly upper triangular. To convert the real Schur form of *S* to the
complex Schur form, use the **Run-Time Library** function schtoc.

*Z* is an orthogonal matrix that transforms *A* into *S* and vice versa. Thus

::

   S = Z'*A*Z;

and since *Z* is orthogonal,

::

   A = Z*S*Z';

.. seealso:: Functions :func:`hess`, :func:`schtoc`

