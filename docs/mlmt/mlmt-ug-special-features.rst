Special Features in Maximum Likelihood MT
======================================================

The following sections describe the special features found in **Maximum Likelihood MT**.

Structures
----------

In **MLMT**, the same procedure that computes the objective function will also be used to compute analytical derivatives if they are being provided. This procedure will have an additional argument which tells the function whether to compute the log-likelihood or objective, the first derivatives, the second derivatives, or all three. This means that calculations in common will not have to be redone.

:class:`modelResults` Structure
+++++++++++++++++++++++++++++++

This objective procedure will return a :class:`modelResults` structure which has three member variables:

- **function**: Scalar value of the objective function.
- **gradient**: Optional Kx1 vector of first derivatives.
- **Hessian**: Optional KxK matrix of second derivatives.

::

    //  Example log-likelihood function
    proc (1) = myLogLikelihood(struct PV parms, ind);
    struct modelResults mm;

        // Perform any calculations common to
        // objective function, gradient, and Hessian

        // If the first element of 'ind' is
        // non-zero, calculate objective function
        if ind[1];
          mm.function = // Calculate objective function
        endif;

        // If the second element of 'ind' is
        // non-zero, calculate gradient
        if ind[2];
          mm.gradient = // Calculate gradient
        endif;

        // If the third element of 'ind' is
        // non-zero, calculate Hessian
        if ind[3];
          mm.Hessian = // Calculate Hessian
        endif;

        // Return modelResults structure
        retp(mm);
    endp;

In the objective function the function value return is required. However, the derivatives are optional or even partially optional, i.e., you can compute a subset of the derivatives if you like, and the remaining will be computed numerically. When computing only a subset of the derivatives, set the uncomputed element of the gradient vector to a missing value. **MLMT** will attempt to compute numerical derivatives for any element of the gradient vector that contains a missing value.

Parameter Vector (PV) Structure
+++++++++++++++++++++++++++++++
If the parameters of your model can be easily represented by a Px1 parameter vector, you can use a standard **GAUSS** vector to hold your parameters.

In many cases, however, the model parameters represent a combination of one or more scalars, vectors and matrices. For these cases, :func:`maxlikmt` allows you to use the PV structure, to pass parameters to the log-likelihood function. The PV structure provides methods to easily store your model parameters as vectors, matrices or n-dimensional arrays.

::

    // Add symmetric matrix of starting
    // values to 'PV' structure
    omega_strt = {  1.0 0.8 -0.4,
                    0.8 1.0  0.6,
                   -0.4 0.6  1.0 };
    p = pvPackS(pvCreate(), omega_strt, "omega");

    proc (1) = myobjective(struct PV parms, ind);
    local omega;

    // Retrieve updated symmetric matrix
    // inside of objective function
    omega = pvUnpack(parms, "omega");

    // Perform calculations and return

No more do you have to struggle to get the parameter vector into matrices for calculating the function and its derivatives, trying to remember or figure out which parameter is where in the vector. If your log-likelihood uses matrices or arrays, you can store them directly into the PV structure and remove them as matrices or arrays with the parameters already plugged into them. The PV structure can even efficiently handle symmetric matrices where parameters below the diagonal are repeated above the diagonal.

The functions :func:`pvPackM` and :func:`pvPackMI` allow you to specify some elements inside your PV structure as fixed values and others as free parameters. It remembers the fixed values and only updates the values of the free parameters.

Optional Dynamic Arguments
+++++++++++++++++++++++++++

Any inputs that your procedure needs other than the parameters of the model can be passed into **MLMT** as `optional dynamic arguments <https://www.aptech.com/blog/the-basics-of-optional-arguments-in-gauss-procedures/>`_. These optional arguments will be passed directly and untouched to your objective function.

::

    // Inputs to log-likelihood function for
    // MLMT version 2.0 and lower
    proc (1) = myLogLikelihood(struct PV parms, struct DS d, ind);

    // Inputs to objective function for
    // MLMT current version that requires no
    // data other than model parameters.
    // And the parameters are simply a vector.
    proc (1) = myobjective(x, ind);

    // Inputs to objective function for
    // MLMT current version that requires no
    // data other than model parameters.
    // And the parameters are packed in a PV struct.
    proc (1) = myobjective(struct PV parms, ind

    // Inputs to objective function for
    // MLMT current version that requires
    // 2 extra matrices 'theta' and 'gamma'
    // Place extra inputs between the parameter vector and 'ind'
    proc (1) = myobjective(x, theta, gamma, ind);

    // Inputs to objective function for
    // MLMT current version that requires
    // 2 extra matrices 'theta' and 'gamma'
    // and using the PV structure for parameters
    // Place extra inputs between 'PV' struct and 'ind'
    proc (1) = myobjective(struct PV parms, theta, gamma, ind);

Previous versions of **MLMT** required the use of the DS structure for this purpose. The current version is backwards compatible with version 2.0 and lower, so programs written using the DS structure will continue to work.

Control Structures
+++++++++++++++++++++++++++

The functions in this library use control structures to set optimization options, rather than global control variables. This means in addition to thread safety that it will be straightforward to nest calls to :func:`maxlikmt` inside of a call to :func:`maxlikmt` or other multi-threaded **GAUSS** functions.

::

    // Declare 'c0' to be a maxlikmtControl struct
    struct maxlikmtControl c0;

    // Fill 'c0' with default settings
    c0 = maxlikmtControlCreate(); 

    // Turn on threading of numerical derivatives in MLMT
    c0.useThreads = 1;

An important advantage of threading occurs in computing numerical derivatives. If the derivatives are computed numerically, threading will significantly decrease the time of computation.

Threading
-------------

If you have a multi-core processor in your computer, you may take advantage of this capability by selecting threading. This is done by setting the *useThreads* member of the :class:`maxlikmtControl` instance.

::

  // Declare 'c0' to be a cmlmtControl struct
  struct maxlikmtControl c0;

  // Fill 'c0' with default settings
  c0 = maxlikmtControlCreate();

  // Turn on threading of numerical derivatives in MLMT
  c0.useThreads = 1;

The *useThreads member* enables threading of

* Numerical derivative calculations.
* Resampling in the :func:`maxlikmtBoot` and :func:`maxlikmtBayes` procedures.

Note that the *useThreads* structure member controls the high-level threading of sections of the
**MLMT** source code, but does not control the low-level threads that are internal to the **GAUSS**
intrinsic functions.

Hypothesis Testing for Models
------------------------------------------
Ordinary statistical inference is not correct for models with bounded parameters. This includes bootstrapping and profile likelihoods. The :func:`conscore` function in the **GAUSS Run-Time Library** can be used that computes a test statistic and its probability for the hypotheses :math:`H_0 : \Psi = 0` against :math:`H_1: G(\Psi) \geq 0, \Psi \neq 0` where :math:`G(\Psi)` is a general function of the parameters and is a subset of the parameters. 

A special procedure is included in **MLMT** that computes a test statistic and its probability for the hypotheses :math:`H_0 : \Psi` against :math:`H_1 : G(\Psi) \geq 0, \Psi \neq 0` where :math:`G(\Psi)` is a general function of the parameters and :math:`\Psi` is a subset of the parameters.

