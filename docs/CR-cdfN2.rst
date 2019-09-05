
cdfN2
==============================================

Purpose
----------------
Computes the Normal cumulative distribution function over the interval between *x* and *x+dx*.

Format
----------------
.. function:: p = cdfN2(x, dx)

    :param x: Lower limit at which to evaluate the normal cumulative distribution function. 
    :type x: MxN matrix

    :param dx: ExE conformable to *x*, intervals used to compute the upper bound, *x + dx*.
    :type dx: KxL matrix

    :return p: The normal cumulative distribution function over the interval :math:`x` to :math:`x + dx`, i.e., :math:`Pr(x < X < x + dx)`

    :rtype p: matrix, max(M,K) by max(N,L)

Remarks
-------

The relative error is:

.. csv-table::
    :widths: auto

    ":math:`\left| x \right| \leq 1` and :math:`dx \leq 1`", ":math:`\pm 1e-14`"
    ":math:`1 < \left| x \right| < 37` and :math:`\left| dx \right| < \frac{1}{\left| x \right|}`", ":math:`\pm 1e-13`"
    ":math:`min(x, x + dx) > -37` and :math:`y > 1e-300`", ":math:`\pm 1e-11` or better"

A relative error of :math:`\pm 1e-14` implies that the answer is accurate to better
than :math:`±1` in the 14th digit.

Examples
----------------

::

    // Starting x
    x = 0;

    // Interval
    dx = 1.96;

    // Call the cdfN2
    print cdfN2(x, dx);

After the above code:

::

    0.4750021048517795

::

  // Starting x
  x = 1;

  // Interval
  dx = 0.5;

  // Call the cdfN2
  print cdfN2(x, dx);

After the above code:

::

  9.1848052662599017e-02

::

  // Starting x
  x = 20;

  // Interval
  dx = 1e-2;

  // Call the cdfN2
  print cdfN2(x, dx);

After the above code:

::

  5.0038115018684521e-90

::

  // Starting value
  x = { 0 0.25   1  -2  -1,
        1    0 0.4 2.3   1,
        3    1 0.9 0.4 0.1 };

  dx = { 0.5, 1.4, 2 };

  print cdfN2(x, dx);

After the above code:

::

  0.1915   0.1747   0.0918   0.0441   0.1499
  0.1505   0.4192   0.3086   0.0106   0.1505
  0.0013   0.1573   0.1822   0.3364   0.4423

.. seealso:: Functions :func:`lncdfn2`
