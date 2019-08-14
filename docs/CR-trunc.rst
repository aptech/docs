
trunc
==============================================

Purpose
----------------
Converts numbers to integers by truncating the fractional portion.

Format
----------------
.. function:: y = trunc(x)

    :param x: data
    :type x: NxK matrix or N-dimensional array

    :returns: y (*NxK matrix or N-dimensional array*) containing the truncated elements of *x*.

Examples
----------------

::

    x = 100*rndn(2,2);
    y = trunc(x);

If *x* equals:

::

    -153.373  -1.972
     109.412 127.732

then, *y* will equal:

::

    -153.000  -1.000
     109.000 127.000

.. seealso:: Functions :func:`ceil`, :func:`floor`, :func:`round`

