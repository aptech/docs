
sin
==============================================

Purpose
----------------
Returns the sine of its argument.

Format
----------------
.. function:: y = sin(x)

    :param x: data
    :type x: NxK matrix or N-dimensional array

    :return y: contains the sine of *x*.

    :rtype y: NxK matrix or N-dimensional array

Examples
----------------

::

    x = { 0, .5, 1, 1.5 };
    y = sin(x);
    print y;

::

       0.000000
       0.479426
       0.841471
       0.997495

Remarks
-------

For real data, *x* should contain angles measured in radians.

To convert degrees to radians, multiply the degrees by :math:`\pi/180`.

.. seealso:: Functions :func:`atan`, :func:`cos`, :func:`sinh`, :func:`pi`
