
exp
==============================================

Purpose
----------------

Calculates the exponential function.

Format
----------------
.. function:: exp(x)

    :param x: NxK matrix or N-dimensional array.
    :type x: TODO

    :returns: y (*TODO*), NxK matrix or N-dimensional array containing  e, the base of natural
        logs, raised to the powers given by the
        elements of x.

Examples
----------------

::

    x = eye(3);
     y = exp(x);

::

    1.000000  0.000000  0.000000
     x = 0.000000  1.000000  0.000000
         0.000000  0.000000  1.000000

::

    2.718282  1.000000  1.000000
     y = 1.000000  2.718282  1.000000
         1.000000  1.000000  2.718282

This example creates a 3x3 identity matrix and
computes the exponential function for each one of
its elements. Note that exp(1) returns  e, the
base of natural logs.

.. seealso:: Functions :func:`ln`

exp exponential function
