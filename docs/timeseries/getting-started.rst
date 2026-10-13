.. _getting-started:

Getting Started
===============

This page takes four quarterly US series through a complete forecasting
exercise: choose the lags, fit a Bayesian VAR, check it on quarters it had not
seen, and forecast two years ahead with bands. The script takes about 20
seconds to run.

It is the short version of the workflow example
``examples/workflows/bvar_first_forecast.e`` in the ``timeseries`` package
folder; the guide next to it, ``bvar_first_forecast.md``, explains every step
at length.

The Script
----------

::

    new;
    library timeseries;

    // Step 1: load the data and keep 1960Q1-2019Q4.
    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv"));
    y = selif(data, data[., "date"] .>= "1960-01-01" .and data[., "date"] .<= "2019-10-01");
    series = y[., "gdp_growth" "inflation" "unemployment" "fed_funds"];

    // Step 2: choose the number of lags.
    lags = varLagSelect(series, 8);

    // Step 3: fit the Bayesian VAR. The prior centres each variable's own
    // first lag at 0 for GDP growth and at 1 for the three persistent series.
    bvar = bvarFit(y, p=lags.best_p, lag1_prior_mean=0|1|1|1, overall_tightness=0.2, quiet=1);
    call varFitInspect(bvar, name="BVAR(" $+ ntos(lags.best_p) $+ "), Minnesota prior");

    // Step 4: check it on quarters it had not seen, against a least-squares VAR.
    ols = varFit(y, p=lags.best_p, quiet=1);
    models = forecastModel(ols, name="VAR") | forecastModel(bvar, name="BVAR");
    fe = forecastEval(y, models, target="inflation", train_end="1984-Q4", h=4, benchmark="VAR", seed=42);

    // Step 5: forecast two years ahead and draw the fan chart.
    fc = bvarForecast(bvar, 8, seed=42);
    plotForecast(bvar, fc, history=40, output_dir=".");

The rest of this page goes through the five steps and what each prints.

Step 1: The Data
----------------

``us_macro_fred_qd.csv`` holds quarterly US data from the February 2026
vintage of the FRED-QD database of the Federal Reserve Bank of St. Louis. The
script keeps the 240 quarters from 1960Q1 to 2019Q4 and leaves the pandemic
years out.

.. list-table::
   :widths: 20 50 30
   :header-rows: 1

   * - Column
     - Meaning
     - Unit
   * - ``gdp_growth``
     - Growth of real GDP on the previous quarter
     - percent, annual rate
   * - ``inflation``
     - Change in the consumer price index on the previous quarter
     - percent, annual rate
   * - ``unemployment``
     - Unemployment rate
     - percent
   * - ``fed_funds``
     - Federal funds rate
     - percent

Keep the data as a dataframe with its ``date`` column: the functions below
use the column names in their tables and the dates in their forecasts.

Step 2: Choose the Lags
-----------------------

:func:`varLagSelect` fits a VAR with one to eight lags and compares them::

    VAR lag selection
    ================================================================================
    Selected lags     5 (smallest AIC)
    Smaller is better; * marks the smallest value of each criterion.

    Lags        AIC       BIC         HQ          FPE
    -------------------------------------------------
    1     -0.108     0.189      0.012     0.897657
    2     -0.496     0.039*    -0.280     0.609114
    3     -0.670     0.103     -0.358*    0.512031
    4     -0.636     0.374     -0.229     0.529991
    5     -0.720*    0.528     -0.216     0.487938*
    6     -0.720     0.766     -0.120     0.488625
    7     -0.711     1.013     -0.016     0.493905
    8     -0.654     1.307      0.137     0.524139

AIC picks five lags, BIC two and HQ three. The script uses AIC's five
(``lags.best_p``). With four variables that is 21 coefficients per equation,
which is where a prior starts to help.

Step 3: Fit the Bayesian VAR
----------------------------

A Bayesian VAR adds a prior that pulls the coefficients toward a simple model
and lets the data pull them away where the evidence is strong. The Minnesota
prior centres each variable's coefficient on its own first lag, and every
other coefficient on zero. ``lag1_prior_mean = 0|1|1|1`` sets that centre to 0
for GDP growth, which moves around a stable mean, and to 1 (a random walk)
for inflation, unemployment and the funds rate, which drift.
``overall_tightness = 0.2`` sets how hard the prior pulls; it is the common
default.

``varFitInspect`` prints a summary of the fit::

    BVAR(5), Minnesota prior
    ================================================================================
    Sample:                1960Q1-2019Q4    Lags:                                  5
    Observations:                    240    Used after lags:                     235
    Intercept:                       yes    Regressors:                            0
    Coefficients:        21 per equation    Largest root:                     0.9614
    Stable:                          yes    Overall tightness:                   0.2
    Posterior draws:               5,000    Exogenous scale:                       1
    Seed:                             42

    Largest root and stability refer to the posterior-mean coefficients.

A largest root below 1 means the fitted model is stable: its forecasts settle
down instead of exploding. To see the coefficient tables, call
:func:`bvarFit` without ``quiet=1``.

Step 4: Check It on Quarters It Had Not Seen
--------------------------------------------

