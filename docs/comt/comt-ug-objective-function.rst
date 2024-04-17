The Objective Procedure
=======================

**COMT **requires that you write a procedure computing the objective function. The output from this procedure is a :class:`modelResults` structure containing the value of the objective function and optionally the first and second derivatives of the objective function with
respect to the parameters. 

There are three input arguments to this procedure:

#. The model parameters either as a Px1 matrix, or an instance of a PV structure containing parameter values.
#. Optional arguments; extra data matrices or arrays (other than the model parameters)
used by the objective procedure.
#. Indicator vector.
   
There is one return argument:

#. An instance of a :class:`modelResults` structure containing computational results.
   
First Argument: The Model Parameters
-------------------------------------

This argument contains either a Px1 matrix, or a PV structure, containing the parameter matrices and arrays that you need for computing the log-likelihood and (optionally) derivatives. If the parameters are packed in a PV struct, the :func:`pvUnpack` function retrieves them from the PV structure.

Px1 Matrix case
+++++++++++++++++

Below is part of a simple example in which the parameter vector contains two values. The first element will be ``beta_`` and the second will be ``gamma_``.

::

   proc lpr(p, ind);
      local beta_, gamma_;
      beta_ = p[1];
      gamma_ = p[2];
      .
      .
      .
   endp;

PV struct case
+++++++++++++++++

Next is the same as the example above, but using a PV structure.

::

    proc lpr(struct PV p, ind);
      local beta_, gamma_;
      beta_ = pvUnpack(p, "beta");
      gamma_ = pvUnpack(p, "gamma");
      .
      .
      .
    endp;

If you are using a PV structure, you may have decided to speed the program up a bit by packing the matrices or arrays using the "i" pack functions, :func:`pvPacki`, :func:`pvPackmi`, :func:`pvPacksi`, etc., You can then unpack the matrices and arrays with the integers used in packing them:

::

    proc lpr(struct PV p, ind);
      local beta_, gamma_;
      beta_ = pvUnpacki(p, 1);
      gamma_ = pvUnpacki(p, 2);
      .
      .
      .
    endp;

where it has been assumed that they’ve been packed accordingly:

::

   struct PV p;
   p = pvCreate();
   
   //Pack vector by index
   b = { 1, 0.1 };
   p = pvPacki(p,b,"beta",1);
   
   //Pack symmetric matrix by index
   g = { 1 0,
   0 1 };
   
   p = pvPacksi(p,g,"gamma",2);


Optional Arguments
-------------------

The optional arguments are available for use in your objective function procedure. For example, for an objective function with a dependent variable vector and a matrix of independent variables, we have:

::

   // Loadd all data from 'nlin.dat'
   nldat = loadd("nlin.dat");
   
   // Set 'y' equal to the first column of 'nldat'
   // and set 'x' equal to the second column of 'nldat'
   y = nldat[., 1];
   x = nldat[., 2];
   
   proc fct(b, y, x, ind);
      struct modelResults mm;
      local dev;
   
      dev = y - b[1] - b[2] * exp(-b[3] * x);
      if ind[1];
         mm.function = dev'dev;
      endif;
   retp(mm);
   endp;

Final Input Argument: Indicator Vector
--------------------------------------

The final argument is a vector with three elements set to zero or one, indicating whether or not the function, first derivatives, or second derivatives are to be computed. This vector is created inside of :func:`comt`` and passed to your objective procedure when it is called by :func:`comt`. You do not need to create or declare the indicator vector.

.. list-table::
   :widths: auto

   * - **1st element**
     - If nonzero, the function is to be computed.
   * - **2nd element**
     - If nonzero, the first derivatives are to be computed.
   * - **3rd element**
     - If nonzero, the second derivatives are to be computed.

The second and third elements associated with the first and second derivatives are optional.

For example,

::

   proc logl(b, y, x, ind);
     struct modelResults mm;
     
     if ind[1]; // compute objective function
       mm.function = ....
     endif;
   
     if ind[2]; // compute optional first derivatives
       mm.gradient = ....
     endif;
   
     if ind[3]; // compute optional second derivatives
       mm.Hessian = ....
     endif;
   
     retp(mm);
   endp;

Output Argument: modelResults Structure
----------------------------------------
The return argument for your log-likelihood procedure is an instance of a :class:`modelResults` structure. The members of this structure are

.. list-table::
   :widths: auto

   * - mm.function
     - Scalar log-likelihood.
   * - mm.gradient
     - K×1 vector of first derivatives (optional).
   * - mm.hessian
     - K×K matrix of second derivatives (optional).