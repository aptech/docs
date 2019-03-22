
polymroot
==============================================

Purpose
----------------

Computes the roots of the determinant of a matrix polynomial.

Format
----------------
.. function:: polymroot(c)

    :param c: 
    :type c: (N+1)*KxK matrix of coefficients of an Nth order polynomial of rank K

    :returns: r (*K*N vector*) containing the roots of the determinantal equation.

Remarks
-------

c is constructed of N+1 KxK coefficient matrices stacked vertically with
the coefficient matrix of the t\ n at the top, t\ (n-1) next, down to
the t\ 0 matrix at the bottom.

Note that this procedure solves the scalar problem as well, that is, the
one that POLYROOT solves.


Examples
----------------
Solve

::

    det(A2*t2 + A1*t + A0) = 0

::

    A2 =  1  2    A1 =  5  8   A0 = 3  4
          2  1         10  7        6  5

::

    // Setup coefficient matrices
    a2 = { 1 2, 2 1 };
    a1 = { 5 8, 10 7 };
    a0 = { 3 4, 6 5 };
    
    // The pipe operator '|' provides vertical concatenation
    print  polymroot(a2|a1|a0);

::

    -4.3027756
     -.69722436
     -2.6180340
     -.38196601

