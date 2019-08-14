
isden
==============================================

Purpose
----------------

Returns whether a scalar, matrix or N-dimensional array contains denormals.

Format
----------------
.. function:: y = isden(x)

    :param x: data
    :type x: NxK matrix or N-dimensional array

    :return x_isden: 1 if *x* contains a denormal, 0 if it does not.

    :type x_isden: scalar

Examples
----------------
Sometimes denormals can unnecessarily slow down calculations and it is best to flush them to zero. This example tests whether the vector *x* contains any denormals and then sets any values between 0 and 1e-25 to be equal to 0.

::

    tol = 1e-25;

    // Create a vector that contains a denormal
    x = { 1, exp(-724.5), 3 };

    if isden(x);
       // Get the index of all elements between 0 and tol
       idx = indexcat(x, 0|tol);

       // Set all elements between 0 and tol equal to 0
       x[idx] = 0;

    endif;

Before the `if` block in the code above, the second element of *x* is equal to approximately 3e-57. After the `if` block this element is set equal to 0, the other elements of *x* are unchanged.

This results in :

::

        1.0000000000
    x = 0.0000000000
        3.0000000000

.. seealso:: Functions :func:`denToZero`
