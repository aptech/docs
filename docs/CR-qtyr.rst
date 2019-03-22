
qtyr
==============================================

Purpose
----------------

Computes the orthogonal-triangular (QR) decomposition of a matrix X and returns
            Q'Y and R.

Format
----------------
.. function:: qtyr(y, X)

    :param y: 
    :type y: NxL matrix

    :param X: 
    :type X: NxP matrix

    :returns: qty (*NxL unitary matrix*) .

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
X'X. For most problems Q or Q\ 1 is not what is required. Rather, we
require Q'Y or Q\ 1'Y where Y is an NxL matrix (if either QY or Q\ 1\ Y
are required, see qyr). Since Q can be a very large matrix, qtyr has
been provided for the calculation of Q'Y which will be a much smaller
matrix. Q\ 1'Y will be a submatrix of Q'Y. In particular,

::

                   
                       
                           
                               
                                   
                                       
                                           G
                                           ⁢
                                           
                                               
                                                   =
                                                    
                                                   
                                                       
                                                           
                                                               
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

                   
                       
                           
                               
                                   
                                       
                                           H
                                           ⁢
                                           
                                               
                                                   =
                                                    
                                                   
                                                       
                                                           
                                                               
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
                                       
                                   
                               
                           
                       
                   
               

Suppose that X is an NxK data set of independent variables, and Y is an
Nx1 vector of dependent variables. Then it can be shown that

::

                   
                       
                           
                               
                                   
                                       
                                           b
                                           ⁢
                                           
                                               
                                                   =
                                                    
                                                   
                                                       
                                                           
                                                               
                                                                   R
                                                               
                                                               
                                                                   −
                                                                   1
                                                               
                                                           
                                                           G
                                                       
                                                   
                                               
                                           
                                       
                                   
                               
                           
                       
                   
               

and

::

   sj= N−PΣi=1⁢Hi,j,⁢j = 1,2,...L

where b is a PxL matrix of least squares coefficients and s is a 1xL
vector of residual sums of squares. Rather than invert R directly,
however, it is better to apply qrsol to

::

   Rb⁢= Q1′Y

For rank deficient least squares problems, see qtyre and qtyrep.


Examples
----------------
The QR algorithm is the numerically superior method for the solution of least squares problems:

::

    loadm x, y;
    { qty, r } = qtyr(y,x);
    q1ty = qty[1:rows(r),.];
    q2ty = qty[rows(r)+1:rows(qty),.];
    
    //LS coefficients 
    b = qrsol(q1ty,r);
    
    //Residual sums of squares 
    s2 = sumc(q2ty^2);

Source
------

qtyr.src

.. seealso:: Functions :func:`qqr`, :func:`qtyre`, :func:`qtyrep`, :func:`olsqr`

QR decomposition returns Q'Y R
