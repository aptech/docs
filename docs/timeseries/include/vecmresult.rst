.. list-table::
   :widths: auto

   * - vr.m
     - Scalar, number of series.

   * - vr.p
     - Scalar, lag order in levels.

   * - vr.r
     - Scalar, cointegrating rank.

   * - vr.det_case
     - Scalar, deterministic terms (1 to 5).

   * - vr.season
     - Scalar, number of seasons used for the seasonal dummies. 0 = none.

   * - vr.n_total
     - Scalar, rows of *y*.

   * - vr.n_obs
     - Scalar, rows used in estimation (``n_total - p``).

   * - vr.n_exo
     - Scalar, number of seasonal dummies plus your own regressors.

   * - vr.var_names
     - Mx1 string array, names of the series.

   * - vr.alpha
     - Mxr matrix, adjustment coefficients.

   * - vr.alpha_se
     - Mxr matrix, standard errors of ``alpha``, computed with ``vr.sigma_u`` without a degrees-of-freedom adjustment.

   * - vr.beta
     - kxr matrix, cointegrating vectors, normalized so that the first *r* rows are the identity matrix. k = M in cases 1, 3 and 5; k = M+1 in cases 2 and 4, where the last row is the constant or trend inside the relations.

   * - vr.beta_se
     - kxr matrix, standard errors of ``beta``, computed with ``vr.sigma_u`` without a degrees-of-freedom adjustment. Zero in the rows fixed by the normalization.

   * - vr.beta_levels
     - Mxr matrix, the first *M* rows of ``beta`` (the coefficients on the series).

   * - vr.Gamma
     - (M*(p-1))xM matrix, :math:`\Gamma_1` to :math:`\Gamma_{p-1}` stacked by rows. Empty when ``p = 1``. :func:`vecmGamma` returns one of them.

   * - vr.phi_det
     - Mxd matrix, coefficients of the unrestricted deterministic terms: the constant (cases 3 and 4), or the constant and the trend (case 5). Empty in cases 1 and 2.

   * - vr.phi_exo
     - Mx(n_exo) matrix, coefficients of your own regressors, then of the seasonal dummies. Empty if there are none.

   * - vr.sigma_u
     - MxM matrix, maximum likelihood residual covariance (divided by ``n_obs``).

   * - vr.loglik
     - Scalar, maximized log-likelihood.

   * - vr.aic
     - Scalar, Akaike information criterion.

   * - vr.bic
     - Scalar, Bayesian (Schwarz) information criterion.

   * - vr.hq
     - Scalar, Hannan-Quinn information criterion.

   * - vr.residuals
     - (n_obs)xM matrix, residuals.

   * - vr.fitted
     - (n_obs)xM matrix, fitted values of the differences :math:`\Delta y_t`.

   * - vr.johansen_eigenvalues
     - Mx1 vector, eigenvalues of the reduced-rank regression, largest first.

   * - vr.trace_stat
     - Mx1 vector, Johansen trace statistics.

   * - vr.max_eigen_stat
     - Mx1 vector, Johansen maximum-eigenvalue statistics.

   * - vr.var_coefs
     - (M*p)xM matrix, the lag matrices :math:`A_1` to :math:`A_p` of the same model written as a VAR in levels, stacked by rows.

   * - vr.companion_eig
     - (M*p)x1 vector, moduli of the eigenvalues of the companion matrix of the VAR in levels (the inverse roots of its lag polynomial), largest first. A model with rank *r* has at least *M-r* of them equal to 1.

   * - vr.y
     - TxM matrix, the data.

   * - vr.xreg
     - (n_obs)x(n_exo) matrix, your own regressors and the seasonal dummies in the rows used in estimation (data rows p+1 to T). Empty if there are none.
