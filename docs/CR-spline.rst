
spline
==============================================

Purpose
----------------
Computes a two-dimensional interpolatory spline.

Format
----------------
.. function:: spline(x, y, z, sigma, g)

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

    :returns: u (*TODO*), (K*g)x1 vector, x-abscissae, regularly spaced.

    :returns: v (*TODO*), (N*g)x1 vector, y-abscissae, regularly spaced.

    :returns: w (*TODO*), (K*g)x(N*g) matrix, interpolated ordinates.



Remarks
-------

sigma contains the tension factor. This value indicates the curviness
desired. If sigma is nearly zero (e.g., .001), the resulting surface is
approximately the tensor product of cubic splines. Ifsigma is large
(e.g., 50.0), the resulting surface is approximately bi-linear. Ifsigma
equals zero, tensor products of cubic splines result. A standard value
forsigma is approximately 1.

g is the grid size factor. It determines the fineness of the output
grid. Forg = 1, the output matrices are identical to the input matrices.
Forg = 2, the output grid is twice as fine as the input grid, i.e.,u
will have twice as many columns as x,v will have twice as many rows as
y, andw will have twice as many rows and columns asz.



Source
------

spline.src

