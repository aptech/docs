
curve
==============================================

Purpose
----------------

Computes a one-dimensional smoothing curve.

Format
----------------
.. function:: curve(x, y, d, s, sigma, G)

    :param x: x-abscissae (X-axis values).
    :type x: Kx1 vector

    :param y: y-ordinates (Y-axis values).
    :type y: Kx1 vector

    :param d: observation weights.
    :type d: Kx1 vector or scalar

    :param s: smoothing parameter. If s = 0, curve
        performs an interpolation. If  d contains
        standard deviation estimates, a reasonable value for
        s is K.
    :type s: scalar

    :param sigma: tension factor.
    :type sigma: scalar

    :param G: grid size factor.
    :type G: scalar

    :returns: u (*TODO*), (K*G)x1 vector, x-abscissae, regularly spaced.

    :returns: v (*TODO*), (K*G)x1 vector, y-ordinates, regularly spaced.

