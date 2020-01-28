
exp
==============================================

Purpose
----------------

Calculates the exponential function.

Format
----------------
.. function:: y = exp(x)

    :param x: The values used to compute :math:`e^x`.
    :type x: NxK matrix or N-dimensional array

    :return y: contains :math:`e^x`, the base of natural
        logs raised to the powers given by the elements of *x*.

    :rtype y: NxK matrix or N-dimensional array

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
its elements.

.. NOTE:: :code:`exp(1)` returns *e*, the base of natural logs.

.. seealso:: Functions :func:`ln`
