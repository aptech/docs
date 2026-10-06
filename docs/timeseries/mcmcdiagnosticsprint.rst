mcmcDiagnosticsPrint
====================

Purpose
-------
Print the summary of an :func:`mcmcDiagnostics` result again.

Format
------

.. function:: mcmcDiagnosticsPrint(dx)

   :param dx: An instance of an :class:`mcmcDiagResult` structure returned by :func:`mcmcDiagnostics`.
   :type dx: struct

Examples
--------

::

    dx = mcmcDiagnostics(result, quiet=1);
    mcmcDiagnosticsPrint(dx);

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`mcmcDiagnostics`
