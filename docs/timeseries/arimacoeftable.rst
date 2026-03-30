arimaCoefTable
==============

Purpose
-------
Return the coefficient table from a fitted ARIMA model as a dataframe.

Format
------

.. function:: tab = arimaCoefTable(result)

   :param result: an instance of an :class:`arimaResult` structure returned by :func:`arimaFit`.
   :type result: struct

   :return tab: Kx6 dataframe with columns: Coef, SE, t-stat, p-value, CI_lo, CI_hi. Row names are the coefficient labels.
   :rtype tab: dataframe

Examples
--------

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/airline.dat");
    y = loadd(fname, "passengers");

    result = arimaFit(y, order=1|1|1, season=12, quiet=1);

    // Get coefficient table as dataframe
    tab = arimaCoefTable(result);
    print tab;

::

                  Coef        SE    t-stat   p-value     CI_lo     CI_hi
    AR(1)       0.8731    0.0543   16.076     0.000     0.767     0.979
    MA(1)      -0.4018    0.1237   -3.248     0.001    -0.644    -0.159
    SMA(1)     -0.5569    0.0730   -7.630     0.000    -0.700    -0.414

Remarks
-------

The returned dataframe can be used for programmatic access to coefficients:

::

    // Extract p-values column
    pvals = tab[., "p-value"];

    // Find significant coefficients (p < 0.05)
    sig = selif(tab, tab[., "p-value"] .< 0.05);

Library
-------
timeseries

Source
------
arima.src

.. seealso:: Functions :func:`arimaFit`, :func:`arimaResults`
