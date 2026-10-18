
ssPrintArima
==============================================

Purpose
----------------

:func:`ssPrint`'s counterpart for a model fit via :func:`ssARIMA`/:func:`ssSARIMA` -- prints the same style of results table (header, parameter estimates, confidence-interval tables, diagnostics), but reads estimation results directly from ``sOut.mleResults`` rather than from a separate :class:`cmlmtResults` argument, and takes a plain parameter-name vector rather than a full :class:`ssControl` (:func:`ssARIMA`/:func:`ssSARIMA` build their parameter names internally rather than through ``ssControl.param_names``). Called automatically at the end of :func:`ssSARIMA` (and therefore :func:`ssARIMA`, which delegates to it).

Format
----------------
.. function:: ssPrintArima(sOut, param_names)

    :param sOut: a filled instance of an :class:`ssOut` structure (e.g. as returned by :func:`ssSARIMA`, before it is returned to the caller).
    :type sOut: struct

    :param param_names: String array, one label per parameter in ``sOut.final_params``, in the same order.
    :type param_names: String array

    :return: None -- prints directly to the screen; does not return a value.

Examples
----------------

::

    new;
    library cmlmt, tsmt, sslib;

    fname = getGAUSShome $+ "pkgs/tsmt/examples/enders_sim2.dat";
    y = loadd(fname);
    y = y[., "ar2"];

    struct ssOut sOut;
    sOut = ssARIMA(y, 2);

    // sOut's parameter table was already printed automatically by
    // ssARIMA; ssPrintArima can be called again directly, e.g. after
    // modifying sOut, with the same parameter names
    param_names = "phi : y[t-1]"$|"phi : y[t-2]"$|"Sigma2";
    ssPrintArima(sOut, param_names);

Source
------

ssprintutil.src

.. seealso:: Functions :func:`ssARIMA`, :func:`ssSARIMA`, :func:`ssPrint`
