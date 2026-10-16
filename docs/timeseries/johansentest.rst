johansenTest
============

Purpose
-------
Test for the number of cointegrating relations among several series with Johansen's trace and maximum-eigenvalue tests.

Format
------

.. function:: jt = johansenTest(y)
              jt = johansenTest(y, p=1, det_case=3, test_type="trace", season=0, quiet=0)

   :param y: the series in levels. If a dataframe, one date-typed column is removed before estimation and the remaining column names label the output; two or more date-typed columns are refused. Dates are not stored in the result.
   :type y: TxM matrix or dataframe

   :param p: Optional keyword, lag order of the model written in levels. The test regression uses ``p-1`` lagged differences. Default = 1.
   :type p: scalar

   :param det_case: Optional keyword, deterministic terms, 1 to 5 (see Remarks). Default = 3.
   :type det_case: scalar

   :param test_type: Optional keyword, the statistic that sets ``jt.rank``: ``"trace"`` or ``"max"``. Both tables are always computed and printed. Default = ``"trace"``.
   :type test_type: string

   :param season: Optional keyword, 0 for no seasonal dummies; otherwise a whole number giving the number of seasons per year, at least 2 (4 for quarterly data, 12 for monthly). Adds ``season-1`` centered seasonal dummies. 1 is refused. Default = 0.
   :type season: scalar

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :return jt: An instance of a :class:`johansenResult` structure containing:

       .. include:: include/johansenresult.rst

   :rtype jt: struct

Examples
--------

::

    new;
    library timeseries;

    // Canadian employment, productivity, real wage and unemployment, 1980Q1-2000Q4
    fname = getGAUSSHome("pkgs/timeseries/examples/data/canada.csv");
    y = loadd(fname);

    struct johansenResult jt;
    jt = johansenTest(y, p=2, det_case=3);

The printout:

::

    Johansen Cointegration Test
    ================================================================================
    Det. case 3: Unrestricted constant
    Lags: 2        Variables: 4        Obs: 82 (84 rows)

    H0: rank      Eigenvalue    Trace Stat           10%            5%            1%       P value
    ----------------------------------------------------------------------------------------------
    r <= 0            0.4386       75.9321       44.4932       47.8564       54.6847       <0.0001
    r <= 1            0.2128       28.5952       27.0660       29.7976       35.4657        0.0683
    r <= 2            0.1001        8.9711       13.4295       15.4948       19.9396        0.3681
    r <= 3            0.0039        0.3227        2.7055        3.8415        6.6349        0.5700

    H0: rank      Eigenvalue      Max Stat           10%            5%            1%       P value
    ----------------------------------------------------------------------------------------------
    r = 0             0.4386       47.3369       25.1238       27.5856       32.7171       <0.0001
    r = 1             0.2128       19.6241       18.8925       21.1323       25.8613        0.0802
    r = 2             0.1001        8.6483       12.2969       14.2644       18.5193        0.3166
    r = 3             0.0039        0.3227        2.7055        3.8415        6.6349        0.5700

    Selected rank (trace, 5%): 1

The trace statistic rejects rank 0 at the 5% level (75.93 > 47.86) and does
not reject rank 1 (28.60 < 29.80), so ``jt.rank`` is 1. Pass it to
:func:`vecmFit`:

::

    struct vecmResult vr;
    vr = vecmFit(y, jt.rank, p=2, det_case=3);

Remarks
-------

**Statistics.** With :math:`\hat\lambda_1 > \dots > \hat\lambda_M` the
eigenvalues of Johansen's reduced-rank regression and :math:`T` the number of
rows used in estimation (the rows of *y* minus *p*),

.. math::

   \text{trace}(r) = -T \sum_{i=r+1}^{M} \ln(1-\hat\lambda_i),
   \qquad
   \lambda_{\max}(r) = -T \ln(1-\hat\lambda_{r+1}).

The trace statistic tests rank at most *r* against a larger rank. The
maximum-eigenvalue statistic tests rank *r* against rank *r+1*.

