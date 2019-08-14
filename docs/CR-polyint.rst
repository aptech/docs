
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

    :type y: TODO

Global Input
------------

:_poldeg: (*scalar*), the degree of polynomial required, default 6.

Global Output
------------

:_polerr: (*scalar*), interpolation error.

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

