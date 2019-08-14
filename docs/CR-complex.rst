
complex
==============================================

Purpose
----------------

Converts a pair of real matrices to a complex matrix.

Format
----------------
.. function:: z = complex(xr, xi)

    :param xr: the real elements of *z*.
    :type xr: NxK real matrix

    :param xi: the imaginary elements of *z*.
    :type xi: NxK real matrix or scalar

    :returns: **z** (*NxK complex matrix*)

Examples
----------------

::

    // The real elements
    xr = { 4 6,
           9 8 };

    // The imaginary elements
    xi = { 3 5,
           1 7 };

    z = complex(xr, xi);

After the code above, *z* will be equal to:

::

    4 + 3i   6 + 5i
    9 + 1i   8 + 7i

.. seealso:: Functions :func:`imag`, :func:`real`
