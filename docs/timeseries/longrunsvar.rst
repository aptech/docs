longRunSvar
===========

Purpose
-------
Blanchard-Quah (1989) long-run SVAR identification. Computes structural impulse responses by imposing long-run restrictions via the Cholesky decomposition of the cumulative impact matrix.

Format
------

.. function:: lr = longRunSvar(y, n_ahead)
              lr = longRunSvar(y, n_ahead, p=4)
              lr = longRunSvar(y, n_ahead, p=4, xreg=X)

   :param y: endogenous variables. If a dataframe, column names are used as variable labels in output. If a matrix, variables are labeled "Y1", "Y2", etc.
   :type y: TxM matrix or dataframe

   :param n_ahead: number of impulse response horizons to compute (h = 0, 1, ..., n_ahead).
   :type n_ahead: scalar

   :param p: Optional keyword, lag order. Default = 1.
   :type p: scalar

   :param xreg: Optional keyword, TxK exogenous regressors. Default = {} (none).
   :type xreg: matrix or dataframe

   :param quiet: Optional keyword, set to 1 to suppress output. Default = 0.
   :type quiet: scalar

   :param ctl: Optional keyword, an instance of a :class:`longRunSvarControl` structure. When provided, struct values are used and keywords are ignored. An instance is initialized by calling :func:`longRunSvarControlCreate` and the following members can be set:

       .. include:: include/longrunsvarcontrol.rst

   :type adv: struct

   :return lr: An instance of a :class:`longRunSvarResult` structure containing:

       .. include:: include/longrunsvarresult.rst

   :rtype lr: struct

Examples
--------

Blanchard-Quah Supply and Demand Shocks
++++++++++++++++++++++++++++++++++++++++

The classic Blanchard and Quah (1989) decomposition with GDP growth and unemployment. The first shock (supply) has a permanent effect on GDP; the second shock (demand) has zero long-run effect on GDP:

::

    new;
    library timeseries;

    // Load US macro quarterly data
    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    y = loadd(fname, "gdp_growth + unemployment");

    // Long-run SVAR with 4 lags and 20-step IRF
    lr = longRunSvar(y, 20, p=4);

Output:

::

    ================================================================================
    Long-Run SVAR (Blanchard & Quah 1989)
    Variables: 2, Lags: 4, Horizons: 0-20
    ================================================================================
    Structural Impact Matrix (B0):
              Supply    Demand
    GDP       0.0083    0.0071
    UNEMP    -0.0512    0.1243
    ================================================================================

The impact matrix shows that a supply shock raises GDP and lowers unemployment on impact, while a demand shock raises both.

Technology Shock Identification (Gali 1999)
+++++++++++++++++++++++++++++++++++++++++++

Identify technology shocks using labor productivity and hours worked. Only the technology shock (first variable) has a permanent effect on productivity:

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    y = loadd(fname, "productivity_growth + hours_growth");

    // Ordering: productivity first, hours second
    // Technology shock = permanent productivity effect
    // Non-technology shock = zero long-run productivity effect
    lr = longRunSvar(y, 40, p=8);

    // Access IRF at horizon 10: response of hours to technology shock
    print "Hours response to technology shock at h=10:";
    print lr.irf.irf[11*2, 1];

With Exogenous Regressors
+++++++++++++++++++++++++

Include a time trend as an exogenous regressor:

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    y = loadd(fname, "gdp_growth + cpi_inflation");

    lr = longRunSvar(y, 20, p=4, xreg=seqa(1, 1, rows(y)), quiet=1);

    print "Structural impact matrix:";
    print lr.impact;

Model
-----

The reduced-form VAR(p) is estimated by OLS:

.. math::

   y_t = B_1 y_{t-1} + \cdots + B_p y_{t-p} + u + \varepsilon_t, \quad \varepsilon_t \sim N(0, \Sigma)

The long-run cumulative impact matrix is:

.. math::

   C(1) = (I_m - B_1 - B_2 - \cdots - B_p)^{-1}

This matrix captures the total (cumulative) effect of a reduced-form shock on the
level of each variable. To identify structural shocks, compute:

.. math::

   C(1) \, \Sigma \, C(1)' = P \, P'

where :math:`P` is the lower-triangular Cholesky factor. The structural impact matrix is:

.. math::

   B_0 = C(1)^{-1} \, P

The identification imposes that the second shock (and higher) has zero long-run effect on the first variable, the third shock has zero long-run effect on the first two variables, and so on. The structural IRF at horizon h is:

.. math::

   \Theta_h = J \, F^h \, J' \, B_0

where :math:`F` is the VAR companion matrix and :math:`J = [I_m \; 0 \; \cdots \; 0]`.


Remarks
-------

**Variable ordering matters:**
The ordering of variables in *y* determines the identification. The first variable
is the one on which all shocks except the first have zero long-run effect. The
second variable allows only the first two shocks to have permanent effects, and so
on. In the Blanchard-Quah setup, GDP (or productivity) must be ordered first so that
the demand shock has zero long-run effect on output.

**Stationarity requirement:**
The VAR must be stationary for the long-run matrix :math:`C(1) = (I - B_1 - \cdots - B_p)^{-1}`
to exist. If the companion matrix has eigenvalues near or on the unit circle,
:math:`C(1)` becomes ill-conditioned and the identification is unreliable. Check
stationarity with :func:`varFit` before using this function.

**Point identification only:**
This function provides point-identified structural IRFs from a single OLS VAR
estimate. There are no posterior uncertainty bands. For inference with uncertainty,
bootstrap the VAR or use a Bayesian approach with :func:`bvarFit` and
:func:`svarIrfCompute`.

**Differenced vs. level data:**
The Blanchard-Quah method is typically applied to growth rates (first differences
of log levels). The cumulative IRF from *lr.irf* then gives the level response.
If variables are already in levels and stationary, the IRF itself is the level
response.

**Accessing IRF values:**
The IRF is stored in *lr.irf.irf* as an (n_ahead+1)*m x m stacked matrix. Block
h (rows h*m+1 to (h+1)*m) is the mxm response matrix at horizon h. Element [i, j]
of block h is the response of variable i to structural shock j at horizon h.


References
----------

- Blanchard, O.J. and D. Quah (1989). "The dynamic effects of aggregate demand and supply disturbances." *American Economic Review*, 79(4), 655-673.
- Gali, J. (1999). "Technology, employment, and the business cycle: Do technology shocks explain aggregate fluctuations?" *American Economic Review*, 89(1), 249-271.
- Lutkepohl, H. (2005). *New Introduction to Multiple Time Series Analysis*. Springer, Chapter 9.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`longRunSvarControlCreate`, :func:`svarIrfCompute`, :func:`varFit`, :func:`irfCompute`
