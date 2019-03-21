
ln
==============================================

Purpose
----------------

Computes the natural log of all elements of x.

Format
----------------
.. function:: ln(x)

    :param x: 
    :type x: NxK matrix or N-dimensional array

    :returns: y (*TODO*), NxK matrix or N-dimensional array
        containing the natural log values of the
        elements of x.

Remarks
-------

ln is defined for x ≠ 0.

If x is negative, complex results are returned.

You can turn the generation of complex numbers for negative inputs on or
off in the GAUSS configuration file, and with the sysstate function,
case 8. If you turn it off, ln will generate an error for negative
inputs.

If x is already complex, the complex number state doesn't matter; ln
will compute a complex result.

x can be any expression that returns a matrix.


Examples
----------------

::

    y = ln(16);

::

    y = 2.7725887

.. seealso:: Functions :func:`log`

natural logarithm log
