
eqSolvemt
==============================================

Purpose
----------------
Solves a system of nonlinear equations.

Format
----------------
.. function:: out = eqSolvemt(&fct, par, ..., c)

    :param &fct: pointer to a procedure that computes the
        function to be minimized. This procedure must have an instance of a :class:`PV` structure 
        containing the parameters as the first input. Extra data needed by this function may
        be passed in after the :class:`PV` structure, but before the control structure. 
        This procedure must have one output argument, a column vector
        containing the result of each equation.
    :type &fct: scalar function pointer

    :param par: The *par* instance is passed to the user-provided procedure pointed to by *&fct*. *par* is
        constructed using the :func:`pvPack` functions.
    :type par: an instance of a :class:`PV` structure

    :param ....: Optional extra arguments.
        These arguments are passed untouched to the user-provided objective function, by :func:`eqSolveMT`.

    :param c: Optional. Normally an instance is initialized by calling
        :func:`eqSolvemtControlCreate` and members of this instance
        can be set to other values by the user. For an instance named
        *c*, the members are:

        .. list-table::
            :widths: auto

            * - *c.jacobianProc*
              - pointer to a procedure which computes the analytical Jacobian. By default, :func:`eqSolvemt` will compute the Jacobian numerically.
            * - *c.maxIters*
              - scalar, the maximum number of iterations. Default = 100.
            * - *c.stepTolerance*
              - scalar, the step tolerance. Default = :math:`macheps^{2/3}`
            * - *c.typicalF*
              - Kx1 vector of the typical :code:`fct(x)` values at a point not near a root, used for scaling. This becomes important when the magnitudes of the components of :code:`fct(x)` are expected to be very different. By default, function values are not scaled.
            * - *c.typicalX*
              - Kx1 vector of the typical magnitude of *x*, used for scaling. This becomes important when the magnitudes of the components of *x* are expected to be very different. By default, variable values are not scaled.
            * - *c.printIters*
              - scalar, if nonzero, iteration information is printed. Default = 0.
            * - *c.tolerance*
              - scalar, the tolerance of the scalar function :math:`f = 0.5*||fct(X)||2` required to terminate the algorithm. That is, the condition that :math:`|f(x)| <= c.tolerance` must be met before that algorithm can terminate successfully. Default = 1e-5.
            * - *c.altNames*
              - Kx1 string array of alternate names to be used by the printed output. By default, the names :code:`X1,X2,X3...` will be used.
            * - *c.title*
              - string, printed as a title in output.
            * - *c.output*
              - scalar. If non-zero, final results are printed.

    :type c: an instance of an :class:`eqSolvemtControl` structure.

    :returns: **out** (*struct*) - instance of :class:`eqSolvemtOut` struct. For an instance named *out*, the members are:

        .. list-table::
            :widths: auto

            * - *out.par*
              - an instance of a :class:`PV` structure containing the parameter estimates.
            * - *out.fct*
              - scalar, function evaluated at *x*
            * - *out.retcode*
              - scalar, return code:

                  :-1: Jacobian is singular.
                  :1: Norm of the scaled function value is less than *c.tolerance*. *x* given is an approximate root of :code:`fct(x)` (unless c.tolerance is too large).
                  :2: The scaled distance between the last two steps is less than the step-tolerance (*c.stepTolerance*). *x* may be an approximate root of :code:`fct(x)`, but it is also possible that the algorithm is making very slow progress and is not near a root, or the step-tolerance is too large.
                  :3: The last global step failed to decrease :code:`norm2(fct(x))` sufficiently; either *x* is close to a root of :code:`fct(x)` and no more accuracy is possible, or an incorrectly coded analytic Jacobian is being used, or the secant approximation to the Jacobian is inaccurate, or the step-tolerance is too large.
                  :4: Iteration limit exceeded.
                  :5: Five consecutive steps of maximum step length have been taken; either :code:`norm2(fct(x))` asymptotes from above to a finite value in some direction or the maximum step length is too small.
                  :6: *x* seems to be an approximate local minimizer of :code:`norm2(fct(x))` that is not a root of :code:`fct(x)`. To find a root of :code:`fct(x)`, restart :func:`eqSolvemt` from a different region.

Remarks
-------

The equation procedure should return a column vector containing the
result for each equation. For example, consider a two-equation system given by:

.. math:: x_1^2 + x_2^2 - 2 = 0
.. math:: e^{x_1-1} + x_2^3 - 2 = 0


