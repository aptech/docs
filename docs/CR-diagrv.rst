
diagrv
==============================================

Purpose
----------------
Inserts a vector into the diagonal of a matrix.

Format
----------------
.. function:: diagrv(x,  v)

    :param x: NxK matrix.
    :type x: TODO

    :param v: min(N,K)x1 vector.
    :type v: TODO

    :returns: y (*TODO*), NxK matrix equal to x with its principal diagonal elements equal to those of  v.

Examples
----------------

::

    x = rndu(3,3);
    v = ones(3,1);
    y = diagrv(x,v);

After the code above:

::

    0.614 0.686 0.633     1.000     1.000 0.686 0.633
    x = 0.802 0.185 0.707 v = 1.000 y = 0.802 1.000 0.707
        0.551 0.761 0.418     1.000     0.551 0.761 1.000

.. seealso:: Functions :func:`diag`
