
qqr
==============================================

Purpose
----------------
Computes the orthogonal-triangular (QR) decomposition of a matrix x, such that:
X = Q1R

Format
----------------
.. function:: qqr(x)

    :param x: 
    :type x: NxP matrix

    :returns: q1 (*NxK unitary matrix*), K = min(N,P).

    :returns: r (*TODO*), KxP upper triangular matrix.



Remarks
-------

Given X, there is an orthogonal matrix Q such that Q'x is zero below its
diagonal, i.e.,

::

   Q′X=[R0]

where R is upper triangular. If we partition

::

   Q⁢ = [ Q1Q2⁢]

where Q\ 1 has P columns, then

::

   X⁢= Q1⁢ R

is the QR decomposition of X. If X has linearly independent columns, R
is also the Cholesky factorization of the moment matrix of X, i.e., of
X'X.

If you want only the R matrix, see the function qr. Not computing Q\ 1
can produce significant improvements in computing time and memory usage.

An unpivoted R matrix can also be generated using cholup:

::

   r = cholup(zeros(cols(x), cols(x)), x);

For linear equation or least squares problems, which require Q\ 2 for
computing residuals and residual sums of squares, see olsqr and qtyr.

For most problems an explicit copy of Q\ 1 or Q\ 2 is not required.
Instead one of the following, Q'Y, QY, Q\ 1'Y, Q\ 1\ Y, Q\ 2'Y, or
Q\ 2\ Y, for some Y, is required. These cases are all handled by qtyr
and qyr. These functions are available because Q and Q\ 1 are typically
very large matrices while their products with Y are more manageable.

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
                                                                    
                                                               
                                                           
                                                           ⁢
                                                            
                                                            
                                                           
                                                               
                                                                   R
                                                               
                                                               
                                                                   2
                                                               
                                                           
                                                       
                                                   
                                                   ]
                                               
                                           
                                       
                                   
                               
                           
                       
                   
               

where R\ 1 is a PxP upper triangular matrix and R\ 2 is Px(N-P). Thus Q
is a PxP matrix and R is a PxN matrix containing R\ 1 and R\ 2. This
type of factorization is useful for the solution of underdetermined
systems. However, unless the linearly independent columns happen to be
the initial rows, such an analysis also requires pivoting (see qre and
qrep).



Source
------

qqr.src

