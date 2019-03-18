
integrate1d
==============================================

Purpose
----------------

Integrates a user-defined function, using adaptive quadrature, over a user defined interval

Format
----------------
.. function:: integrate1d(&fct,  x_min,  x_max,  ...,  ctl)

    :param &fct: pointer to the procedure containing the function to be integrated
    :type &fct: scalar

    :param x_min: starting point for the integration
    :type x_min: scalar

    :param x_max: ending point for the integration
    :type x_max: scalar

    :param ...: a variable number of extra arguments to pass to the user function. These arguments will be passed to the user function untouched.
    :type ...: Optional input

    :param ctl: an instance of an integrateControl structure with members
    :type ctl: Optional input

    .. csv-table::
        :widths: auto

        "ctl.subDivisions", "scalar, maximum number of divisions of the region (x_min, x_max)"
        "ctl.absTol", "scalar, absolute accuracy requested."
        "ctl.relTol", "scalar, relative accuracy requested."

    :returns: y (*scalar*), the estimated integral of f(x) evaluated over the interval (x_min, x_max)

Examples
----------------

Basic Example
+++++++++++++

Calculate the integral ∫031x+1ⅆx

::

    //Define procedure to be integrated
    proc (1) = fct(x);
       retp(1 ./ (x + 1));
    endp;
    
    //Calculate integral for procedure 'fct', from 0 - 3
    ans = integrate1d(&fct, 0, 3);

will result in:

::

    ans = 1.3862943611

Passing extra arguments to the user function
++++++++++++++++++++++++++++++++++++++++++++

Calculate the integral ∫−10001000e−x22×aⅆx⁢⁢, a⁢=3

::

    //Define procedure to be integrated
    proc (1) = myProc(x, var);
       retp(exp( -(x .* x) / (2 .* var) ));
    endp;
    
    //Define limits of integration
    x_min = -1000;
    x_max = 1000;
    
    //Define extra argument for procedure 'myProc'
    a = 3;
    
    ans = integrate1d(&myProc, x_min, x_max, a);

will result in:

::

    ans = 4.3416075273

Bound at negative infinity
++++++++++++++++++++++++++

Calculate the integral ∫−∞01σ2πe−(x−μ)22σ2ⅆx

::

    //Define procedure to be integrated
    proc (1) = myPdfn(x, mu, sigma);
       retp(pdfn((x - mu) ./ sigma) ./ sigma);
    endp;
    
    //Set bounds of integration to be (-Inf, 0)
    x_min = __INFN;
    x_max = 0;
    
    //Extra inputs for user function
    mu = 0.33;
    sigma = 7;
    
    ans = integrate1d(&myPdfn, x_min, x_max, mu, sigma);

will result in:

::

    ans = 0.481199685115

Using a control structure
+++++++++++++++++++++++++

Calculate the integral ∫−∞01σ2πe−(x−μ)22σ2ⅆx

::

    //Define procedure to be integrated
    proc (1) = myPdfn(x, mu, sigma);
       retp(pdfn((x - mu) ./ sigma) ./ sigma);
    endp;
    
    //Set bounds of integration to be (0, +Inf)
    x_min = 0;
    x_max = __INFP;
    
    //Extra inputs for user function
    mu = 0.33;
    sigma = 7;
    
    //Declare instance of 'integrateControl' structure
    //and fill with default values
    struct integrateControl ctl;
    ctl = integrateControlCreate();
    
    //Lower required tolerance for faster return
    ctl.absTol = 1e-2;
    
    ans = integrate1d(&myPdfn, x_min, x_max, mu, sigma, ctl);

will result in:

::

    ans = 0.518798668212

Remarks
+++++++

The user-provided function must be able to accept a vector of scalar
values and return a vector of outputs. Make sure to use the element by
element operators (``.* ./``) instead of the overloaded matrix operators
(``* /``). For example, the following procedure:

::

   proc (1) = myProc(x);
      local  ret;
      ret = x / (x * x);
      retp(ret);
   endp;

will work as expected for a scalar input. For example:

::

   a = 2;
   b = 3;
   c = myProc(a);
   d = myProc(b);

will assign c to be equal to 0.5 and d to be equal to 0.334. However, if
we pass in a vector like this:

::

   a = { 2,
         3 };
   c = myProc(a);

we will cause an the error ``matrices not conformable`` when we try to
multiply the incoming 2x1 vector times itself inside of myProc. To avoid
this, we simply need to change the operators ``*`` and ``/`` to the
element-by-element versions by prepending the operator with a dot like
this:

::

   proc (1) = myProc(x);
       local  ret;
       ret = x ./ (x .* x);
       retp(ret);
   endp;

Source
++++++

integrate.src

.. seealso:: Functions :func:`integrateControlCreate`, :func:`inthp2`, :func:`inthp3`, :func:`inthp4`

intergrate user-defined adaptive quadrature
