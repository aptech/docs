varDiagnosePrint
================

Purpose
-------
Reprint the diagnostics summary table.

Format
------

.. function:: varDiagnosePrint(diag)

   :param diag: an instance of a :class:`diagResult` structure from :func:`varDiagnose` or :func:`varDiagnoseMulti`.
   :type diag: struct

Examples
--------

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));
    result = bvarSvFit(data, quiet=1);

    // Suppress initial output, print later
    diag = varDiagnose(result, quiet=1);

    // Reprint
    call varDiagnosePrint(diag);

Library
-------
timeseries

Source
------
diagnostics.src

.. seealso:: Functions :func:`varDiagnose`, :func:`varDiagnoseMulti`
