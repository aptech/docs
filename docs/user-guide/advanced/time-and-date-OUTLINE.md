# Time and Date — Chapter Outline

## Design Principles

1. **Dataframe-first.** Lead with `loadd` auto-detection and date columns.
   The reader's first experience should be: load a CSV, dates just work.
2. **Workflow-driven** (pandas approach). Follow the natural sequence:
   load → inspect → extract components → filter → compute → plot → aggregate.
3. **Conceptual anchor** (Stata approach). Early section: "dates are POSIX
   numbers under the hood." This explains why arithmetic works and why
   `selif(data, data[., "Date"] .< "2018")` is valid.
4. **Legacy clearly labeled** (MATLAB approach). DT scalars, DTV vectors,
   4x1 date vectors go in a final reference section, not mixed in.
5. **Econometric connection.** Show dates in the context of time series
   analysis — the actual reason our users need dates.

## Target Audience

Econometricians and financial analysts who:
- Have CSV/Excel data with date columns
- Need to load, filter, transform, and plot time series
- May be coming from Stata (`%td`, `tsset`), R/pandas (`as.Date`, `DatetimeIndex`), or MATLAB (`datetime`)

---

## Outline

### 1. Introduction (short)
- What this page covers
- R/Python/Stata equivalence note (like other pages)
- Key idea: GAUSS stores dates as POSIX seconds internally; display
  format controls how they appear

### 2. Loading Data with Dates
- `loadd("file.csv")` — auto-detection (the happy path, ~30 formats)
- Verifying date detection: `print head(data)`, `getColTypes`
- When auto-detection fails: the `date()` formula keyword
  - `loadd("file.csv", "date(mydate) + x1 + x2")`
  - Specifying format explicitly: `date($mydate, '%d/%m/%Y')`
- Loading from Excel (same `loadd` behavior)
- Example: load a real-world dataset, show dates display correctly

### 3. How Dates Work Internally
- All date columns store POSIX seconds (seconds since Jan 1, 1970 UTC)
- Display format is separate from storage (the Stata insight)
- `asDate` — mark a numeric column as date, or change display format
- `setColDateFormats` — set display format for existing date columns
- `getColDateFormats` — query current display format
- Default display: `%Y-%m-%d`; quarterly: `%Y-Q%q`; monthly: `%Y-%m`
- Table of common format specifiers (compact — just the top 10-15 most
  used, not the full BSD strftime dump)

### 4. Creating Dates
- From strings: `asDate("2024-03-15")`, `strctoposix("2024-03-15", "%Y-%m-%d")`
- Date sequences: `seqaPosix("2020-01-01", 1, "months", 24)` — monthly
  sequence starting Jan 2020, 24 periods
- Building a date column for a dataframe: create sequence, combine with data
- From components: (brief mention of `dtdate`, `dtday` for legacy code)

### 5. Extracting Date Components
- The `dt*` family — present as a single scannable table:
  `dtYear`, `dtMonth`, `dtQuarter`, `dtDayofMonth`, `dtDayofWeek`,
  `dtDayofYear`, `dtWeek`, `dtHour`, `dtMinute`, `dtSecond`,
  `dtMonthName`, `dtDayName`
- Example: add a "Quarter" column to a dataframe
  `data = dfaddcol(data, "Quarter", dtQuarter(data, "Date"))`
- Example: filter to weekdays only
  `data = selif(data, dtDayofWeek(data, "Date") .> 0 .and dtDayofWeek(data, "Date") .< 6)`

### 6. Filtering and Subsetting by Date
- String comparison on date columns:
  `selif(data, data[., "Date"] .>= "2020-01-01" .and data[., "Date"] .< "2021-01-01")`
- The `between` function (date-aware):
  `mask = between(data[., "Date"], "2020-01-01", "2020-12-31")`
- Partial date strings work: `.< "2020"` means before Jan 1, 2020

### 7. Date Arithmetic
- Adding time: `timeDeltaPosix(date, 3, "months")` — add 3 months
- Subtracting time: `timeDeltaPosix(date, -7, "days")` — go back a week
- Differences: `timeDiffPosix(date1, date2, "days")` — days between dates
- Supported units table: years, months, days, hours, seconds
  (note: "months" for delta but not for diff)
- Example: compute holding period in days between buy and sell dates

### 8. Plotting Time Series
- The simple case: `plotXY(data, "Date ~ Price")` — auto-detects dates,
  auto-routes to time series plot
- `plotTS` for evenly-spaced data (frequency-based: 1=yearly, 4=quarterly,
  12=monthly)
- `plotTSHF` for irregularly-spaced or high-frequency data
- Customizing date axes: `plotSetXTicLabel`, `plotSetXTicInterval`
- Example: load stock prices, plot with custom date formatting

### 9. Frequency Conversion
- `tsAggregate` — downsample time series data
  - Frequencies: "D", "M", "Q", "Y" (and "H", "N", "S" for intraday)
  - Methods: "last", "mean", "sum", "lastBD", etc.
- Example: convert daily stock data to monthly (last trading day)
- Example: convert monthly GDP to quarterly (sum or mean)

### 10. Converting Between Formats
- String ↔ POSIX: `strctoposix` / `posixtostrc`
- String ↔ DT: `strctodt` / `dttostrc`
- DT → POSIX: `dttoposix`
- When you need each (brief guidance, not exhaustive)

### 11. Format Specifier Reference
- Compact table of BSD strftime specifiers (the important ones)
- Note the GAUSS extension: `%q` for quarter
- GAUSS legacy format codes (YYYY, MO, DD, etc.) — used by `plotSetXTicLabel`

### 12. Legacy Date Representations
- Brief section clearly marked as legacy
- DT scalars: what they are, when you'll encounter them
- DTV vectors: what they are
- 4x1 date/time vectors: what they are
- Migration guidance: use `dttoposix` to convert DT → POSIX
- Trading day functions: `elapsedTradingDays`, `getNextTradingDay`,
  `getNextWeekDay` (note: DT scalar input, NYSE calendar through 2004)

### 13. Quick Reference
- Task → Function table (same format as other pages)
- Load with dates, create sequence, extract year/month/quarter,
  filter by date range, add months, compute difference, plot,
  change display format, aggregate to monthly

---

## What We're Deliberately NOT Covering

- **Time zones** — GAUSS has no built-in TZ conversion. Don't document
  what doesn't exist; would be misleading.
- **Business calendars beyond NYSE** — the existing functions are
  limited and somewhat outdated. Mention them in legacy section,
  don't promote as a feature.
- **Full BSD strftime table** — the legacy docs dump all 30+ specifiers.
  We'll include the top 15 and link to a reference for the rest.
- **DTV vector internals** — almost nobody uses these. Brief mention only.
- **Timed iterations with `hsec`** — this is a benchmarking pattern,
  not really a "dates" topic. Could go in a future performance page.

## Open Questions

1. Should `tsAggregate` go here or in data-management? It's deeply
   date-related but also a data transformation. (Leaning: here, since
   frequency conversion is core to time series dates.)
2. Should we include a "Coming from Stata/R" migration sidebar that
   maps their date concepts to GAUSS? (Leaning: yes, brief note box.)
3. The `plotXY` auto-routing to `plotTSHF` is a great feature — should
   we lead the plotting section with it? (Leaning: yes, it's the
   simplest path.)
