
stdc
==============================================

Purpose
----------------
Computes the standard deviation of the
elements in each column of a matrix.

Format
----------------
.. function:: stdc(x)

    :param x: 
    :type x: NxK matrix

    :returns: y (*Kx1 vector*), the standard
        deviation of each column of x.

Examples
----------------

::

    //Set the rng seed so that the random numbers produced will
    //be repeatable
                    
    rndseed 94243524;
    
    //Create a vector of random normal numbers
    y = rndn(8100,1);
    
    //Compute the standard deviation of the column vector 'y'
    std = stdc(y);

The standard deviation, in variable std, is equal to:

::

    1.00183907

.. seealso:: Functions :func:`meanc`

standard deviation column matrix
