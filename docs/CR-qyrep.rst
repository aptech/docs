
qyrep
==============================================

Purpose
----------------

Computes the orthogonal-triangular (QR) decomposition of a matrix X using a pivot vector
 and returns QY and R.                      

Format
----------------
.. function:: qyrep(y, x, pvt)

    :param y: 
    :type y: NxL matrix

    :param x: 
    :type x: NxP matrix

    :param pvt: controls the selection of the pivot
        columns:
    :type pvt: Px1 vector

    .. csv-table::
        :widths: auto

        "if   pvt[i] > 0, x[i] is an initial column."
        "if pvt[i] = 0, x[i] is a free column."
        "if   pvt[i] < 0, x[ i] is a final column."
        "The initial columns are placed at the beginning of the matrix and the final columns are placed at the end. Only the free columns will be moved during the decomposition."

    :returns: qy (*NxL unitary matrix*) .

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

qyrep allows you to control the pivoting. For example, suppose that X is
a data set with a column of ones in the first column. If there are
linear dependencies among the columns of X, the column of ones for the
constant may get pivoted away. This column can be forced to be included
among the linearly independent columns using pvt.

For most problems Q or Q\ 1 is not what is required. Since Q can be a
very large matrix, qyrep has been provided for the calculation of QY,
where Y is some NxL matrix, which will be a much smaller matrix.

If either Q'Y or Q\ 1'Y are required, see qtyrep.

If N<P, the factorization assumes the form:

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
                                   
                               
                           
                       
                   
                   

where R\ 1\ :sub:` ` is a PxP upper triangular matrix andR\ 2 is
Px(N-P). Thus Q is a PxP matrix and R is a PxN matrix containing R\ 1
and R\ 2.



Source
------

qyr.src

.. seealso:: Functions :func:`qr`, :func:`qqrep`, :func:`qrep`, :func:`qtyrep`
