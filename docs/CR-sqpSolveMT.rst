
sqpSolveMT
==============================================

Purpose
----------------

Solves the nonlinear programming problem.

Format
----------------
.. function:: sqpSolveMT(&fct, par1, ctl)

    :param &fct: pointer to a procedure that computes the
        function to be minimized. The first input to this procedure must be an instance of structure of type :class:`PV`.
    :type &fct: TODO

    :param par1: 
        The par1 instance is passed to the user-provided
        procedure pointed to by &fct.
        par1 is constructed using the ''pack''
        functions.
    :type par1: an instance of structure of type :class:`PV`

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

        "outx.par", "an instance of structure of type :class:`PV` containing the parameter estimates will be placed in the member matrix  out.par."
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



Remarks
-------

There is one required user-provided procedure, the one computing the
objective function to be minimized, and four other optional functions,
one each for computing the equality constraints, the inequality
constraints, the gradient of the objective function, and the Hessian of
the objective function.

All of these functions must take exactly the same input arguments. The
first input argument is an instance of a structure of type :class:`PV`. On input
to the call to sqpSolveMT, this PV structure contains starting values
for the parameters.

Both of the structures of type PV are set up using the PV ''pack''
procedures, pvPack, pvPackm, pvPacks, and pvPacksm. These procedures
allow for setting up a parameter vector in a variety of ways.

For example, we might have the following objective function for fitting
a nonlinear curve to data:

::

   proc (1) = micherlitz(struct PV par1, y, x);
      local p0,e,s2,x,y;
      p0 = pvUnpack(par1, "parameters");
      e = y - p0[1] - p0[2]*exp(-p0[3] * x);
      retp(e'*e);
   endp;

In this example the dependent and independent variables are passed to
the procedure as the second and third arguments to the procedure.

The other optional procedures must take exactly the same arguments as
the objective function. For example, to constrain the squared sum of the
first two parameters to be greater than one in the above problem,
provide the following procedure:

::

   proc (1) = ineqConst(struct PV par1, y, x);
      local p0;
      p0 = pvUnpack(p0, "parameters");
      retp( (p0[2]+p0[1])^2 - 1);
   endp;

The following is a complete example for estimating the parameters of the
Micherlitz equation in data with bounds constraints on the parameters
and where an optional gradient procedure has been provided:

::

   // Create data needed by 'Micherlitz' procedure
   y =  { 3.183,
          3.059,
          2.871,
          2.622,
          2.541,
          2.184,
          2.110,
          2.075,
          2.018,
          1.903,
          1.770,
          1.762,
          1.550 };
    
   x = seqa(1,1,13);
    
   // Declare control structure
   struct sqpSolveMTControl c0;
    
   // Initialize structure to default values
   c0 = sqpSolveMTControlCreate();
    
   // Constrain parameters to be positive  
   c0.bounds = 0~100; 
    
   // Declare 'par1' to be a PV structure
   struct PV par1;

   // Initialize 'par1'
   par1 = pvCreate();

   // Add 3x1 vector named 'parameters' to 'p1'
   par1 = pvPack(par1,.92|2.62|.114, "parameters");

   // Declare 'out' to be an sqpsolvemt control structure
   // to hold the results from sqpsolvemt
   struct sqpSolveMTout out;

   // Estimate the model parameters
   out = sqpSolveMT(&Micherlitz,par1,y,x,c0);
    
   // Print returned parameter estimates
   print "parameter estimates ";
   print pvUnPack(out.par, "parameters");
    
   proc Micherlitz(struct PV par1, y, x);
      local p0,e,s2;
      p0 = pvUnpack(par1, "parameters");
      e = y - p0[1] - p0[2]*exp(-p0[3] * x);
     retp(e'*e);
   endp;



Source
------

sqpsolvemt.src

.. seealso:: Functions :func:`sqpSolveMTControlCreate`, :func:`sqpSolveMTlagrangeCreate`
