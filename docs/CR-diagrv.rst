
diagrv
==============================================

Purpose
----------------
Inserts a vector into the diagonal of a matrix.

Format
----------------
.. function:: y = diagrv(x, v)

    :param x: Data matrix.
    :type x: NxK matrix

    :param v: Vector to replace the diagonal in *x* with.
    :type v: min(N,K)x1 vector.

    :return y: equal to *x* with its principal diagonal elements equal to those of *v*.

    :rtype y: NxK matrix

Remarks
-------

:func:`diag` reverses the procedure and pulls the diagonal out of a matrix.


Examples
----------------

::

    // Set rng seed for reproducibility
    rndseed 458716;

    // Build random x matrix
    x = rndu(3, 3);

    // Vector of ones to put in diagonal
    v = ones(3,1);

    // Call diagrv
    y = diagrv(x, v);

After the code above:

::

        0.967 0.318 0.465     1.000     1.000 0.318 0.465
    x = 0.046 0.786 0.205 v = 1.000 y = 0.046 1.000 0.205
        0.738 0.305 0.734     1.000     0.738 0.305 1.000

.. seealso:: Functions :func:`diag`
