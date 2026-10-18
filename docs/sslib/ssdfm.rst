ssDFM
==============================================

Purpose
----------------

Estimates a dynamic factor model by EM for nowcasting and forecasting a panel of monthly series, optionally with quarterly flow series. Missing data in any pattern is allowed, including ragged edges.

.. note::
   **New in sslib 2.1.0; GAUSS 26.1.4+.** The optional arguments are keyword arguments and may be supplied by name, in any order. The result needs no preceding ``struct ssDFMOut`` declaration.

Format
----------------
.. function:: dOut = ssDFM(y [, factors, factor_order, n_quarterly, maxiter, tol, start, normalize, quiet])

    :param y: nobs x k data in original units, one row per month, missing values allowed. The last *n_quarterly* columns are quarterly series on the monthly grid: each quarterly value goes in its quarter's third month and every other month is missing. All quarterly values must fall in the same month of the quarter.
    :type y: Matrix

    :param factors: Optional keyword, the number of factors. At most the number of monthly series. Default 1.
    :type factors: Scalar

    :param factor_order: Optional keyword, the order of the factors' vector autoregression. Default 1.
    :type factor_order: Scalar

    :param n_quarterly: Optional keyword, the number of quarterly series (the last columns of *y*). At least one series must be monthly. Default 0.
    :type n_quarterly: Scalar

    :param maxiter: Optional keyword, the maximum number of EM iterations. Default 500.
    :type maxiter: Scalar

    :param tol: Optional keyword, the relative log-likelihood tolerance: EM stops when :math:`2|l_i - l_{i-1}| / (|l_i| + |l_{i-1}|) \le` *tol*. Default 1e-6.
    :type tol: Scalar

    :param start: Optional keyword, an :class:`ssDFMOut` from an earlier fit with the same *factors*, *factor_order*, number of series and *n_quarterly*, whose parameters start EM -- for example, when refitting after new data arrive. Default: a principal-components start.
    :type start: Struct

    :param normalize: Optional keyword, 1 to report the factors under the normalization described in the Remarks, 0 for EM's own rotation. Default 1.
    :type normalize: Scalar

    :param quiet: Optional keyword, 1 to suppress the printed summary. Default 0.
    :type quiet: Scalar

    :return dOut: An instance of an :class:`ssDFMOut` structure. Its main members:

        .. csv-table::
            :widths: auto

            "dOut.fitted", "nobs x k, each series' smoothed value in original units: the data where observed, the backcast or nowcast elsewhere. A quarterly column holds the three-month 1-2-3-2-1 aggregate in every month; the quarterly figure is its value at a quarter end."
            "dOut.fitted_se", "nobs x k, standard errors of *fitted* (0 where observed)."
            "dOut.common", "nobs x k, the factor-driven part of each series, original units."
            "dOut.common_se", "nobs x k, standard errors of *common*."
            "dOut.factors", "nobs x factors, the smoothed factors."
            "dOut.factors_se", "nobs x factors, their standard errors."
            "dOut.is_quarter_end", "nobs x 1, 1 in quarter-end months (all 0 without quarterly series)."
            "dOut.loadings", "k x factors loadings, standardized scale."
            "dOut.factor_ar", "factors x (factors*factor_order), the VAR coefficients [A_1 ... A_p]."
            "dOut.factor_cov", "factors x factors innovation covariance (the identity when normalized)."
            "dOut.idio_ar", "k x 1 idiosyncratic AR(1) coefficients."
            "dOut.idio_var", "k x 1 idiosyncratic innovation variances."
            "dOut.series_mean", "1 x k means used to standardize."
            "dOut.series_sd", "1 x k standard deviations used to standardize."
            "dOut.rotation", "The matrix *M* with reported factors = *M* times EM's factors."
            "dOut.loglikelihood", "Log-likelihood of the standardized data."
            "dOut.iterations", "Number of EM iterations."
            "dOut.status", "1 converged, 0 *maxiter* reached, 2 stopped on a log-likelihood decrease, 3 stopped on a non-stationary update."
            "dOut.aic", "Akaike information criterion."
            "dOut.bic", "Bayesian information criterion."

    :rtype dOut: Struct

Model
----------------

.. math::

    y_t &= \Lambda f_t + e_t\\
    f_t &= A_1 f_{t-1} + \cdots + A_p f_{t-p} + u_t, \quad u_t \sim N(0, Q_f)\\
    e_{i,t} &= \phi_i e_{i,t-1} + v_{i,t}, \quad v_{i,t} \sim N(0, \sigma^2_i)

on data standardized series by series, with no measurement error. A quarterly flow series is the sum :math:`y^q_t = \sum_{j=0}^{4} w_j x_{t-j}`, :math:`w = (1, 2, 3, 2, 1)`, of a latent monthly series *x* of the form above (Mariano and Murasawa, 2003). This is the model of Banbura and Modugno (2014), and statsmodels' ``DynamicFactorMQ(factors=1, factor_multiplicities=r, idiosyncratic_ar1=True)``.

