
imag
==============================================

Purpose
----------------

Returns the imaginary part of *x*.

Format
----------------
.. function:: imag(x)

    :param x: data
    :type x: NxK matrix or N-dimensional array

    :returns: **zi** (*NxK matrix or N-dimensional array*) - the imaginary part of *x*.

Remarks
-------

If *x* is real, *zi* will be an NxK matrix or N-dimensional array of zeros.


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

.. seealso:: Functions :func:`complex`, :func:`real`
