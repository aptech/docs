
loess
==============================================

Purpose
----------------

Computes coefficients of locally weighted regression.

Format
----------------
.. function:: loess(depvar, indvars)

    :param depvar: dependent variable.
    :type depvar: Nx1 vector

    :param indvars: independent variables.
    :type indvars: NxK matrix

    :returns: yhat (*Nx1 vector*), predicted depvar given  indvars.

    :returns: ys (*_loess_numEvalx1 vector*), ordinate values
        given abscissae values in  xs.

    :returns: xs (*_loess_numEvalx1 vector*), equally spaced
        abscissae values.



Global Input
------------

+-----------------+-----------------------------------------------------+
| \_loess_Span    | scalar, degree of smoothing. Must be greater than   |
|                 | 2/N. Default = .67777.                              |
+-----------------+-----------------------------------------------------+
| \_loess_NumEval | scalar, number of points in ys and xs. Default =    |
|                 | 50.                                                 |
+-----------------+-----------------------------------------------------+
| \_loess_Degree  | scalar, if 2, quadratic fit, otherwise linear.      |
|                 | Default = 1.                                        |
+-----------------+-----------------------------------------------------+
| \_loess_WgtType | scalar, type of weights. If 1, robust, symmetric    |
|                 | weights, otherwise Gaussian. Default = 1.           |
+-----------------+-----------------------------------------------------+
| \__output       | scalar, if 1, iteration information and results are |
|                 | printed, otherwise nothing is printed.              |
+-----------------+-----------------------------------------------------+


Remarks
-------

Based on Cleveland, William S. "Robust Locally Weighted Regression and
Smoothing Scatterplots." JASA, Vol. 74, 1979, 829-836.



Source
------

loess.src

