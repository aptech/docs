varDiagnosticsPrint
===================

Purpose
-------
Reprint the diagnostics summary table.

Format
------

.. function:: varDiagnosticsPrint(diag)

   :param diag: an instance of a :class:`diagResult` structure from :func:`varDiagnostics` or :func:`varDiagnosticsMulti`.
   :type diag: struct

Examples
--------

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    data = loadd(fname);
    result = bvarSvFit(data, quiet=1);

    // Suppress initial output, print later
    diag = varDiagnostics(result, quiet=1);

    // Reprint
    call varDiagnosticsPrint(diag);

Library
-------
timeseries

Source
------
diagnostics.src

.. seealso:: Functions :func:`varDiagnostics`, :func:`varDiagnosticsMulti`
