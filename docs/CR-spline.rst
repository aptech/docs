
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

