
ltrisol
==============================================

Purpose
----------------

Computes the solution of :math:`Lx = b` where *L* is a lower triangular matrix.

Format
----------------
.. function:: x = ltrisol(b, L)

    :param b: data
    :type b: PxK matrix

    :param L: lower triangular matrix
    :type L: PxP matrix

    :return x: solution of :math:`Lx = b`.

    :rtype x: PxK matrix

Examples
---------------

::

  rndseed 123131;

  // Create lower triangular matrix
  l = lowmat(rndn(4, 4));

  // Create random b matrix
  b = rndn(4, 1);

  print "b/l ="; b/l;

  x = ltrisol(b, l);

  print "x ="; x;

This code produces

::

  b/l =

    1.31626
    3.24920
   -4.95390
    4.62379
  x =

    1.31626
    3.24920
   -4.95390
    4.62379

Remarks
---------------

:func:`ltrisol` applies a forward solve to :math:`Lx = b` to solve for *x*. If *b* has more
than one column, each column will be solved for separately,
i.e., :func:`ltrisol` will apply a forward solve to :math:`L*x[., i] = b[., i]`.
