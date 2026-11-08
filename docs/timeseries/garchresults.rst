garchResults
============

Purpose
-------
Print the summary of a fitted GARCH or GJR-GARCH model again.

Format
------

.. function:: garchResults(result)

   :param result: a fit returned by :func:`garchFit`.
   :type result: struct

Examples
--------

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/dmbp.csv");
    dm = loadd(fname, "return_pct");

    // Fit without the summary, use a result, then print the summary
    struct garchResult fit;
    fit = garchFit(dm, garch=1, arch=1, quiet=1);
    print "Persistence: " fit.persistence;
    garchResults(fit);

::

    Persistence:       0.95910770
    ================================================================================
    GARCH Family Model Results
    ================================================================================
    Model:        GARCH(1,0,1)
    Mean model:   constant_mean
    Distribution: normal
    Observations: 1974
    Log likelihood: -1106.61
    AIC: 2221.22    BIC: 2243.57

    Parameters on the original data scale

           Parameter         Estimate       SE_Hessian        SE_Robust  P_Robust_Normal Lower_95_Robust_ Upper_95_Robust_
                  mu    -0.0061904139     0.0084621193     0.0091893537       0.50053346     -0.024201216      0.011820388
               omega      0.010761404     0.0028527145     0.0064931937      0.097451542    -0.0019650214      0.023487830
              alpha1       0.15313409      0.026522838      0.053531721     0.0042280922      0.048213839       0.25805433
               beta1       0.80597362      0.033552706      0.072461499    9.7190780e-29       0.66395169       0.94799555
    Inference: available; Hessian and unadjusted score sandwich; robust normal p-values and limits
    Initialization: sample_variance_presample
    P-values and limits: robust asymptotic normal, level=0.95

    Optimizer: lbfgsb_tight_repolish; projected_gradient_at_or_below_pgtol
    Iterations: 13; function evaluations: 15
    Projected-gradient norm: 4.01748e-05 (requested 0.0001)
    Persistence: 0.959108 (admissible)

Remarks
-------

The summary is the one :func:`garchFit` prints when *quiet* is 0. Its lines:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Line
     - Contents
   * - Model
     - The model with its GARCH, leverage and ARCH orders: GARCH(1,0,1) is a
       GARCH(1,1), GJR-GARCH(1,1,1) the GJR model.
   * - Mean model, Mean terms
     - ``constant_mean`` or ``zero_mean``; with AR terms or regressors, how
       many of each.
   * - AR inverse roots
     - With AR terms: the largest modulus, and whether the AR part is
       stationary (below 1).
   * - Distribution, Observations
     - The error distribution and the number of observations in the
       likelihood. Below 100 a warning line follows.
   * - Log likelihood, AIC, BIC
     - Fit statistics; see *result.aic* and *result.bic* on the
       :func:`garchFit` page.
   * - Parameter table
     - *result.parameter_table*: estimate, Hessian and robust standard
       errors (and OPG with ``covariance="opg"``), robust p-value and limits.
       The printed column names are cut to 16 characters.
   * - Inference
     - *result.standard_error_status* and *result.inference_message*.
   * - Initialization
     - The start-up rule of the fit.
   * - Optimizer, Iterations, Projected-gradient norm
     - How the optimizer finished, the work it did, and the gradient norm
       it reached against the tolerance requested (*ctl.tol*).
   * - Persistence
     - *alpha* + *beta* (plus *gamma*/2 for GJR), ``admissible`` below 1 or
       ``boundary`` within 1e-6 of 1.

A fit that did not converge (status 2) ends with a warning that the
estimates are the best finite run and have no standard errors. For a fit
refused with ``on_error="return"``, :func:`garchResults` prints
``GARCH Family Model: no fit`` and the message, for example:

::

    GARCH Family Model: no fit
    garchFit: the series has 10 observations; this model needs at least 20 (5 per estimated parameter, 4 parameters).

Library
-------
timeseries

Source
------
garch.src

.. seealso:: Functions :func:`garchFit`, :func:`garchDiagnostics`
