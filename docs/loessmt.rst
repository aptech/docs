
loessmt
==============================================

Purpose
----------------

Computes coefficients of locally weighted regression.

Format
----------------
.. function:: { yhat, ys, xs } = loessmt(depvar, indvars [, l_ctl])


    :param depvar: dependent variable.
    :type depvar: Nx1 vector

    :param indvars: independent variables.
    :type indvars: NxK matrix

    :param l_ctl: Optional input, an instance of a :class:`loessmtControl` structure containing the following members:

        .. csv-table::
            :widths: auto

            "*l_ctl.Span*", "scalar, degree of smoothing. Must be greater than 2/N. Default = .67777."
            "*l_ctl.NumEval*", "scalar, number of points in *ys* and *xs*. Default = 50."
            "*l_ctl.Degree*", "scalar, if 2, quadratic fit, otherwise linear. Default = 1."
            "*l_ctl.WgtType*", "scalar, type of weights. If 1, robust, symmetric weights, otherwise Gaussian. Default = 1."
            "*l_ctl.output*", "scalar, if 1, iteration information and results are printed, otherwise nothing is printed."

    :type l_ctl: struct

    :return yhat: predicted *depvar* given *indvars*.

    :rtype yhat: Nx1 vector

    :return ys: ordinate values given abscissae values in *xs*.

    :rtype ys: l_ctl.numEval x 1 vector

    :return xs: equally spaced abscissae values.

    :rtype xs: l_ctl.numEval x 1 vector

Examples
-----------

Example 1: Basic usage
+++++++++++++++++++++++++

::

      // Load dataset
      fname = getGAUSSHome("examples/lowess1.dta");
      data = loadd(fname, "h1 + depth");

      // Define dependent variable
      depvar = data[., 1];

      // Define independent variable
      indvars = data[., 2];

      { yhat, ys, xs } = loessmt(depvar, indvars);

After the above code, the first few lines of the printed results will be:

::

    Obs        X       Y  Fitted Y    Weights  Residuals
      1    0.000   6.642     6.169      0.985      0.473
      2    4.040   5.705     6.218      0.982     -0.514
      3    8.081   4.698     6.267      0.837     -1.569
      4   12.121   7.164     6.316      0.951      0.848
    

Example 2: Set options 
+++++++++++++++++++++++++

::

      // Load dataset
      fname = getGAUSSHome("examples/lowess1.dta");
      data = loadd(fname, "h1 + depth");

      // Control structure
      struct loessmtControl l_ctl;
      l_ctl = loessmtControlCreate;

      // Quadratic fit
      l_ctl.Degree = 2;

      // Do not print output to screen
      l_ctl.output = 0;


      // Define dependent variable
      depvar = data[., 1];

      // Define independent variable
      indvars = data[., 2];

      { yhat, ys, xs } = loessmt(depvar, indvars, l_ctl);

Remarks
-------

Based on Cleveland, William S. ''Robust Locally Weighted Regression and
Smoothing Scatterplots.'' JASA, Vol. 74, 1979, 829-836.

For backward compatibility, you may still call :func:`loessmt` like this:

::

    { yhat, ys, xs } = loessmt(l_ctl, depvar, indvars);

though this is not recommended for new code.

Source
------

loessmt.src

.. seealso:: Functions :func:`loessmtControlCreate`
