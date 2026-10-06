stationarityTests
=================

Purpose
-------
Run the ADF and KPSS tests (and optionally the Phillips-Perron test) together and print one table with a plain-language reading of the result.

Format
------

.. function:: stationarityTests(y)
              stationarityTests(y, trend="ct", pp=1)

   :param y: the series. A dataframe with one numeric column and an optional date column is also accepted; the column name labels the output.
   :type y: Nx1 vector or dataframe

   :param trend: Optional keyword, deterministic terms in the test regressions: ``"c"`` (constant) or ``"ct"`` (constant and linear trend). Accepted in any letter case; other values give an error. Default = ``"c"``.
   :type trend: string

   :param pp: Optional keyword, 1 to add the Phillips-Perron test. Default = 0.
   :type pp: scalar

Examples
--------

::

    new;
    library timeseries;

    nile = loadd(getGAUSSHome("pkgs/timeseries/examples/data/nile.csv"));
    stationarityTests(nile);

The output:

::

    Stationarity tests: Flow (constant, 100 observations)
    ================================================================================
    Test                   Statistic  p-value  5% critical   At 5%
    --------------------------------------------------------------
    ADF (H0: unit root)       -4.049    0.001       -2.892  reject
    KPSS (H0: stationary)      0.869   < 0.01        0.463  reject

    The tests disagree: ADF rejects a unit root but KPSS rejects stationarity.
    This often signals a structural break or level shift; differencing (d=1) is
    the cautious choice.

Remarks
-------

The two tests have opposite null hypotheses:

- ADF (and PP): H0 is a unit root. Rejecting suggests the series is stationary.
- KPSS: H0 is stationarity. Rejecting suggests a unit root.

Decisions are at the 5% level, and the reading below the table covers the
four outcomes:

- **ADF rejects, KPSS does not:** both indicate the series is stationary; no differencing is needed.
- **KPSS rejects, ADF does not:** both indicate a unit root; difference the series (d=1).
- **Both reject:** the tests disagree. This often signals a structural break or level shift; differencing is the cautious choice.
- **Neither rejects:** the data cannot tell the two apart; compare models with and without differencing.

The ADF lag length is chosen by AIC, as in :func:`adfTest`. For *n* input
levels, the search runs from zero through
:math:`\min(\lceil12(n/100)^{1/4}\rceil,\lfloor n/2\rfloor-d-1)`, with
*d* = 1 for ``"c"`` and 2 for ``"ct"``. Candidates use the same
*n* - *max_lags* - 1 observations; the selected regression is refit on
*n* - *lags* - 1 observations. ADF p-values are asymptotic MacKinnon (1994)
approximations; critical values use MacKinnon (2010) at that final sample size.

KPSS uses the Newey-West (1994) data-driven bandwidth with Bartlett weights
and all *n* observations, as in :func:`kpssTest` with ``lags="auto"``.
Its pilot lag is :math:`q=\lfloor n^{2/9}\rfloor`; using detrended residual
autocovariances :math:`\gamma_j` divided by *n*, set
:math:`s_0=\gamma_0+2\sum_{j=1}^q\gamma_j` and
:math:`s_1=2\sum_{j=1}^q j\gamma_j`. The bandwidth is
:math:`\min(n-1,\lfloor1.1447((s_1/s_0)^2)^{1/3}n^{1/3}\rfloor)`.
This differs from the short rule used by the KPSS check inside
:func:`autoArima`. KPSS critical values are asymptotic values from
Kwiatkowski et al. (1992), Table 1; p-values are interpolated from that table,
with values outside it shown as "< 0.01" or "> 0.10".

When included, PP uses *m* = *n* - 1 regression observations and bandwidth
:math:`\max(1,\lfloor4(m/100)^{2/9}\rfloor)`, as in :func:`ppTest` with
``lags="auto"``. The table reports its Z(t) statistic and asymptotic p-value.

Trend values are accepted in any letter case. Invalid trends, missing or
nonfinite data, constant series, or degenerate test regressions give an
error; missing rows are not silently removed.

The function prints only. Use :func:`adfTest`, :func:`kpssTest` and
:func:`ppTest` for the individual results.

Library
-------
timeseries

Source
------
tests.src

.. seealso:: Functions :func:`tsDisplay`, :func:`adfTest`, :func:`kpssTest`, :func:`ppTest`
