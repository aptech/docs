
varmall
==============================================

Purpose
----------------
Computes log-likelihood of a Vector ARMA model.

Format
----------------
.. function:: varmall(w, phi, theta, vc)

    :param w: time series.
    :type w: NxK matrix

    :param phi: AR coefficient matrices.
    :type phi: (K*P)xK matrix

    :param theta: MA coefficient matrices.
    :type theta: (K*Q)xK matrix

    :param vc: covariance matrix.
    :type vc: KxK matrix

    :returns: ll (*scalar*), log-likelihood. If the calculation fails *ll* is set to missing value with error code:

        ============= ==============================
        Error Code    Reason for Failure
        ============= ==============================
        1             :math:`M < 1`
        2             :math:`N < 1`
        3             :math:`P < 0`
        4             :math:`Q < 0`
        5             :math:`P = 0` and :math:`Q = 0`
        7             floating point work space too small
        8             integer work space too small
        9             vc is not positive definite
        10            AR parameters too close to stationarity boundary
        11            model not stationary
        12            model not invertible
        13            :math:`I+M'H'HM` not positive definite
        ============= ==============================

Remarks
-------

:func:`varmall` is adapted from code developed by Jose Alberto Mauricio of the
Universidad Complutense de Madrid. It was published as Algorithm AS311
in Applied Statistics. Also described in "Exact Maximum Likelihood
Estimation of Stationary Vector ARMA Models," JASA, 90:282-264.

