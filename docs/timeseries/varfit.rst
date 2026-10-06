varFit
======

Purpose
-------
Fit a vector autoregression (VAR) by least squares.

Format
------

.. function:: fit = varFit(y)
              fit = varFit(y, p=4)
              fit = varFit(y, p=4, const=0, xreg=X)
              fit = varFit(y, ctl=ctl)

   :param y: the data, one column per variable. A dataframe's column names label the output; a single date-typed column is used as the time index and left out of the model. A matrix's variables are labeled "Y1", "Y2", ...
   :type y: TxM matrix or dataframe

   :param p: Optional keyword (or second argument), lag order. Default = 1.
   :type p: scalar

   :param const: Optional keyword, 1 to include a constant in each equation, 0 to leave it out. Default = 1.
   :type const: scalar

   :param xreg: Optional keyword, exogenous regressors, one row per observation of *y*. Default = none.
   :type xreg: TxK matrix

   :param dates: Optional keyword, POSIX dates for matrix input. Not needed when *y* is a dataframe with a date column. Default = none.
   :type dates: Tx1 vector

   :param freq: Optional keyword, frequency of the dates: ``"annual"``, ``"quarterly"``, ``"monthly"``, ``"weekly"`` or ``"daily"``. Default = inferred from the dates.
   :type freq: string

   :param quiet: Optional keyword, 1 to suppress printing. Default = 0.
   :type quiet: scalar

   :param ctl: Optional keyword, an instance of a :class:`varControl` structure holding the same settings. When *ctl* is given, the other keywords except *dates* and *freq* are ignored. An instance is created by :func:`varControlCreate` and has these members:

       .. include:: include/varcontrol.rst

   :type ctl: struct

   :return fit: An instance of a :class:`varResult` structure containing:

       .. include:: include/varresult.rst

   :rtype fit: struct

Examples
--------

Four US series
++++++++++++++

::

    new;
    library timeseries;

    // Four quarterly US series, 1960Q1-2019Q4: GDP growth and inflation
    // (annualized percent changes), unemployment and the funds rate (percent)
    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv"));
    y = selif(data, data[., "date"] .>= "1960-01-01" .and data[., "date"] .<= "2019-10-01");
    y = y[., "date" "gdp_growth" "inflation" "unemployment" "fed_funds"];

    fit = varFit(y, p=2);

The output starts:

::

    VAR(2), least squares
    ================================================================================
    Variables:                         4    Observations:                        240
    Lags:                              2    Effective obs.:                      238
    Constant:                        Yes    Log-likelihood:                 -1254.68
    AIC:                         -0.5054    BIC:                              0.0198
    HQ:                          -0.2937    Largest root:            0.9651 (stable)

    Equation 1: gdp_growth
                        Coef.  Std. err.      t  p-value
    ----------------------------------------------------
    gdp_growth(-1)     0.1568     0.0772   2.03    0.043
    inflation(-1)     -0.1431     0.1075  -1.33    0.184
    unemployment(-1)  -1.4559     0.9292  -1.57    0.119
    fed_funds(-1)     -0.0500     0.2620  -0.19    0.849
    gdp_growth(-2)     0.1526     0.0699   2.18    0.030
    inflation(-2)     -0.0882     0.1080  -0.82    0.415
    unemployment(-2)   1.6837     0.9148   1.84    0.067
    fed_funds(-2)      0.0826     0.2598   0.32    0.751
    Constant           1.3875     0.8694   1.60    0.112

and continues with the other three equations in the same layout.

Choosing the lags and using the result
++++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv"));
    y = selif(data, data[., "date"] .>= "1960-01-01" .and data[., "date"] .<= "2019-10-01");
    y = y[., "date" "gdp_growth" "inflation" "unemployment" "fed_funds"];

    // Let BIC choose the lag order, fit quietly, and use the result
    lags = varLagSelect(y, 8, ic="bic", quiet=1);
    fit = varFit(y, p=lags.best_p, quiet=1);

    print "Lags chosen by BIC: " ntos(fit.p);
    print "Largest root of the companion matrix: " sprintf("%.4f", fit.max_eigenvalue);
    print "Residual standard deviations (ML):";
    print sqrt(diag(fit.sigma_ml))';

The output is:

::

    Lags chosen by BIC: 2
    Largest root of the companion matrix: 0.9651
    Residual standard deviations (ML):
           2.8813127        1.7771012       0.21941408       0.79532065

Remarks
-------

**Model.** With :math:`y_t` the M variables at time *t*,

.. math::

   y_t = c + B_1 y_{t-1} + \cdots + B_p y_{t-p} + \Phi x_t + \varepsilon_t, \qquad \varepsilon_t \sim N(0, \Sigma),

where :math:`x_t` are the exogenous regressors (*xreg*). The first *p* observations
are the initial conditions, so T - p observations are explained. Each equation is
estimated by least squares on the same K regressors (Mp lags, the
exogenous regressors and the constant).

**Covariance.** *sigma* divides the residual cross-products by T - p - K; *sigma_ml*
divides by T - p and is the maximum-likelihood estimate. *se*, *tstat* and *pval*
use *sigma*; the log-likelihood, the information criteria, forecast intervals and
impulse responses use *sigma_ml*.

**Information criteria.** With :math:`T_e = T - p`,

.. math::

   \text{AIC} = \ln|\hat\Sigma_{ML}| + \frac{2KM}{T_e}, \quad
   \text{BIC} = \ln|\hat\Sigma_{ML}| + \frac{KM\ln T_e}{T_e}, \quad
   \text{HQ} = \ln|\hat\Sigma_{ML}| + \frac{2KM\ln\ln T_e}{T_e}.

They compare models fitted on the same observations; to choose the lag order,
use :func:`varLagSelect`, which fits every lag order on a common sample.

**Stability.** *max_eigenvalue* is the largest modulus of the companion matrix's
eigenvalues; below 1 the VAR is stable and its forecasts return to the mean.

References
----------

- Kilian, L. and H. Lutkepohl (2017). *Structural Vector Autoregressive Analysis*. Cambridge University Press, chapter 2.
- Lutkepohl, H. (2005). *New Introduction to Multiple Time Series Analysis*. Springer, chapters 3 and 4.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`varLagSelect`, :func:`varForecast`, :func:`irfCompute`, :func:`bvarFit`, :func:`forecastEval`
