
floor
==============================================

Purpose
----------------

Round down toward :math:`-∞`.

Format
----------------
.. function:: x_floor = floor(x)

    :param x: The values to be rounded down.
    :type x: NxK matrix or N-dimensional array

    :return x_floor: Contains the elements of *x* rounded down to the nearest integer.

    :rtype x_floor: NxK matrix or N-dimensional array

Examples
----------------

::

    x = { -2.6  3.75, 
          2.79 -0.27 };
    
    print floor(x);

will return:

::

    -3  3
     2 -1

.. seealso:: Functions :func:`ceil`, :func:`round`, :func:`trunc`
