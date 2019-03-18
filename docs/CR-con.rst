
con
==============================================

Purpose
----------------
Requests input from the keyboard
(console), and returns it in a matrix.

Format
----------------
.. function:: con(r, c)

    :param r: row dimension of matrix.
    :type r: scalar

    :param c: column dimension of matrix.
    :type c: scalar

    :returns: x (*TODO*), r x c matrix.

Examples
----------------

::

    n = con(1,1);
    print rndn(n,n);

If you enter 2 at the con generated prompt:

::

    ? 2

the code above will return a 2x2 random matrix, similar to:

::

    -1.2505596        1.6322417
    -1.0894098       0.74763307

In this example, the con function is used to obtain
the size of a square matrix of Normal random
variables which is to be printed out.

.. seealso:: Functions :func:`cons`, :func:`let`, :func:`load`
