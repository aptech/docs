
sqrt
==============================================

Purpose
----------------
Computes the square root of every element in x.

Format
----------------
.. function:: y = sqrt(x)

    :param x: data
    :type x: NxK matrix or N-dimensional array

    :returns: y (NxK matrix or N-dimensional array) the square roots of each element of *x*.

Remarks
-------

If *x* is negative, complex results are returned by default. You can turn
the generation of complex numbers for negative inputs on or off in the
GAUSS configuration file, and with the :func:`sysstate` function, case 8. If you
turn it off, :func:`sqrt` will generate an error for negative inputs.

If *x* is already complex, the complex number state does not matter; :func:`sqrt`
will compute a complex result.


Examples
----------------

::

    let x[2,2] = 1 2 3 4;
    y = sqrt(x);

The output, in variable *y* is equal to:

::

    1.00000000 
    1.41421356 
    1.73205081 
    2.00000000

