
tanh
==============================================

Purpose
----------------

Computes the hyperbolic tangent.

Format
----------------
.. function:: y = tanh(x)

    :param x: data
    :type x: NxK matrix or N-dimensional array

    :returns: y (*NxK matrix or N-dimensional array*) containing the hyperbolic tangents of the elements of *x*.

Examples
----------------

::

    // Create a sequence starting at -0.5 and increasing by
    // 0.25, i.e. -0.5, -0.25, 0, 0.25...1
    x = seqa(-0.5, 0.25, 7);
    x = x * pi;
    y = tanh(x);

After the above code, *y* is equal to:

::

    -0.46211716
    -0.24491866
     0.00000000
     0.24491866
     0.46211716
     0.63514895
     0.76159416

Source
------

trig.src