::

   proc (1) = f(struct PV p);
      local x1, x2, eqns;

      // Set x1
      x1 = pvUnpack(p, "x1");

      // Set x2
      x2 = pvUnpack(p, "x2");

      // Preallocate output vector
      eqns = { 0, 0 };

      // Equation 1
      eqns[1] = x1^2 + x2^2 - 2;

      // Equation 2
      eqns[2] = exp(x1-1) + x2^3 - 2;

      retp(eqns);
   endp;

Note that the first equation in the system is contained in the first row of ``eqns`` and the second equation is contained in the second row of ``eqns``.



Examples
----------------

Basic usage
+++++++++++
For example, consider a two-equation system given by:

.. math:: x_1^2 + x_2^2 - 5 = 0
.. math:: e^{x_1-1} + x_2^3 - 5 = 0


::

    new;

    // Declare 'par' to be an instance of a PV vector
    struct PV par;

    /*
    ** Create default PV struct and add a parameter
    ** named 'x1' with a starting value of 1
    */
    par = pvPack(pvCreate(), 1, "x1");

    /*
    ** Add a parameter named 'x2' to 'par'
    ** with a starting value of 1
    */
    par = pvPack(par, 1, "x2");

    /*
    ** Solve the system of equations
    ** and print the output to the screen
    */
    call eqSolvemt(&fct, par);

    // The definition of the function to be minimized
    proc fct(struct PV p);
       local x1, x2, z;
       x1 = pvUnpack(p, "x1");
       x2 = pvUnpack(p, "x2");
       z = (x1^2 + x2^2 - 5) | (exp(x1 - 1) + x2^3 - 5);
       retp(z);
    endp;

After the code above, a short report will be printed to the program input/output window. Part of the output is displayed below:

::

    --------------------------------------------------------------------
    VARIABLE          START               ROOTS             F(ROOTS)
    --------------------------------------------------------------------

    X1               1.00000           1.7146639625        0.0000000001
    X2               1.00000           1.4352447511        0.0000000002
    --------------------------------------------------------------------

Using control and output structures
+++++++++++++++++++++++++++++++++++
Again, consider a two-equation system given by:

.. math:: x_1^2 + x_2^2 - 5 = 0
.. math:: e^{x_1-1} + x_2^3 - 5 = 0


::

    new;

    // Declare control structure and fill with defaults
    struct eqSolvemtControl c;
    c = eqSolvemtControlCreate();

    // Turn on printing of iteration information
    c.printIters = 1;

    // Assign variable names printed output
    c.altNames = "alpha" $| "beta";

    // Declare 'par' to be an instance of a PV vector
    struct PV par;

    /*
    ** Create default PV struct and add a parameter
    ** named 'x1' with a starting value of 1
    */
    par = pvPack(pvCreate(),1, "x1");

    /*
    ** Add a parameter named 'x2' to 'par'
    ** with a starting value of 1
    */
    par = pvPack(par, 1, "x2");

    // Declare output structure to hold results
    struct eqSolvemtOut out;

    // Solve the system of equations
    out = eqSolvemt(&fct, par, c);

    // The definition of the function to be minimized
    proc fct(struct PV p);
       local x1, x2, z;
       x1 = pvUnpack(p, "x1");
       x2 = pvUnpack(p, "x2");
       z = (x1^2 + x2^2 - 5) | (exp(x1 - 1) + x2^3 - 5);
       retp(z);
    endp;

The code above will print out a report similar to the previous example. Notice that the variable names in the report are what we assigned to the *altNames* member of the control structure.

::

    --------------------------------------------------------------------------------
    VARIABLE              START                   ROOTS                 F(ROOTS)
    --------------------------------------------------------------------------------

    alpha                1.00000               1.7146639625            0.0000000001
    beta                 1.00000               1.4352447511            0.0000000002
    --------------------------------------------------------------------------------

The parameter values returned by :func:`eqSolveMT` are located in the par member of the :class:`eqsolveMTOut` struct. They can be accessed with :func:`pvGetParVector` or :func:`pvUnpack` like this:

::

    // Return the values of 'x1' and 'x2' as a 2x1 vector
    x_all = pvGetParVector(out.par);

    // Return the value of 'x1'
    x1 = pvUnpack(out.par, "x1");

    // Return the value of 'x2'
    x2 = pvUnpack(out.par, "x2");

Source
------

eqsolvemt.src

.. seealso:: Functions :func:`eqSolvemtControlCreate`, :func:`eqSolvemtOutCreate`
