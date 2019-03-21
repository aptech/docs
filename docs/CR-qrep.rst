
qrep
==============================================

Purpose
----------------
Computes the orthogonal-triangular (QR) decomposition of a matrix X, such that:

X[.,E] = Q1R

Format
----------------
.. function:: qrep(X, pvt)

    :param X: 
    :type X: NxP matrix

    :param pvt: controls the selection of the pivot columns:
    :type pvt: Px1 vector

    .. csv-table::
        :widths: auto

        "if pvt[i] > 0, X[i] is an initial column."
        "if pvt[i] = 0, X[i] is a free column."
        "if pvt[i] < 0, X[i] is a final column."
        "The initial columns are placed at the beginningof the matrix and the final columns are placedat the end. Only the free columns will be movedduring the decomposition."

    :returns: r (*KxP upper triangular matrix*), K = min(N,P).

    :returns: e (*TODO*), Px1 permutation vector.



Remarks
-------

qrep is the same as qqrep but doesn't return the Q\ 1 matrix. If Q\ 1 is
not wanted, qrep will save a significant amount of time and memory
usage, especially for large problems.

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

qrep does not return the Q\ 1 matrix because in most cases it is not
required and can be very large. If you need the Q\ 1 matrix, see the
function qqrep. If you need the entire Q matrix, call qyrep with Y set
to a conformable identity matrix. For most problems Q'Y, Q\ 1'Y, or QY,
Q\ 1\ Y, for some Y, are required. For these cases see qtyrep and qyrep.

qrep allows you to control the pivoting. For example, suppose that X is
a data set with a column of ones in the first column. If there are
linear dependencies among the columns of X, the column of ones for the
constant may get pivoted away. This column can be forced to be included
among the linearly independent columns using pvt.

