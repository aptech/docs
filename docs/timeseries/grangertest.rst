grangerTest
===========

Purpose
-------
Test whether one variable Granger-causes another in a fitted VAR model.

Format
------

.. function:: g = grangerTest(result, cause, effect)

   :param result: an instance of a :class:`varResult` structure from :func:`varFit`.
   :type result: struct

   :param cause: index (1 to m) of the potential cause variable.
   :type cause: scalar

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
            - Scalar, numerator degrees of freedom (number of restricted lags = p).

          * - g.df2
            - Scalar, denominator degrees of freedom.

          * - g.cause_name
            - String, name of the cause variable.

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

    fname = getGAUSSHome("pkgs/timeseries/examples/data/macro.dat");
    data = loadd(fname);
    result = varFit(data, 4);

    // Does FFR Granger-cause GDP?
    g = grangerTest(result, 3, 1);

    print g.cause_name "Granger-causes" g.effect_name "?";
    print "F =" g.f_stat "p =" g.p_value;

All Pairs
+++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/macro.dat");
    data = loadd(fname);
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

Tests H0: all p lags of the cause variable are jointly zero in the effect
variable's equation. Uses an F-test with p numerator and (T - mp - 1)
denominator degrees of freedom.

**Granger causality is a predictive concept,** not a structural one. "X
Granger-causes Y" means X contains information useful for forecasting Y
beyond what Y's own lags provide. It does not imply X structurally causes Y.

Model
-----

The Granger causality test (Granger 1969) tests the null hypothesis that all :math:`p`
lags of the cause variable are jointly zero in the effect variable's equation:

.. math::

   H_0: B_{\text{cause},1} = B_{\text{cause},2} = \cdots = B_{\text{cause},p} = 0

in the equation for the effect variable. The F-statistic is:

.. math::

   F = \frac{(\text{RSS}_r - \text{RSS}_u) / p}{\text{RSS}_u / (T - mp - 1)} \sim F(p, T - mp - 1)

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

Granger causality F-statistics and p-values verified against R ``vars::causality()``
at :math:`10^{-6}` tolerance on a 2-variable VAR(1) with known DGP. Both directions
tested (Y1→Y2 and Y2→Y1).

See ``gausslib-var/tests/r_benchmark.rs``.


References
----------

- Granger, C.W.J. (1969). "Investigating causal relations by econometric models and cross-spectral methods." *Econometrica*, 37(3), 424-438.
- Lutkepohl, H. (2005). *New Introduction to Multiple Time Series Analysis*. Springer. Section 3.6.


Library
-------
timeseries

Source
------
granger.src

.. seealso:: Functions :func:`varFit`, :func:`varLagSelect`
