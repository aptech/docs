
loess
==============================================

Purpose
----------------

Computes coefficients of locally weighted regression.

Format
----------------
.. function:: loess(depvar,  indvars)

    :param depvar: dependent variable.
    :type depvar: Nx1 vector

    :param indvars: independent variables.
    :type indvars: NxK matrix

    :returns: yhat (*Nx1 vector*), predicted depvar given  indvars.

    :returns: ys (*_loess_numEvalx1 vector*), ordinate values
        given abscissae values in  xs.

    :returns: xs (*_loess_numEvalx1 vector*), equally spaced
        abscissae values.

