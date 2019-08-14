
iscplx
==============================================

Purpose
----------------

Returns whether a matrix or N-dimensional array is complex or real.

Format
----------------
.. function:: y = iscplx(x)

    :param x: data
    :type x: NxK matrix or N-dimensional array

    :return x_iscplx: 1 if *x* is complex, 0 if it is real.

    :type x_iscplx: scalar

Examples
----------------

::

    // Define x
    x = { 1, 2i, 3 };

    // Test if x is complex
    if iscplx(x);
       print "X is complex";
    else;
       print "X is not complex";
    endif;

.. seealso:: Functions :func:`hasimag`, :func:`iscplxf`
