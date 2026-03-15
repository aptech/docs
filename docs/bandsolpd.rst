
bandsolpd
==============================================

Purpose
----------------

Solves the system of equations :math:`Ax = b` for *x*, where *A* is a positive definite banded matrix stored in compact form. Banded matrices arise in spline interpolation, finite difference methods, and time series models where each variable depends only on nearby neighbors.

Format
----------------
.. function:: x = bandsolpd(b, A)

    :param b: right-hand side vector or matrix. If *b* has multiple columns, the system is solved for each column independently.
    :type b: KxM matrix

    :param A: positive definite banded matrix in compact form, where *N* is the number of bands (including the diagonal). See :func:`band` for how to convert a full matrix to compact form.
    :type A: KxN compact form matrix

    :return x: the solution vector(s). Each column of *x* is the solution corresponding to the matching column of *b*.

    :rtype x: KxM matrix

Remarks
-------

*A* is a positive definite banded matrix in compact form. See :func:`band` for a
description of the format of *A*.

*b* can have more than one column. If so, :math:`Ax = b` is solved for each
column. That is,

.. math:: A*x[.,i] = b[.,i]

Examples
--------

::

    // Create a 4x4 tridiagonal positive definite system
    // In compact banded form:
    //   col 1 = sub-diagonal elements (first element is 0, no element above row 1)
    //   col 2 = main diagonal elements
    A_compact = { 0 4,
                  1 5,
                  1 6,
                  1 7 };

    // Right-hand side vector
    b = { 8, 11, 13, 14 };

    // Solve Ax = b
    x = bandsolpd(b, A_compact);
    print x;

The above code produces:

::

       1.6111851
       1.5552597
       1.6125166
       1.7696405

.. seealso:: Functions :func:`band`, :func:`bandchol`, :func:`bandcholsol`, :func:`bandltsol`, :func:`bandrv`
