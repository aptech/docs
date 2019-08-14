
sylvester
==============================================

Purpose
----------------
Computes the solution to the Sylvester matrix equation, :math:`AX + XB = C`.

Format
----------------
.. function:: X = sylvester(A, B, C)

    :param A: data
    :type A: MxM real or complex matrix

    :param B: data
    :type B: NxN real or complex  matrix

    :param C: data
    :type C: MxN real or complex matrix

    :return X: solution to the equation :math:`AX + XB = C`.

    :type X: MxN matrix

Examples
----------------

Real input
++++++++++

::

    // Create a 3 x 3 real matrix
    A = {  0.9069  -0.3150  -0.9732,
           0.6023   0.6848   0.4925,
          -0.8555  -0.7430   0.6521 };
          
    // Create a 2 x 2 real matrix
    B = { -0.9876   0.4503,
          -0.3043   0.9807 };
          
    // Create a 3 x 2 real matrix
    C = { -0.8625   0.5247,
           0.6331  -0.3334,
           0.7912   0.0711 };
    
    // Solve the Sylvester matrix equation
    X = sylvester(A, B, C);

After the code above, *X* will equal the 3x2 matrix:

::

    X =  -0.4279   0.3246 
         -1.0525  -0.0013 
          1.1609  -0.1071

Complex input
+++++++++++++

::

    // Create a 3 x 3 complex matrix
    A = { 7 + 7i     4 + 10i     2 + 8i,
         10 - 3i    -7 -  5i   -10 - 7i,
          3 + 5i   -10 -  2i     2 - 4i };
          
    // Create a 2 x 2 complex matrix
    B = { 5 +  1i    -5 - 8i,
          8 - 10i    8 - 1i };
          
    // Create a 3 x 2 complex matrix
    C = { -9 - 3i   -1 - 1i,
           9 - 8i   -5 + 8i,
          -1 - 2i   -5 + 5i };
    
    // Solve the Sylvester matrix equation
    X = sylvester(A, B, C);

After the code above, *X* will equal the 3x2 complex matrix:

::

    X =   0.1697 - 0.2242i    -0.5923 + 0.2221i 
         -0.5684 + 0.4562i     0.3670 - 0.7153i 
         -0.7502 + 0.2470i    -0.0636 - 0.4208i

Remarks
-------

The equation :math:`AX + XB = C` will not have a unique solution if the
eigenvalues of the matrices *A* and *-B* are equal. In this case an error
will be returned.

.. seealso:: Functions :func:`hess`, :func:`schur`

