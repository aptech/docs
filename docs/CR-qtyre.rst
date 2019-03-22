
qtyre
==============================================

Purpose
----------------

Computes the orthogonal-triangular (QR) decomposition of a matrix X and returns
Q'Y and R.

Format
----------------
.. function:: qtyre(y, x)

    :param y: 
    :type y: NxL matrix

    :param x: 
    :type x: NxP matrix

    :returns: qty (*NxL unitary matrix*) .

    :returns: r (*KxP upper triangular matrix*), K = min(N,P).

    :returns: e (*Px1 permutation vector*) .



Remarks
-------

Given X[.,E], where E is a permutation vector that permutes the columns
of X, there is an orthogonal matrix Q such that Q'X[.,E] is zero below
its diagonal, i.e.,

::

                   
                       
                           
                               
                                   
                                       
                                           Q
                                           ′
                                           X
                                           
                                               
                                                    
                                                   
                                                       [
                                                       .
                                                       ⁢
                                                       ,
                                                        
                                                       
                                                           
                                                               E
                                                           
                                                       
                                                       ]
                                                   
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
                                       
                                   
                                   
                                       
                                           
                                               [
                                               .
                                               ⁢
                                                
                                               ,
                                                
                                               
                                                   
                                                       E
                                                   
                                               
                                               ]
                                                
                                               =
                                                
                                               
                                                   
                                                       
                                                           
                                                               Q
                                                           
                                                           
                                                               1
                                                           
                                                       
                                                       ⁢
                                                        
                                                       R
                                                   
                                               
                                           
                                       
                                   
                               
                           
                       
                   
               

is the QR decomposition of X[.,E].

If X has rank P, then the columns of X will not be permuted. If X has
rank M<P, then the M linearly independent columns are permuted to the
front of X by E. Partition the permuted X in the following way:

::

   X[.⁢ , E] = [  X1⁢   X2⁢ ]

where X\ 1 is NxM and X\ 2 is Nx(P-M). Further partition R in the
following way:

::

                   
                       
                           
                               
                                   
                                       
                                           R
                                           ⁢
                                           
                                               
                                                   =
                                                    
                                                   
                                                       [
                                                       
                                                           
                                                               
                                                                   
                                                                       
                                                                           
                                                                               
                                                                                   R
                                                                               
                                                                               
                                                                                   
                                                                                       
                                                                                           11
                                                                                       
                                                                                   
                                                                               
                                                                           
                                                                       
                                                                   
                                                               
                                                               
                                                                   
                                                                       
                                                                           
                                                                               
                                                                                   R
                                                                               
                                                                           
                                                                       
                                                                       
                                                                           12
                                                                       
                                                                   
                                                               
                                                           
                                                           
                                                               
                                                                   0
                                                               
                                                               
                                                                   0
                                                               
                                                           
                                                       
                                                       ]
                                                   
                                               
                                           
                                       
                                   
                               
                           
                       
                     

where R\ 11 is MxM and R\ 12 is Mx(P-M). Then

::

                   
                       
                           
                               
                                   
                                       
                                           A
                                       
                                   
                                   
                                       
                                            
                                           =
                                            
                                           
                                               
                                                   
                                                       
                                                           
                                                               
                                                                   R
                                                               
                                                               
                                                                   −
                                                                   1
                                                               
                                                           
                                                       
                                                       
                                                           11
                                                       
                                                   
                                                   ⁢
                                                    
                                                   
                                                       
                                                           R
                                                       
                                                       
                                                           12
                                                       
                                                   
                                               
                                           
                                       
                                   
                               
                           
                       
                   
               

and

::

                   
                       
                           
                               
                                   
                                       
                                           
                                               
                                                   X
                                               
                                               
                                                   2
                                               
                                           
                                           ⁢
                                           
                                               
                                                   =
                                                    
                                                   
                                                       
                                                           
                                                               
                                                                   X
                                                               
                                                               
                                                                   1
                                                               
                                                           
                                                           ⁢
                                                            
                                                            
                                                           A
                                                       
                                                   
                                               
                                           
                                       
                                   
                               
                           
                       
                   
               

that is, A is an Mx(P-N) matrix defining the linear combinations of X\ 2
with respect to X\ 1.

For most problems Q or Q\ 1 is not it is required. Rather, we require
Q'Y or Q\ 1'Y where Y is an NxL matrix. Since Q can be a very large
matrix, qtyre has been provided for the calculation of Q'Y which will be
a much smaller matrix. Q\ 1'Y will be a submatrix of Q'Y. In particular,

