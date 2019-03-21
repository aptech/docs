
sqpSolveMT
==============================================

Purpose
----------------

Solves the nonlinear programming problem.

Format
----------------
.. function:: sqpSolveMT(&fct, par1, ctl)

    :param &fct: pointer to a procedure that computes the
        function to be minimized. The first input to this procedure must be an instance of structure of type PV.
    :type &fct: TODO

    :param par1: 
        The par1 instance is passed to the user-provided
        procedure pointed to by &fct.
        par1 is constructed using the ''pack''
        functions.
    :type par1: an instance of structure of type PV

    :param ...: Optional extra arguments.
        These arguments are passed untouched to the user-provided objective function, by sqpSolveMT.
    :type ...: TODO

    :param ctl: instance of an sqpSolveMTControl
        structure. Normally an instance is initialized by calling
        sqpSolveMTControlCreate and members of this instance
        can be set to other values by the user. For an instance named
        ctl, the members are:
    :type ctl: Optional input

    .. csv-table::
        :widths: auto

        "ctl.A", "MxK matrix, linear equality  constraint coefficients:  ctl.A * p =  ctl.B where p is a vector of the parameters."
        "ctl.B", "Mx1 vector, linear equality  constraint constants:  ctl.A *  p = ctl.B where p is a vector of the parameters."
        "ctl.C", "MxK matrix, linear inequality constraint coefficients:  ctl.C *  p >=ctl.D where p is a vector of the parameters."
        "ctl.D", "Mx1 vector, linear  inequality constraint constants:  ctl.C * p>=ctl.D where  p is a vector of the parameters."
        "ctl.eqProc", "scalar, pointer to a procedure that computes the nonlinear equality constraints. When such a  procedure has been provided, it has one input argument, a structure of type SQPdata, and one output argument, a vector of computed equality constraints. For more details see Remarks below.  Default = ., i.e., no equality procedure."
        "ctl.weights", "vector, weights for objective function returning a vector. Default = 1."
        "ctl.ineqProc", "scalar, pointer to a  procedure that computes the nonlinear inequality constraints. When  such a procedure has been provided, it has one input argument, a  structure of type SQPdata, and one output argument, a vector of computed inequality constraints. For more details see  Remarks below. Default = ., i.e., no inequality procedure."
        "ctl.bounds", "1x2 or Kx2  matrix, bounds on parameters. If 1x2 all  parameters have same bounds. Default = -1e256 1e256 ."
        "ctl.covType", "scalar, if 2, QML covariance  matrix, else if 0, no covariance matrix is computed, else ML  covariance matrix is computed."
        "ctl.gradProc", "scalar, pointer to a  procedure that computes the gradient of the function with respect  to the parameters. Default = ., i.e., no gradient procedure has  been provided."
        "ctl.hessProc", "scalar, pointer to a  procedure that computes the Hessian, i.e., the matrix of second  order partial derivatives of the function with respect to the  parameters. Default = ., i.e., no Hessian procedure has been provided."
        "ctl.maxIters", "scalar, maximum number of  iterations. Default = 1e+5."
        "ctl.dirTol", "scalar, convergence tolerance  for gradient of estimated coefficients. Default = 1e-5. When this  criterion has been satisfied SQPSolve exits the iterations."
        "ctl.feasibleTest", "scalar, if nonzero, parameters are tested for feasibility before computing function in  line search. If function is defined outside inequality boundaries, then this test can be turned off. Default = 1."
        "ctl.randRadius", "scalar, If zero, no random search is attempted. If nonzero, it is the radius of random search  which is invoked whenever the usual line search fails. Default = .01."
        "ctl.output", "scalar, if nonzero, results  are printed. Default = 0."
        "ctl.printIters", "scalar, if nonzero, prints iteration information. Default = 0."

    :returns: out (*TODO*), an instance of an sqpSolveMTout
        structure. For an instance named  out, the members are:

    .. csv-table::
        :widths: auto

        "outx.par", "an instance of structure of type PV containing the parameter estimates will be placed in the member matrix  out.par."
        "out.fct", "scalar, function evaluated at x."
        "out.lagr", "an instance of a SQPLagrange structure containing the Lagrangeans for the constraints. The members are:"
        "", "out.lagr.lineq", "Mx1 vector, Lagrangeans of linear equality constraints."
        "", "out.lagr.nlineq", "Nx1 vector, Lagrangeans of nonlinear equality constraints."
        "", "out.lagr.linineq", "Px1 vector,Lagrangeans of linear inequality constraints."
        "", "out.lagr.nlinineq", "Qx1 vector,Lagrangeans of nonlinear inequality constraints."
        "", "out.lagr.bounds", "Kx2 matrix, Lagrangeans of bounds."
        "Whenever a constraint is active, its associated Lagrangean will be nonzero. For any constraint that is inactive throughout the iterations as well as at convergence, the corresponding Lagrangean matrix will be set to a scalar missing value."
        "out.retcode", "return code:"
        "", "0", "normal convergence."
        "", "1", "forced exit."
        "", "2", "maximum number of iterations exceeded."
        "", "3", "function calculation failed."
        "", "4", "gradient calculation failed."
        "", "5", "Hessian calculation failed."
        "", "6", "line search failed."
        "", "7", "error with constraints."
        "", "8", "function complex."

