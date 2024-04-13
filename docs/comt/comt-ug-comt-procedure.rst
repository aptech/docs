The COMT Procedure
===================

First Input Argument: Pointer to Procedure
----------------------------------------------

The first input argument is the pointer to the procedure computing the log-likelihood function and, optionally, the gradient and/or Hessian. You can create a pointer to a procedure by prepending the name of the procedure with an ampersand (&). For example, if your log-likelihood procedure is named `lpr`, then your call to :func:`comt` would look like this (at least with respect to the first input):

::

    // The & makes the first input a pointer to a procedure
    out = comt(&lpr, p);

See Section 8 for details.

Second Input Argument: Model Parameters
-------------------------------------------

**COMT** allows you to pass the model parameters as either a Px1 matrix where P is the number of parameters in the model, or inside a PV structure containing the model parameters.

PV Parameter Instance
+++++++++++++++++++++++

The **GAUSS Run-Time Library** contains special functions that work with the PV structure. They are prefixed by "pv" and defined in pv.src. These functions store matrices and arrays with parameters in the structure and retrieve the original matrices and arrays along with various kinds of information about the parameters and parameter vector from it.

The advantage of the PV structure is that it permits you to retrieve the parameters in the form of matrices and/or arrays ready for use in calculating your log-likelihood. The matrices and arrays are defined in your command file when the start values are set up. It isn’t necessary that a matrix or array be completely free parameters to be estimated. There are pvPack functions that take mask arguments defining what is a parameter versus what is a fixed value. There are also functions for handling symmetric matrices where the parameters below the diagonal are duplicated above the diagonal.

For example, a PV structure is created in your command file:

::

    // Declare 'p' to be a PV struct
    struct PV p;

    // Set PV defaults (required)
    p = pvCreate();
    
    // Create 3x1 vector
    garch = { .1, .1, .1 };

    // Add 3x1 vector, 'garch' to 'p' with name "garch"
    p = pvPack(p, garch, "garch");

Fixed Parameters
+++++++++++++++++++++++

A matrix or array in the model may contain a mixture of fixed values along with parameters to be estimated. In most cases, it is simplest to assign some parameters as fixed by using the *active* member of the :class:`comtControl` structure.

You can also specify some parameters to be fixed to their start value by 'packing' them in the PV struct with :func:`pvPackM`, which has an additional argument called a "mask," strictly conformable to the input matrix or array, indicating which elements are fixed (the corresponding element in the mask is zero) or being estimated (the corresponding element in the mask is nonzero). For example:

::

    // Declare 'p' to be a 'PV' structure
    struct PV p;

    // Initialize PV struct
    p = pvCreate();

    // Create parameter matrix
    b = { 1.0, 0.0, 0.0;
          0.5, 1.0, 0.2;
          0.3, 0.0, 1.0 };

    // Create mask with 1 for each
    // free parameter to be estimated
    // or a 0 for fixed parameters
    b_mask = { 0, 0, 0;
               1, 0, 1;
               1, 0, 1 };

    p = pvPackM(p, b, "beta", b_mask);

In this case, there are four free parameters to be estimated, :math:`b_{21}`, :math:`b_{23}`, :math:`b_{31}`, and :math:`b_{33}`.  The parameters :math:`b_{11}` and :math:`b_{22}` are fixed to 1.0 and :math:`b_{12}`, :math:`b_{13}`, and :math:`b_{32}` are fixed to 0.0.

Optional Input Argument: Instance of a :class:`comtControl`' Structure
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The :class:`comtControl` structure is an optional input. If used, it must be the final argument passed into :func:`comt`. The members of the :class:`comtControl`structure instance set the options for the optimization. For example, suppose you want **COMT** to stop after 100 iterations:

::

    // Declare 'c0' to be a comtControl structure
    struct comtControl c0;

    // Fill 'c0' with default values
    c0 = comtControlCreate();

    // Set the 'maxIters' member to 100
    c0.maxIters = 100;

The :func:`comtControlCreate` procedure sets all of the defaults. The default values for all the members of a :class:`comtControl` instance can be found in that procedure located at the top of `comtutil.src` in the GAUSS `src` subdirectory.

7.3 Optional Extra Input Arguments
----------------------------------

Any data that your objective procedure needs other than the model parameters can be passed in as `optional dynamic arguments <https://www.aptech.com/blog/the-basics-of-optional-arguments-in-gauss-procedures/>`_ to :func:`comt`. These optional input arguments can be any **GAUSS** type such as matrices
