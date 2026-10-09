grangerTest
===========

Purpose
-------
Test whether one or several variables Granger-cause one variable in a fitted VAR model.

Format
------

.. function:: g = grangerTest(result, cause, effect)
              g = grangerTest(result, 2|3, 1, quiet=1)

   :param result: an instance of a :class:`varResult` structure from :func:`varFit`.
   :type result: struct

   :param cause: one index or a nonempty column vector of distinct indices (1 to m) of potential cause variables. The effect must not be among them.
   :type cause: scalar or column vector

   :param effect: index (1 to m) of the effect variable.
   :type effect: scalar

   :param quiet: Optional keyword, set to 1 to suppress output. Default = 0.
   :type quiet: scalar

   :return g: An instance of a :class:`grangerResult` structure containing:

       .. list-table::
          :widths: auto

          * - g.f_stat
            - Scalar, F-statistic.

          * - g.p_value
            - Scalar, p-value.

          * - g.df1
            - Scalar, numerator degrees of freedom (number of restricted lags = q·p, where q is the number of causes).

          * - g.df2
            - Scalar, T_eff - k, where T_eff = T - p and k counts all regressors per equation.

          * - g.cause_name
            - String, name of the first cause variable (also for a vector of causes).

          * - g.cause_var
            - Scalar, index of the first cause variable.

          * - g.causes
            - qx1 vector, distinct cause indices in input order.

          * - g.cause_names
            - qx1 string array, cause names in input order.

          * - g.effect_var
            - Scalar, index of the effect variable.

          * - g.effect_name
            - String, name of the effect variable.

   :rtype g: struct

Examples
--------

Single Pair
+++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv"),
                 "gdp_growth + cpi_inflation + fed_funds");
    result = varFit(data, 4);

    // Does FFR Granger-cause GDP?
    g = grangerTest(result, 3, 1);

    print g.cause_name "Granger-causes" g.effect_name "?";
    print "F =" g.f_stat "p =" g.p_value;

Several causes
++++++++++++++

::

    // Do CPI and FFR jointly help predict GDP?
    g_group = grangerTest(result, 2|3, 1);
    print g_group.cause_names;

All Pairs
+++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv"),
                 "gdp_growth + cpi_inflation + fed_funds");
    result = varFit(data, 4);

    for i (1, 3, 1);
        for j (1, 3, 1);
            if i /= j;
                g = grangerTest(result, i, j, quiet=1);
                print g.cause_name "->" g.effect_name ": p=" g.p_value;
            endif;
        endfor;
    endfor;

Remarks
-------

Tests H0: all p lags of all q cause variables are jointly zero in the
effect variable's equation. The exact single-equation F test uses q·p
numerator and T_eff - k denominator degrees of freedom, where
T_eff = T - p and k = mp + const + trend + number of xreg columns. The
constant, trend and xreg remain in both regressions. The test refits the
regressions and does not depend on the fit's residual-covariance divisor.

Causes must be distinct integer indices and must exclude the effect. The
effect must be one scalar. Supplying a group of effects raises
``grangerTest: effect must be one scalar; groups of effect variables are not supported.``

**Granger causality is a predictive concept,** not a structural one. "X
Granger-causes Y" means X contains information useful for forecasting Y
beyond what Y's own lags provide. It does not imply X structurally causes Y.

Model
-----

The Granger causality test (Granger 1969) tests the null hypothesis that all :math:`qp`
lag coefficients of the cause variables are jointly zero in the effect variable's equation:

.. math::

   H_0: B_{\text{cause},\ell} = 0 \quad \text{for every cause and } \ell=1,\ldots,p

in the equation for the effect variable. The F-statistic is:

.. math::

   F = \frac{(\text{RSS}_r - \text{RSS}_u) / (qp)}{\text{RSS}_u / (T_{eff} - k)} \sim F(qp, T_{eff} - k)

where :math:`\text{RSS}_r` and :math:`\text{RSS}_u` are residual sums of squares from
the restricted and unrestricted regressions.


Troubleshooting
---------------

**Significant Granger causality in both directions:**
This is possible and common — it means both variables contain predictive information
about each other. This does not imply feedback causation in a structural sense.

**Result depends on lag order:**
Granger causality tests are sensitive to p. Use :func:`varLagSelect` to choose p
before testing.


Verification
------------

Reference checks use restricted and unrestricted least-squares regressions
for one effect equation, with the same regressors and degrees of freedom.
The p-value is the upper tail of F(q·p, T_eff - k).


References
----------

- Granger, C.W.J. (1969). "Investigating causal relations by econometric models and cross-spectral methods." *Econometrica*, 37(3), 424-438.
- Lutkepohl, H. (2005). *New Introduction to Multiple Time Series Analysis*. Springer. Section 3.6.


Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`varFit`, :func:`varLagSelect`
