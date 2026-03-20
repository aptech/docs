stlDecompose
============

Purpose
-------
Seasonal-Trend decomposition via LOESS (STL).

Format
------

.. function:: stl = stlDecompose(y, period)
              stl = stlDecompose(y, period, s_window=7)

   :param y: time series data.
   :type y: Nx1 vector

   :param period: seasonal period (e.g., 12 for monthly, 4 for quarterly, 52 for weekly).
   :type period: scalar

   :param s_window: Optional keyword, seasonal smoothing window (must be odd, >= 7). Default = auto.
   :type s_window: scalar

   :param quiet: Optional keyword, set to 1 to suppress output. Default = 0.
   :type quiet: scalar

   :return stl: An instance of a :class:`stlResult` structure containing:

       .. list-table::
          :widths: auto

          * - stl.seasonal
            - Nx1 vector, seasonal component.

          * - stl.trend
            - Nx1 vector, trend component.

          * - stl.remainder
            - Nx1 vector, remainder (y - seasonal - trend).

   :rtype stl: struct

Examples
--------

Monthly Data
++++++++++++

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/airline.dat"), "passengers");

    stl = stlDecompose(y, 12);

    print "Seasonal component (first year):";
    print stl.seasonal[1:12];

    print "Trend (first 5):";
    print stl.trend[1:5];

Deseasonalize then Fit ARIMA
+++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/airline.dat"), "passengers");

    stl = stlDecompose(y, 12, quiet=1);

    // Fit ARIMA on seasonally adjusted series
    y_adj = y - stl.seasonal;
    result = arimaFit(y_adj);

Weekly Data
+++++++++++

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/weekly.dat"), "sales");

    stl = stlDecompose(y, 52, s_window=15);

Remarks
-------

STL decomposes a time series into three additive components:

.. math::

   y_t = S_t + T_t + R_t

where :math:`S_t` is the seasonal component, :math:`T_t` is the trend, and
:math:`R_t` is the remainder.

**The seasonal smoothing window** (*s_window*) controls how rapidly the seasonal
pattern can change. Larger values produce a more stable seasonal pattern.
Must be odd and >= 7. The default is typically ``period + 1`` (rounded to odd).

Algorithm
---------

STL uses an inner loop of iterative LOESS (locally weighted regression) smoothing:

1. **Detrend:** Subtract the current trend estimate from the series.
2. **Seasonal smoothing:** Apply LOESS to each subseries (e.g., all Januaries) with window *s_window*.
3. **Low-pass filter:** Remove high-frequency artifacts from the seasonal estimate.
4. **Deseasonalize:** Subtract the seasonal estimate from the original series.
5. **Trend smoothing:** Apply LOESS to the deseasonalized series.
6. **Iterate** steps 1-5 (typically 2 inner iterations, 1 outer iteration for robustness weights).

See Cleveland et al. (1990) for the complete specification.


Troubleshooting
---------------

**Seasonal component is too smooth / not smooth enough:**
Increase *s_window* for smoother seasonal patterns; decrease for more adaptive patterns.
The default is typically ``period + 1``.

**Remainder has visible seasonal pattern:**
*s_window* is too large — the seasonal smoother can't track changes in the seasonal
pattern. Reduce *s_window* or use a multiplicative decomposition (take logs first,
decompose, exponentiate).


Verification
------------

STL decomposition verified against R ``stats::stl()`` with ``s.window=13`` on the
AirPassengers dataset. Seasonal, trend, and remainder components match at :math:`10^{-4}`
tolerance.

See ``crossval/03_arima_crossval.R``.


References
----------

- Cleveland, R.B., W.S. Cleveland, J.E. McRae, and I. Terpenning (1990). "STL: A seasonal-trend decomposition procedure based on Loess." *Journal of Official Statistics*, 6(1), 3-73.


Library
-------
timeseries

Source
------
stl.src

.. seealso:: Functions :func:`arimaFit`
