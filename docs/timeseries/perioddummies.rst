periodDummies
=============

Purpose
-------
Create one indicator column for each quarter in a historical window, with matching future columns for forecasting.

Format
------

.. function:: { X, X_future } = periodDummies(dates, start_period="2008Q1", end_period="2009Q4", horizon=8, mode="quarter-dummies")
              { X, X_future } = periodDummies(dates, start_period="2008Q1", end_period="2009Q4", horizon=8, mode="baseline")

   :param dates: Nonempty, finite POSIX date column vector, increasing by one quarter without gaps. Dates must follow a regular quarterly calendar convention at midnight.
   :type dates: Tx1 vector

   :param start_period: Optional keyword, first quarter of the inclusive indicator window, in ``YYYYQ1`` through ``YYYYQ4`` form. The default empty string is not a valid window; supply both period labels in either mode.
   :type start_period: string

   :param end_period: Optional keyword, last quarter of the inclusive window, in the same form.
   :type end_period: string

   :param horizon: Optional keyword, positive integer number of future rows. Default = 1.
   :type horizon: scalar

   :param mode: Optional keyword, ``"quarter-dummies"`` to create indicators, or ``"baseline"`` (default) to return two empty matrices after the same input checks. The strings are case-sensitive.
   :type mode: string

   :return X: Historical indicators. Each column is 1 in its quarter and 0 elsewhere, named ``D_YYYYQn``. Columns are in chronological order. Empty for baseline mode.
   :rtype X: TxJ dataframe or empty matrix

   :return X_future: All-zero future indicators with the same named columns in the same order. The complete window is in the training sample. Empty for baseline mode.
   :rtype X_future: horizon x J dataframe or empty matrix

Examples
--------

::

    new;
    library timeseries;

    macro_data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv"));
    train_data = selif(macro_data, macro_data[., "date"] .<= "2019-10-01");
    quarter_dates = train_data[., "date"];
    model_data = train_data[., "gdp_growth" "inflation" "unemployment" "fed_funds"];

    { X, X_future } = periodDummies(quarter_dates, start_period="2008Q1",
        end_period="2009Q4", horizon=8, mode="quarter-dummies");

    struct varResult fit_dummy;
    fit_dummy = varFit(model_data, p=2, xreg=X, quiet=1);
    fc_dummy = varForecast(fit_dummy, 8, xreg_future=X_future);

Remarks
-------

The ordered window must lie entirely within the training dates, including
both endpoints. J is the number of quarters in that inclusive window.
Future rows are zero because none of those historical quarters is in the
forecast period. These are separate indicators for historical quarters,
not seasonal indicators repeated each year.

The date index must advance by exactly one quarter. Each date uses the
same month position within its quarter. All dates may be at month end;
otherwise they use a fixed day, shortened to the month's last day when
necessary. Intraday times, gaps, duplicates and irregular positions are
errors. Both modes validate the dates, labels and complete window.

An invalid mode, an empty or non-column date index, a missing or nonfinite
date, an invalid quarter label, a reversed or out-of-sample window, or a
non-positive or non-integer horizon raises an error. A window that creates
redundant regressors can still be refused by :func:`varFit`'s rank check.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`varFit`, :func:`varForecast`, :func:`condForecast`
