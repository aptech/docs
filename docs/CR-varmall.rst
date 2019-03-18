
varmall
==============================================

Purpose
----------------
Computes log-likelihood of a Vector ARMA model.

Format
----------------
.. function:: varmall(w,  phi,  theta,  vc)

    :param w: time series.
    :type w: NxK matrix

    :param phi: (K*P)xK matrix, AR coefficient matrices.
    :type phi: TODO

    :param theta: (K*Q)xK matrix, MA coefficient matrices.
    :type theta: TODO

    :param vc: covariance matrix.
    :type vc: KxK matrix

    :returns: ll (*scalar*), log-likelihood. If the calculation fails
        ll is set to missing value with error code:

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
        "9", "vc is not positive definite"
        "10", "AR parameters too close to stationarity boundary"
        "11", "model not stationary"
        "12", "model not invertible"
        "13", "I+M'H'HM not positive definite"

