stlDecompose
============

Purpose
-------
Seasonal-Trend decomposition via LOESS (STL).

Format
------

.. function:: stl = stlDecompose(y, period)
              stl = stlDecompose(y, period, s_window=7)

   :param y: time series data, with at least 2 x *period* + 1 observations.
   :type y: Nx1 vector

   :param period: seasonal period, an integer of at least 2 (e.g., 12 for monthly, 4 for quarterly, 52 for weekly).
   :type period: scalar

   :param s_window: Optional keyword, seasonal smoothing window: an odd number of at least 7 (see Remarks). Default = the smallest odd number greater than *period*, and at least 7 (13 for monthly data).
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

Monthly international airline passengers, January 1949 to December 1960. The
seasonal swing grows with the number of passengers, so the series is decomposed
in logs.

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/airpassengers.csv");
    y = ln(loadd(fname, "value"));

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

    fname = getGAUSSHome("pkgs/timeseries/examples/data/airpassengers.csv");
    y = ln(loadd(fname, "value"));

    stl = stlDecompose(y, 12, quiet=1);

    // Fit ARIMA on the seasonally adjusted series
    y_adj = y - stl.seasonal;
    result = autoArima(y_adj);

Choosing the Seasonal Window
++++++++++++++++++++++++++++

Monthly carbon dioxide concentration at Mauna Loa, January 1959 to December
1997, in parts per million. With the default window of 13, the seasonal swing
(the largest month minus the smallest) grows from 5.86 in the first year to 6.71
in the last. A window of 35 lets the seasonal pattern change more slowly: the
swing grows only from 5.95 to 6.45.

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/co2.csv");
    y = loadd(fname, "value");

    stl_13 = stlDecompose(y, 12, quiet=1);
    stl_35 = stlDecompose(y, 12, s_window=35, quiet=1);

    // Seasonal swing in the first and last year
    first = seqa(1, 1, 12);
    last = seqa(rows(y) - 11, 1, 12);
    print "s_window = 13: " (maxc(stl_13.seasonal[first]) - minc(stl_13.seasonal[first]))
        (maxc(stl_13.seasonal[last]) - minc(stl_13.seasonal[last]));
    print "s_window = 35: " (maxc(stl_35.seasonal[first]) - minc(stl_35.seasonal[first]))
        (maxc(stl_35.seasonal[last]) - minc(stl_35.seasonal[last]));

The output:

::

    s_window = 13:        5.8618313        6.7080267
    s_window = 35:        5.9461446        6.4532171

Remarks
-------

STL decomposes a time series into three additive components:

.. math::

   y_t = S_t + T_t + R_t

where :math:`S_t` is the seasonal component, :math:`T_t` is the trend, and
:math:`R_t` is the remainder.

**Series length.** *y* needs two full periods and one more observation,
2 x *period* + 1: at least 25 observations for monthly data and 9 for quarterly
data. :func:`stlDecompose` stops with an error message for a shorter series or
for a *period* that is not an integer of at least 2.

**The seasonal smoothing window** (*s_window*) controls how quickly the seasonal
pattern can change. Each seasonal value is a weighted average over *s_window*
consecutive values of its cycle-subseries (for example, 13 consecutive
Januaries), so a larger window gives a more stable seasonal pattern. *s_window*
is an odd number of at least 7: a smaller value is raised to 7, and an even value
to the next odd number. The default is the smallest odd number greater than
*period*, and at least 7: 13 for monthly data and 7 for quarterly data.

Algorithm
---------

STL uses an inner loop of iterative LOESS (locally weighted regression) smoothing:

1. **Detrend:** Subtract the current trend estimate from the series.
2. **Seasonal smoothing:** Apply LOESS to each subseries (e.g., all Januaries) with window *s_window*.
3. **Low-pass filter:** Remove high-frequency artifacts from the seasonal estimate.
4. **Deseasonalize:** Subtract the seasonal estimate from the original series.
5. **Trend smoothing:** Apply LOESS to the deseasonalized series.
6. **Repeat** steps 1-5 once, for two passes in all.

:func:`stlDecompose` does not compute robustness weights, so an outlier can move
the seasonal and trend values near it.

See Cleveland et al. (1990) for the complete specification.


Troubleshooting
---------------

**Seasonal component is too smooth / not smooth enough:**
Increase *s_window* for smoother seasonal patterns; decrease for more adaptive patterns.
The default is the smallest odd number greater than *period*, and at least 7.

**Remainder has visible seasonal pattern:**
*s_window* is too large — the seasonal smoother can't track changes in the seasonal
pattern. Reduce *s_window* or use a multiplicative decomposition (take logs first,
decompose, exponentiate).


Verification
------------

The seasonal, trend and remainder components are checked at every observation
against two independent implementations of STL with the same settings: on
monthly atmospheric CO2, monthly temperatures, quarterly gas consumption and the
airline passenger series in logs, and on a 600-value series with period 2. Every
value agrees to 12 digits of the series' largest absolute value.

References
----------

- Cleveland, R.B., W.S. Cleveland, J.E. McRae, and I. Terpenning (1990). "STL: A seasonal-trend decomposition procedure based on Loess." *Journal of Official Statistics*, 6(1), 3-73.


Library
-------
timeseries

Source
------
arima.src

.. seealso:: Functions :func:`autoArima`, :func:`arimaFit`
