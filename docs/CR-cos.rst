
cos
==============================================

Purpose
----------------

Returns the cosine of its argument.

Format
----------------
.. function:: y = cos(x)

    :param x: data, for real matrices should contain angles measured in radians. To convert degrees to radians, multiply the degrees by :math:`π/180`.
    :type x: NxK matrix

    :return y: containing the cosines of the elements of *x*.

    :type y: NxK matrix

Examples
----------------

::

    // Create a sequence starting at 0 and increasing by pi/4
    x = seqa(0, pi/4, 5);
    y = cos(x);

::

        0.0000      1.0000
        0.7854      0.7071
    x = 1.5708  y = 0.0000
        2.3562     -0.7071
        3.1416     -1.0000

.. seealso:: Functions :func:`atan`, :func:`atan2`, :func:`pi`
