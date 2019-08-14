
qz
==============================================

Purpose
----------------

Compute the complex QZ, or generalized Schur, form of a pair of real or complex general matrices with an option to sort the eigenvalues.

Format
----------------
.. function:: { S, T, Q, Z } = qz(A, B[, sort_type])

    :param A: real or complex general matrix
    :type A: NxN matrix

    :param B: real or complex general matrix
    :type B: NxN matrix

    :param sort_type: Optional input, specifying how to sort the eigenvalues. Options include:

        == ====== ===============================
        1  "udi"  Absolute value of the eigenvalue less than 1.0. (Unit disk inside)
        2  "udo"  Absolute value of the eigenvalue greater than or equal to 1.0. (Unit disk outside)
        3  "lhp"  Value of the real portion of the eigenvalue less than 0. (Left hand plane)
        4  "rhp"  Value of the real portion of the eigenvalue greater than 0. (Right hand plane)
        5  "ref"  Real eigenvalues first. (Complex portion less than imagtol see remarks section)
        6  "cef"  Complex eigenvalues first. (Complex portion greater than imagtol see remarks section)
        == ====== ===============================

    :type sort_type: scalar or string 

    :return S: Schur form of *A*

    :type S: NxN matrix

    :return T: Schur form of *B*

    :type T: NxN matrix

    :return Q: left Schur vectors

    :type Q: NxN matrix

    :return Z: right Schur vectors

    :type Z: NxN matrix

Remarks
-------

-  The pair of matrices *S* and *T* are in generalized complex Schur form if
   *S* and *T* are upper triangular and the diagonal of *T* contains positive
   real numbers.

-  The real generalized eigenvalues can be computed by dividing the
   diagonal element of S by the corresponding diagonal element of *T*.

-  The generalized Schur vectors *Q* and *Z* are orthogonal matrices (:math:`Q'Q = I`
   and :math:`Z'Z = I`) that reduce *A* and *B* to Schur form:

   .. math::

       S = Q'A*Z
       T = Q'B*Z

       A = Q*S*Z'
       B = Q*T*Z'      

-  For the real generalized schur decomposition, call :func:`lapgschur`.

-  If only the generalized eigenvalues are needed, you can call :func:`lapgeig`, or :func:`lapgeigv`.

-  By default *imagtol* is set to 2.23e-16. If your program requires
   *imagtol* to be a different value, you may change it using :func:`sysstate`
   case 21, like this:

   ::

       // Set imagtol to 1e-15   
       imagtol_org = sysstate(21, 1e-15);

   Note that while the function :func:`qz` IS threadsafe, setting *imagtol* is NOT
   threadsafe. Therefore, *imagtol* should not be changed inside of a
   `threadStat` or `threadBegin` block.

-  This procedure calls the *LAPACK* routine ``ZGGES``.

Examples
----------------

Basic usage
+++++++++++

::

    // For repeatable random numbers
    rndseed 23434;
    
    // Matrix dimensions
    order = 4;
    
    // Create 2 square, real matricies
    A = rndn(order, order);
    B = rndn(order, order);
    
    // Perform 'QZ' decomposition
    { S, T, Q, Z } =  qz(A,B);
    
    // Calculate generalized eigenvalues
    eig_vals = diag(S) ./ diag(T);
    
    print "Generalized eigenvalues = ";
    print eig_vals;
    
    print "Absolute value of the generalized eigenvalues = ";
    print abs(eig_vals);

The above code should return the following output:

::

    Generalized eigenvalues = 
    
    	   20.703871 -    1.9686543e-16i 
          0.16170711 -    1.6939178e-17i 
    	 -0.83402664 -       0.34681937i 
    	 -0.83402664 +       0.34681937i 
    
    Absolute value of the generalized eigenvalues = 
    
    	 20.703871 
    	0.16170711 
    	0.90326303 
    	0.90326303

Ordering eigenvalues
++++++++++++++++++++

You can order the eigenvalues, by passing in the optional third input, *sort_type*. The code below 
uses the same *A* and *B* variables made in the example above.

::

    // Perform 'QZ' decomposition and
    // reorder generalized eigenvalues, placing
    // those with absolute value less than 1
    // on the upper left
    { S, T, Q, Z } =  qz(A, B, "udi");
    
    // Calculate generalized eigenvalues
    eig_vals = diag(S) ./ diag(T);
    
    print "Generalized eigenvalues = ";
    print (eig_vals);
    
    print "Absolute value of the generalized eigenvalues = ";
    print abs(eig_vals);

The code above should print out the sorted eigenvalues as we see below.

::

    Generalized eigenvalues = 
    
    	 0.16170711 -    1.6819697e-17i 
    	-0.83402664 -       0.34681937i 
    	-0.83402664 +       0.34681937i 
    	  20.703871 -    2.1311282e-14i 
    
    Absolute value of the generalized eigenvalues = 
    
    	0.16170711 
    	0.90326303 
    	0.90326303 
    	 20.703871