**Selected rank.** ``jt.rank`` is the first *r*, starting from 0, whose
statistic does not exceed its 5% critical value; *test_type* chooses the
statistic. If every hypothesis is rejected, the rank is *M* (the series are
stationary in levels). The printed statistics are the ones compared with the
critical values: no small-sample adjustment is applied. To apply the
adjustment of Reimers (1992) yourself, multiply the statistics by
:math:`(T - Mp)/T`.

**Deterministic terms.**

=== ============================================================================
1   No constant and no trend.
2   A constant inside the cointegrating relations only.
3   An unrestricted constant: the levels can have linear trends. (Default)
4   An unrestricted constant and a linear trend inside the cointegrating relations.
5   An unrestricted constant and an unrestricted linear trend.
=== ============================================================================

In case 4 the trend inside the cointegrating relations equals the row number
of the lagged levels: in the equation for data row *t* it is *t-1*, with the
first data row numbered 1. In case 5 the unrestricted trend is the data row
number *t* itself.

**Seasonal dummies.** The seasonal dummies are centered: a column equals
:math:`1 - 1/s` in its own season and :math:`-1/s` otherwise, with *s* =
*season*. Data row *i* is in season :math:`((i-1) \bmod s) + 1`. Centered
dummies sum to zero over a full year, so they do not add a trend to the
levels, and the critical values of the chosen case are used unchanged.

**Critical values.** The 10%, 5% and 1% critical values are from MacKinnon,
Haug and Michelis (1999), computed with the authors' program ``johval``
and printed to four decimals, for all five cases up to 12 variables. The tables
are indexed by *M - r*. With more than 12 series, the rows whose *M - r* is
above 12 hold missing critical values. The first row
(*r* = 0) is one of them, so ``jt.rank`` is a missing value. The statistics
and the other critical values are still returned.

**Observations.** ``Obs`` is the number of rows used in estimation, the rows
of *y* minus *p*; the total number of rows follows in parentheses.

**p-values.** ``jt.trace_pval`` and ``jt.max_eigen_pval`` hold the asymptotic
p-values of the trace and maximum eigenvalue statistics, in the same order as
the statistics. They are computed from the authors' tables of 221 quantiles of
each limiting distribution by the local approximation of MacKinnon (1996) and
MacKinnon, Haug and Michelis (1999): a weighted cubic fit of the inverse normal
probability on the eleven quantiles nearest the statistic. The tables cover
p-values from 0.0001 to 0.9999; beyond them the bound is returned and printed
as ``<0.0001`` or ``>0.9999``. With more than 12 variables all p-values are missing values.

**Source of the tables.** The critical values and p-values use the tables of
MacKinnon, Haug and Michelis (1999), published with the paper in the Journal
of Applied Econometrics data archive (DOI 10.15456/jae.2022314.0707472522).
They are used with credit to the authors.

**Data requirements.** The number of rows used in estimation, *T - p*, must
be at least *k + M*, the same count as in :func:`vecmFit`; with fewer rows
the test is refused, because the largest eigenvalues equal one and the
statistics are infinite.

References
----------

- Johansen, S. (1995). *Likelihood-Based Inference in Cointegrated Vector Autoregressive Models*. Oxford University Press.
- MacKinnon, J.G. (1996). "Numerical distribution functions for unit root and cointegration tests." *Journal of Applied Econometrics*, 11(6), 601-618.
- MacKinnon, J.G., A.A. Haug and L. Michelis (1999). "Numerical distribution functions of likelihood ratio tests for cointegration." *Journal of Applied Econometrics*, 14(5), 563-577.
- Reimers, H.-E. (1992). "Comparisons of tests for multivariate cointegration." *Statistical Papers*, 33, 335-359.

Library
-------
timeseries

Source
------
tests.src

.. seealso:: Functions :func:`vecmFit`, :func:`vecmAuto`, :func:`vecmBootstrap`, :func:`engleGrangerTest`
