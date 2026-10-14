vecmToVar
=========

Purpose
-------
Write a fitted VECM as the equivalent VAR in levels.

Format
------

.. function:: var_result = vecmToVar(vr)

   :param vr: an instance of a :class:`vecmResult` structure returned by :func:`vecmFit` or :func:`vecmAuto`.
   :type vr: struct

   :return var_result: An instance of a :class:`varResult` structure holding the same model in levels (see Remarks for what it contains).
   :rtype var_result: struct

Examples
--------

::

    new;
    library timeseries;

    // Canadian employment, productivity, real wage and unemployment, 1980Q1-2000Q4
    fname = getGAUSSHome("pkgs/timeseries/examples/data/canada.csv");
    y = loadd(fname);

    struct vecmResult vr;
    vr = vecmFit(y, 1, p=2, det_case=3, quiet=1);

    struct varResult var_result;
    var_result = vecmToVar(vr);

    // Rows: lag 1 of e, prod, rw, U; lag 2 of the same; the constant.
    // Columns: equations.
    print var_result.b;

::

       1.7788626      -0.23192895      -0.37795767      -0.62843471
      0.16712385        1.1579201     -0.071036449     -0.079677352
    -0.026870094       0.10678987       0.98783225     -0.018299590
      0.18991727      -0.60271167      -0.22139362       0.70854689
     -0.76562256       0.29857108       0.19624183       0.58459494
     -0.16513409      -0.14790495      0.043727644      0.073088979
     0.023606252      -0.12321796      0.056962902      0.029106624
     -0.14208335       0.84347705      -0.43511122       0.13306833
      -12.225480       -61.905895        170.24794        41.052610

Remarks
-------

**The conversion.** A VECM with *p-1* lagged differences is a VAR with *p*
lags in levels whose lag matrices are

.. math::

   A_1 = I + \alpha\beta' + \Gamma_1, \qquad
   A_i = \Gamma_i - \Gamma_{i-1} \;\; (1 < i < p), \qquad
   A_p = -\Gamma_{p-1},

with :math:`A_1 = I + \alpha\beta'` when *p* = 1 (Lutkepohl 2005, section
6.3). All five deterministic cases convert:

- Case 2: the constant inside the relations becomes a VAR constant equal to
  :math:`\alpha` times that constant.
- Case 4: the trend inside the relations multiplies *t-1*, while the VAR
  trend multiplies the data row number *t*. The VAR trend coefficient is
  :math:`\alpha` times the trend coefficient inside the relation, and the
  VAR constant is ``vr.phi_det`` minus that same product.
- Cases 3 and 5: the constant, and in case 5 the trend, of ``vr.phi_det``
  carry over unchanged.

The VAR trend equals the data row number, with the first row numbered 1.
Coefficients of seasonal dummies and of your own regressors carry over
unchanged.

**What the result contains.** ``var_result.b`` holds the coefficients, one
column per equation, with the rows ordered as in a :func:`varFit` result.
``var_result.sigma`` is the maximum likelihood residual covariance of the
VECM (``var_result.resid_cov`` is ``"vecm"``). The residuals, the fitted
levels, the data and the information criteria of the VECM are carried over.
No standard errors are computed for the levels coefficients: ``se``,
``tstat``, ``pval`` and ``vcov`` are empty.

``var_result.xreg`` has as many rows as the data: the first *p* rows are
missing values, because those rows are not used in the fit, followed by
``vr.xreg``. ``var_result.companion`` and ``var_result.max_eigenvalue`` are
filled. ``var_result.is_stationary`` is 0 whenever *r* is less than *M*,
because the VAR in levels then has unit roots.

**Where the result can be used.** :func:`condForecast`,
:func:`scenarioPath` and :func:`scenarioCompare` accept the result when the
VECM was fit without seasonal dummies or your own regressors: they need only
the coefficients, the residual covariance and the data, so conditional
forecasts and scenarios keep the long-run relations of the VECM. A result
from a fit with seasonal dummies or regressors is refused, because their
future values would be needed. These procedures do not accept the result:
:func:`varForecast`, :func:`irfCompute`, :func:`hdCompute`,
:func:`varDiagnostics`, :func:`forecastModel`, :func:`forecastEval`,
``forecastCompare``, :func:`grangerTest`, :func:`varResults` and
:func:`varCoefTable`. Use :func:`vecmForecast`, :func:`vecmIrf` and
:func:`vecmDiagnostics` for forecasts, impulse responses and residual checks
of a VECM.

References
----------

- Lutkepohl, H. (2005). *New Introduction to Multiple Time Series Analysis*. Springer.

Library
-------
timeseries

Source
------
vecm.src

.. seealso:: Functions :func:`vecmFit`, :func:`vecmForecast`, :func:`vecmIrf`, :func:`varFit`
