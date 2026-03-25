plotStl
=======

Purpose
-------
Plot STL decomposition in four panels: original data, trend, seasonal pattern,
and remainder.

Format
------

.. function:: plotStl(y, stl)

   :param y: Original time series.
   :type y: Nx1 matrix

   :param stl: STL decomposition result from :func:`stlDecompose`.
   :type stl: struct stlResult

Examples
--------

Airline Passengers Decomposition
+++++++++++++++++++++++++++++++++

::

    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/airline_passengers.csv");
    y = loadd(fname, "passengers");

    stl = stlDecompose(y, 12);

    // 4 stacked panels
    plotStl(y, stl);

Save to File
++++++++++++

::

    plotStl(y, stl);
    plotSave("stl_decomposition.png", "px", 800 | 800);

Remarks
-------

**Four panels:**

1. **Data** — the original series (black line)
2. **Trend** — long-run level extracted by LOESS (blue line)
3. **Seasonal** — repeating periodic pattern with zero line (green line)
4. **Remainder** — what's left after removing trend and seasonal (red line, with zero line)

The decomposition is additive: Data = Trend + Seasonal + Remainder.

**Reading the plot:**

- If the **trend** is smooth and captures the long-run movement, the seasonal
  period is correctly specified.
- If the **seasonal** pattern changes amplitude over time, consider a
  multiplicative decomposition (take logs first).
- If the **remainder** shows patterns or autocorrelation, the decomposition
  didn't capture all the structure — the ARIMA model on the remainder should
  handle it.

.. seealso:: Functions :func:`stlDecompose`, :func:`arimaFit`
