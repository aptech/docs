
orth
==============================================

Purpose
----------------

Computes an orthonormal basis for the column space of a matrix.

Format
----------------
.. function:: orth(x)

    :param x: 
    :type x: NxK matrix

    :returns: y (*TODO*), NxL matrix such that y'y = eye(L) and whose
        columns span the same space as the columns of
        x; L is the rank of x.

Examples
----------------

::

    x = { 6 5 4,
          2 7 5 };
     
    y = orth(x);

After the code above:

::

    y = -0.58123819      -0.81373347    y'y = 1  0
        -0.81373347       0.58123819          0  1

Source
++++++

qqr.src

.. seealso:: Functions :func:`qqr`, :func:`olsqr`

orthonormal basis column space x
