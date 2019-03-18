
sumc
==============================================

Purpose
----------------
Computes the sum of each column of a matrix or the sum across the second-fastest moving dimension of an L-dimensional array.

Format
----------------
.. function:: sumc(x)

    :param x: NxK matrix or L-dimensional array where the last two dimensions are NxK.
    :type x: TODO

    :returns: y (*TODO*), Kx1 vector or L-dimensional array where the last two dimensions are Kx1.

Examples
----------------

::

    //Create a 12x1 vector containing an additive sequence 
    //counting by twos, from 0-22, i.e. 2, 4, 6, 8...22
    x = seqa(0,2,12);
    
    //Reshape the 12x1 vector 'x' into a 3x4 matrix
    x = reshape(x,3,4));
    
    //Sum the columns
    y = sumc(x);

After the above code, the variables x and y are equal to:

::

    0  2  4  6
    x =  8 10 12 14
        16 18 20 22
    
        24
    y = 30
        36
        42

::

    //Create an additive sequence from 1-24 and reshape it into 
    //a 2x3x4 array
    a = areshape(seqa(1,1,24),2|3|4);
    
    //Sum the columns across the second fastest moving 
    //dimension
    z = sumc(a);

a is a 2x3x4 array such that:

::

    Plane [1,.,.]
    
          1.0000000     2.0000000     3.0000000     4.0000000
          5.0000000     6.0000000     7.0000000     8.0000000
          9.0000000     10.000000     11.000000     12.000000
    
    Plane [2,.,.]
    
          13.000000     14.000000     15.000000     16.000000
          17.000000     18.000000     19.000000     20.000000
          21.000000     22.000000     23.000000     24.000000

Variable z is a 2x4x1 array equal to:

::

    Plane [1,.,.]
    
          15.000000
          18.000000
          21.000000
          24.000000
    
    Plane [2,.,.]
    
          51.000000
          54.000000
          57.000000
          60.000000

.. seealso:: Functions :func:`cumsumc`, :func:`meanc`, :func:`stdc`
