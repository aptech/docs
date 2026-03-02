.. _time-and-date:

Time and Date
===============================================

GAUSS provides a modern date system built around dataframes. Date
columns are auto-detected when loading data, display in human-readable
formats, and support filtering, arithmetic, and plotting.

.. note::

    If you are coming from **Stata**: ``loadd`` is like ``import
    delimited`` plus ``generate date = daily(...)`` plus ``format %td``
    in one step. GAUSS does **not** require a ``tsset`` declaration —
    functions like :func:`lagn` and :func:`plotXY` operate on columns
    directly. If you are coming from **R/pandas**: :func:`loadd`
    combines ``read.csv`` + ``as.Date``; :func:`asDate` is similar to
    ``as.Date()`` or ``pd.to_datetime()``.

.. list-table::
    :widths: 30 35 35
    :header-rows: 1

    * - Task
      - Stata
      - GAUSS

    * - Load with dates
      - ``import delimited`` + ``gen date = daily(...)``
      - ``loadd("file.csv")`` (auto-detects)

    * - Set date format
      - ``format date %tq``
      - ``asDate(data, "%Y-Q%q", "Date")``

    * - Extract year
      - ``gen yr = year(date)``
      - ``dtYear(data, "Date")``

    * - Lag
      - ``tsset date`` then ``L.x``
      - ``lagn(data[., "x"], 1)``

    * - Plot time series
      - ``tsline gdp``
      - ``plotXY(data, "GDP ~ Date")``

    * - Aggregate frequency
      - ``collapse (mean) x, by(qdate)``
      - ``tsAggregate(data, "Q", "mean")``


Under the hood, GAUSS stores all dates as **POSIX seconds** — the
number of seconds since January 1, 1970 UTC. This is similar to
Stata's internal date numbers (days since January 1, 1960), but using
seconds from 1970 as the epoch. The **display format** is separate
from the stored value — changing a display format from ``%Y-%m-%d`` to
``%Y-Q%q`` does not alter the underlying number, only how it prints.


Loading Data with Dates
--------------------------------------------

The most common way to get dates into GAUSS is through :func:`loadd`,
which auto-detects approximately 30 date formats in CSV and Excel
files:

::

    data = loadd("stock_prices.csv");
    print head(data);

::

              Date        Close
        2024-01-02       472.65
        2024-01-03       468.38
        2024-01-04       467.77
        2024-01-05       473.48
        2024-01-08       479.18

To verify that a column was recognized as a date, check its type:

::

    print getColTypes(data);

::

            type
            date
          number

When auto-detection fails
++++++++++++++++++++++++++++++++++++

If a date column loads as a string instead of a date (check with
:func:`getColTypes` — a failed detection shows ``string`` rather
than ``date``), use the ``date()`` keyword in a formula string to
force conversion:

::

    // Tell GAUSS that "mydate" is a date column
    data = loadd("file.csv", "date(mydate) + x1 + x2");

    // Specify the format explicitly when auto-detection cannot guess it
    data = loadd("file.csv", "date(mydate, '%d/%m/%Y') + x1 + x2");

.. tip::

    If your data has the common quarterly format ``2020Q1``,
    ``2020-Q3``, etc., use the ``%q`` specifier (a GAUSS extension):

    ::

        data = loadd("macro.csv", "date(quarter, '%YQ%q') + gdp + cpi");

    This converts ``2020Q1`` to January 1, 2020, ``2020Q3`` to July 1,
    2020, and so on.


Handling missing or unparseable dates
+++++++++++++++++++++++++++++++++++++++

When a date column contains blank cells or values that cannot be
parsed, GAUSS inserts a missing value (``.``). Use :func:`packr` to
drop rows with missing dates, or compare against :func:`miss` to
find them (:func:`ismiss` returns a scalar, not a row-by-row mask):

::

    // Find rows with missing dates (element-wise)
    mask = data[., "Date"] .== miss();

    // Get row indices of missing dates
    idx = findIdx(mask);

    // Drop rows where date is missing
    data = packr(data);


Displaying and Formatting Dates
--------------------------------------------

The default display format is ``%Y-%m-%d`` (e.g., ``2024-03-15``).
Use :func:`asDate` to change how dates are displayed and return
the updated dataframe, or :func:`setColDateFormats` to set the
format metadata directly. Neither alters the stored POSIX values:

