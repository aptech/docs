plotIrf
=======

Purpose
-------
Plot impulse response functions in an m × m grid. Each cell shows the
response of one variable to a one-standard-deviation shock to another.

Format
------

.. function:: plotIrf(irf)

   :param irf: IRF result from :func:`irfCompute` or :func:`girfCompute`.
   :type irf: struct irfResult

Examples
--------

Cholesky IRF Grid
+++++++++++++++++

::

    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    data = loadd(fname, "gdp_growth + cpi_inflation + fed_funds");

    ctl = varControlCreate();
    ctl.p = 4;
    ctl.quiet = 1;

    rv = varFit(data, ctl);
    irf = irfCompute(rv, 20);

    // 3×3 grid of impulse responses
    plotIrf(irf);

Save to File
++++++++++++

::

    plotIrf(irf);
    plotSave("irf_grid.png", "px", 900 | 900);

Remarks
-------

**Grid layout:** Row *i*, column *j* shows the response of variable *i* to a
shock to variable *j*. Each cell is titled "response ← shock" using the
variable names from the estimation result.

**Zero line:** A horizontal dashed gray line at zero is drawn in every cell.
If the IRF stays above (or below) zero at all horizons, the effect is
consistently positive (or negative).

**Diagonal cells:** These show each variable's response to its own shock. For
Cholesky identification, the impact response (h=0) on the diagonal equals
the Cholesky factor of :math:`\Sigma`.

**For credible bands:** Use :func:`plotSvIrf` with an :class:`svIrfResult` from
:func:`irfSvCompute`. The point-estimate :func:`plotIrf` does not show bands.

.. seealso:: Functions :func:`irfCompute`, :func:`girfCompute`, :func:`plotSvIrf`
