
imag
==============================================

Purpose
----------------

Returns the imaginary part of *x*.

Format
----------------
.. function:: zi = imag(x)

    :param x: data
    :type x: NxK matrix or N-dimensional array

    :return zi: the imaginary part of *x*.

    :rtype zi: NxK matrix or N-dimensional array

Examples
----------------

::

    // X-matrix
    x = { 4i 9    3,
          2  5-6i 7i };

     // Find imaginary part of x
     y = imag(x);

::

    y = 4   0   0
        0  -6   7

Remarks
-------

If *x* is real, *zi* will be an NxK matrix or N-dimensional array of zeros.


.. seealso:: Functions :func:`complex`, :func:`real`
