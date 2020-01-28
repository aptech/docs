
denToZero
==============================================

Purpose
----------------

Converts every denormal to a 0 in a matrix or array.

Format
----------------
.. function:: y = denToZero(x)

    :param x: Data to be converted.
    :type x: matrix or an N-dimensional array

    :return y: with the same orders as the input. Every denormal in the input will be converted to 0 in the output.

    :rtype y: matrix or an N-dimensional array

Examples
----------------

::

    x =  1 | exp(-724.5) | 3;

    // If 'x' contains any denormals set them to 0
    if isden(x);
       y = denToZero(x);
    endif;

After the first line above, *x* is equal to:

::

    1.000e+000
          +DEN
    3.000e+000

At the end of the example, *y* is equal to:

::

    1.000e+000
    0.000e+000
    3.000e+000