Examples
----------------

::

  new;
  library sslib, cmlmt, tsmt;

  // Simulate 120 months of one common factor
  rndseed 8675309;
  nobs = 120;
  f = zeros(nobs, 1);
  u = rndn(nobs, 1);
  for t(2, nobs, 1);
      f[t] = 0.8*f[t-1] + u[t];
  endfor;

  // Four monthly indicators and one latent monthly series
  x = f .* (1 ~ 0.7 ~ -0.5 ~ 0.9 ~ 0.6) + 0.6*rndn(nobs, 5);

  // The fifth series is quarterly: the 1-2-3-2-1 sum of its monthly
  // values, recorded in each quarter's third month only
  y = x[., 1:4] ~ miss(zeros(nobs, 1), 0);
  for t(6, nobs, 3);
      y[t, 5] = sumc((1 | 2 | 3 | 2 | 1) .* x[t-4:t, 5]);
  endfor;

  // Ragged edge: the last two months of series 2 and 4 are not yet out,
  // nor is the last quarter
  y[nobs-1:nobs, 2 4] = miss(zeros(2, 2), 0);
  y[nobs, 5] = miss(0, 0);

  // Estimate a one-factor model with an AR(2) factor
  dOut = ssDFM(y, factors=1, factor_order=2, n_quarterly=1);

  // Nowcast of the last quarter and its standard error
  print "Nowcast of the last quarter:";
  print dOut.fitted[nobs, 5]~dOut.fitted_se[nobs, 5];

  // Forecasts of the next two quarters
  fOut = ssDFMPredict(dOut, horizon=6);
  print "Quarterly forecasts:";
  print selif(fOut.period~fOut.forecast[., 5]~fOut.forecast_se[., 5], fOut.is_quarter_end);

The printed summary and output are:

::

  Dynamic factor model, estimated by EM
  ==========================================================================
  Months: 120   Series: 5 (4 monthly, 1 quarterly)
  Factors: 1   Factor VAR order: 2   States: 14
  Log-likelihood (standardized data): -434.1839
  AIC: 904.3677   BIC: 954.5426   Parameters: 18
  EM iterations: 96, converged (relative tol 1e-06)
  Factors normalized: factor_cov = I, orthogonal loadings columns.
  --------------------------------------------------------------------------
  Loadings (standardized scale), then idiosyncratic AR(1) and variance
  Series 1            0.6175   -0.0013    0.0986
  Series 2            0.5616    0.0460    0.2507
  Series 3           -0.5069    0.1021    0.3883
  Series 4            0.5987   -0.0419    0.1290
  Series 5 (Q)        0.0810   -0.7976    0.0136
  ==========================================================================
  Nowcast of the last quarter:
         7.8457346        2.7276617
  Quarterly forecasts:

         123.00000        8.5734938        4.9033692
         126.00000        5.0400099        7.3266779

Remarks
-------

Estimation is EM with an ECM step for the loadings. With no measurement error, the textbook Banbura-Modugno M-step leaves the loadings at their starting values, because :math:`y = \Lambda f + e` holds exactly under the smoothed distribution; the loadings are instead estimated from the complete data :math:`(f, y)`. Every E-step starts from the stationary distribution at the current parameters. The EM fixed point lies slightly below the exact maximum likelihood, because every M-step conditions on the first month's state.

The log-likelihood, AIC and BIC are those of the standardized data. The parameter count includes every free parameter, without deducting the rotation.

The factors are identified only up to an invertible rotation; fitted values, nowcasts and forecasts do not depend on it. With *normalize* = 1 the reported factors have unit-covariance innovations, the columns of the loadings are orthogonal and in decreasing order of size, and each column of the loadings sums to a positive number.

With quarterly series EM converges slowly. On 300 months with 45 monthly and 5 quarterly series it stopped after about 100 iterations at the default *tol*, while the exact fixed point took about 600; the fitted values moved by less than 0.02 standard deviations between the two. The slow direction is the quarterly series' idiosyncratic AR(1) coefficients, which the data barely identify. Check *dOut.status*, and lower *tol* if the parameter estimates themselves matter.

Standard errors condition on the estimated parameters.

References
----------

Banbura, M. and Modugno, M. (2014). Maximum likelihood estimation of factor models on datasets with arbitrary pattern of missing data. *Journal of Applied Econometrics*, 29(1), 133-160.

Mariano, R. S. and Murasawa, Y. (2003). A new coincident index of business cycles based on monthly and quarterly series. *Journal of Applied Econometrics*, 18(4), 427-443.

Source
------

ssdfm.src

.. seealso:: Functions :func:`ssDFMPredict`
