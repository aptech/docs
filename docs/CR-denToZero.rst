
denToZero
==============================================

Purpose
----------------

Converts every denormal to a 0 in a matrix or array.

Format
----------------
.. function:: denToZero(x)

    :param x: 
    :type x: A matrix or an N-dimensional array

    :returns: y (*matrix or an N-dimensional array*) with the same orders as the input. Every denormal in the input will be converted to 0 in the output.

Examples
----------------

::

    x = { 1, exp(-724.5), 3 };
    
    //If 'x' contains any denormals set them to 0
    if isden(x);
       x2 = denToZero(x);
    endif;

After the first line above, *x* is equal to:

::

    1.000e+000 
    2.902e-057
    3.000e+000

At the end of the example, *x* is equal to:

::

    1.000e+000 
    0.000e+000 
    3.000e+000

