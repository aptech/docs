
polyint
==============================================

Purpose
----------------

Calculates an Nth order polynomial interpolation.

Format
----------------
.. function:: polyint(xa, ya, x)

    :param xa: x values.
    :type xa: Nx1 vector

    :param ya: y values.
    :type ya: Nx1 vector

    :param x: x value to solve for.
    :type x: scalar

    :returns: y (*TODO*), result of interpolation or extrapolation.



Remarks
-------

Calculates an Nth order polynomial interpolation or extrapolation of x
on y given the vectors xa and ya and the scalar x. The procedure uses
Neville's algorithm to determine an up to Nth order polynomial and an
error estimate.

Polynomials above degree 6 are not likely to increase the accuracy for
most data. Test \_polerr to determine the required \_poldeg for your
problem.

