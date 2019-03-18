
balance
==============================================

Purpose
----------------
Balances a square matrix.

Format
----------------
.. function:: balance(x)

    :param x: KxK matrix or N-dimensional array where the last two dimensions are KxK.
    :type x: TODO

    :returns: b (*TODO*), KxK matrix or N-dimensional array where the last two dimensions are KxK, balanced matrix.

    :returns: z (*TODO*), KxK matrix or N-dimensional array where the last two dimensions are KxK, diagonal scale matrix.

Examples
----------------

::

    let x[3,3] = 100 200 300
                  40  50  60
                   7   8   9;
    { b,z } = balance(x);
    
        b = 100.0  100.0  37.5
             80.0   50.0  15.0
             56.0   32.0   9.0
    
        z = 4.0  0.0  0.0
            0.0  2.0  0.0
            0.0  0.0  0.5

balance matrix diagonal scaling to improve eigenvalue accuracy
