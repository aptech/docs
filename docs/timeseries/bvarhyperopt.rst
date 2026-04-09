bvarHyperopt
============

Purpose
-------
Optimize Minnesota prior hyperparameters by maximizing the log marginal likelihood.

Format
------

.. function:: ho = bvarHyperopt(y)
              ho = bvarHyperopt(y, p=4)
              ho = bvarHyperopt(y, p=4, ctl=ctl)

   :param y: endogenous variables.
   :type y: TxM matrix or dataframe

   :param p: Optional keyword, lag order. Default = 1.
   :type p: scalar

   :param xreg: Optional keyword, exogenous regressors. Default = {} (none).
   :type xreg: TxK matrix or dataframe

   :param quiet: Optional keyword, set to 1 to suppress output. Default = 0.
   :type quiet: scalar

   :param ctl: Optional keyword, a :class:`bvarControl` structure with initial hyperparameter values. When provided, struct values are used and keywords are ignored. The optimization mode is determined by which tightness values are nonzero:

       - *soc_tightness* = 0, *sur_tightness* = 0: optimize overall_tightness only
       - *soc_tightness* > 0: optimize overall_tightness + soc_tightness (SOC)
       - *sur_tightness* > 0: optimize overall_tightness + sur_tightness (SUR)
       - Both > 0: optimize overall_tightness + soc_tightness + sur_tightness

   :type ctl: struct

   :return ho: An instance of a :class:`hyperoptResult` structure containing:

       .. list-table::
          :widths: auto

          * - ho.overall_tightness
            - Scalar, optimized overall tightness.

          * - ho.lag_decay
            - Scalar, optimized lag decay (if included in optimization).

          * - ho.soc_tightness
            - Scalar, optimized SOC tightness (if included).

          * - ho.sur_tightness
            - Scalar, optimized SUR tightness (if included).

          * - ho.log_ml
            - Scalar, maximized log marginal likelihood.

          * - ho.converged
            - Scalar, 1 if optimizer converged.

          * - ho.n_evals
            - Scalar, number of function evaluations.

          * - ho.ctl
            - :class:`bvarControl` struct, pre-populated with all optimal values. Ready to pass directly to :func:`bvarFit`.

   :rtype ho: struct

Examples
--------

One-Line Optimal BVAR
+++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    data = loadd(fname);

    // Optimize and estimate in two lines
    ho = bvarHyperopt(data);
    result = bvarFit(data, ctl=ho.ctl);

    print "Optimal overall_tightness:" ho.overall_tightness;
    print "Log ML:" ho.log_ml;

Optimize with SOC and SUR
++++++++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    data = loadd(fname);

    ctl = bvarControlCreate();
    ctl.soc_tightness = 1;      // Enable SOC (initial value)
    ctl.sur_tightness = 1;      // Enable SUR (initial value)

    ho = bvarHyperopt(data, p=4, ctl=ctl);
    result = bvarFit(data, ctl=ho.ctl);

    print "Optimal overall_tightness:" ho.overall_tightness;
    print "Optimal soc_tightness:" ho.soc_tightness;
    print "Optimal sur_tightness:" ho.sur_tightness;

Remarks
-------

Implements the Giannone, Lenza & Primiceri (2015) approach to hyperparameter
selection. The marginal likelihood is maximized using L-BFGS-B constrained
optimization, treating the Minnesota hyperparameters as continuous variables
with positivity constraints.

The returned *ho.ctl* structure is a complete :class:`bvarControl` with all
fields populated — the optimal tightness values plus all other settings carried
over from the input. Pass it directly to :func:`bvarFit` without further
modification.

Model
-----

The marginal likelihood of the data under the conjugate Minnesota prior is:

.. math::

   p(Y | \lambda) = \pi^{-\frac{T m}{2}} \frac{|\bar\Phi|^{m/2}}{|\Omega|^{m/2}} \frac{|\bar{S}|^{-\bar\alpha/2}}{|S_0|^{-\alpha_0/2}} \prod_{i=1}^{m} \frac{\Gamma((\bar\alpha + 1 - i)/2)}{\Gamma((\alpha_0 + 1 - i)/2)}

where :math:`\lambda = (\lambda_1, \lambda_6, \lambda_7)` are the hyperparameters being
optimized, and the posterior parameters :math:`\bar\Phi, \bar{S}, \bar\alpha` depend on
:math:`\lambda` through the prior.

The optimum :math:`\lambda^* = \arg\max_\lambda \log p(Y | \lambda)` is the
empirical Bayes or "type II maximum likelihood" estimate.

Algorithm
---------

1. Evaluate :math:`\log p(Y | \lambda)` analytically (closed form for conjugate NIW).
2. Maximize using L-BFGS-B with positivity constraints on all :math:`\lambda`.
3. Starting values: the input *ctl* tightness values (defaults: overall_tightness=0.2).

The optimization is fast because each function evaluation is :math:`O(K^2 m)` (no MCMC).
Typical wall-clock time is 0.01-0.05 seconds.

Troubleshooting
---------------

**Optimizer returns overall_tightness at the upper bound:**
The data wants a very loose prior (overall_tightness → ∞ approaches OLS). This suggests
the sample is large enough that the prior doesn't help. Consider using OLS
(:func:`varFit`) or reducing the search bounds.

**soc_tightness or sur_tightness optimized to near zero:**
The data does not support sum-of-coefficients or single-unit-root priors.
This is informative — the prior is not needed for this dataset.

Verification
------------

GLP hyperparameter optimization verified against R ``BVAR::bvar()`` with
``hyper = "auto"`` on multiple datasets. Optimal tightness values and maximized
log marginal likelihoods agree within optimization tolerance.


References
----------

- Giannone, D., M. Lenza, and G. E. Primiceri (2015). "Prior selection for vector autoregressions." *Review of Economics and Statistics*, 97(2), 436-451.

Library
-------
timeseries

Source
------
bvar.src

.. seealso:: Functions :func:`bvarFit`, :func:`bvarControlCreate`
