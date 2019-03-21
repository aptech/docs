
spTScalar
==============================================

Purpose
----------------
Multiplies a sparse matrix by a scalar.

Format
----------------
.. function:: spTScalar(s, scal, rinds, cinds)

    :param s: 
    :type s: NxM sparse matrix

    :param scal: 
    :type scal: scalar

    :param rinds: 
    :type rinds: Kx1 vector of row indices

    :param cinds: 
    :type cinds: Lx1 vector of column indices

    :returns: y (*TODO*), KxL sparse matrix.

Examples
----------------

::

    sparse matrix y;
    x = { 3 0 2 1,
          0 4 0 0,
          5 0 0 3,
          0 1 2 0 };
          
    rinds = 0;
    cinds = { 2,4 }; 
    
    //Multiply all elements in the second and fourth column 
    //by 'scal'
    y = spTScalar(x,10,rinds,cinds);
    d = spDenseSubmat(y,0,0);

The result, in d is:

::

    3 0  2 1
    0 40 0 0
    5 0  0 3
    0 10 2 0

.. seealso:: Functions :func:`spTrTDense`
