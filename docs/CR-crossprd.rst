
crossprd
==============================================

Purpose
----------------

Computes the cross-products (vector products) of sets of 3x1 vectors.

Format
----------------
.. function:: crossprd(x, y)

    :param x: each column is treated as a 3x1 vector.
    :type x: 3xK matrix

    :param y: each column is treated as a 3x1 vector.
    :type y: 3xK matrix

    :returns: **z** (*3xK matrix*) - each column is the cross-product
        (sometimes called vector product) of the
        corresponding columns of *x* and *y*.

Remarks
-------

The cross-product vector *z* is orthogonal to both *x* and *y*. :code:`sumc(x .* z)`
and :code:`sumc(y .* z)` will be Kx1 vectors, all of whose elements are 0
(except for rounding error).

Examples
----------------

::

    // First matrix
    x = { 10  4,
          11 13,
         14 13 };

    // Second matrix
    y = { 3 11,
          5 12,
          7  9 };

    z = crossprd(x, y);

After the above code,

::

          7  -39
    z = -28  107
         17  -95

Source
------------

crossprd.src
