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

   :param trend: Optional keyword, deterministic terms in the test regressions: ``"c"`` (constant) or ``"ct"`` (constant and linear trend). Default = ``"c"``.
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

The output is:

::

    Stationarity tests: Flow (constant, 100 observations)
    ================================================================================
    Test                   Statistic  p-value  5% critical   At 5%
    --------------------------------------------------------------
    ADF (H0: unit root)       -3.846    0.002       -2.896  reject
    KPSS (H0: stationary)      0.795   < 0.01        0.463  reject

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

The ADF lag length is chosen by AIC, as in :func:`adfTest`. KPSS p-values are
interpolated from its critical-value table; values outside the table are
shown as "< 0.01" or "> 0.10".

The function prints only. Use :func:`adfTest`, :func:`kpssTest` and
:func:`ppTest` for the individual results.

Library
-------
timeseries

Source
------
tests.src

.. seealso:: Functions :func:`tsDisplay`, :func:`adfTest`, :func:`kpssTest`, :func:`ppTest`
