varFit
======

Purpose
-------
Fit a VAR(p) model by ordinary least squares.

Format
------

.. function:: result = varFit(y)
              result = varFit(y, p)
              result = varFit(y, p, xreg=X)
              result = varFit(y, ctl)

   :param y: endogenous variables. If a dataframe, column names are used as variable names.
   :type y: TxM matrix or dataframe

   :param p: Optional input, lag order. Default = 1.
   :type p: scalar

   :param ctl: Optional input, an instance of a :class:`varControl` structure. Overrides *p* if provided. An instance is initialized by calling :func:`varControlCreate` and the following members can be set:

       .. include:: include/varcontrol.rst

   :type ctl: struct

   :param xreg: Optional keyword, exogenous regressors.
   :type xreg: TxK matrix

   :param xreg_names: Optional keyword, column names for *xreg*. If omitted, defaults to ``"X1"``, ``"X2"``, etc.
   :type xreg_names: Kx1 string array

   :param var_names: Optional keyword, endogenous variable names. If omitted and *y* is a dataframe, column headers are used. Otherwise defaults to ``"Y1"``, ``"Y2"``, etc.
   :type var_names: Mx1 string array

   :param quiet: Optional keyword, set to 1 to suppress printed output. Overrides *ctl.quiet*.
   :type quiet: scalar

   :return result: An instance of a :class:`varResult` structure containing:

       .. include:: include/varresult.rst

   :rtype result: struct

Examples
--------

VAR(1) with Defaults
++++++++++++++++++++

::

    new;
    library timeseries;

    // Load macroeconomic data
    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));

    // Fit VAR(1)
    result = varFit(data);

The results are printed to the **Command Window**:

::

    ================================================================================
    VAR(1)                                  Variables:             3
    Method: OLS                             Observations:        200
    Constant: Yes                           Effective obs:       199
    ================================================================================
    AIC:       -12.384          BIC:       -11.927          HQ:        -12.198
    Log-Lik:    1232.86         |Sigma|:    2.41e-08
    ================================================================================
    Companion eigenvalues: 0.981  0.854  0.723  (all inside unit circle)
    ================================================================================

    Equation 1: GDP
                        Coef      Std.Err.     t-stat    p-value
    --------------------------------------------------------------------------------
    GDP(-1)            0.8731      0.0543     16.076      0.000
    CPI(-1)           -0.0218      0.0437     -0.499      0.618
    FFR(-1)            0.0012      0.0089      0.135      0.893
    Constant           0.0080      0.0012      6.588      0.000
    ================================================================================
    ...

VAR(4)
++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));

    // Fit VAR(4)
    result = varFit(data, 4);

VAR with Named Variables
++++++++++++++++++++++++

::

    new;
    library timeseries;

    // Load raw matrix
    y = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"), "gdp + cpi + ffr");

    // Provide variable names
    names = "GDP" $| "CPI" $| "FFR";
    result = varFit(y, 4, var_names=names);

VAR with Exogenous Regressors
+++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    y = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"), "gdp + cpi + ffr");
    X = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"), "oil");

    result = varFit(y, 2, xreg=X, xreg_names="Oil");

Remarks
-------

**Coefficient layout in result.b:**

The coefficient matrix *result.b* is Kxm where K = m*p + n_exo + include_const
and m is the number of endogenous variables:

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Rows
     - Content
   * - 1 to m
     - Lag 1 coefficients (mxm block)
   * - m+1 to 2m
     - Lag 2 coefficients
   * - ...
     - ...
   * - (p-1)*m+1 to pm
     - Lag p coefficients
   * - pm+1 to pm+n_exo
     - Exogenous coefficients (if any)
   * - K
     - Constant (if *include_const* = 1)

Column j corresponds to equation j (variable j as dependent variable).
This layout matches the standard convention in Lutkepohl (2005).

**Stability:**

The companion form eigenvalues are computed automatically and printed in the
summary. A VAR is stable (stationary) if all eigenvalues of the companion
matrix have modulus strictly less than 1. Non-stationary models produce a
warning but are not rejected — they may be appropriate for cointegrated systems.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`varLagSelect`, :func:`bvarFit`, :func:`varResults`, :func:`varCompanion`, :func:`varCoefTable`
