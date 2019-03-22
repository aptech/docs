
log
==============================================

Purpose
----------------

Computes the log  of all elements of x.

Format
----------------
.. function:: log(x)

    :param x: 
    :type x: NxK matrix or N-dimensional array

    :returns: y (*NxK matrix or N-dimensional array*) containing the log 10 values of the
        elements of x.

Remarks
-------

log is defined for x ≠ 0.

You can turn the generation of complex numbers for negative inputs on or
off in the GAUSS configuration file, and with the sysstate function,
case 8. If you turn it off, log will generate an error for negative
inputs.

If x is already complex, the complex number state doesn't matter; log
will compute a complex result.

x can be any expression that returns a matrix.


Examples
----------------

::

    //Create a 3x3 matrix of random uniform integers from 1 
    //to 11
    x = round(rndu(3,3)*10+1);
    y = log(x);

If x is equal to:

::

    4.000  9.000  2.000 
    5.000  3.000  7.000 
    2.000  6.000 10.000

Then y will be equal to:

::

    0.602  0.954  0.301 
    0.699  0.477  0.845 
    0.301  0.778  1.000

.. seealso:: Functions :func:`ln`

natural logarithm log base 10
