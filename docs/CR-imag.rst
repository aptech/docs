
imag
==============================================

Purpose
----------------

Returns the imaginary part of x.

Format
----------------
.. function:: imag(x)

    :param x: NxK matrix or N-dimensional array.
    :type x: TODO

    :returns: zi (*TODO*), NxK matrix or N-dimensional array, the imaginary part of x.

Examples
----------------

::

    x = { 4i 9    3,
          2  5-6i 7i };
     y = imag(x);

::

    y = 4   0   0
        0  -6   7

.. seealso:: Functions :func:`complex`, :func:`real`
