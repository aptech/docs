
varmares
==============================================

Purpose
----------------
Computes residuals of a Vector ARMA model.

Format
----------------
.. function:: varmares(w,  phi,  theta)

    :param w: time series.
    :type w: NxK matrix

    :param phi: (K*P)xK matrix, AR coefficient matrices.
    :type phi: TODO

    :param theta: (K*Q)xK matrix, MA coefficient matrices.
    :type theta: TODO

    :returns: res (*NxK matrix*), residuals. If the calculation
        fails  res is set to missing value with error code:

    .. csv-table::
        :widths: auto

        "Error Code", "Reason for Failure"
        "1", "M < 1"
        "2", "N < 1"
        "3", "P < 0"
        "4", "Q < 0"
        "5", "P = 0 and Q = 0"
        "7", "floating point work space too small"
        "8", "integer work space too small"
        "10", "AR parameters too close to stationarity boundary"
        "11", "model not stationary"
        "12", "model not invertible"
        "13", "I+M'H'HM not positive definite"

