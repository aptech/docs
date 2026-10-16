vecmAuto
========

Purpose
-------
Choose the cointegrating rank with the Johansen trace test and estimate the VECM at that rank, in one call.

Format
------

.. function:: vr = vecmAuto(y)
              vr = vecmAuto(y, p=1, det_case=3, season=0, quiet=0, freq="")

   :param y: the series in levels. If a dataframe, one date-typed column is removed before estimation and the remaining column names label the output; two or more date-typed columns are refused. The input-row dates are stored in ``vr.dates`` and the resolved frequency in ``vr.freq``. There is no ``dates=`` keyword.
   :type y: TxM matrix or dataframe

   :param p: Optional keyword, lag order of the model written in levels. It is used as given; :func:`vecmAuto` does not choose the lag order. Default = 1.
   :type p: scalar

   :param det_case: Optional keyword, deterministic terms, 1 to 5 (see :func:`vecmFit`). Default = 3.
   :type det_case: scalar

   :param season: Optional keyword, 0 for no seasonal dummies; otherwise a whole number giving the number of seasons per year, at least 2 (4 for quarterly data, 12 for monthly). Adds ``season-1`` centered seasonal dummies. 1 is refused. Default = 0.
   :type season: scalar

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :param freq: Optional keyword, calendar frequency: ``"annual"``, ``"quarterly"`` (or ``"q"``), ``"monthly"``, ``"weekly"`` or ``"daily"``. Default = ``""``, inferred from a date column. Irregular spacing or fewer than three dates requires an explicit frequency. A nonempty frequency without a date column is refused.
   :type freq: string

   :return vr: An instance of a :class:`vecmResult` structure, the same as :func:`vecmFit` returns at the selected rank:

       .. include:: include/vecmresult.rst

   :rtype vr: struct

Dates and seasons
-----------------

An undated fit has empty ``dates`` and ``freq`` members. A dated fit keeps
one date for every input row, including the rows used only for lags.
:func:`vecmForecast` extends that index and prints period labels.
Dates must be finite and strictly increasing even when ``freq`` is supplied.

Seasonal dummies use row order: data row 1 is season 1 and row *i* is season
``mod(i-1,season)+1``. Calendar dates and ``freq`` do not change this rule.

Examples
--------

::

    new;
    library timeseries;

    // Canadian employment, productivity, real wage and unemployment, 1980Q1-2000Q4
    fname = getGAUSSHome("pkgs/timeseries/examples/data/canada.csv");
    y = loadd(fname);

    struct vecmResult vr;
    vr = vecmAuto(y, p=2, det_case=3);

    print "Selected rank: " vr.r;

The trace test selects rank 1 for these data, so the result is the same as
``vecmFit(y, 1, p=2, det_case=3)``.

Remarks
-------

:func:`vecmAuto` runs :func:`johansenTest` with the same *p*, *det_case* and
*season*, takes the rank selected by the trace statistic at the 5% level, and
calls :func:`vecmFit` with that rank. It fits exactly the rank the test
selects:

- If the test selects rank 0 (no cointegration), :func:`vecmAuto` stops with
  an error, because a VECM needs rank at least 1. Fit a VAR in differences
  as described below, or call :func:`vecmFit` with a rank you choose.
- If the sample is too short for the full-rank model (fewer than *k + M* rows
  in estimation, see :func:`vecmFit`), :func:`vecmAuto` stops with an error
  before running the test.
- If critical values are not tabulated for this many series (more than 12),
  :func:`vecmAuto` stops with an error. Call :func:`vecmFit` with a rank you
  choose.
- If the test selects full rank (*r* = *M*), the fit is kept and a note says
  that it is a VAR in levels written in error-correction form.

When *quiet* is 0, the fitted model prints as :func:`vecmFit` does, with
labelled beta and equation tables and coefficient standard errors. The
returned structure has the same standard-error members.

**Rank zero.** Use only the series without the date column in *y* before
forming differences; the automatic removal inside :func:`vecmAuto` does not
change the dataframe in your program. With *p* at least 2, form the first
differences and fit ``p-1`` lags. For Case III (the default) or IV, the call is::

    dy = y[2:rows(y),.] - y[1:rows(y)-1,.];
    struct varResult diff_fit;
    diff_fit = varFit(dy, p=p-1, const=1, trend=0);

Here *p* is the levels lag order supplied to :func:`vecmAuto`. In Cases I
and II use ``const=0, trend=0``: a restricted constant disappears at rank
zero. In Case V use ``const=1, trend=1``. The trend in *dy* starts one
period later in the original data, which its unrestricted constant absorbs.
To retain the maximum-likelihood covariance convention, also pass
``resid_cov="ml"``; :func:`varFit` otherwise uses its degrees-of-freedom divisor.

If *season* was nonzero, also pass ``xreg=season_diff`` with the same centered
seasonal columns for original data rows 2 to T. Constructing these columns
before dropping the first row preserves the seasonal alignment::

    season_diff = zeros(rows(y), season-1);
    for season_idx (1, season-1, 1);
        season_diff[.,season_idx] = ((seqa(0,1,rows(y)) % season) .== (season_idx-1)) - 1/season;
    endfor;
    season_diff = season_diff[2:rows(y),.];
    diff_fit = varFit(dy, p=p-1, const=1, trend=0, xreg=season_diff);

Use the same ``const`` and ``trend`` choices above for the selected case.
With *p* = 1 there are no lagged differences, and :func:`varFit` does not fit
zero lags. For Cases III and IV without seasonals, fit the mean of the
differences, ``meanc(dy)'``. Cases I and II have zero fitted mean; Case V
requires a regression of the differences on a constant and trend. With
seasonals, regress the differences on the chosen deterministic terms and
centered seasonal columns.

To see the test table, or to select the rank with the maximum-eigenvalue
statistic, call :func:`johansenTest` yourself and pass its rank to
:func:`vecmFit`.

Library
-------
timeseries

Source
------
vecm.src

.. seealso:: Functions :func:`johansenTest`, :func:`vecmFit`, :func:`vecmBootstrap`
