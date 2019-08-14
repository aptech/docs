
QNewtonmt
==============================================

Purpose
----------------
Minimize an arbitrary function.

Format
----------------
.. function:: out = QNewtonmt(&fct, par[, ...[, c]])

    :param &fct: pointer to a procedure that computes the
        function to be minimized. This procedure must have at least one input
        argument, an instance of a PV structure containing
        the parameters. And, one output argument, the value of the function evaluated
        at the input vector of parameter values.
    :type &fct: function pointer

    :param par: Optional, an instance of a :class:`PV` structure. The *par* instance is passed to the user-provided procedure
        pointed to by *&fct*. *par* is constructed using the :func:`pvPack` functions.
    :type par: struct

    :param ...: Optional extra arguments. These arguments are passed untouched to the user-provided 
        objective function, by :func:`QNewtonmt`.
    :type ...: any

    :param c: An instance of a :class:`QNewtonmtControl` structure. Normally an instance is initialized 
        by calling :func:`QNewtonmtControlCreate` and members of this instance can be set to other values by the user.

        For an instance named *c*, the members are:

        .. csv-table::
            :widths: auto
    
            "c.CovType", "scalar, if 1, ML covariance matrix, else if 2, QML covariance matrix is computed. Default is 0, no covariance matrix."
            "c.GradProc", "scalar, pointer to a procedure that computes the gradient of the function with respect to the parameters. Default = ., i.e., no gradient procedure has been provided."
            "c.MaxIters", "scalar, maximum number of iterations. Default = 1e+5."
            "c.MaxTries", "scalar, maximum number of attemps in random search. Default = 100."
            "c.relGradTol", "scalar, convergence tolerance for gradient of estimated coefficients. Default = 1e-5. When this criterion has been satisifed :func:`QNewtonmt` exits the iterations."
            "c.randRadius", "scalar, If zero, no random search is attempted. If nonzero, it is the radius of the random search. Default = .001."
            "c.output", "scalar, if nonzero, results are printed. Default = 0."
            "c.PrintIters", "scalar, if nonzero, prints iteration information. Default = 0."
            "c.disableKey", "scalar, if nonzero, keyboard input disabled"

    :type c: struct

    :return out: instance of :class:`QNewtonmtOut` struct.

        For an instance named *out*, the members are:

        .. list-table::
            :widths: auto
    
            * - out.par
              - instance of a :class:`PV` structure containing the parameter estimates will be placed in the member matrix *out.par*.
            * - out.fct
              - scalar, function evaluated at *x*.
            * - out.retcode
              - scalar, return code:

                :0: normal convergence.
                :1: forced exit.
                :2: maximum number of iterations exceeded.
                :3: function calculation failed.
                :4: gradient calculation failed.
                :5: Hessian calculation failed.
                :6: line search failed.
                :7: error with constraints.
                :8: function complex.

            * - out.moment
              - KxK matrix, covariance matrix of parameters, if *c.covType* > 0.
            * - out.hessian
              - KxK matrix, matrix of second derivatives of objective function with respect to parameters.

    :type out: struct

Remarks
-------

There is one required user-provided procedure, the one computing the
objective function to be minimized, and another optional functions, the
gradient of the objective function.

These functions have one input argument that is an instance of type
struct :class:`PV`. On input to the call to :func:`QNewtonmt`, the first argument
contains starting values for the parameters. The arguments following the
:class:`PV` structure (except for the optional control structure) contain any
required data.

The :class:`PV` structures are set up using the :class:`PV` pack procedures, :func:`pvPack`,
:func:`pvPackm`, :func:`pvPacks`, and :func:`pvPacksm`. These procedures allow for setting up a
parameter vector in a variety of ways.

For example, we might have the following objective function for fitting
a nonlinear curve to data:

::

   proc (1) = Micherlitz(struct PV par1, y, x);
      local p0,e,s2;
      p0 = pvUnpack(par1, "parameters");
      e = y - p0[1] - p0[2]*exp(-p0[3] * x);
      retp(-lnpdfmvn(e,e'e/rows(e)));
   endp;

In this example the dependent and independent variables are passed to
the procedure as the second and third arguments to the procedure.

If the objective function is the negative of a proper log-likelihood,
and if *c.covType* is set to 1, the covariance matrix of the parameters is
computed and returned in *out.moment*, and standard errors, t-statistics
and probabilities are printed if *c.output* = 1.

If the objective function returns the negative of a vector of
log-likelihoods, and if *c.covType* is set to 2, the quasi-maximum
likelihood (QML) covariance matrix of the parameters is computed.


Examples
----------------

::

    // Define function to be minimized
    // The first input is a PV structure containing the parameters
    // The following arguments contain data, other than the parameters,
    // which is needed by the function
    proc (1) = Micherlitz(struct PV par1, y, x);
       local p0,e,s2;
       p0 = pvUnpack(par1, "parameters");
       e = y - p0[1] - p0[2]*exp(-p0[3] * x);
       retp(-lnpdfmvn(e,e'e/rows(e)));
    endp;
    
    // Create extra data needed by objective function
    y = { 3.183,
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
     
    // Declare 'par' to be a PV structure
    struct PV par;
    
    // Set PV defaults in 'par'
    par = pvCreate();
    
    // Add a variable named 'parameters' to par with a 3x1
    // vector of starting values
    par = pvPack(par, 1|1|0, "parameters");
     
    // Declare 'out' to be a QNewtonmtOut structure
    // to hold data returned by QNewtonmt
    struct QNewtonmtout out;
    
    // Minimize the 'Micherlitz' function
    out = QNewtonmt(&Micherlitz,par,y,x);
    
    // Get returned parameters from the output structure
    parms = pvGetParVector(out.par);
    
    // Print returned parameters
    print parms;

The code above should return the following output:

::

    0.96312060 
    2.5189989 
    0.10305485

Source
------

qnewtonmt.src

.. seealso:: Functions :func:`QNewtonmtControlCreate`, :func:`QNewtonmtOutCreate`

