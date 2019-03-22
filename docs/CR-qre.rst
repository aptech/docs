
qre
==============================================

Purpose
----------------

Computes the orthogonal-triangular (QR) decomposition of a matrix x, such that: X[.,E] = Q1R

Format
----------------
.. function:: qre(x)

    :param x: 
    :type x: NxP matrix

    :returns: r (*KxP upper triangular matrix*), K = min(N,P).

    :returns: e (*Px1 permutation vector*) .



Remarks
-------

qre is the same as qqre but doesn't return the Q\ 1 matrix. If Q\ 1 is
not wanted, qre will save a significant amount of time and memory usage,
especially for large problems.

Given X[.,E], where E is a permutation vector that permutes the columns
of x, there is an orthogonal matrix Q such that Q'X[.,E] is zero below
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

qre does not return the Q\ 1 matrix because in most cases it is not
required and can be very large. If you need the Q\ 1 matrix, see the
function qqre. If you need the entire Q matrix, call qyre with Y set to
a conformable identity matrix. For most problems Q'Y, Q\ 1'Y, or QY,
Q\ 1\ Y, for some y, are required. For these cases see qtyre and qyre.

If X has rank P, then the columns of X will not be permuted. If X has
rank M<P, then the M linearly independent columns are permuted to the
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
                                                       
                                                   
                                               
                                           
                                       
                                   
                               
                           
                       
                   
               

where X\ 1 is NxM and X\ 2 is Nx(P-M). Further partition R in the
following way:

where R\ 11 is MxM and R\ 12 is Mx(P-M). Then

::

                   
                       
                           
                               
                                   
                                       
                                           A
                                           ⁢
                                           
                                               
                                                   =
                                                    
                                                   
                                                       
                                                           
                                                               
                                                                   
                                                                       
                                                                           R
                                                                       
                                                                       
                                                                           11
                                                                       
                                                                   
                                                               
                                                           
                                                       
                                                       
                                                           
                                                               −
                                                               1
                                                           
                                                       
                                                   
                                               
                                           
                                       
                                   
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
with respect to X\ 1

If N<P the factorization assumes the form:

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



Source
------

qr.src

