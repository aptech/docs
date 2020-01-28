
loessmt
==============================================

Purpose
----------------

Computes coefficients of locally weighted regression.

Format
----------------
.. function:: { yhat, ys, xs } = loessmt(lc0, depvar, indvars)

    :param lc0: An instance of a :class:`loessmtControl` structure containing the following members:

        .. csv-table::
            :widths: auto

            "*lc0.Span*", "scalar, degree of smoothing. Must be greater than 2/N. Default = .67777."
            "*lc0.NumEval*", "scalar, number of points in *ys* and *xs*. Default = 50."
            "*lc0.Degree*", "scalar, if 2, quadratic fit, otherwise linear. Default = 1."
            "*lc0.WgtType*", "scalar, type of weights. If 1, robust, symmetric weights, otherwise Gaussian. Default = 1."
            "*lc0.output*", "scalar, if 1, iteration information and results are printed, otherwise nothing is printed."

    :type lc0: struct

    :param depvar: dependent variable.
    :type depvar: Nx1 vector

    :param indvars: independent variables.
    :type indvars: NxK matrix

    :return yhat: predicted *depvar* given *indvars*.

    :rtype yhat: Nx1 vector

    :return ys: ordinate values given abscissae values in *xs*.

    :rtype ys: lc0.numEval x 1 vector

    :return xs: equally spaced abscissae values.

    :rtype xs: lc0.numEval x 1 vector

Examples
-----------

::

      // Load dataset
      data = loadd("lowess1.dta", "h1 + depth");

      // Control structure
      struct loessmtControl lc0;
      lc0 = loessmtControlCreate;

      // Define independent variable
      depvar = data[., 1];

      // Defined dependent variable
      indvars = data[., 2];

      { yhat, ys, xs } = loessmt(lc0, depvar, indvars);

Remarks
-------

Based on Cleveland, William S. ''Robust Locally Weighted Regression and
Smoothing Scatterplots.'' JASA, Vol. 74, 1979, 829-836.

Source
------

loessmt.src

.. seealso:: Functions :func:`loessmtControlCreate`