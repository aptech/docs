
spScale
==============================================

Purpose
----------------
Scales a sparse matrix.

Format
----------------
.. function:: spScale(x)

    :param x: 
    :type x: MxN sparse matrix

    :returns: a (*TODO*), MxN scaled sparse matrix.

    :returns: r (*Mx1 vector*), row scale factors.

    :returns: s (*Nx1 vector*), column scale factors.

Remarks
-------

spScale scales the elements of the matrix by powers of 10 so that they
are all within (-10,10).


Examples
----------------

::

    x = { 25  -12    0, 
           3    0  -11,
           8 -100    0 };
    
    declare sparse matrix sm, smsc;
    sm = denseToSp(x,0);
     
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

