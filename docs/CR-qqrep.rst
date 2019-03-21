
qqrep
==============================================

Purpose
----------------
Computes the orthogonal-triangular (QR) decomposition of a matrix x, such that:
 X[.,E] = Q1R

Format
----------------
.. function:: qqrep(x, pvt)

    :param x: 
    :type x: NxP matrix

    :param pvt: controls the selection of the pivot
        columns:
    :type pvt: Px1 vector

    .. csv-table::
        :widths: auto

        "if  pvt[i] > 0, x[i] is an initial column"
        "if   pvt[i] = 0, x[i] is a free column"
        "if   pvt[i] < 0, x[i] is a final column"
        "The initial columns are placed at the beginning of the matrix and the final columns are placedat the end. Only the free columns will be moved during the decomposition."

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
                                                   
                                               
                                           
                                       
                                   
                               
                           
                       
                   
               

| is the QR decomposition of X[.,E].

qqrep allows you to control the pivoting. For example, suppose that x is
a data set with a column of ones in the first column. If there are
linear dependencies among the columns of x, the column of ones for the
constant may get pivoted away. This column can be forced to be included
among the linearly independent columns using pvt.

If you want only the R matrix, see qrep. Not computing Q\ 1 can produce
significant improvements in computing time and memory usage.



Source
------

qqr.src

