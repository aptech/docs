
qyre
==============================================

Purpose
----------------

Computes the orthogonal-triangular (QR) decomposition of a matrix x and returns
            QY and R.                                  

Format
----------------
.. function:: qyre(y, x)

    :param y: 
    :type y: NxL matrix

    :param x: 
    :type x: NxP matrix

    :returns: qy (*TODO*), NxL unitary matrix.

    :returns: r (*KxP upper triangular matrix*), K = min(N,P).

    :returns: e (*TODO*), Px1 permutation vector.



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

For most problems Q or Q\ 1 is not what is required. Since Q can be a
very large matrix, qyre has been provided for the calculation of QY,
where Y is some NxL matrix, which will be a much smaller matrix.

If either Q'Y or Q\ 1'Y are required, see qtyre.

If N <P, the factorization assumes the form:

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
                                                   
                                               
                                           
                                       
                                   
                                   ⁢
                                   =
                                    
                                   
                                       [
                                       
                                           
                                               
                                                   
                                                       R
                                                   
                                                   
                                                       1
                                                   
                                               
                                               
                                                   
                                                        
                                                       R
                                                   
                                                   
                                                       2
                                                   
                                               
                                           
                                       
                                       ]
                                   
                               
                           
                       
                   
               

where R\ 1 is a PxP upper triangular matrix and R\ 2 is Px(N-P). Thus Q
is a PxP matrix and R is a PxN matrix containing R\ 1 and R\ 2.



Source
------

qyr.src

