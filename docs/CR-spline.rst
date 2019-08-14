
spline
==============================================

Purpose
----------------
Computes a two-dimensional interpolatory spline.

Format
----------------
.. function:: { u, v, w } = spline(x, y, z, sigma, g)

    :param x: x-abscissae (x-axis values).
    :type x: Kx1 vector

    :param y: y-abscissae (y-axis values).
    :type y: Nx1 vector

    :param z: ordinates (z-axis values).
    :type z: KxN matrix

    :param sigma: tension factor.
    :type sigma: scalar

    :param g: grid size factor.
    :type g: scalar

    :return u: x-abscissae, regularly spaced.

    :type u: (K*g)x1 vector

    :return v: y-abscissae, regularly spaced.

    :type v: (N*g)x1 vector

    :return w: interpolated ordinates.

    :type w: (K*g)x(N*g) matrix

Remarks
-------

*sigma* contains the tension factor. This value indicates the curviness
desired. If *sigma* is nearly zero (e.g., .001), the resulting surface is
approximately the tensor product of cubic splines. If *sigma* is large
(e.g., 50.0), the resulting surface is approximately bi-linear. If *sigma*
equals zero, tensor products of cubic splines result. A standard value
for *sigma* is approximately 1.

*g* is the grid size factor. It determines the fineness of the output
grid. For :math:`g = 1`, the output matrices are identical to the input matrices.
For :math:`g = 2`, the output grid is twice as fine as the input grid, i.e., *u*
will have twice as many columns as *x*, *v* will have twice as many rows as
*y*, and *w* will have twice as many rows and columns as *z*.

Source
------

spline.src

