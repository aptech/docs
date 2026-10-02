plotIrf
=======

Purpose
-------
Plot impulse responses, cumulative responses or forecast error variance
shares in a grid, with credible bands for posterior results.

Format
------

.. function:: plotIrf(irf)
              plotIrf(irf, plot_type="cirf")
              plotIrf(irf, plot_type="fevd")
              plotIrf(irf, shock="fed_funds")

   :param irf: an instance of an :class:`irfResult` structure from :func:`irfCompute`.
   :type irf: struct

   :param plot_type: Optional keyword, what to plot:

       .. list-table::
           :widths: auto

           * - "irf"
             - Responses (default).
           * - "cirf"
             - Cumulative responses. Compute *irf* with ``cumulative=1``.
           * - "fevd"
             - Forecast error variance shares (see :func:`fevdCompute`).

   :type plot_type: string

   :param shock: Optional keyword, the shocks to plot, by name (*irf.shock_names*) or by number. A string array or a vector selects several. Default = every shock, or only the restricted shocks under sign identification.
   :type shock: string, string array, scalar or vector

Examples
--------

Responses from a VAR
++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    y = loadd(fname, "gdp_growth + cpi_inflation + fed_funds");

    fit = varFit(y, p=4, quiet=1);
    irf = irfCompute(fit, 20, quiet=1);

    // 3 x 3 grid: one row per variable, one column per shock
    plotIrf(irf);

    // One column: the responses to the funds rate shock. With recursive
    // identification each shock is named after its variable.
    plotIrf(irf, shock="fed_funds");

Posterior bands and a sign-restricted shock
+++++++++++++++++++++++++++++++++++++++++++

::

    fit = bvarFit(y, p=4, quiet=1);

    signs = signRestrictions({ "fed_funds"     "monetary" "0:4" "+",
                               "cpi_inflation" "monetary" "0:4" "-" });
    irf = irfCompute(fit, 20, restrictions=signs, cumulative=1, quiet=1);

    // One column: the responses to the monetary shock
    plotIrf(irf);

    // Cumulative responses
    plotIrf(irf, plot_type="cirf");

Save to file
++++++++++++

::

    plotIrf(irf);
    plotSave("irf_grid.png", "px", 900 | 900);

Remarks
-------

**Grid layout.** Row *i*, column *j* shows the response of variable *i* to
shock *j*. Each panel is titled "variable ← shock" using the variable and
shock names stored in *irf*. Under sign identification only the restricted
shocks are plotted.

**Bands.** For posterior results the median is drawn as a line over shaded
pointwise credible bands; the darker band is the narrower one. A dashed
gray line marks zero.

**Variance shares** are plotted from horizon 1, the one-step decomposition.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`irfCompute`, :func:`fevdCompute`, :func:`irfPlotData`
