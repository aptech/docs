bvarHyperopt
============

Purpose
-------
Optimize Minnesota prior hyperparameters by maximizing the log marginal likelihood.

Format
------

.. function:: ho = bvarHyperopt(y)
              ho = bvarHyperopt(y, ctl)
              ho = bvarHyperopt(y, ctl, xreg=X)

   :param y: endogenous variables.
   :type y: TxM matrix or dataframe

   :param ctl: Optional input, a :class:`bvarControl` structure with initial hyperparameter values. The optimization mode is determined by which lambda values are nonzero:

       - *lambda6* = 0, *lambda7* = 0: optimize lambda1 only
       - *lambda6* > 0: optimize lambda1 + lambda6 (SOC)
       - *lambda7* > 0: optimize lambda1 + lambda7 (SUR)
       - Both > 0: optimize lambda1 + lambda6 + lambda7

   :type ctl: struct

   :param xreg: Optional keyword, exogenous regressors.
   :type xreg: TxK matrix

   :param quiet: Optional keyword, set to 1 to suppress output. Default = 0.
   :type quiet: scalar

   :return ho: An instance of a :class:`hyperoptResult` structure containing:

       .. list-table::
          :widths: auto

          * - ho.lambda1
            - Scalar, optimized overall tightness.

          * - ho.lambda3
            - Scalar, optimized lag decay (if included in optimization).

          * - ho.lambda6
            - Scalar, optimized SOC tightness (if included).

          * - ho.lambda7
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

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));

    // Optimize and estimate in two lines
    ho = bvarHyperopt(data);
    result = bvarFit(data, ho.ctl);

    print "Optimal lambda1:" ho.lambda1;
    print "Log ML:" ho.log_ml;

Optimize with SOC and SUR
++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));

    struct bvarControl ctl;
    ctl = bvarControlCreate();
    ctl.p = 4;
    ctl.lambda6 = 1;      // Enable SOC (initial value)
    ctl.lambda7 = 1;      // Enable SUR (initial value)

    ho = bvarHyperopt(data, ctl);
    result = bvarFit(data, ho.ctl);

    print "Optimal lambda1:" ho.lambda1;
    print "Optimal lambda6:" ho.lambda6;
    print "Optimal lambda7:" ho.lambda7;

Remarks
-------

Implements the Giannone, Lenza & Primiceri (2015) approach to hyperparameter
selection. The marginal likelihood is maximized using L-BFGS-B constrained
optimization, treating the Minnesota hyperparameters as continuous variables
with positivity constraints.

The returned *ho.ctl* structure is a complete :class:`bvarControl` with all
fields populated — the optimal lambda values plus all other settings carried
over from the input. Pass it directly to :func:`bvarFit` without further
modification.

Library
-------
timeseries

Source
------
bvar.src

.. seealso:: Functions :func:`bvarFit`, :func:`bvarControlCreate`
