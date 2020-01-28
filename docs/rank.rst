
rank
==============================================

Purpose
----------------
Computes the rank of a matrix, using the singular value decomposition.

Format
----------------
.. function:: k = rank(x)

    :param x: data
    :type x: NxP matrix

    :return k: an estimate of the rank of *x*. This
        equals the number of singular values of *x*
        that exceed a prespecified tolerance in absolute value.

    :rtype k: scalar

Examples
------------------

::

  // Completely random x
  x1 = rndn(150, 1);
  rank(x1);

  // X2 is multiple of x1
  x2 = 2*x1;
  rank(x1~x2);

For this example, the rank of both ``x1`` and  ``x1~x2`` is one:

::

  1.0000000
  1.0000000

Global Input
------------

:_svdtol: scalar, the tolerance used in determining if any of the singular values
    are effectively 0. The default value is 10e\ :sup:`-13`. This can be changed
    before calling the procedure.

Source
------

svd.src

.. seealso:: Functions :func:`detl`, :func:`norm`
