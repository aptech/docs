irfPlotData
===========

Purpose
-------
Reshape IRF, FEVD, or SV-BVAR IRF results into a plot-ready long-format dataframe.

Format
------

.. function:: df = irfPlotData(result, shock, response)
              df = irfPlotData(result)

   :param result: an instance of an :class:`irfResult`, :class:`svIrfResult`, or :class:`fevdResult` structure.
   :type result: struct

   :param shock: Optional, shock index (1 to m). If omitted, all shocks are included.
   :type shock: scalar

   :param response: Optional, response variable index (1 to m). If omitted, all responses are included.
   :type response: scalar

   :return df: Dataframe. For :class:`irfResult`: columns horizon, shock, response, value. For :class:`svIrfResult`: columns horizon, shock, response, median, plus lower/upper columns for each credible band level. For :class:`fevdResult`: columns horizon, shock, response, share.
   :rtype df: dataframe

Examples
--------

Plot a Single Shock-Response Pair
+++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/macro.dat");
    data = loadd(fname);
    result = varFit(data, 4);
    irf = irfCompute(result, 20, quiet=1);

    // GDP response to FFR shock
    df = irfPlotData(irf, 3, 1);
    plotXY(df[., "horizon"], df[., "value"]);

Plot SV-BVAR IRF with Credible Bands
+++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/macro.dat");
    data = loadd(fname);
    result = bvarSvFit(data, quiet=1);
    irf = irfSvCompute(result, 20, quiet=1);

    // GDP response to FFR shock with bands
    df = irfPlotData(irf, 3, 1);

    // Plot median with 68% band
    plotXY(df[., "horizon"],
        df[., "median"]~df[., "bands[1].lower"]~df[., "bands[1].upper"]);

Extract All Pairs
+++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/macro.dat");
    data = loadd(fname);
    result = varFit(data, 4, quiet=1);
    irf = irfCompute(result, 20, quiet=1);

    // All m*m pairs in long format
    df = irfPlotData(irf);
    print df[1:10, .];

Remarks
-------

This is a convenience function for plotting. It reshapes the array-of-matrices
representation into a long-format dataframe that can be passed directly to
:func:`plotXY` or exported to CSV.

**No Rust FFI call** — this is a pure GAUSS reshape operation.

Library
-------
timeseries

Source
------
irf.src

.. seealso:: Functions :func:`irfCompute`, :func:`irfSvCompute`, :func:`fevdCompute`
