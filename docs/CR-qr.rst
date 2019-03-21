
qr
==============================================

Purpose
----------------
Computes the orthogonal-triangular (QR) decomposition of a matrix x, such that:
 X = Q1R

Format
----------------
.. function:: qr(x)

    :param x: 
    :type x: NxP matrix

    :returns: r (*KxP upper triangular matrix*), K = min(N,P).



Remarks
-------

qr is the same as qqr but doesn't return the Q\ 1 matrix. If Q\ 1 is not
wanted, qr will save a significant amount of time and memory usage,
especially for large problems.

Given X, there is an orthogonal matrix Q such that Q'X is zero below its
diagonal, i.e.,

::

                   
                       
                           
                               
                                   
                                       
                                           Q
                                           ′
                                           X
                                           
                                               
                                                    
                                                   =
                                                    
                                                   
                                                       [
                                                       
                                                           
                                                               
                                                                   
                                                                       
                                                                           R
                                                                       
                                                                   
                                                               
                                                           
                                                           
                                                               
                                                                   0
                                                               
                                                           
                                                       
                                                       ]
                                                   
                                               
                                           
                                       
                                   
                               
                           
                       
                   
               

where R is upper triangular. If we partition

::

                   
                       
                           
                               
                                   
                                       
                                           Q
                                           
                                               
                                                    
                                                   =
                                                    
                                                   
                                                       [
                                                       
                                                           
                                                               
                                                                   
                                                                       Q
                                                                   
                                                                   
                                                                       1
                                                                   
                                                               
                                                               ⁢
                                                                
                                                               
                                                                   
                                                                        
                                                                       Q
                                                                   
                                                                   
                                                                       2
                                                                   
                                                               
                                                           
                                                       
                                                       ]
                                                   
                                               
                                           
                                       
                                   
                               
                           
                       
                   
               

where Q\ 1 has P columns, then

::

                   
                       
                           
                               
                                   
                                       
                                           X
                                           ⁢
                                           
                                               
                                                   =
                                                    
                                                   
                                                       
                                                           
                                                               
                                                                   Q
                                                               
                                                               
                                                                   1
                                                               
                                                           
                                                           ⁢
                                                           R
                                                       
                                                   
                                               
                                           
                                       
                                   
                               
                           
                       
                   
               

is the QR decomposition of X. If X has linearly independent columns, R
is also the Cholesky factorization of the moment matrix of X, i.e., of
X'X.

qr does not return the Q\ 1 matrix because in most cases it is not
required and can be very large. If you need the Q\ 1 matrix, see the
function qqr. If you need the entire Q matrix, call qyr with Y set to a
conformable identity matrix.

For most problems Q'Y, Q\ 1'Y, or QY, Q\ 1\ Y, for some Y, are required.
For these cases see qtyr and qyr.

For linear equation or least squares problems, which require Q\ 2 for
computing residuals and residual sums of squares, see olsqr.

If N<P, the factorization assumes the form:

::

                   
                       
                           
                               
                                   
                                       
                                           Q
                                           ′
                                           X
                                           ⁢
                                           
                                               
                                                   =
                                                    
                                                   
                                                       [
                                                        
                                                        
                                                        
                                                       
                                                           
                                                               
                                                                   
                                                                       R
                                                                   
                                                                   
                                                                       1
                                                                   
                                                               
                                                               ⁢
                                                                
                                                                
                                                               
                                                                   
                                                                       R
                                                                   
                                                                   
                                                                       2
                                                                   
                                                               
                                                           
                                                       
                                                       ⁢
                                                        
                                                        
                                                       ]
                                                   
                                               
                                           
                                       
                                   
                               
                           
                       
                   
               

where R\ 1 is a PxP upper triangular matrix and R\ 2 is Px(N-P). Thus Q
is a PxP matrix and R is a PxN matrix containing R\ 1 and R\ 2. This
type of factorization is useful for the solution of underdetermined
systems. However, unless the linearly independent columns happen to be
the initial rows, such an analysis also requires pivoting (see qre and
qrep).

