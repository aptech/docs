tsDisplay
=========

Purpose
-------
Plot a series with its sample autocorrelation (ACF) and partial autocorrelation (PACF) functions in one figure.

Format
------

.. function:: tsDisplay(y)
              tsDisplay(y, d=1, lags=20, dates=years, level=0.95, title="Nile")

   :param y: the series. A dataframe with one numeric column and an optional date column (the date column labels the time axis) is also accepted.
   :type y: Nx1 vector or dataframe

   :param d: Optional keyword, the number of first differences applied before plotting. The time plot, ACF and PACF all show the differenced series. Default = 0.
   :type d: scalar

   :param lags: Optional keyword, the largest lag shown. Default = :math:`\lfloor 10 \log_{10} T \rfloor`, capped at :math:`T-1`, where :math:`T = N - d`.
   :type lags: scalar

   :param dates: Optional keyword, time values for the x-axis of the time plot, for example years. Overrides a date column in *y*. Default = the date column of *y* if present, otherwise 1, 2, ..., N.
   :type dates: Nx1 vector

   :param level: Optional keyword, coverage of the white-noise band. Default = 0.95.
   :type level: scalar in (0, 1)

   :param title: Optional keyword, series name used in the time-plot title. Default = "Series".
   :type title: string

Examples
--------

The first look at a series before choosing an ARIMA model: the series, then
its first difference.

::

    new;
    library timeseries;

    // nile.csv has a Year date column and a Flow column
    nile = loadd(getGAUSSHome("pkgs/timeseries/examples/data/nile.csv"));

    tsDisplay(nile, title="Nile annual flow");

    // After one difference only lag 1 stands out in the ACF: an MA(1)
    // in differences
    tsDisplay(nile, d=1, title="Nile annual flow");

Remarks
-------

The figure has three panels: the series (or its differences) across the top,
the ACF bottom left and the PACF bottom right. Lag 0 is omitted. The ACF and
PACF panels share one y-axis range so bar heights can be compared.

The dashed lines mark :math:`\pm z_{(1+\text{level})/2} / \sqrt{T}`, the usual
approximate band for a white-noise series, where :math:`T` is the number of
values after differencing.

Autocorrelations are the Box-Jenkins estimates, the same as R's ``acf()`` and
``pacf()``. The layout follows ``gg_tsdisplay(..., plot_type = "partial")`` in
the R feasts package (Hyndman & Athanasopoulos, *Forecasting: Principles and
Practice*, 3rd ed., section 9.5).

Each call opens its own graph window.

Library
-------
timeseries

Source
------
arima.src

.. seealso:: Functions :func:`stationarityTests`, :func:`arimaFit`, :func:`autoArima`
