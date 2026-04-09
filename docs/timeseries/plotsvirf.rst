plotSvIrf
=========

Purpose
-------
Plot SV-BVAR impulse responses with credible bands in an m × m grid.
Shows median IRF with shaded 68% and 90% posterior bands.

Format
------

.. function:: plotSvIrf(irf)

   :param irf: Posterior IRF result from :func:`irfSvCompute`.
   :type irf: struct svIrfResult

Examples
--------

Posterior IRF with Bands
++++++++++++++++++++++++

::

    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    data = loadd(fname, "gdp_growth + cpi_inflation + fed_funds");

    svr = bvarSvFit(data, p=4, ar=0, n_draws=5000, n_burn=2000, quiet=1);
    irf = irfSvCompute(svr, 20);

    // 3×3 grid with shaded credible bands
    plotSvIrf(irf);

Remarks
-------

**Band shading:** The inner band (68%) is drawn with darker shading, the outer
band (90%) with lighter shading. The median IRF is a solid blue line.

**Grid layout:** Same as :func:`plotIrf` — row *i* = response variable,
column *j* = shock source.

**Significance:** If both the 68% and 90% bands exclude zero at a given horizon,
the response is significant at that horizon with high posterior probability.

**Zero line:** A horizontal dashed gray line at zero is drawn in every cell.

.. seealso:: Functions :func:`irfSvCompute`, :func:`plotIrf`, :func:`bvarSvFit`
