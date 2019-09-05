
ln
==============================================

Purpose
----------------

Computes the natural log of all elements of *x*.

Format
----------------
.. function:: y = ln(x)

    :param x: data
    :type x: NxK matrix or N-dimensional array

    :return y: containing the natural log values of the elements of *x*.

    :rtype y: NxK matrix or N-dimensional array

Remarks
-------

:func:`ln` is defined for :math:`x ≠ 0`.

If *x* is negative, complex results are returned.

You can turn the generation of complex numbers for negative inputs on or
off in the GAUSS configuration file, and with the :func:`sysstate` function,
case 8. If you turn it off, :func:`ln` will generate an error for negative
inputs.

If *x* is already complex, the complex number state doesn't matter; :func:`ln`
will compute a complex result.

*x* can be any expression that returns a matrix.


Examples
----------------

::

    y = ln(16);

::

    y = 2.7725887

.. seealso:: Functions :func:`log`
