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

Library
-------
timeseries

Source
------
stl.src

.. seealso:: Functions :func:`arimaFit`
