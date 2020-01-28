
tan
==============================================

Purpose
----------------

Returns the tangent of its argument.

Format
----------------
.. function:: y = tan(x)

    :param x: data
    :type x: NxK matrix or N-dimensional array

    :return y: the tangent of the elements in *x*.

    :rtype y: NxK matrix or N-dimensional array

Examples
----------------

::

    // Create an additive sequence 0.1, 0.2, 0.3...0.9
    x = seqa(0.1, 0.1, 9);

    y = tan(x);

The above code produces:

::

        0.1003346
        0.2027100
        0.3093362
        0.4227932
    y = 0.5463024
        0.6841368
        0.8422883
        1.0296386
        1.2601582

Remarks
-------

For real matrices, *x* should contain angles measured in radians.

To convert degrees to radians, multiply the degrees by :math:`π/180`.


.. seealso:: Functions :func:`atan`, :func:`pi`