::

    // Display as month/day/year
    data = asDate(data, "%m/%d/%Y", "Date");

    // Display as quarterly
    data = asDate(data, "%Y-Q%q", "Date");

    // Display with time
    data = asDate(data, "%Y-%m-%d %H:%M", "Date");

To check the current display format:

::

    print getColDateFormats(data, "Date");

.. _date-format-specifiers:

Common format specifiers
++++++++++++++++++++++++++++++++++++

If your dates look like this, use this format string:

.. list-table::
    :widths: 35 25 40
    :header-rows: 1

    * - Example
      - Format string
      - Used by

    * - ``2024-03-15``
      - ``%Y-%m-%d``
      - :func:`asDate`, :func:`strctoposix`

    * - ``03/15/2024``
      - ``%m/%d/%Y``
      - :func:`asDate`, :func:`strctoposix`

    * - ``15-Mar-2024``
      - ``%d-%b-%Y``
      - :func:`asDate`, :func:`strctoposix`

    * - ``2024-Q1``
      - ``%Y-Q%q``
      - :func:`asDate`, :func:`strctoposix`

    * - ``2024Q3``
      - ``%YQ%q``
      - :func:`asDate`, :func:`strctoposix`

    * - ``March 15, 2024``
      - ``%B %d, %Y``
      - :func:`asDate`, :func:`strctoposix`

    * - ``2024-03-15 14:30``
      - ``%Y-%m-%d %H:%M``
      - :func:`asDate`, :func:`strctoposix`

    * - ``2024``
      - ``%Y``
      - :func:`asDate`, :func:`strctoposix`

    * - ``2024-03``
      - ``%Y-%m``
      - :func:`asDate`, :func:`strctoposix`

The ``%q`` specifier for quarters is a GAUSS extension — it is not
part of standard BSD strftime. See :ref:`format-reference` for the
full list.

.. warning::

    GAUSS has **two separate format systems**. Modern functions
    (:func:`strctoposix`, :func:`posixtostrc`, :func:`asDate`,
    :func:`setColDateFormats`) use **BSD strftime** specifiers like
    ``%Y-%m-%d``. Legacy functions (:func:`strtodt`, :func:`dttostr`)
    and plot axis labels (:func:`plotSetXTicLabel`) use **GAUSS format
    codes** like ``YYYY-MO-DD``. These are **not interchangeable**.


Extracting Date Components
--------------------------------------------

The ``dt*`` family of functions extracts components from date columns:

.. list-table::
    :widths: 30 35 35
    :header-rows: 1

    * - Function
      - Returns
      - Example output

    * - :func:`dtYear`
      - Year
      - ``2024``

    * - :func:`dtMonth`
      - Month (1–12)
      - ``3``

    * - :func:`dtQuarter`
      - Quarter (1–4)
      - ``1``

    * - :func:`dtDayofMonth`
      - Day of month (1–31)
      - ``15``

    * - :func:`dtDayofWeek`
      - Day of week. Default: 0=Sun … 6=Sat. With ``start_Monday=1``: 1=Mon … 7=Sun
      - ``5`` (Friday, default)

    * - :func:`dtDayofYear`
      - Day of year (1–366)
      - ``75``

    * - :func:`dtWeek`
      - Week of year (0–53; 0 = before first Monday)
      - ``11``

    * - :func:`dtHour`
      - Hour. Default: 1–12. With ``twenty_four=1``: 0–23
      - ``2`` (default) or ``14`` (24-hr)

    * - :func:`dtMinute`
      - Minute (0–59)
      - ``30``

    * - :func:`dtSecond`
      - Second (0–59)
      - ``0``

    * - :func:`dtMonthName`
      - Month name
      - ``"March"``

    * - :func:`dtDayName`
      - Day name
      - ``"Friday"``

All ``dt*`` functions take a dataframe and an optional column name:

::

    // Add a quarter column
    data = dfaddcol(data, "Quarter", dtQuarter(data, "Date"));

    // Filter to weekdays only
    // Monday-start mode: Mon=1, Tue=2, ..., Fri=5, Sat=6, Sun=7
    dow = dtDayofWeek(data, "Date", 1);
    data = selif(data, dow .>= 1 .and dow .<= 5);


Filtering by Date
--------------------------------------------

The simplest way to filter by date range is :func:`between`:

::

    // Keep only 2020 data
    mask = between(data[., "Date"], "2020-01-01", "2020-12-31");
    data_2020 = selif(data, mask);

