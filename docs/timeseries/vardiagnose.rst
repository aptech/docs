varDiagnose
===========

Purpose
-------
Run MCMC convergence diagnostics on SV-BVAR results from :func:`bvarSvFit`.

.. note::

   Conjugate BVAR draws from :func:`bvarFit` are independent (iid) — not MCMC —
   and do not require convergence diagnostics. This function is designed for the
   Gibbs sampler output of :func:`bvarSvFit`.

Format
------

.. function:: diag = varDiagnose(result)
              diag = varDiagnose(result, rhat_threshold=1.01)

   :param result: an instance of a :class:`bvarResult` or :class:`bvarSvResult` structure.
   :type result: struct

   :param rhat_threshold: Optional keyword, R-hat threshold for convergence warnings. Default = 1.05.
   :type rhat_threshold: scalar

   :param min_ess: Optional keyword, minimum ESS threshold for convergence warnings. Default = 400.
   :type min_ess: scalar

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :return diag: An instance of a :class:`diagResult` structure containing:

       .. include:: include/diagresult.rst

   :rtype diag: struct

Examples
--------

Basic Convergence Check
+++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));

    ctl = bvarSvControlCreate();
    ctl.p = 4;
    ctl.n_draws = 10000;
    ctl.n_burn = 5000;
    result = bvarSvFit(data, ctl, quiet=1);

    diag = varDiagnose(result);

    // One-bit convergence check
    if diag.converged;
        print "All checks passed.";
    else;
        print diag.n_warnings "issues found:";
        print diag.warnings;
    endif;

SV-BVAR with SSVS Diagnostics
++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));

    ctl = bvarSvControlCreate();
    ctl.p = 4;
    ctl.ssvs = 1;
    ctl.n_draws = 10000;
    ctl.n_burn = 5000;
    result = bvarSvFit(data, ctl, quiet=1);

    diag = varDiagnose(result);

    // SSVS diagnostics
    print "Inclusion probabilities:";
    print diag.ssvs_pip;

    print "Switching rates:";
    print diag.ssvs_switch_rate;

    // MH acceptance rates for SV persistence
    print "Phi acceptance rates:";
    print diag.phi_accept_rate;

Stricter Thresholds
+++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));
    result = bvarSvFit(data, quiet=1);

    // Publication-quality thresholds
    diag = varDiagnose(result, rhat_threshold=1.01, min_ess=1000);

Remarks
-------

**Diagnostics computed:**

- **Split-R-hat** (Vehtari et al. 2021): Splits the chain in half and computes
  the ratio of between-half to within-half variance. Values > 1.05 indicate
  incomplete convergence.
- **Bulk ESS**: Effective sample size for the bulk of the posterior. Low values
  (< 400) indicate high autocorrelation.
- **Tail ESS**: Effective sample size for the tails (5th/95th quantiles). Can
  be lower than bulk ESS for heavy-tailed posteriors.
- **Geweke z-test**: Compares the mean of the first 10% and last 50% of the
  chain. Values outside [-2, 2] suggest non-stationarity. Only computed for
  single-chain results.
- **SSVS diagnostics**: Posterior inclusion probabilities and indicator switching
  rates. A switching rate of 0 means the indicator never moved.
- **SV acceptance rates**: MH acceptance rates for SV persistence phi. Rates
  outside [0.15, 0.70] suggest tuning issues.

**Warnings include corrective suggestions:**

- R-hat > threshold: ``"Consider increasing n_draws or running more chains."``
- ESS < threshold: ``"Consider increasing n_draws or n_burn."``
- phi_accept < 0.15: ``"SV persistence MH acceptance rate too low. Consider adjusting sv_phi_std."``

Model
-----

**Split-R-hat** (Vehtari et al. 2021) assesses convergence by comparing within-chain
and between-chain variance on rank-normalized draws:

.. math::

   \hat{R} = \sqrt{\frac{\hat{\text{var}}^+(\theta | y)}{W}}

where :math:`\hat{\text{var}}^+` is the pooled variance estimate and :math:`W` is
the within-chain variance. Values near 1 indicate convergence; :math:`\hat{R} > 1.01`
is the recommended threshold for concern.

**Bulk ESS** estimates the number of independent draws the chain is worth for
central tendency (posterior mean, median). Computed via Geyer's initial monotone
sequence estimator with rank normalization.

**Tail ESS** estimates independent draws for tail quantiles (5th, 95th percentiles)
by applying the ESS estimator to folded draws :math:`|x - \text{median}(x)|`.
References
----------

- Vehtari, A., A. Gelman, D. Simpson, B. Carpenter, and P.C. Burkner (2021). "Rank-normalization, folding, and localization: An improved R-hat for assessing convergence of MCMC." *Bayesian Analysis*, 16(2), 667-718.
- Geweke, J. (1992). "Evaluating the accuracy of sampling-based approaches to the calculation of posterior moments." In *Bayesian Statistics 4*, 169-193.
Library
-------
timeseries

Source
------
diagnostics.src

.. seealso:: Functions :func:`varDiagnoseMulti`, :func:`varDiagnosePrint`, :func:`bvarSvFit`
