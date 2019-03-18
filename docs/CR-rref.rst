
rref
==============================================

Purpose
----------------
Computes the reduced row echelon form of a matrix.

Format
----------------
.. function:: rref(x)

    :param x: MxN matrix.
    :type x: TODO

    :returns: y (*TODO*), MxN matrix containing reduced row
        echelon form of x.

Examples
----------------

::

    // Since (row 2) = 2*(row 1), we do not expect this
    // matrix to have full rank
    x[3,3] = 1 2 3
             2 4 6
             3 5 2;
    y = rref(x);
    
    // compute rank of x
    r = sumc(sumc(abs(rref(x)')) .> 1e-15);
    print "The rank of x = " r;

::

    The rank of x = 2.000

Source
++++++

rref.src

reduced row echelon form matrix