.. note::

    :func:`between` is **inclusive** on both endpoints by default. A
    partial string like ``"2021"`` is interpreted as January 1, 2021 at
    midnight, so ``between(dates, "2020", "2021")`` includes
    January 1, 2021. Use the optional fourth argument to control this:

    ::

        // Exclude the right endpoint
        mask = between(data[., "Date"], "2020", "2021", "left");

    Options: ``"both"`` (default), ``"left"``, ``"right"``,
    ``"neither"``.

For more complex conditions, use relational operators on date
columns — GAUSS automatically compares the string against the stored
POSIX value:

::

    // Keep data from 2018 through 2022
    data = selif(data, data[., "Date"] .>= "2018-01-01"
                 .and data[., "Date"] .< "2023-01-01");

Partial date strings work: ``"2020"`` means January 1, 2020 at
midnight, so ``.< "2021"`` selects all of 2020.


Creating Dates
--------------------------------------------

From strings
++++++++++++++++++++++++++++++++++++

::

    // Single date (auto-detects format, returns a date-typed dataframe)
    dt = asDate("2024-03-15");

    // With explicit format (when auto-detection cannot guess)
    dt = strctoposix("15-Mar-2024", "%d-%b-%Y");

Date sequences
++++++++++++++++++++++++++++++++++++

Use :func:`seqaPosix` to generate evenly-spaced date sequences:

::

    // Monthly: 24 months starting January 2020
    monthly = seqaPosix("2020-01-01", 1, "months", 24);

    // Quarterly: use 3-month increments
    quarterly = seqaPosix("2020-01-01", 3, "months", 20);

    // Daily: 365 days
    daily = seqaPosix("2024-01-01", 1, "days", 365);

Supported units: ``"years"``, ``"months"``, ``"days"``, ``"hours"``,
``"minutes"``, ``"seconds"``.

To build a new dataframe from scratch, use ``~`` to combine columns
horizontally. Use :func:`dfaddcol` to append a computed column to an
existing dataframe (as in the growth rate example later):

::

    dates = asDate(seqaPosix("2020-01-01", 1, "months", 24), "%Y-%m");
    values = rndn(24, 1);
    data = dates ~ dfname(values, "GDP");


Date Arithmetic
--------------------------------------------

Adding and subtracting time
++++++++++++++++++++++++++++++++++++

:func:`timeDeltaPosix` adds (or subtracts) a duration to a date:

::

    dt = strctoposix("2024-01-15", "%Y-%m-%d");

    // Add 3 months
    dt_plus3m = timeDeltaPosix(dt, 3, "months");

    // Subtract 7 days
    dt_minus7d = timeDeltaPosix(dt, -7, "days");

Supported units: ``"years"``, ``"months"``, ``"days"``, ``"hours"``,
``"minutes"``, ``"seconds"``.

.. warning::

    ``"months"`` adds calendar months, but does **not** clip to
    month-end. January 31 + 1 month = **March 2**, not February 28
    or 29. If you need month-end dates, generate a sequence of 1st-of-
    month dates and subtract one day, or use :func:`tsAggregate` with
    ``"lastBD"`` on daily data.

Computing differences
++++++++++++++++++++++++++++++++++++

:func:`timeDiffPosix` computes the difference between two dates:

::

    d1 = strctoposix("2024-06-15", "%Y-%m-%d");
    d2 = strctoposix("2024-01-01", "%Y-%m-%d");

    print timeDiffPosix(d1, d2, "days");     // 166

Supported units for :func:`timeDiffPosix`: ``"days"``, ``"hours"``,
``"minutes"``, ``"seconds"``. The result is ``d1 - d2`` in the
requested unit. Note that ``"months"`` and ``"years"`` are **not**
available as difference units — compute them manually from the day
count or use :func:`dtYear` / :func:`dtMonth` to compare
components.


Lags, Differences, and Growth Rates
--------------------------------------------

For time series work, dates matter most when computing lags and
growth rates. GAUSS provides :func:`lagn` for shifting data by
position:

::

    // Lag GDP by one period (missing value fills the first row)
    gdp_lag = lagn(data[., "GDP"], 1);

    // Lead GDP by one period (missing fills the last row)
    gdp_lead = lagn(data[., "GDP"], -1);

Computing percentage change:

::

    gdp = data[., "GDP"];
    growth = (gdp - lagn(gdp, 1)) ./ lagn(gdp, 1);

