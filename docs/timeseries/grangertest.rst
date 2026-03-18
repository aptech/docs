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

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));
    result = varFit(data, 4, var_names="GDP"$|"CPI"$|"FFR", quiet=1);

    // Does FFR Granger-cause GDP?
    g = grangerTest(result, 3, 1);

    print g.cause_name "Granger-causes" g.effect_name "?";
    print "F =" g.f_stat "p =" g.p_value;

All Pairs
+++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));
    result = varFit(data, 4, var_names="GDP"$|"CPI"$|"FFR", quiet=1);

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

Library
-------
timeseries

Source
------
granger.src

.. seealso:: Functions :func:`varFit`, :func:`varLagSelect`
