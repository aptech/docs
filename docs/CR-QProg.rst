
QProg
==============================================

Purpose
----------------
Solves the quadratic programming problem.

Format
----------------
.. function:: QProg(start, q, r, a, b, c, d, bnds)

    :param start: start values.
    :type start: Kx1 vector

    :param q: symmetric model matrix.
    :type q: KxK matrix

    :param r: model constant vector.
    :type r: Kx1 vector

    :param a: equality constraint coefficient matrix,
        or scalar 0, no equality constraints.
    :type a: MxK matrix

    :param b: equality constraint constant vector,
        or scalar 0, will be expanded to Mx1 vector of zeros.
    :type b: Mx1 vector

    :param c: inequality constraint coefficient matrix,
        or scalar 0, no inequality constraints.
    :type c: NxK matrix

    :param d: inequality constraint constant vector,
        or scalar 0, will be expanded to Nx1 vector of zeros.
    :type d: Nx1 vector

    :param bnds: bounds on x, the first column contains
        the lower bounds on x, and the second column the
        upper bounds. If scalar 0, the bounds for all elements
        will default to ±1e200.
    :type bnds: Kx2 matrix

    :returns: x (*Kx1 vector*), coefficients at the minimum of the function.

    :returns: u1 (*Mx1 vector*), Lagrangian coefficients of equality constraints.

    :returns: u2 (*Nx1 vector*), Lagrangian coefficients of inequality constraints.

    :returns: u3 (*Kx1 vector*), Lagrangian coefficients of lower bounds.

    :returns: u4 (*Kx1 vector*), Lagrangian coefficients of upper bounds.

    :returns: ret (*scalar*), return code.

    .. csv-table::
        :widths: auto

        "0     successful termination"
        "1     max iterations exceeded"
        "2     machine accuracy is insufficient to maintain         decreasing function values"
        "3     model matrices not conformable"
        "< 0     active constraints inconsistent"



Global Input
------------

+-----------------+-----------------------------------------------------+
| \_qprog_maxit   | scalar, maximum number of iterations. Default =     |
|                 | 1000.                                               |
+-----------------+-----------------------------------------------------+


Remarks
-------

QProg solves the standard quadratic programming problem:

::

                   min ½x'Qx - x'R
               

subject to constraints,

::

                   Ax = B
                   Cx ≤ D
               

and bounds,

::

                   xlow ≤ x ≤ xup
               



Source
------

qprog.src

