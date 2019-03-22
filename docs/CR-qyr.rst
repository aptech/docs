
qyr
==============================================

Purpose
----------------
Computes the orthogonal-triangular (QR) decomposition of a matrix X and returns
            QY and R.

Format
----------------
.. function:: qyr(y, x)

    :param y: 
    :type y: NxL matrix

    :param X: 
    :type X: NxP matrix

    :returns: qy (*NxL unitary matrix*) .

    :returns: r (*KxP upper triangular matrix*), K = min(N,P).



Remarks
-------

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

For most problems Q or Q\ 1 is not what is required. Since Q can be a
very large matrix, qyr has been provided for the calculation of QY,
where Y is some NxL matrix, which will be a much smaller matrix.

If either Q'Y or Q\ 1'Y are required, see qtyr.



Source
------

qyr.src

.. seealso:: Functions :func:`qqr`, :func:`qyre`, :func:`qyrep`, :func:`olsqr`
