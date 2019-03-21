
qqre
==============================================

Purpose
----------------
Computes the orthogonal-triangular (QR) decomposition of a matrix x, such that:
 X[.,E] = Q1R

Format
----------------
.. function:: qqre(x)

    :param x: 
    :type x: NxP matrix

    :returns: q1 (*NxK unitary matrix*), K = min(N,P).

    :returns: r (*TODO*), KxP upper triangular matrix.

    :returns: e (*TODO*), Px1 permutation vector.



Remarks
-------

Given X[.,E], where E is a permutation vector that permutes the columns
of X, there is an orthogonal matrix Q such that Q'X[.,E] is zero below
its diagonal, i.e.,

::

                   
                       
                           
                               
                                   
                                       
                                           Q
                                           ′
                                           R
                                           ⁢
                                           
                                               
                                                   
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

If you want only the R matrix, see qre. Not computing Q\ 1 can produce
significant improvements in computing time and memory usage.

If X has rank P, then the columns of X will not be permuted. If X has
rank M < P, then the M linearly independent columns are permuted to the
front of X by E. Partition the permuted X in the following way:

::

                   
                       
                           
                               
                                   
                                       
                                           X
                                       
                                   
                                   
                                       
                                           [
                                           .
                                           ⁢
                                            
                                           ,
                                            
                                           
                                               
                                                   E
                                               
                                           
                                           ]
                                            
                                           =
                                            
                                           
                                               [
                                                
                                                
                                               
                                                   
                                                       
                                                           
                                                               X
                                                           
                                                           
                                                               1
                                                           
                                                       
                                                       ⁢
                                                        
                                                        
                                                        
                                                       
                                                           
                                                               X
                                                           
                                                           
                                                               2
                                                           
                                                       
                                                   
                                               
                                               ⁢
                                                
                                                
                                               ]
                                           
                                       
                                   
                               
                           
                       
                   
               

where X is NxM and X\ 2 is Nx(P-M). Further partition R in the following
way:

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

If N < P, the factorization assumes the form:

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

The explicit formation here of Q, which can be a very large matrix, can
be avoided by using the function qtyre.

For further discussion of QR factorizations see the remarks under qqr.