Computing log returns from a price series:

::

    price = data[., "Close"];
    log_returns = ln(price) - ln(lagn(price, 1));

.. note::

    :func:`lagn` shifts by **position**, not by calendar time. If
    your data is not already sorted, sort it first:

    ::

        data = sortc(data, "Date");

    This is the step that Stata's ``tsset`` handles automatically.
    The first row after a lag (or last row after a lead) will contain
    a missing value (``.``). Estimation functions in TSMT, CML, and
    built-ins like :func:`olsmt` handle missing values by listwise
    deletion. Low-level matrix operations do not — use :func:`packr`
    to drop incomplete rows when needed.

Using ``lag()`` in formula strings
++++++++++++++++++++++++++++++++++++

The ``lag()`` keyword in formula strings lets you specify lags
directly in model estimation — no need to create lagged columns
manually:

::

    // Regress inflation on lagged GDP growth
    call olsmt(data, "inflation ~ lag(gdp_growth)");

    // Two lags
    call olsmt(data, "inflation ~ lag(gdp_growth, 1) + lag(gdp_growth, 2)");

This is similar to Stata's ``L.x`` and ``L2.x`` operators, but does
not require a ``tsset`` declaration first.

.. warning::

    If your data has a **panel structure** (multiple entities observed
    over time), :func:`lagn` will lag across entity boundaries
    unless you group the data first — this is a silent error that
    produces wrong results. For panel-aware lags, see the
    :doc:`/data-management/index` section on panel data operations.
    :func:`lagTrim` is a performance variant of :func:`lagn` that
    removes leading missing rows, but it is **not** panel-aware.


Plotting Time Series
--------------------------------------------

When a dataframe column is typed as a date, :func:`plotXY` and
:func:`plotScatter` automatically format the X axis with date labels:

::

    // Simplest case — auto-detects date axis
    plotXY(data, "Close ~ Date");

For more control over date-axis plots:

::

    // plotTSHF — explicit date vector and label unit
    plotTSHF(data[., "Date"], "months", data[., "Close"]);

    // plotTS — for evenly-spaced data (frequency-based)
    // dtstart is a DT scalar: use strctodt to create one
    dtstart = strctodt("20200101", "%Y%m%d");
    plotTS(dtstart, 4, data[., "Close"]);   // 4 = quarterly

:func:`plotTS` frequency codes:

.. list-table::
    :widths: 30 20 50
    :header-rows: 1

    * - Frequency
      - Code
      - Date axis labels

    * - Yearly
      - 1
      - ``YYYY``

    * - Quarterly
      - 4
      - ``YYYY-QQ``

    * - Monthly
      - 12
      - ``YYYY-MO``

    * - Weekly
      - 52
      - ``MO-DD``

    * - Daily
      - 365
      - ``MO-DD``

The axis label formats above (``YYYY-QQ``, ``YYYY-MO``, etc.) are
**GAUSS legacy format codes**, not BSD strftime specifiers — see
:ref:`format-reference`.

Customizing date axis labels:

::

    struct plotControl myPlot;
    myPlot = plotGetDefaults("xy");

    // Set date format for X-axis labels (uses GAUSS format codes)
    plotSetXTicLabel(&myPlot, "YYYY-QQ");

    plotXY(myPlot, data, "Close ~ Date");


Frequency Conversion
--------------------------------------------

:func:`tsAggregate` converts time series data between frequencies:

::

    // Daily to monthly (last observation of each month)
    monthly = tsAggregate(daily_data, "M", "last");

    // Daily to quarterly (mean)
    quarterly = tsAggregate(daily_data, "Q", "mean");

    // Monthly to yearly (sum)
    yearly = tsAggregate(monthly_data, "Y", "sum");

Frequency codes: ``"S"`` (second), ``"N"`` (minute), ``"H"``
(hourly), ``"D"`` (daily), ``"M"`` (monthly), ``"Q"`` (quarterly),
``"Y"`` (yearly).

Aggregation methods: ``"last"``, ``"first"``, ``"lastBD"`` (last
business day), ``"mean"``, ``"sum"``, ``"max"``, ``"min"``,
``"median"``, ``"sd"``, ``"count"``, ``"mode"``.

::

    // Get end-of-month last business day prices
    monthly_bd = tsAggregate(daily_data, "M", "lastBD");

