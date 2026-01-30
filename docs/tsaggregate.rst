
tsAggregate
==============================================

Purpose
----------------

Aggregates time series data to lower frequency.

Format
----------------
.. function:: result = tsAggregate(df, freq, method[, skip_miss_check])

    :param df: Data with date column.
    :type df: NxK dataframe or matrix

    :param freq: Aggregation frequency.

        **Valid options:**

        .. list-table::
            :widths: auto

            * - "Second" or "S"
              - Second frequency
            * - "Minute" or "N"
              - Minute frequency
            * - "Hourly" or "H"
              - Hourly frequency
            * - "Daily" or "D"
              - Daily frequency
            * - "Monthly" or "M"
              - Monthly frequency
            * - "Quarterly" or "Q"
              - Quarterly frequency
            * - "Yearly" or "Y"
              - Yearly frequency

    :type freq: String

    :param method: Aggregation method.

        **Valid options:**

        .. list-table::
            :widths: auto

            * - "last"
              - Last observation in period
            * - "first"
              - First observation in period
            * - "lastBD"
              - Last business day (Mon-Fri)
            * - "mean"
              - Mean of all observations
            * - "sum"
              - Sum of all observations
            * - "max"
              - Maximum value
            * - "min"
              - Minimum value
            * - "median"
              - Median value
            * - "sd"
              - Standard deviation
            * - "count"
              - Count of observations
            * - "mode"
              - Mode (most frequent value)

    :type method: String

    :param skip_miss_check: Optional. Default: 0. Set to 1 to skip checking for missing values (faster but missings may affect results). When 0, missing values are handled per-column.
    :type skip_miss_check: scalar

    :return result: Aggregated data with exactly 1 observation per period. The "count" method returns only 2 columns (date + count).
    :rtype result: MxK dataframe or matrix

Examples
----------------

Example 1: Convert daily to monthly
+++++++++++++++++++++++++++++++++++

This example shows how to aggregate daily stock price data to monthly frequency using the last observation of each month.

::

    // Load daily stock data
    fname = getGAUSSHome("examples/xle_daily.xlsx");
    xle = loadd(fname, "date(Date) + Adj Close");

    // Get month-end prices
    monthly_prices = tsAggregate(xle, "Monthly", "last");

    // Print first 5 months
    print monthly_prices[1:5,.];

::

            Date        Adj Close 
      2017-06-30        63.202347 
      2017-07-31        64.857376 
      2017-08-31        61.303944 
      2017-09-29        67.546112 
      2017-10-31        66.983879

Example 2: Last vs Last Business Day
+++++++++++++++++++++++++++++++++++++

This example demonstrates the difference between "last" and "lastBD" methods using simulated data that includes weekends.

::

    // Set for repeatable random numbers
    rndseed 435325;

    // Create 90 days of data including weekends
    dates = asdate(seqaPosix("2025-05-01", 1, "days", 92));
    prices = 100 + cumsumc(rndn(rows(dates), 1) * 2);
    daily_data = asdf(dates ~ prices, "date", "price");

    // Get last calendar day of each month (including weekends)
    monthly_last = tsAggregate(daily_data, "Monthly", "last");

    print "Last calendar day:";
    print monthly_last;

::

      Last calendar day:

            date            price 
      2025-05-31        109.73152 
      2025-06-30        110.60293 
      2025-07-31        108.83946

::

    // Get last business day of each month (Mon-Fri only)
    monthly_lastbd = tsAggregate(daily_data, "Monthly", "lastBD");

    print "Last business day:";
    print monthly_lastbd;

::

      Last business day:

            date            price 
      2025-05-30        109.30650 
      2025-06-30        110.60293 
      2025-07-31        108.83946

In this example, May 31, 2025 is a Saturday, so "lastBD" returns May 30 (Friday) instead.


Example 3: Monthly statistics
++++++++++++++++++++++++++++++

This example demonstrates different statistical aggregation methods on daily volume data.

::

    // Load daily stock data
    fname = getGAUSSHome("examples/xle_daily.xlsx");
    xle = loadd(fname, "date(Date) + Volume");

    // Calculate total monthly volume
    monthly_vol = tsAggregate(xle, "Monthly", "sum");

    print monthly_vol[1:3,.];

::

            Date           Volume 
      2017-06-30    2.6235880e+08
      2017-07-31    3.1071860e+08
      2017-08-31    2.8355080e+08

