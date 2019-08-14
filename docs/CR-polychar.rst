
polychar
==============================================

Purpose
----------------

Computes the characteristic polynomial of a square matrix.

Format
----------------
.. function:: c = polychar(x)

    :param x: data
    :type x: NxN matrix

    :returns: c (*(N+1)x1 vector*) of coefficients of the Nth order characteristic polynomial of *x*:
        
        .. math:: p(x) = c[1]*xn + c[2]*x(n-1) + ... + c[n]*x + c[n+1];

.. DANGER:: fix equations

Remarks
-------

The coefficient of :math:`x\ n` is set to unity (:math:`c[1]=1`).

Source
------

poly.src

.. seealso:: Functions :func:`polymake`, :func:`polymult`, :func:`polyroot`, :func:`polyeval`

