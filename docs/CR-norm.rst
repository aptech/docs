
norm
==============================================

Purpose
----------------

			Computes one of several specified matrix norms, or a vector p-norm.

		

Format
----------------
.. function:: norm(A) 
			  norm(A, norm_type)

    :param A: 
    :type A: Nx1 vector or NxN matrix

    :param norm_type: specifying which norm to compute.
        Matrix norm options:
        
        
        
        
        1
        Scalar, equivalent to:  maxc(sumc(abs(x)))
        
        
        2
        Scalar, the spectral norm, equivalent to: maxc(svds(x))
        
        
        __INFP
        Scalar, the infinity norm, equivalent to: maxc(sumr(abs(x)))
        
        
        "fro"
        String, the Frobenius norm, equivalent to: sqrt(sumc(vecr(x.^2))).
        
        
        "nuc"
        String, the nuclear norm, equivalent to: sumc(svds(A)).
        
        
        
        Vector norm options:
        
        
        
        
        1
        Scalar, equivalent to:  sumcs(abs(x)) for column vectors, or sumr(abs(x)) for row vectors.
        
        
        2
        Scalar, the l2 or Euclidean norm, equivalent to: sqrt(sumc(x.^2)), or sqrt(sumr(x.^2))
        
        
        p
        Scalar, any real number, equivalent to: sumc(abs(x.^p)).^(1/p), or sumr(abs(x.^p)).^(1/p)
        
        
        __INFP
        Scalar, equivalent to: maxc(abs(x)), or maxc(abs(x'))
        
        
        __INFN
        Scalar, equivalent to: minc(abs(x)), or minc(abs(x'))
        1
        Scalar, equivalent to:  maxc(sumc(abs(x)))
        2
        Scalar, the spectral norm, equivalent to: maxc(svds(x))
        __INFP
        Scalar, the infinity norm, equivalent to: maxc(sumr(abs(x)))
        "fro"
        String, the Frobenius norm, equivalent to: sqrt(sumc(vecr(x.^2))).
        "nuc"
        String, the nuclear norm, equivalent to: sumc(svds(A)).
        1
        Scalar, equivalent to:  sumcs(abs(x)) for column vectors, or sumr(abs(x)) for row vectors.
        2
        Scalar, the l2 or Euclidean norm, equivalent to: sqrt(sumc(x.^2)), or sqrt(sumr(x.^2))
        p
        Scalar, any real number, equivalent to: sumc(abs(x.^p)).^(1/p), or sumr(abs(x.^p)).^(1/p)
        __INFP
        Scalar, equivalent to: maxc(abs(x)), or maxc(abs(x'))
        __INFN
        Scalar, equivalent to: minc(abs(x)), or minc(abs(x'))
    :type norm_type: Optional string or integer input

    :param 1: equivalent to:  maxc(sumc(abs(x)))
    :type 1: Scalar

    :param 2: the spectral norm, equivalent to: maxc(svds(x))
    :type 2: Scalar

    :param __INFP: the infinity norm, equivalent to: maxc(sumr(abs(x)))
    :type __INFP: Scalar

    :param "fro": the Frobenius norm, equivalent to: sqrt(sumc(vecr(x.^2))).
    :type "fro": String

    :param "nuc": the nuclear norm, equivalent to: sumc(svds(A)).
    :type "nuc": String

    :param 1: equivalent to:  sumcs(abs(x)) for column vectors, or sumr(abs(x)) for row vectors.
    :type 1: Scalar

    :param 2: the l2 or Euclidean norm, equivalent to: sqrt(sumc(x.^2)), or sqrt(sumr(x.^2))
    :type 2: Scalar

    :param p: any real number, equivalent to: sumc(abs(x.^p)).^(1/p), or sumr(abs(x.^p)).^(1/p)
    :type p: Scalar

    :param __INFP: equivalent to: maxc(abs(x)), or maxc(abs(x'))
    :type __INFP: Scalar

    :param __INFN: equivalent to: minc(abs(x)), or minc(abs(x'))
    :type __INFN: Scalar

    :returns: n (*Scalar*), the requested norm of  A

Examples
----------------

Matrix norms
++++++++++++

::

    // Create 4x3 matrix
    A = { 0.35148166       0.53337376      -0.91676553,
          0.89133334      0.099774011        1.1669254,
         -0.54380494      -0.52901019       0.38900312,
         -0.67434004       -1.1692513      -0.14388126 };
    
    // Matrix 1 norm
    n_1 = norm(A, 1);
    
    // Matrix spectral norm
    n_2 = norm(A, 2);
    
    // Matrix Infinity norm
    n_inf = norm(A, __INFP);
    
    // Matrix Frobenius norm
    n_fro = norm(A, "fro");
    
    // Matrix nuclear norm
    n_nuc = norm(A, "nuc");
    
    // Singular values of 'A'
    s = svds(A);

The above code will make the following assignments:

::

    n_1   = 2.6166     n_2   = 1.7835    n_inf = 2.1580
    n_fro = 2.4462     n_nuc = 3.8478
    
    s =   1.7835
          1.6121
          0.4522

Vector norms
++++++++++++

::

    // Column vector
    v = { 0.0502,
         -0.7841,
          0.5719,
         -0.8668 };
    
    // Vector 1 norm
    n_1 = norm(v, 1);
    
    // Vector Euclidean norm
    n_2 = norm(v, 2);
    
    // Vector p norm
    n_p = norm(v, 3);
    
    n_pos_inf = norm(v, __INFP);
    n_neg_inf = norm(v, __INFN);

The above code will make the following assignments:

::

    n_1       = 2.2730    n_2       = 1.3022    n_p = 1.0971
    n_pos_inf = 0.8668    n_neg_inf = 0.0502

::

    // Row vector
    vt = { -0.5396  -0.0972  -0.0176   1.0552 };
    
    // Vector 1 norm
    n_1 = norm(vt, 1);
    
    // Vector Euclidean norm
    n_2 = norm(vt, 2);
    
    // Vector p norm
    n_p = norm(vt, 3);
    
    n_pos_inf = norm(vt, __INFP);
    n_neg_inf = norm(vt, __INFN);

The above code will make the following assignments:

::

    n_1       = 1.7096    n_2       = 1.1893    n_p = 1.0005
    n_pos_inf = 1.0552    n_neg_inf = 0.0176

Remarks
+++++++

-  To compute the Euclidean norm of each column vector of a matrix,
   call:

   ::

      n = sqrt(dot(A, A));

.. seealso:: Functions :func:`detl`, :func:`dot`, :func:`rank`

complex QZ generalized Schur form real matrix sort eigenvalue
