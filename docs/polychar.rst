
polychar
==============================================

Purpose
----------------

Computes the characteristic polynomial of a square matrix.

Format
----------------
.. function:: c = polychar(x)

    :param x: data.
    :type x: NxN matrix

    :return c: coefficients of the Nth order characteristic polynomial of *x*:

        .. math:: p(x) = c[1]*x^n + c[2]*x^{(n-1)} + ... + c[n]*x + c[n+1];

    :rtype c: (N+1)x1 vector

Remarks
-------

The coefficient of :math:`x^n` is set to unity (:math:`c[1]=1`).

Examples
----------------

::

    x = { 2 1, 1 2 };

    // Compute the characteristic polynomial
    c = polychar(x);
    print c;

The code above produces the following output:

::

    1.0000000
   -4.0000000
    3.0000000

This represents the polynomial :math:`p(\lambda) = \lambda^2 - 4\lambda + 3`.

Source
------

poly.src

.. seealso:: Functions :func:`polymake`, :func:`polymult`, :func:`polyroot`, :func:`polyeval`
