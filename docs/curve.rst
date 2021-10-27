
curve
==============================================

Purpose
----------------

Computes a one-dimensional smoothing curve.

Format
----------------
.. function:: { u, v } = curve(x, y, d, s, sigma, G)

    :param x: x-abscissae (x-axis values).
    :type x: Kx1 vector

    :param y: y-ordinates (y-axis values).
    :type y: Kx1 vector

    :param d: observation weights.
    :type d: Kx1 vector or scalar

    :param s: smoothing parameter. If :math:`s = 0`, curve
        performs an interpolation. If *d* contains
        standard deviation estimates, a reasonable value for
        *s* is *K*.
    :type s: scalar

    :param sigma: tension factor.
    :type sigma: scalar

    :param G: grid size factor.
    :type G: scalar

    :return u: vector, x-abscissae, regularly spaced.

    :rtype u: (KxG)x1

    :return v: vector, y-ordinates, regularly spaced.

    :rtype v: (KxG)x1

Example:
----------
::

  new;

  // Generate data
  x = seqa(0, .25, 24);
  y = 5*x + 4 + 10*rndn(rows(x), 1);

  // Observation weights
  d = 1;

  // Smoothing parameter
  s = 2;

  // Tension factor
  sigma = 1;

  // Grid factor;
  G = 2;

  { u, v } = curve(x, y, d, s, sigma, G);

  // Quick plot of results
  plotScatter(x, y);
  plotAddXY(u, v);

Remarks
-------

*sigma* contains the tension factor. This value indicates the curviness
desired. If *sigma* is nearly zero (e.g. .001), the resulting curve is
approximately the tensor product of cubic curves. If *sigma* is large,
(e.g. 50.0) the resulting curve is approximately bi-linear. If *sigma*
equals zero, tensor products of cubic curves result. A standard value
for *sigma* is approximately 1.

*G* is the grid size factor. It determines the fineness of the output
grid. For :math:`G = 1`, the input and output vectors will be the same size. For
:math:`G = 2`, the output grid is twice as fine as the input grid, i.e., *u* and *v*
will have twice as many rows as *x* and *y*.



Source
------

spline.src

.. seealso:: Functions :func:`spline`
