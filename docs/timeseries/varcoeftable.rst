varCoefTable
============

Purpose
-------
Return the coefficient table from a fitted VAR or BVAR model as a dataframe.

Format
------

.. function:: tab = varCoefTable(result)
              tab = varCoefTable(result, equation=2)

   :param result: an instance of a :class:`varResult`, :class:`bvarResult`, or :class:`bvarSvResult` structure.
   :type result: struct

   :param equation: Optional keyword, equation number (1 to m) to extract. Default = 0 (all equations stacked).
   :type equation: scalar

   :return tab: Dataframe. For frequentist: columns Name, Coef, SE, t-stat, p-value. For Bayesian: columns Name, Mean, SD, 16%, 84%.
   :rtype tab: dataframe

Examples
--------

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/macro.dat");
    data = loadd(fname);
    result = varFit(data, 4, quiet=1);

    // Full table (all equations)
    tab = varCoefTable(result);
    print tab;

    // Single equation
    tab_gdp = varCoefTable(result, equation=1);
    print tab_gdp;

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`varFit`, :func:`bvarFit`, :func:`bvarSvFit`, :func:`varResults`
