
bandltsol
==============================================

Purpose
----------------
Solves the system of equations :math:`Ax = b` for *x*, where *A* is a lower triangular banded matrix.

Format
----------------
.. function:: x = bandltsol(b, A)

    :param b:
    :type b: KxM matrix

    :param A:
    :type A: KxN compact form matrix

    :return x: KxM matrix.

    :type x: matrix

Remarks
-------

*A* is a lower triangular banded matrix in compact form. See :func:`band` for a
description of the format of *A*.

*b* can have more than one column. If so, :math:`Ax = b` is solved for each
column. That is,

.. math:: A*x[.,i] = b[.,i];

Examples
----------------

::

    // Create matrix 'A' and right-hand side 'b'
    A = { 1 2 0 0,
          2 8 1 0,
          0 1 5 2,
          0 0 2 3 };

    b = { 1.3, 2.1, 0.7, 1.8 };

    /*
    ** Create a matrix containing the lower triangular part
    ** of 'A'
    */
    Alower = lowmat(A);

    // Create banded matrix from of 'Alower'
    Abandlow = band(Alower, 1);

    // Solve the system of equations
    x = bandltsol(b, Abandlow);

After the code above:

::

             1  0  0  0         0  1      1.300     1.3            1.3
    Alower = 2  8  0  0 Aband = 2  8 x = -0.063 b = 2.1 Alower*x = 2.1
             0  1  5  0         1  5      0.153     0.7            0.7
             0  0  2  3         2  3      0.498     1.8            1.8

.. seealso:: Functions :func:`band`, :func:`bandchol`, :func:`bandcholsol`, :func:`bandrv`, :func:`bandsolpd`
