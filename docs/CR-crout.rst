
crout
==============================================

Purpose
----------------

Computes the Crout decomposition
of a square matrix without row pivoting, such that:
X = LU.

Format
----------------
.. function:: crout(x)

    :param x: NxN square nonsingular matrix.
    :type x: TODO

    :returns: y (*TODO*), NxN matrix containing the lower (L) and upper
        (U) matrices of the Crout decomposition
        of x. The
        main diagonal of y is the main diagonal of the
        lower matrix  L. The upper matrix has an implicit main
        diagonal of ones. Use lowmat
        and upmat1 to extract the  L and  U matrices from y.

Examples
----------------

::

    X = { 1 2 -1,
          2 3 -2,
          1 -2 1 };
    
    //Perform crout decomposition
    y = crout(x);
    
    //Extract lower triangle of 'y' and assign it to 'L'
    L = lowmat(y);
    
    //Extract upper triangle of 'y', fill the diagonal with
    //ones and assign it to 'L'
    U = upmat1(y);

After the code above:

::

    1.0  2.0 -1.0       1.0  0.0  0.0       1.0  2.0 -1.0 
    y = 2.0 -1.0  0.0   L = 2.0 -1.0  0.0   U = 0.0  1.0  0.0 
        1.0 -4.0  2.0       1.0 -4.0  2.0       0.0  0.0  1.0

.. seealso:: Functions :func:`croutp`, :func:`chol`, :func:`lowmat`, :func:`lowmat1`, :func:`lu`, :func:`upmat`, :func:`upmat1`

computes crout decomposition real matrices
