ljungBoxTest
============

Purpose
-------
Ljung-Box test of autocorrelation in one or more series.

Format
------

.. function:: lb = ljungBoxTest(x)
              lb = ljungBoxTest(x, lags=12, n_params=2)

   :param x: series to test: a vector, a matrix with one series per column, or a dataframe (date columns are skipped). Missing values are dropped series by series.
   :type x: Nx1 vector, NxK matrix or dataframe

   :param lags: Optional keyword, number of autocorrelations tested (lags 1 to *lags*). Default = 10.
   :type lags: scalar

   :param n_params: Optional keyword, number of estimated parameters to remove from the degrees of freedom, for example *p* + *q* for the residuals of an ARMA(*p*, *q*) model. Must be smaller than *lags*. Default = 0 (a raw series).
   :type n_params: scalar

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :return lb: An instance of a :class:`ljungBoxResult` structure containing:

       .. list-table::
          :widths: auto

          * - lb.names
            - Kx1 string array, series names.
          * - lb.lags
            - Scalar, lags tested.
          * - lb.n_params
            - Scalar, estimated parameters removed from the degrees of freedom.
          * - lb.df
            - Scalar, degrees of freedom, *lags* - *n_params*.
          * - lb.n_obs
            - Kx1 vector, observations used in each series.
          * - lb.stat
            - Kx1 vector, Ljung-Box *Q* of each series.
          * - lb.p_value
            - Kx1 vector, p-value of each series.

   :rtype lb: struct

Examples
--------

::

    new;
    library timeseries;

    // Annual flow of the Nile, 1871-1970
    nile = loadd(getGAUSSHome("pkgs/timeseries/examples/data/nile.csv"));

    lb = ljungBoxTest(nile);

The output:

::

    Ljung-Box test, 10 lags
    ================================================================================
    Chi-square with 10 degrees of freedom (10 lags - 0 estimated parameters).

    Series               Obs         Q   p-value
    --------------------------------------------
    Flow                 100     88.13   <0.0001

Remarks
-------

The statistic is

.. math::

   Q = n(n+2)\sum_{k=1}^{\text{lags}} \frac{r_k^2}{n-k},

where :math:`r_k` is the sample autocorrelation at lag *k* of the series
after removing its mean, compared with a chi-square on *lags* - *n_params*
degrees of freedom (Ljung and Box 1978). For the residuals of a fitted
model, set *n_params* to the number of estimated ARMA parameters.

For the residuals of a VAR use :func:`varDiagnostics`, and of a VECM
:func:`vecmDiagnostics`: in these models one equation's residual
autocorrelations do not have this chi-square reference.

References
----------

- Ljung, G.M. and G.E.P. Box (1978). "On a measure of lack of fit in time series models." *Biometrika*, 65(2), 297-303.

Library
-------
timeseries

Source
------
arima.src

.. seealso:: Functions :func:`varDiagnostics`, :func:`arimaDiagnostics`, :func:`etsDiagnostics`
