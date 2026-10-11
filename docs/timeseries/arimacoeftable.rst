arimaCoefTable
==============

Purpose
-------
Return the coefficient table from a fitted ARIMA model as a dataframe.

Format
------

.. function:: coef_tab = arimaCoefTable(result)

   :param result: an instance of an :class:`arimaResult` structure returned by
                  :func:`arimaFit` or :func:`autoArima`.
   :type result: struct

   :return coef_tab: Kx6 dataframe with columns: Coef, SE, t-stat, p-value, CI_lo, CI_hi. The rows are in the order of *result.coef_names*.
   :rtype coef_tab: dataframe

Examples
--------

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/data/airpassengers.csv"), "value");

    // Airline model for the logged series
    result = arimaFit(ln(y), d=1, q=1, sd=1, sq=1, period=12, quiet=1);

    // Get coefficient table as dataframe
    coef_tab = arimaCoefTable(result);
    print result.coef_names;
    print coef_tab;

The rows are MA(1) and SMA(1):

::

            Coef               SE           t-stat          p-value            CI_lo            CI_hi
     -0.40182313      0.089644652       -4.4823993    7.3808461e-06      -0.57752342      -0.22612284
     -0.55693650      0.073105100       -7.6182989    2.5704063e-14      -0.70021987      -0.41365314

Remarks
-------

The returned dataframe can be used for programmatic access to coefficients:

::

    // Extract p-values column
    pvals = coef_tab[., "p-value"];

    // Find significant coefficients (p < 0.05)
    sig = selif(coef_tab, coef_tab[., "p-value"] .< 0.05);

Library
-------
timeseries

Source
------
arima.src

.. seealso:: Functions :func:`autoArima`, :func:`arimaFit`, :func:`arimaResults`
