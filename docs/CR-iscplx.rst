
iscplx
==============================================

Purpose
----------------

Returns whether a matrix or N-dimensional array is complex or real.

Format
----------------
.. function:: iscplx(x)

    :param x: NxK matrix or N-dimensional array.
    :type x: TODO

    :returns: y (*scalar*), 1 if x is complex, 0 if it is real.

Examples
----------------

::

    x = { 1, 2i, 3 };
    if iscplx(x);
       //code path for complex case
    else;
       //code path for real case
    endif;

.. seealso:: Functions :func:`hasimag`, :func:`iscplxf`
