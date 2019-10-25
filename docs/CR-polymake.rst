
polymake
==============================================

Purpose
----------------

Computes the coefficients of a polynomial given the roots.

Format
----------------
.. function:: c = polymake(r)

    :param r: roots of the desired polynomial
    :type r: Nx1 vector

    :return c: contains the coefficients of the Nth order polynomial with roots *r*:

        .. math:: p(z)=c[1]*z^n + c[2]*z^{(n-1)} + ... c[n]*z + c[n+1]

    :rtype c: (N+1)x1 vector

Examples
----------------

::

    // Assign values for the roots of the polynomial
    r = { 2, 1, 3 };

    // Calculate the coefficients
    c = polymake(r);

    // Print 3 spaces for each number and 1 digit after the
    // decimal place
    format /rd 3,1;

    // Iterate through each root in 'r'
    for i(1, 3, 1);
       rtmp = r[i];
       // Calculate the polynomial
       rout = c[1]*rtmp^3 + c[2]*rtmp^2 + c[3]*rtmp + c[4];
       print "rtmp = " rtmp "rout = " rout;
    endfor;

Since the values of *r* are roots for this polynomial, *rout* should equal 0.

Thus the code above gives the following output:

::

    rtmp = 2.0 rout = 0.0
    rtmp = 1.0 rout = 0.0
    rtmp = 3.0 rout = 0.0

This example assigns *c* to be equal to:

::

         1.0
    c = -6.0
        11.0
        -6.0

This represents the polynomial:

.. math::

    x^3 - 6x^2 + 11^x - 6

Remarks
-------

The coefficient of :math:`z^n` is set to unity (:math:`c[1]=1`).

Source
------

poly.src

.. seealso:: Functions :func:`polychar`, :func:`polymult`, :func:`polyroot`, :func:`polyeval`, :func:`polymroot`
