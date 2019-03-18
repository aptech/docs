
bessely
==============================================

Purpose
----------------

Computes a Bessel function of the second kind (Weber's function),
Yn(x).

Format
----------------
.. function:: bessely(n, x)

    :param n: NxK matrix or P-dimensional array where the last two dimensions are NxK, the order of the Bessel function. Nonintegers will be truncated to an integer.
    :type n: TODO

    :param x: LxM matrix or P-dimensional array where the last two dimensions are LxM, ExE conformable with  n.
    :type x: TODO

    :returns: y (*TODO*), max(N,L) by max(K,M) matrix or P-dimensional array where the last two dimensions are max(N,L) by max(K,M).

Examples
----------------

::

    //Create the sequence 0.1, 0.2, 0.3, 0.4, 0.5
    x = seqa(0.1, 0.1, 5);
    
    //Create the sequence 1, 1.1, 1.2, 1.3, 1.4
    x2 = seqa(1, 0.1, 5);
    
    //Calculate a first order bessel function against 'x' and 
    //calculate a third order bessel function agains 'x2'
    //NOTE: The '~' provides horizontal concatenation
    ord = { 1 3 };
    y = bessely(ord, x~x2);

After the code above:

::

    -6.459 -5.822         0.100  1.000
        -3.324 -4.507         0.200  1.100
    y = -2.293 -3.590  x~x2 = 0.300  1.200
        -1.781 -2.930         0.400  1.300
        -1.471 -2.442         0.500  1.400

.. seealso:: Functions :func:`besselj`, :func:`mbesseli`, :func:`besselk`

bessel
