Density Forecast Evaluation
===========================

This guide walks through a complete density forecast evaluation workflow:
estimate multiple models, generate density forecasts, score them with
proper scoring rules, and compare using statistical tests.

.. contents:: On this page
   :local:

Quick Example
-------------

::

    new;
    library timeseries;

    // Load data
    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    y = loadd(fname, "gdp_growth + cpi_inflation + fed_funds");

    // Estimate two competing models
    r1 = bvarFit(y, p=2);
    r2 = bvarFit(y, p=4);

    // Generate density forecasts (h=4 quarters ahead)
    fc1 = bvarForecast(r1, 4);
    fc2 = bvarForecast(r2, 4);

    // Score against actuals using CRPS
    actual = y[rows(y)-3:rows(y), .];  // last 4 observations
    crps1 = fcScore(fc1, actual, "crps");
    crps2 = fcScore(fc2, actual, "crps");

    print "CRPS (lower is better):";
    print "  VAR(2):" crps1;
    print "  VAR(4):" crps2;

Step-by-Step Workflow
---------------------

**Step 1: Estimate competing models**

Any combination of models that produce density forecasts:

- ``bvarFit`` → conjugate BVAR (iid draws)
- ``bvarSvFit`` → SV-BVAR (Gibbs draws)
- ``arimaFit`` → ARIMA/ETS (ML + simulation)

**Step 2: Generate density forecasts**

Each model's forecast function returns draws from the predictive distribution:

- ``bvarForecast`` → point + interval from conjugate posterior
- ``bvarSvForecast`` → density with volatility propagation
- ``arimaForecast`` → point + interval from ML

**Step 3: Score with proper scoring rules**

Use :func:`fcScore` with one of:

- ``"crps"`` — Continuous Ranked Probability Score (lower is better)
- ``"logscore"`` — Log Predictive Score (higher is better)
- ``"energy"`` — Energy Score for multivariate forecasts (lower is better)

**Step 4: Test for significant differences**

- :func:`dmTest` — Diebold-Mariano test (pairwise comparison)
- :func:`cwTest` — Clark-West test (nested model comparison)
- :func:`mcsTest` — Model Confidence Set (select best subset from many models)

**Step 5: Calibration diagnostics**

- :func:`pitTest` — Probability Integral Transform test for calibration
- :func:`pitHistogram` — Visual PIT histogram (should be uniform for well-calibrated forecasts)

See Also
--------

- :func:`fcScore` — Scoring rule computation
- :func:`dmTest` — Diebold-Mariano pairwise test
- :func:`cwTest` — Clark-West nested model test
- :func:`mcsTest` — Hansen-Lunde-Nason Model Confidence Set
- :func:`pitTest` — PIT calibration test
- :func:`pitHistogram` — PIT histogram plot
- :doc:`getting-started` — Basic BVAR tutorial
