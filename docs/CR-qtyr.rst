
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

    :returns: qty (*TODO*), NxL unitary matrix.

    :returns: r (*KxP upper triangular matrix*), K = min(N,P).

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
++++++

qtyr.src

.. seealso:: Functions :func:`qqr`, :func:`qtyre`, :func:`qtyrep`, :func:`olsqr`

QR decomposition returns Q'Y R
