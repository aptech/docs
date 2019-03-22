
loessmt
==============================================

Purpose
----------------

Computes coefficients of locally weighted regression.

Format
----------------
.. function:: loessmt(lc0, depvar, indvars)

    :param lc0: containing the following members:
    :type lc0: an instance of a loessmtControl structure

    .. csv-table::
        :widths: auto

        "lc0.Span", "scalar, degree of smoothing. Must be greater than 2/N. Default = .67777."
        "lc0.NumEval", "scalar, number of points in  ys and   xs. Default = 50."
        "lc0.Degree", "scalar, if 2, quadratic fit, otherwise linear. Default = 1."
        "lc0.WgtType", "scalar, type of weights. If 1, robust, symmetric weights, otherwise Gaussian. Default = 1."
        "lc0.output", "scalar, if 1, iteration information and results are printed, otherwise nothing is printed."

    :param depvar: dependent variable.
    :type depvar: Nx1 vector

    :param indvars: independent variables.
    :type indvars: NxK matrix

    :returns: yhat (*Nx1 vector*), predicted  depvar given  indvars.

    :returns: ys (*lc0.numEval x 1 vector*) , ordinate values given abscissae values in  xs.

    :returns: xs (*lc0.numEval x 1 vector*) , equally spaced
        abscissae values.



Remarks
-------

Based on Cleveland, William S. ''Robust Locally Weighted Regression and
Smoothing Scatterplots.'' JASA, Vol. 74, 1979, 829-836.



Source
------

loessmt.src

.. seealso:: Functions :func:`loessmtControlCreate`
