
orth
==============================================

Purpose
----------------

Computes an orthonormal basis for the column space of a matrix.

Format
----------------
.. function:: y = orth(x)

    :param x: data
    :type x: NxK matrix

    :returns: y (*NxL matrix*) such that :math:`y'y = eye(L)` and whose
        columns span the same space as the columns of *x*; *L* is the rank of *x*.

Global Input
------------

:_orthol: (*scalar*), the tolerance for testing if diagonal elements are approaching zero. The default is 1.0e-14.

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
------

qqr.src

.. seealso:: Functions :func:`qqr`, :func:`olsqr`

