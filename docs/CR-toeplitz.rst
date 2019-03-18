
toeplitz
==============================================

Purpose
----------------
Creates a Toeplitz matrix from a column vector.

Format
----------------
.. function:: toeplitz(x)

    :param x: Kx1 vector.
    :type x: TODO

    :returns: t (*TODO*), KxK Toeplitz matrix.

Examples
----------------

::

    //Create the sequence 1, 2, 3, 4, 5 and assign it to 'x'
    x = seqa(1,1,5);
    
    //Create a diagonal-constant or Toeplitz matrix
    y = toeplitz(x);

After the code above, y is equal to:

::

    1  2  3  4  5
    2  1  2  3  4
    3  2  1  2  3
    4  3  2  1  2
    5  4  2  2  3

Source
++++++

toeplitz.src

Toeplitz matrix column vector
