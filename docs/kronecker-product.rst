
kronecker-product
==============================================

Purpose
----------------

Computes the Kronecker product (tensor product) of two matrices.

Format
----------------

::

    y = a .*. b

Parameters
----------------

    :param a: Left matrix.
    :type a: MxN matrix

    :param b: Right matrix.
    :type b: PxQ matrix

Returns
----------------

    :return y: Kronecker product of *a* and *b*.

    :rtype y: (M*P) x (N*Q) matrix

Examples
----------------

Basic Example
+++++++++++++

::

    a = { 1 2,
          3 4 };
    b = { 0 5,
          6 7 };
    y = a .*. b;

::

    y =    0.0000000    5.0000000    0.0000000   10.0000000
           6.0000000    7.0000000   12.0000000   14.0000000
           0.0000000   15.0000000    0.0000000   20.0000000
          18.0000000   21.0000000   24.0000000   28.0000000

Identity Kronecker Product
++++++++++++++++++++++++++

::

    I2 = eye(2);
    a = { 1 2,
          3 4 };
    y = I2 .*. a;

::

    y =    1.0000000    2.0000000    0.0000000    0.0000000
           3.0000000    4.0000000    0.0000000    0.0000000
           0.0000000    0.0000000    1.0000000    2.0000000
           0.0000000    0.0000000    3.0000000    4.0000000

Vector Example
++++++++++++++

::

    a = { 1, 2, 3 };
    b = { 1, 10 };
    y = a .*. b;

::

    y =    1.0000000
          10.0000000
           2.0000000
          20.0000000
           3.0000000
          30.0000000

Remarks
-------

- The Kronecker product of an MxN matrix *a* and a PxQ matrix *b* produces an (M*P) x (N*Q) matrix.
- Each element ``a[i,j]`` is replaced by the block ``a[i,j] * b``.
- Useful in econometrics for SUR (Seemingly Unrelated Regressions), vec operators, and covariance matrix calculations.
- The Kronecker product is associative but not commutative: ``a .*. b != b .*. a`` in general.

.. seealso:: Operators :doc:`matrix-multiplication`, :doc:`element-by-element-multiplication`, Functions :func:`vec`, :func:`reshape`
