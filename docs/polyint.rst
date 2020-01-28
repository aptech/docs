
polyint
==============================================

Purpose
----------------

Calculates an Nth order polynomial interpolation.

Format
----------------
.. function:: y = polyint(xa, ya, x)

    :param xa: x values.
    :type xa: Nx1 vector

    :param ya: y values.
    :type ya: Nx1 vector

    :param x: x value to solve for.
    :type x: scalar

    :return y: result of interpolation or extrapolation.

    :rtype y: scalar

Global Input
------------

:_poldeg: (*scalar*), the degree of polynomial required, default 6.

Global Output
-------------

:_polerr: (*scalar*), interpolation error.

Examples
-----------

Example 1: Extrapolate the cosine function
+++++++++++++++++++++++++++++++++++++++++++

::

    // 0.1, 0.2, 0.3...0.8
    x = seqa(0.2, 0.1, 8);
    
    y = cos(x);
    
    // Extrapolate 'y' value at x=0
    y_hat = polyint(x, y, 0);

After the above code, *y_hat* will equal 1.0000003 which is near the actual cosine of 0 which is 1.

Example 2: Interpolate the cosine function
++++++++++++++++++++++++++++++++++++++++++++

::

    // 0.2, 0.4, 0.6...1
    x = seqa(0.2, 0.2, 5);
    
    y = cos(x);
    
    // Interpolate 'y' value at x=0.3
    y_hat = polyint(x, y, 0.3);


After the above code, *y_hat* will equal 0.95534104 which is near the actual cosine of 0.3 which is 0.95533649.


Remarks
-------

Calculates an Nth order polynomial interpolation or extrapolation of *x*
on *y* given the vectors xa and ya and the scalar *x*. The procedure uses
Neville's algorithm to determine an up to Nth order polynomial and an
error estimate.

Polynomials above degree 6 are not likely to increase the accuracy for
most data. Test *_polerr* to determine the required *_poldeg* for your
problem.

Technical Notes
----------------

Press, W.P., B.P. Flannery, S.A. Teukolsky, and W.T. Vettering. 
Numerical Recipes: The Art of Scientific Computing. NY: Cambridge Press, 1986.

Source
------

polyint.src

