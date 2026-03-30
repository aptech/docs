varDiagnoseMulti
================

Purpose
-------
Run multi-chain convergence diagnostics with cross-chain R-hat.

Format
------

.. function:: diag = varDiagnoseMulti(result)
              diag = varDiagnoseMulti(results)

   :param result: a :class:`bvarSvResult` from :func:`bvarSvFit` with ``n_chains > 1``.
   :type result: struct

   :param results: alternatively, an array of :class:`bvarResult` structs from separate chains.
   :type results: array of structs

   :param rhat_threshold: Optional keyword, R-hat threshold. Default = 1.05.
   :type rhat_threshold: scalar

   :param min_ess: Optional keyword, minimum ESS threshold. Default = 400.
   :type min_ess: scalar

   :param quiet: Optional keyword, set to 1 to suppress output. Default = 0.
   :type quiet: scalar

   :return diag: An instance of a :class:`diagResult` structure containing cross-chain diagnostics.

       .. include:: include/diagresult.rst

   :rtype diag: struct

Examples
--------

Multi-Chain SV-BVAR
+++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/macro.dat");
    data = loadd(fname);

    ctl = bvarSvControlCreate();
    ctl.p = 4;
    ctl.n_draws = 10000;
    ctl.n_burn = 5000;
    ctl.n_chains = 4;
    ctl.parallel = 1;

    result = bvarSvFit(data, ctl, quiet=1);

    // Multi-chain diagnostics (cross-chain R-hat)
    diag = varDiagnoseMulti(result);

Remarks
-------

Cross-chain R-hat is more reliable than single-chain split-R-hat because it
detects chains that converge to different modes. Requires at least 2 chains.

The Geweke z-test is not computed for multi-chain diagnostics — cross-chain
R-hat supersedes it.

Library
-------
timeseries

Source
------
diagnostics.src

.. seealso:: Functions :func:`varDiagnose`, :func:`varDiagnosePrint`