::

                   
                       
                           
                               
                                   
                                       
                                           
                                               
                                                    
                                                   
                                                       
                                                           
                                                               
                                                                   Q
                                                               
                                                               
                                                                   1
                                                               
                                                           
                                                           ′
                                                           Y
                                                           
                                                               
                                                                    
                                                                   =
                                                                    
                                                                   
                                                                       
                                                                           q
                                                                           t
                                                                           y
                                                                       
                                                                   
                                                               
                                                           
                                                       
                                                   
                                               
                                           
                                       
                                   
                                   
                                       
                                           [
                                           
                                               
                                                   
                                                       
                                                           1
                                                           :
                                                       
                                                   
                                                   P
                                                   
                                                       
                                                           ,
                                                           .
                                                       
                                                   
                                               
                                           
                                           ]
                                       
                                   
                               
                           
                       
                   
               

and Q\ 2'Y is the remaining submatrix:

::

                   
                       
                           
                               
                                   
                                       
                                           ⁢
                                           
                                               
                                                    
                                                   
                                                       
                                                           
                                                               
                                                                   Q
                                                               
                                                               
                                                                   2
                                                               
                                                           
                                                           ′
                                                           Y
                                                           
                                                               
                                                                    
                                                                   =
                                                                    
                                                                   
                                                                       
                                                                           q
                                                                           t
                                                                           y
                                                                       
                                                                   
                                                               
                                                           
                                                       
                                                   
                                               
                                           
                                       
                                   
                                   
                                       
                                           [
                                           
                                               
                                                   P
                                                   
                                                       
                                                           +
                                                           1
                                                           :
                                                       
                                                   
                                                   N
                                                   
                                                       
                                                           ,
                                                           .
                                                       
                                                   
                                               
                                           
                                           ]
                                       
                                   
                               
                           
                       
                   
               

Suppose that X is an NxK data set of independent variables and Y is an
Nx1 vector of dependent variables. Suppose further that X contains
linearly dependent columns, i.e., X has rank M < P. Then define

::

                   
                       
                           
                               
                                   
                                       
                                           C
                                           ⁢
                                           
                                               
                                                   =
                                                    
                                                   
                                                       
                                                           
                                                               
                                                                   Q
                                                               
                                                               
                                                                   1
                                                               
                                                           
                                                           ′
                                                           Y
                                                           
                                                               
                                                                   
                                                                       [
                                                                       1
                                                                       :
                                                                       
                                                                           
                                                                               M
                                                                               
                                                                                   
                                                                                       ,
                                                                                       .
                                                                                   
                                                                               
                                                                           
                                                                       
                                                                       ]
                                                                   
                                                               
                                                           
                                                       
                                                   
                                               
                                           
                                       
                                   
                               
                           
                       
                   
                   A⁢= R[1:M,1:M]

and the vector (or matrix of L > 1) of least squares coefficients of the
reduced, linearly independent problem is the solution of

::

                   
                       
                           
                               
                                   
                                       
                                           A
                                           b
                                           ⁢
                                           
                                               
                                                   =
                                                    
                                                   
                                                       
                                                           C
                                                       
                                                   
                                               
                                           
                                       
                                   
                               
                           
                       
                   
               

To solve for b use qrsol:

::

   b = qrsol(C, A);

If N < P, the factorization assumes the form:

::

                   
                       
                           
                               
                                   
                                       
                                           Q
                                           ′
                                           X
                                           
                                               
                                                    
                                                   
                                                       [
                                                       .
                                                       ⁢
                                                       ,
                                                        
                                                       
                                                           
                                                               E
                                                           
                                                       
                                                       ]
                                                   
                                                   =
                                                    
                                                   
                                                       [
                                                       
                                                           
                                                               
                                                                   
                                                                       R
                                                                   
                                                                   
                                                                       1
                                                                   
                                                               
                                                               ⁢
                                                                
                                                                
                                                               
                                                                   
                                                                       R
                                                                   
                                                                   
                                                                       2
                                                                   
                                                               
                                                           
                                                       
                                                       ]
                                                   
                                               
                                           
                                       
                                   
                               
                           
                       
                   
               

where R\ 1 is a PxP upper triangular matrix and R\ 2 is Px(N-P). Thus Q
is a PxP matrix and R is a PxN matrix containing R\ 1 and R\ 2. This
type of factorization is useful for the solution of underdetermined
systems. For the solution of

::

                   
                       
                           
                               
                                   
                                       
                                           X
                                       
                                   
                                   
                                       
                                           [
                                           .
                                           ⁢
                                            
                                           ,
                                            
                                           
                                               
                                                   E
                                               
                                           
                                           ]
                                           
                                               b
                                           
                                            
                                           =
                                           
                                               Y 
                                           
                                       
                                   
                               
                           
                       
                   
               

it can be shown that

::

   b = qrsol(Q'Y, R1)|zeros(N-P,1);



Source
------

qtyr.src

