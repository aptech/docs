
QProg
==============================================

Purpose
----------------
Solves the quadratic programming problem.

Format
----------------
.. function:: { x, u1, u2, u3, u4, u5 } = QProg(start, q, r, a, b, c, d, bnds)

    :param start: start values.
    :type start: Kx1 vector

    :param q: symmetric model matrix.
    :type q: KxK matrix

    :param r: model constant vector.
    :type r: Kx1 vector

    :param a: equality constraint coefficient matrix, or scalar 0, no equality constraints.
    :type a: MxK matrix

    :param b: equality constraint constant vector, or scalar 0, will be expanded to Mx1 vector of zeros.
    :type b: Mx1 vector

    :param c: inequality constraint coefficient matrix, or scalar 0, no inequality constraints.
    :type c: NxK matrix

    :param d: inequality constraint constant vector, or scalar 0, will be expanded to Nx1 vector of zeros.
    :type d: Nx1 vector

    :param bnds: bounds on :class:`x`, the first column contains the lower bounds on *x*, and the second column the
        upper bounds. If scalar 0, the bounds for all elements will default to ±1e200.
    :type bnds: Kx2 matrix

    :return x: coefficients at the minimum of the function.

    :rtype x: Kx1 vector

    :return u1: Lagrangian coefficients of equality constraints.

    :rtype u1: Mx1 vector

    :return u2: Lagrangian coefficients of inequality constraints.

    :rtype u2: Nx1 vector

    :return u3: Lagrangian coefficients of lower bounds.

    :rtype u3: Kx1 vector

    :return u4: Lagrangian coefficients of upper bounds.

    :rtype u4: Kx1 vector

    :return ret: return code.

        .. csv-table::
            :widths: auto

            "*0*", "termination"
            "*1*", "iterations exceeded"
            "*2*", "accuracy is insufficient to maintain decreasing function values"
            "*3*", "matrices not conformable"
            "*< 0*", "constraints inconsistent"

    :rtype ret: scalar

Global Input
------------

:_qprog_maxit: (*scalar*), maximum number of iterations. Default = 1000.


Remarks
-------

:func:`QProg` solves the standard quadratic programming problem:

.. math::

    min\; \frac{1}{2} x'Qx - x'R

subject to constraints,

.. math::

    Ax = B\\
    Cx ≤ D


and bounds,

.. math::

    x_{low} ≤ x ≤ x_{up}

Source
------

qprog.src
