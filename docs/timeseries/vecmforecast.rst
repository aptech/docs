vecmForecast
============

Purpose
-------
Forecast the levels of the series from a fitted VECM, with forecast intervals.

Format
------

.. function:: fc = vecmForecast(vr, h)
              fc = vecmForecast(vr, h, level=0.95, quiet=0)

   :param vr: an instance of a :class:`vecmResult` structure returned by :func:`vecmFit` or :func:`vecmAuto`.
   :type vr: struct

   :param h: number of steps ahead.
   :type h: scalar

   :param level: Optional keyword, coverage of the forecast intervals, strictly between 0 and 1. Default = 0.95.
   :type level: scalar

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :return fc: An instance of a :class:`forecastResult` structure. :func:`vecmForecast` fills these members:

       .. list-table::
          :widths: auto

          * - fc.forecasts
            - hxM matrix, point forecasts of the levels. Row *s* is *s* steps ahead.

          * - fc.se
            - hxM matrix, forecast standard errors.

          * - fc.lower
            - hxM matrix, lower bounds of the forecast intervals.

          * - fc.upper
            - hxM matrix, upper bounds of the forecast intervals.

          * - fc.level
            - Scalar, coverage of the intervals.

          * - fc.h
            - Scalar, number of steps ahead.

          * - fc.m
            - Scalar, number of series.

          * - fc.var_names
            - Mx1 string array, names of the series.

          * - fc.model
            - String, ``"VECM"``.

       The other members of the structure, which other forecast procedures use, are left empty or zero.

   :rtype fc: struct

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

    struct forecastResult fc;
    fc = vecmForecast(vr, 8);

The printout:

::

    VECM forecast
    ================================================================================
    8 steps ahead, 95% prediction intervals

    h      e  Lower 95%  Upper 95%   prod  Lower 95%  Upper 95%     rw  Lower 95%  Upper 95%      U  Lower 95%  Upper 95%
    ---------------------------------------------------------------------------------------------------------------------
    1  962.3      961.6      963.1  417.2      416.0      418.5  470.1      468.6      471.6  6.639      6.088      7.190
    2  962.9      961.4      964.3  417.6      415.7      419.5  470.6      468.5      472.7  6.463      5.499      7.428
    3  963.4      961.2      965.6  418.0      415.5      420.4  471.1      468.4      473.7  6.293      4.923      7.663
    4  964.0      961.1      966.8  418.3      415.4      421.2  471.6      468.4      474.7  6.108      4.366      7.851
    5  964.6      961.1      968.1  418.7      415.4      422.0  472.1      468.5      475.7  5.921      3.854      7.988
    6  965.2      961.1      969.2  419.0      415.4      422.6  472.7      468.5      476.8  5.736      3.397      8.075
    7  965.7      961.2      970.3  419.3      415.4      423.3  473.3      468.6      477.9  5.556      2.996      8.117
    8  966.3      961.4      971.3  419.7      415.4      423.9  473.9      468.6      479.1  5.384      2.648      8.120

    Intervals include shocks only.

For 90% intervals without the printout:

::

    fc = vecmForecast(vr, 8, level=0.90, quiet=1);
    print fc.lower~fc.upper;

Remarks
-------

**Point forecasts.** The fitted model is iterated forward from the last *p*
rows of the data, with future shocks set to zero. The forecasts are those of
the same model written as a VAR in levels.

**Intervals.** With :math:`\Phi_i` the moving-average matrices of the VAR in
levels (:math:`\Phi_0 = I`) and :math:`\hat\Sigma_u` the residual covariance
``vr.sigma_u``, the forecast error covariance *s* steps ahead is

.. math::

   \hat\Sigma_y(s) = \sum_{i=0}^{s-1} \Phi_i \hat\Sigma_u \Phi_i'

(Lutkepohl 2005, section 6.5). ``fc.se`` holds the square roots of its
diagonal, and the bounds are the point forecast plus and minus the standard
normal quantile for *level* times the standard error.

The intervals reflect future shocks only. They do not include the
uncertainty of the estimated coefficients or of the cointegrating rank, so
they are somewhat too narrow in short samples. They use the maximum
likelihood covariance, which is divided by the number of rows used in
estimation and not by the residual degrees of freedom.

Because the levels are not stationary, ``fc.se`` grows without bound as the
horizon grows for every series that is itself integrated. Only the forecast
errors of the cointegrating combinations :math:`\beta' y`, which the
procedure does not report, stay bounded.

**Seasonal dummies.** Models fitted with ``season=s`` can be forecast.
The procedure continues the seasonal cycle from the last data row and uses
the same centered columns as estimation: column *j* is ``1-1/s`` in season
*j* and ``-1/s`` otherwise, for *j* = 1, ..., *s*-1. The first input row is
season 1; row *i* is season ``mod(i-1,s)+1``. For quarterly data ending in
season 3, the first forecast uses season 4, then seasons 1, 2 and 3.
These dummies are known, so their future values require no extra input.

**User regressors.** A model fitted with user regressors in ``ctl.xreg``
cannot be forecast because their future values are required. This also
applies when the fit includes both user regressors and seasonal dummies.

References
----------

- Lutkepohl, H. (2005). *New Introduction to Multiple Time Series Analysis*. Springer.

Library
-------
timeseries

Source
------
vecm.src

.. seealso:: Functions :func:`vecmFit`, :func:`vecmAuto`, :func:`vecmIrf`, :func:`varForecast`
