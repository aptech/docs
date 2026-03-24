
polymat
==============================================

Purpose
----------------

Returns a matrix containing the powers of the elements of x from 1 to p.

Format
----------------
.. function:: y = polymat(x, p)

    :param x: data
    :type x: NxK matrix

    :param p: positive integer.
    :type p: scalar

    :return y: contains powers of the elements of *x* from 1 to *p*.
        The first *K* columns will contain first powers, the second *K* columns second powers, and so on.

    :rtype y: Nx(p*K) matrix

Remarks
-------

To do polynomial regression use ols:

::

   { vnam, m, b, stb, vc, stderr, sigma, cx, rsq, resid, dwstat } = ols(0, y, polymat(x, p));


Examples
----------------

::

    x = { 1, 2, 3 };

    // Create matrix with powers 1 through 3
    y = polymat(x, 3);
    print y;

The code above produces the following output:

::

    1.0000000   1.0000000   1.0000000
    2.0000000   4.0000000   8.0000000
    3.0000000   9.0000000   27.000000

Each column contains the elements of *x* raised to the 1st, 2nd, and 3rd powers.

Source
------

polymat.src

.. seealso:: Functions :func:`polychar`, :func:`polymult`, :func:`polyroot`, :func:`polyeval`
