
spScale
==============================================

Purpose
----------------
Scales a sparse matrix.

Format
----------------
.. function:: { a, r, s } = spScale(x)

    :param x: data
    :type x: MxN sparse matrix

    :return a: 

    :rtype a: MxN scaled sparse matrix

    :return r: row scale factors.

    :rtype r: Mx1 vector

    :return s: column scale factors.

    :rtype s: Nx1 vector

Examples
----------------

::

    x = { 25  -12    0, 
           3    0  -11,
           8 -100    0 };
    
    declare sparse matrix sm, smsc;
    sm = denseToSp(x, 0);
     
    { smsc, r, c } = spScale(sm);

The results:

::

            2.50  -0.12   0.00 
    smsc =  0.30   0.00  -0.11 
            0.80  -1.00   0.00 
    
            1.00 
    c =     0.10 
            0.10 
        
            0.10 
    r =     0.10 
            0.10

Remarks
-------

:func:`spScale` scales the elements of the matrix by powers of 10 so that they are all within :math:`(-10,10)`.

