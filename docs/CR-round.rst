
round
==============================================

Purpose
----------------

Round to the nearest integer.

Format
----------------
.. function:: round(x)

    :param x: 
    :type x: NxK matrix or N-dimensional array

    :returns: y (*NxK matrix or N-dimensional array*)         containing the rounded elements of x.

Examples
----------------

::

    let x = { 77.68 -14.10,
              4.73 -158.88 };
    y = round(x);
    print y;

::

    78.00  -14.00
        5.00 -159.00

.. seealso:: Functions :func:`trunc`, :func:`floor`, :func:`ceil`