.. note::

    ``"lastBD"`` uses weekdays (Monday–Friday) only. It does **not**
    consult a holiday calendar.


Putting It All Together
--------------------------------------------

Here is a complete workflow: load quarterly macro data, compute GDP
growth, and run a regression of CPI inflation on lagged GDP growth.

::

    // Load data — dates auto-detected
    data = loadd("macro_quarterly.csv");

    // Verify date column (should show "date", not "string")
    print head(data);
    print getColTypes(data);

    // If the date loaded as "string", reload with explicit format:
    // data = loadd("macro_quarterly.csv", "date(Date, '%YQ%q') + GDP + CPI");

    // Sort by date before computing lags
    data = sortc(data, "Date");

    // Compute GDP growth rate
    gdp = data[., "GDP"];
    growth = (gdp - lagn(gdp, 1)) ./ lagn(gdp, 1);
    data = dfaddcol(data, "GDP_Growth", growth);

    // Compute CPI inflation rate
    cpi = data[., "CPI"];
    inflation = (cpi - lagn(cpi, 1)) ./ lagn(cpi, 1);
    data = dfaddcol(data, "Inflation", inflation);

    // Plot GDP growth over time
    plotXY(data, "GDP_Growth ~ Date");

    // Regress inflation on lagged GDP growth
    call olsmt(data, "Inflation ~ lag(GDP_Growth)");


Trading Day Functions
--------------------------------------------

GAUSS includes functions for working with NYSE trading days:

.. list-table::
    :widths: 35 65
    :header-rows: 1

    * - Function
      - Description

    * - :func:`getNextTradingDay`
      - Next NYSE trading day

    * - :func:`getPreviousTradingDay`
      - Previous NYSE trading day

    * - :func:`getNextWeekDay`
      - Next weekday (Mon–Fri)

    * - :func:`getPreviousWeekDay`
      - Previous weekday (Mon–Fri)

    * - :func:`elapsedTradingDays`
      - Trading days between two dates

    * - :func:`annualTradingDays`
      - Trading days in a given year

These functions take **DT scalar** input (not POSIX dates). There
is no direct POSIX-to-DT conversion function; a string intermediate
is required. To use them with modern date columns:

::

    // Convert a POSIX date to DT scalar for trading day functions
    posix_date = data[1, "Date"];
    dt_str = posixtostrc(posix_date, "%Y%m%d%H%M%S");
    dt_scalar = strctodt(dt_str, "%Y%m%d%H%M%S");

    next_td = getNextTradingDay(dt_scalar);
    print dttostrc(next_td, "%Y-%m-%d");

.. warning::

    The built-in NYSE holiday calendar covers **1888–2020**. For
    dates after 2020, these functions treat all holidays as regular
    trading days (only weekends are excluded). The calendar file
    ``holidays.asc`` in your GAUSS home directory is user-editable —
    you can extend it with additional holidays.

    :func:`tsAggregate` with ``"lastBD"`` is a simpler alternative
    for many use cases and does not depend on the holiday calendar.


.. _format-reference:

Format Reference
--------------------------------------------

BSD strftime specifiers
++++++++++++++++++++++++++++++++++++

Used by :func:`strctoposix`, :func:`posixtostrc`, :func:`asDate`,
:func:`setColDateFormats`, and the DT-scalar bridge functions
:func:`strctodt` and :func:`dttostrc` (which use BSD specifiers
but produce/consume DT scalar values):

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Code
      - Meaning

    * - ``%Y``
      - Four-digit year (2024)

    * - ``%y``
      - Two-digit year (24)

    * - ``%m``
      - Month 01–12

    * - ``%d``
      - Day of month 01–31

    * - ``%H``
      - Hour 00–23

    * - ``%I``
      - Hour 01–12

    * - ``%M``
      - Minute 00–59

    * - ``%S``
      - Second 00–59

    * - ``%B``
      - Full month name (March)

    * - ``%b``
      - Abbreviated month name (Mar)

    * - ``%A``
      - Full day name (Friday)

    * - ``%a``
      - Abbreviated day name (Fri)

    * - ``%p``
      - AM/PM

    * - ``%q``
      - Quarter 1–4 (**GAUSS extension**)

    * - ``%j``
      - Day of year 001–366

    * - ``%F``
      - Shorthand for ``%Y-%m-%d``

    * - ``%T``
      - Shorthand for ``%H:%M:%S``

GAUSS legacy format codes
++++++++++++++++++++++++++++++++++++

