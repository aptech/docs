
fix
==============================================

Purpose
----------------

Round towards 0.

Format
----------------
.. function:: y = fix(x)

    :param x: data
    :type x: NxK matrix or N-dimensional array

    :return y: contains the rounded elements of *x*.

    :rtype y: NxK matrix or N-dimensional array

Examples
----------------

::

    x = { 0.9,
         -0.9,
          2.7,
         -2.7 };

    y = fix(x);
    print y;

::

       0.0000000
       0.0000000
       2.0000000
      -2.0000000

.. seealso:: Functions :func:`trunc`, :func:`floor`, :func:`ceil`, :func:`round`
