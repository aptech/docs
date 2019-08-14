
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

    :returns: y (*NxK matrix or N-dimensional array*) containing the sine of *x*.

Remarks
-------

For real data, *x* should contain angles measured in radians.

To convert degrees to radians, multiply the degrees by :math:`π/180`.

Examples
----------------

::

    let x = { 0, .5, 1, 1.5 };
    y = sin(x);
    print y;

::

       0.000000
       0.479426
       0.841471
       0.997495

.. seealso:: Functions :func:`atan`, :func:`cos`, :func:`sinh`, :func:`pi`