Used by :func:`strtodt`, :func:`dttostr`, :func:`plotSetXTicLabel`:

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Code
      - Meaning

    * - ``YYYY``
      - Four-digit year

    * - ``YR``
      - Two-digit year

    * - ``MO``
      - Month

    * - ``DD``
      - Day

    * - ``HH``
      - Hour

    * - ``MI``
      - Minute

    * - ``SS``
      - Second

    * - ``QQ``
      - Quarter


Legacy Date Representations
--------------------------------------------

Modern GAUSS code should use POSIX dates (dataframe date columns).
**You can skip this section if you are writing new code from scratch.**
You will need it if you are reading older GAUSS programs, using the
trading day functions above, or working with pre-GAUSS 22 code.
Older code may use these legacy formats:

**DT Scalars** — a double-precision number encoding ``YYYYMMDDHHmmSS``.
For example, ``20150910110231`` means September 10, 2015, 11:02:31 AM.
Functions like :func:`dtday`, :func:`dtdate`, and :func:`todaydt`
create DT scalars. The trading day functions above also use DT scalar
input.

**DTV Vectors** — an Nx8 matrix where each row contains: year,
month (1–12), day (1–31), hour (0–23), minute (0–59), second
(0–59), day-of-week (0–6, 0=Sunday), and day-of-year (0–365).
Used by :func:`dtvnormal` and :func:`utctodtv`. Convert from DT
scalar using :func:`dttodtv`.

**4x1 Date/Time Vectors** — a separate legacy format returned by
the :func:`date` and :func:`time` functions (not interchangeable
with DTV). Contains year, month, day, and hundredths-of-second-
since-midnight. Used with :func:`ethsec`, :func:`etdays`, and
:func:`datestr`.

Converting between legacy and modern formats
+++++++++++++++++++++++++++++++++++++++++++++++

::

    // DT scalar → POSIX (one step)
    posix = dttoposix(dt_scalar);

    // POSIX → DT scalar (two steps — no direct conversion exists)
    dt_str = posixtostrc(posix_date, "%Y%m%d%H%M%S");
    dt_scalar = strctodt(dt_str, "%Y%m%d%H%M%S");

Conversion functions:

.. list-table::
    :widths: 30 20 20 30
    :header-rows: 1

    * - Function
      - From
      - To
      - Format system

    * - :func:`dttoposix`
      - DT scalar
      - POSIX
      - —

    * - :func:`strctoposix`
      - String
      - POSIX
      - BSD strftime

    * - :func:`posixtostrc`
      - POSIX
      - String
      - BSD strftime

    * - :func:`strctodt`
      - String
      - DT scalar
      - BSD strftime

    * - :func:`dttostrc`
      - DT scalar
      - String
      - BSD strftime

    * - :func:`strtodt`
      - String
      - DT scalar
      - GAUSS legacy

    * - :func:`dttostr`
      - DT scalar
      - String
      - GAUSS legacy


Quick Reference
--------------------------------------------

.. list-table::
    :widths: 45 55
    :header-rows: 1

    * - Task
      - How

    * - Load CSV with dates
      - ``data = loadd("file.csv");``

    * - Force date detection
      - ``loadd("f.csv", "date(col, '%YQ%q') + x")``

    * - Change display format
      - ``asDate(data, "%Y-Q%q", "Date")``

    * - Create monthly sequence
      - ``seqaPosix("2020-01-01", 1, "months", 24)``

    * - Extract year
      - ``dtYear(data, "Date")``

    * - Extract quarter
      - ``dtQuarter(data, "Date")``

    * - Filter by date range
      - ``selif(data, between(data[.,"Date"], "2020-01-01", "2020-12-31"))``

    * - Add 3 months
      - ``timeDeltaPosix(date, 3, "months")``

    * - Days between dates
      - ``timeDiffPosix(d1, d2, "days")``

    * - Lag by 1 period
      - ``lagn(data[., "x"], 1)``

    * - Growth rate
      - ``(x - lagn(x,1)) ./ lagn(x,1)``

    * - Plot time series
      - ``plotXY(data, "Close ~ Date")``

    * - Aggregate to monthly
      - ``tsAggregate(data, "M", "last")``

    * - DT scalar → POSIX
      - ``dttoposix(dt_scalar)``


.. seealso:: :doc:`/data-management/index`, :doc:`/user-guide/formula-strings`
