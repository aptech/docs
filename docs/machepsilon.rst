
machEpsilon
==============================================

Purpose
----------------

Returns the smallest number such that :math:`1 + eps > 1`.

Format
----------------
.. function:: eps = machEpsilon()

    :return eps: machine epsilon.

    :rtype eps: scalar

Examples
----------------

::

    eps = machEpsilon();
    print eps;

The code above produces the following output:

::

    2.2300000e-16

Source
------

machconst.src

.. seealso:: Functions :func:`sysstate`
