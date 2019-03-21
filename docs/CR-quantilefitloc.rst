
quantileFitLoc
==============================================

Purpose
----------------
Perform local linear or quadratic quantile regression. .

Format
----------------
.. function:: quantileFitLoc(y, x, qCtl) 
			  quantileFitLoc(y, x, tau, xstar, qCtl) 
			   
			  quantileFitLoc(dataset, formula, qCtl) 
			  quantileFitLoc(dataset, formula, tau, xstar, qCtl)

    :param y: dependent variable.
    :type y: Nx1 vector

    :param x: 
    :type x: NxK matrix or sparse matrix or N-dimensional array

    :param dataset: name of dataset.
    :type dataset: string

    :param formula: formula string of the model.
        E.g "y ~ X1 + X2", 'y' is the name of dependent variable, 'X1' and 'X2' are names of independent variables;
        E.g. "y ~ .", '.' means including all variables except dependent variable 'y';
        E.g "y ~ -1 + X1 + X2", '-1' means no intercept model.
    :type formula: String

    :param tau: Mx1 vector, quantile levels. Default = { 0.05, 0.5, 0.95 };
    :type tau: Optional argument

    :param xstar: P*1 vector, quantile points. Default = seqa(0, 1/(50-1), 50).
    :type xstar: Optional argument

    :param qCtl: instance of the qfitControl structure containing the following members:
    :type qCtl: Optional argument

    .. csv-table::
        :widths: auto

        "qCtl.bandwidth", "Scalar, the multiplicative factor of the bandwidth. Default = 1."
        "qCtl.reg_type", "Scalar, the regression type. Default = 1."
        "", "1", "Linear regression."
        "", "2", "Quadratic regression."
        "qCtl.varnames", "String array, variable names. Default = {"X1", "X2", ..., "XK"}."
        "qCtl.verbose", "Scalar, print results Default = 1."
        "", "1", "Printing on."
        "", "0", "No printing."
        "qCtl.const", "Scalar, include constant in regression. Default = 1."
        "", "1", "a constant term will be added."
        "", "0", "no constant term will be added."

    :returns: q (*PxM matrix*), estimated quantile Y|X=xstar

Examples
----------------

::

    new;
    cls;
    
    // Set random number generator seed for 
    // repeatable random numbers
    rndseed 4893;
    
    N = 1000;
    X = rndu(N,1);
    Y = sin(9*X) + (rndu(N,1) - 0.5);
    
    // Call quantileFitLoc
    q = quantileFitLoc(Y, X);

Source
------

quantilefit.src

.. seealso:: Functions :func:`glm`, :func:`olsmt`, :func:`quantileFit`