:func:`forecastEval` stands at every quarter from 1984Q4 to 2019Q3, refits
each model on the data up to that quarter, forecasts the next four quarters,
and compares the forecasts with what happened. Here the BVAR is compared
with a least-squares VAR with the same five lags, for inflation::

    Pseudo out-of-sample forecast evaluation: inflation
    ================================================================================
    Estimation samples: 1960Q1-1984Q4 (first), expanding to 1960Q1-2019Q3; 140 start dates
    Models refitted at every start date; lag order and prior settings held as given.
    BVAR forecasts scored at the mean of the predictive draws.
    RMSE relative to VAR (below 1 is better).
    Diebold-Mariano test vs VAR: * 10%  ** 5%  *** 1%

    Horizon  VAR RMSE  BVAR  Obs
    ----------------------------
    1           2.054  0.97  140
    2           2.368  0.95  139
    3           2.383  0.95  138
    4           2.408  0.95  137

The BVAR column is the BVAR's root mean squared error divided by the VAR's:
0.95 means errors 5% smaller. The prior helps at every horizon, by about 3%
one quarter ahead and about 5% beyond. No star follows these numbers, so the
Diebold-Mariano test does not separate the two models at the 10% level: the
gain is steady but small next to the noise in 140 overlapping forecasts.

The function prints two more tables for each variable: the average error
(forecast minus outcome), and how often the outcome fell inside the 68% and
90% bands. Leave out ``target=`` to score all four variables, and add more
models with ``|``; ``"AR(bic)"`` adds a one-variable autoregression as a
yardstick.

Step 5: Forecast
----------------

:func:`bvarForecast` simulates 5,000 future paths from the fitted model and
reports their medians and bands::

    BVAR forecast, 8 quarters ahead
    ================================================================================
    Point: predictive median of 5,000 simulated paths.
    Band: 68% equal-tailed quantiles of the same paths.

    Period  gdp_growth  Lower 68%  Upper 68%  inflation  Lower 68%  Upper 68%
    -------------------------------------------------------------------------
    2020Q1       3.156      0.307      6.031      2.269      0.488      4.129
    2020Q2       3.157      0.243      6.069      2.195      0.017      4.419
    2020Q3       3.053      0.061      6.044      2.568      0.064      4.819
    2020Q4       2.699     -0.307      5.738      2.561     -0.007      4.969
    2021Q1       2.706     -0.544      5.864      2.628     -0.087      5.260
    2021Q2       2.679     -0.419      5.851      2.717     -0.090      5.577
    2021Q3       2.728     -0.450      5.926      2.829     -0.122      5.667
    2021Q4       2.685     -0.524      5.839      2.790     -0.120      5.769

    Period  unemployment  Lower 68%  Upper 68%  fed_funds  Lower 68%  Upper 68%
    ---------------------------------------------------------------------------
    2020Q1         3.606      3.384      3.834      1.714      0.907      2.525
    2020Q2         3.618      3.229      4.021      1.904      0.703      3.120
    2020Q3         3.662      3.095      4.224      2.113      0.569      3.621
    2020Q4         3.706      2.997      4.405      2.204      0.340      4.008
    2021Q1         3.759      2.930      4.593      2.342      0.166      4.364
    2021Q2         3.846      2.887      4.754      2.413      0.025      4.706
    2021Q3         3.918      2.874      4.941      2.523     -0.134      5.004
    2021Q4         3.966      2.885      5.098      2.557     -0.210      5.268

The bands include both sources of uncertainty: the coefficients are not known
exactly, and future shocks are random. They are wide: two years ahead the 68%
band for GDP growth runs from -0.5% to 5.8%. These are forecasts made with
data to the end of 2019; they know nothing of 2020.

:func:`plotForecast` writes the fan chart ``forecast.png`` to the working
directory, with the last ten years of data and the 68% and 90% bands.

The paths are simulated, so another ``seed`` gives slightly different
numbers; more paths (``n_draws`` in :func:`bvarFit`) make them steadier.

What to Change for Your Data
----------------------------

- Replace the file, the date range and the column list in step 1.
- Give each variable a prior centre in step 3: 1 for series that drift
  (levels, rates), 0 for growth rates.
- Set the first start date (``train_end``), the horizon (``h``) and the
  variable to score (``target``) in step 4.

What's Next
-----------

.. list-table::
   :widths: 30 70

   * - **The full workflow**
     - ``examples/workflows/bvar_first_forecast.e`` and its guide add a look at the data, a third model, residual checks with :func:`varDiagnostics` and a discussion of every table.
   * - **How much shrinkage**
     - :func:`bvarPriorSelect` chooses the overall tightness by marginal likelihood; see ``examples/workflows/bvar_shrinkage_choice.e``.
   * - **Scenarios**
     - "What if the policy rate follows this path?" :func:`condForecast` and ``examples/workflows/conditional_scenarios.e``.
   * - **Structural shocks**
     - :func:`irfCompute` and :func:`signRestrictions`; see ``examples/workflows/svar_monetary_policy.e``.
   * - **One call**
     - :func:`bvarMacroForecast` chooses the lags and the tightness, fits and forecasts in one call.
   * - **Changing volatility**
     - :func:`bvarSvFit` fits a BVAR with stochastic volatility.
   * - **One series**
     - :func:`autoArima` or :func:`arimaFit`; see :ref:`getting-started-arima`.
   * - **Choosing a model**
     - See the :ref:`choosing-a-var-model` decision tree.
