Constraints
===========

There are two general types of constraints:

1. Nonlinear equality constraints,
2. Nonlinear inequality constraints.

However, for computational convenience, they are divided into five types:

1. Linear equality,
2. Linear inequality,
3. Nonlinear equality,
4. Nonlinear inequality,
5. Bounds.

Linear Equality Constraints
---------------------------

Linear equality constraints are of the form:

.. math::

    A\theta = B

where :math:`A` is an :math:`m_1 \times k` matrix of known constants, :math:`B` an :math:`m_1 \times 1` vector of known constants, and :math:`\theta` the vector of parameters.

The specification of linear equality constraints is done by assigning the :math:`A` and :math:`B` matrices to members `A` and `B` of an instance of a :class:`comtControl` structure.

Examples
++++++++

Example 1
^^^^^^^^^^^^^
Set the constraint represented by the equation :math:`1.5x_1 + 2.1x_2 = 14`:

::

    struct comtControl ctl;
    ctl = comtControlCreate();

    // Set constraint
    ctl.A = { 1.5, 2.1 };
    ctl.B = 14;

Example 2
^^^^^^^^^^^^
Constrain the first of four parameters to be equal to the third represented by the equation :math:`x_1 - x_3 = 0`:

::

    struct comtControl ctl;
    ctl = comtControlCreate();

    // Set constraint
    ctl.A = { 1, 0, -1, 0 };
    ctl.B = { 0 };

Linear Inequality Constraints
-----------------------------

Linear inequality constraints are of the form:

.. math::

    C\theta \geq D

where :math:`C` is an :math:`m_1 \times n` matrix of known constants, :math:`D` an :math:`m_1 \times 1` vector of known constants, and :math:`\theta` the vector of parameters.

The specification of linear inequality constraints is done by assigning the :math:`C` and :math:`D` matrices to members `C` and `D` of an instance of a :class:`comtControl` structure.

Examples
+++++++++

Example 1
^^^^^^^^^^^^
Constrain the first of three parameters to be greater than or equal to 2.5 represented by the equation :math:`x_1 \geq 2.5`:

::

    struct comtControl ctl;
    ctl = comtControlCreate();

    // Add the linear inequality constraint:
    ctl.C = { 1, 0, 0 };
    ctl.D = 2.5;

Example 2
^^^^^^^^^^^^^
Constrain the first of four parameters to be greater than the third and, as well, the second plus the fourth greater than 10, represented by the equations :math:`x_1 > x_3` and :math:`x_2 + x_4 > 10`:

::

    struct comtControl ctl;
    ctl = comtControlCreate();

    // Add the linear inequality constraint
    ctl.C = { 1, 0, -1, 0,
              0, 1,  0, 1 };
    ctl.D = { 0,
              10 };

Nonlinear Equality Constraints
------------------------------

Nonlinear equality constraints are of the form:

.. math::

    H(\theta) = 0

where :math:`H(\theta)` is an arbitrary user-supplied function. Nonlinear equality constraints are specified by assigning the procedure pointer to the *eqProc* member of an instance of a :class:`comtControl` structure. This procedure has one required input argument: the model parameters--either as a :math:`P \times 1` matrix or a :class:`PV` structure containing the parameters. Any optional dynamic arguments passed to :func:`comt` will also be passed to this function.

Examples
++++++++++
Apply the nonlinear equality constraint for the equation :math:`x_1 + x_2^2 = 0`:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    // User defined procedure to compute
    // nonlinear equality constraints
    proc (1) = myEqProc(theta);
      local L, K;

      retp(theta[1] + theta[2]^2);
    endp;

    // Declare 'ctl' to be a comtControl struct
    // and fill with default settings
    struct comtControl ctl;
    ctl = comtControlCreate();

    // Assign pointer to equality constraint procedure
    ctl.eqProc = &myEqProc;

Suppose you wish to constrain a covariance matrix to be positive definite:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    struct comtControl ctl;
    ctl = comtControlCreate();

    proc eqp(b);
      retp(b'b - 1);
    endp;

    ctl.eqProc = &eqp;

Nonlinear Inequality Constraints
---------------------------------

Nonlinear inequality constraints are of the form:

.. math::

    G(\theta) \geq 0

where :math:`G(\theta)` is an arbitrary user-supplied function. Nonlinear inequality constraints are specified by assigning the procedure pointer to the *ineqProc* member of an instance of a :class:`comtControl` structure. This procedure has one required input argument: the model parameters. This can be in the form of a :class:`PV` structure containing the parameters or a standard **GAUSS** :math:`P \times 1` matrix. Make sure to use the same form that is expected by your objective procedure. Any optional dynamic arguments passed to :func:`comt` will also be passed to this function.

Examples
++++++++++

Minimize the production cost of 1000 widgets with two variables Labor (L) and Capital (K) 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The production equation is :math:`20 \sqrt{L} \sqrt{K} = 1000`:

::

    proc (1) = ineqProc(theta);
        local L, K;
        L = theta[1];
        K = theta[2];

        // Return the difference between the
        // required quantity 1000 units and the
        // quantity produced at the given parameters
        retp(20 * sqrt(L) * sqrt(K) - 1000);
    endp;

    // Declare 'ctl' to be a comtControl structure
    // and fill with default settings
    struct comtControl ctl;
    ctl = comtControlCreate();

    // Assign pointer to inequality procedure
    ctl.ineqProc = &ineqProc;

Suppose you wish to constrain a covariance matrix to be positive definite
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    proc ineqp(x);
        local v;

        // Expand 'x' into symmetric matrix
        v = xpnd(x);
        retp(minc(eigh(v)) - 1e-5);
    endp;

    // Declare 'ctl' to be a comtControl structure
    // and fill with default settings
    struct comtControl ctl;
    ctl = comtControlCreate();

    // Assign pointer to inequality procedure
    ctl.ineqProc = &ineqp;

Bounds
------

Bounds are a type of linear inequality constraint. For computational convenience, they may be specified separately from the other inequality constraints. To specify bounds, the lower and upper bounds respectively are entered in the first and second columns of a matrix that has the same number of rows as the parameter vector. This matrix is assigned to the *bounds* member of an instance of a :class:`comtControl` structure.

If the bounds are the same for all of the parameters, only the first row is necessary.

Examples
+++++++++++
To bound four parameters to the ranges:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    // Declare 'ctl' to be a comtControl struct
    // and fill with default settings
    struct comtControl ctl;
    ctl = comtControlCreate();

    // Set separate bounds for each of four parameters
    ctl.bounds = { -10, 10,
                   -10, 0,
                     1, 10,
                     0, 1 };

Suppose all of the parameters are to be bounded between -50 and +50
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    ctl.bounds = {-50, 50};

This specification ensures that all parameters within the model are constrained to operate within the defined bounds, thus adhering to any physical, financial, or other types of constraints that may apply to the parameters being estimated.
