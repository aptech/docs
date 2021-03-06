
sinh
==============================================

Purpose
----------------
Computes the hyperbolic sine.

Format
----------------
.. function:: y = sinh(x)

    :param x: data
    :type x: NxK matrix

    :return y: contains the hyperbolic sines of the elements of *x*.

    :rtype y: NxK matrix

Examples
----------------

::

    x = { -0.5, -0.25, 0, 0.25, 0.5, 1 };
    x = x * pi;
    y = sinh(x);

The above statement produces, *y* equal to:

::

    -2.301299
    -0.868671
     0.000000
     0.868671
     2.301299
    11.548739

Source
------

trig.src