::

    // Calculate average daily volume per month
    monthly_avg = tsAggregate(xle, "Monthly", "mean");

    // Calculate maximum daily volume per month
    monthly_max = tsAggregate(xle, "Monthly", "max");

    // Calculate standard deviation of volume per month
    monthly_sd = tsAggregate(xle, "Monthly", "sd");


Example 4: Multiple data columns
+++++++++++++++++++++++++++++++++

This example shows how to aggregate data with multiple columns simultaneously.

::

    // Load daily stock data with multiple columns
    fname = getGAUSSHome("examples/xle_daily.xlsx");
    xle = loadd(fname, "date(Date) + Adj Close + Volume");

    // Get month-end values for both columns
    monthly_last = tsAggregate(xle, "Monthly", "last");

    print monthly_last[1:3,.];

::

            Date        Adj Close          Volume
      2017-06-30        63.202347        19643200
      2017-07-31        64.857376        13519500
      2017-08-31        61.303944        10333700

::

    // Get monthly average for both columns
    monthly_avg = tsAggregate(xle, "Monthly", "mean");


Example 5: Quarterly aggregation
+++++++++++++++++++++++++++++++++

This example aggregates daily data to quarterly frequency.

::

    // Load daily stock data
    fname = getGAUSSHome("examples/xle_daily.xlsx");
    xle = loadd(fname, "date(Date) + Adj Close");

    // Get quarter-end prices
    quarterly_prices = tsAggregate(xle, "Quarterly", "last");

    print quarterly_prices;

::

            Date        Adj Close 
      2017-06-30        63.202347 
      2017-09-29        67.546112 
      2017-12-29        71.749161 
      2018-03-29        67.410004 
      2018-06-13        76.419998


Example 6: Using frequency aliases
+++++++++++++++++++++++++++++++++++

This example shows the use of short frequency aliases.

::

    // Load daily stock data
    fname = getGAUSSHome("examples/xle_daily.xlsx");
    xle = loadd(fname, "date(Date) + Adj Close");

    // These are equivalent
    result1 = tsAggregate(xle, "Monthly", "last");
    result2 = tsAggregate(xle, "M", "last");

    // Also equivalent
    result3 = tsAggregate(xle, "Quarterly", "mean");
    result4 = tsAggregate(xle, "Q", "mean");


Example 7: Chain aggregations
+++++++++++++++++++++++++++++++

This example demonstrates chaining multiple aggregations to go from daily to monthly to yearly.

::

    // Start with 3 years of daily data
    dates = asdate(seqaPosix("2022-01-01", 1, "days", 1095));
    prices = 100 + cumsumc(rndn(1095, 1) * 2);

    daily_data = dates ~ prices;

    // Aggregate to monthly (about 36 observations)
    monthly_data = tsAggregate(daily_data, "Monthly", "last");

    // Aggregate to yearly (3 observations)
    yearly_data = tsAggregate(monthly_data, "Yearly", "last");


Example 8: Count observations
+++++++++++++++++++++++++++++++

This example shows the "count" method, which returns the number of observations in each period.

::

    // Load daily stock data
    fname = getGAUSSHome("examples/xle_daily.xlsx");
    xle = loadd(fname, "date(Date) + Adj Close");

    // Count trading days per month
    monthly_counts = tsAggregate(xle, "Monthly", "count");

    print monthly_counts[1:5,.];

::

            Date         count
      2017-06-30            14
      2017-07-31            20
      2017-08-31            23
      2017-09-29            20
      2017-10-31            22


Remarks
-------

- The date column can be in any position in the input data. It will be automatically detected and moved to the first column in the output.
- Input data is automatically sorted by date before aggregation.
- In the case of duplicate dates, the first match found will be returned for row-selection methods ("first", "last", "lastBD").
- Missing values are removed on a per-column basis before performing the aggregation function. If column A has a missing value in row 5 but column B does not, only column A's aggregation excludes row 5.
- All data columns (except the date column) are aggregated using the specified method.
- For the "lastBD" method, business days are Monday through Friday only. No holiday calendar is applied.
- If no business days are found in a period for the "lastBD" method, the last observation (even if it's a weekend) is used instead.
- Periods with no data are skipped in the output.
- The "count" method returns only 2 columns: the date column and a count column.
- For string frequency parameters, the function is case-insensitive (e.g., "monthly", "Monthly", and "MONTHLY" are all valid).

.. seealso:: Functions :func:`sortc`, :func:`aggregate`, :func:`meanc`, :func:`sumc`
