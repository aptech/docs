
QProgmt
==============================================

Purpose
----------------
Solves the quadratic programming problem.

Format
----------------
.. function:: qOut = QProgmt(qIn)

    :param qIn: instance of a :class:`qprogMTIn` structure containing the following members:

        .. csv-table::
            :widths: auto

            "qIn.start", "Kx1 vector, start values."
            "qIn.q", "KxK matrix, symmetric model matrix."
            "qIn.r", "Kx1 vector, model constant vector."
            "qIn.a", "MxK matrix, equality constraint coefficient matrix, or scalar 0, no equality constraints."
            "qIn.b", "Mx1 vector, equality constraint constant vector, or scalar 0, will be expanded to Mx1 vector of zeros."
            "qIn.c", "NxK matrix, inequality constraint coefficient matrix, or scalar 0, no inequality constraints."
            "qIn.d", "Nx1 vector, inequality constraint constant vector, or scalar 0, will be expanded to Nx1 vector of zeros."
            "qIn.bounds", "Kx2 matrix, bounds on *qOut.x*, the first column contains the lower bounds on *qOut.x*, and the second column the upper bounds. If scalar 0, the bounds for all elements will default to ±1e200."
            "qIn.maxit", "scalar, maximum number of iterations. Default = 1000."

    :type qIn: struct

    :return qOut: instance of :class:`qprogMTOut` struct containing the following members:

        .. list-table::
            :widths: auto

            * - qOut.x
              - Kx1 vector, coefficients at the minimum of the function.
            * - qOut.lagrange
              - instance of a qprogMTLagrange structure containing the following members:
            * - qOut.lagrange.lineq
              - Mx1 vector, Lagrangian coefficients of equality constraints.
            * - qOut.lagrange.linineq
              - Nx1 vector, Lagrangian coefficients of inequality constraints.
            * - qOut.lagrange.bounds
              - Kx2 matrix, Lagrangian coefficients of bounds, the first column contains the lower bounds and the secondthe upper bounds.
            * - qOut.ret
              - scalar, return code.

                :*0*: successful termination
                :*1*: max iterations exceeded
                :*2*: machine accuracy is insufficient to maintain decreasing function values
                :*3*: model matrices not conformable
                :*< 0*: active constraints inconsistent
               


    :rtype qOut: struct


Remarks
-------

:func:`QProgmt` solves the standard quadratic programming problem:

.. math::

   min⁡ \frac{1}{2}x′Qx⁢− x′R

subject to constraints,

.. math::

   Ax⁢ = BC\\
   Cx \geq D

and bounds,

.. math::

   x_{low} \leq x \leq x_{up}

Source
------

qprogmt.src

.. seealso:: Functions :func:`QProgmtInCreate`
