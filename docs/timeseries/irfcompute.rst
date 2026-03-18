irfCompute
==========

Purpose
-------
Compute orthogonalized impulse response functions using Cholesky identification.

Format
------

.. function:: irf = irfCompute(result, n_ahead)

   :param result: an instance of a :class:`varResult` or :class:`bvarResult` structure.
   :type result: struct

   :param n_ahead: number of horizons to compute (e.g., 20).
   :type n_ahead: scalar

   :param var_names: Optional keyword, override variable names from the estimation result.
   :type var_names: Mx1 string array

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :return irf: An instance of an :class:`irfResult` structure containing:

       .. include:: include/irfresult.rst

   :rtype irf: struct

Examples
--------

Cholesky IRF from VAR
+++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));

    // Fit VAR(4) — variable ordering determines identification
    // GDP first (most exogenous), FFR last (most endogenous)
    result = varFit(data, 4, var_names="GDP"$|"CPI"$|"FFR", quiet=1);

    // 20-step IRF
    struct irfResult irf;
    irf = irfCompute(result, 20);

IRF from BVAR
+++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));

    struct bvarControl ctl;
    ctl = bvarControlCreate();
    ctl.p = 4;
    result = bvarFit(data, ctl, quiet=1);

    // IRF at posterior mean
    irf = irfCompute(result, 20);

Accessing Specific Responses
++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));
    result = varFit(data, 4, var_names="GDP"$|"CPI"$|"FFR", quiet=1);
    irf = irfCompute(result, 20, quiet=1);

    // Impact response (h=0) of GDP to FFR shock
    print "Impact of FFR shock on GDP:" irf.irf[1][1, 3];

    // Response at horizon 5 (index 6)
    print "h=5 response:" irf.irf[6][1, 3];

    // Full time path: GDP response to FFR shock
    for h (0, 20, 1);
        print h;; print "  ";; print irf.irf[h+1][1, 3];
    endfor;

Remarks
-------

**Identification:**
The Cholesky decomposition of :math:`\Sigma` is used to orthogonalize the
innovations. The ordering of variables in the data determines the recursive
causal structure: variable 1 can affect all others contemporaneously, variable
2 can affect variables 3, ..., m but not 1, and so on.

**To change the identification ordering,** reorder the columns of the data
before calling :func:`varFit` or :func:`bvarFit`.

**For ordering-invariant responses,** use :func:`girfCompute` (generalized IRF).
For theory-based identification with sign/zero restrictions, see the SVAR
functions.

**For BVAR,** the IRF is computed at the posterior mean of B and :math:`\Sigma`.
For posterior IRF bands, use :func:`irfSvCompute` with an :class:`bvarSvResult`.

**Indexing convention:**
``irf.irf[1]`` is the impact response (h=0). ``irf.irf[h+1]`` is the response
at horizon h. This is because GAUSS arrays are 1-indexed.

Library
-------
timeseries

Source
------
irf.src

.. seealso:: Functions :func:`irfSvCompute`, :func:`girfCompute`, :func:`fevdCompute`, :func:`hdCompute`, :func:`irfPlotData`
