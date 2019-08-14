
cosh
==============================================

Purpose
----------------

Computes the hyperbolic cosine.

Format
----------------
.. function:: y = cosh(x)

    :param x: data
    :type x: NxK matrix

    :return y: containing the hyperbolic cosines of the elements of *x*.

    :type y: NxK matrix

Examples
----------------

::

    x = { -0.5, -0.25, 0, 0.25, 0.5, 1 };
    x = x * pi;
    y = cosh(x);

::

       -1.5708       2.5092
       -0.7854       1.3246
    x = 0.0000   y = 1.0000
        0.7854       1.3246
        1.5708       2.5092
        3.1416      11.5920

Source
------------

trig.src
