
polyroot
==============================================

Purpose
----------------
Computes the roots of a polynomial given the coefficients.

Format
----------------
.. function:: y = polyroot(c)

    :param c: coefficients of an Nth order polynomial:

        .. math:: p(z) = c[1]*z^n + c[2]*z^{n-1} + ... + c[n]*z + c[n+1]

    :type c: (N+1)x1 vector

    :return y: the roots of *c*.

    :rtype y: Nx1 vector

Examples
----------------

::

    /*
    ** Consider the polynomial
    ** y = 7x^4 - 5x^3 + 4x - 3
    */

    /*
    ** First create vector of coefficients.
    ** Note that because there is no x^2 term
    ** we must place a 0 as the third element
    */
    c = 7|(-5)|0|4|(-3);

    // Find roots
    roots = polyroot(c);

    // Print roots
    print "The roots of the polynomial y = 7x^4 - 5x^3 + 4x - 3 are:"
    roots;

The output reads:

::

    The roots of the polynomial y = 7x^4 - 5x^3 + 4x - 3 are:
         -0.83614991
          0.40754502 +       0.72864999i
          0.40754502 -       0.72864999i
          0.73534559

Remarks
-------

Zero leading terms will be stripped from *c*. When that occurs the order
of *y* will be the order of the polynomial after the leading zeros have
been stripped.

:math:`c[1]` need not be normalized to unity.


Source
------

poly.src

.. seealso:: Functions :func:`polymake`, :func:`polychar`, :func:`polymult`, :func:`polyeval`
