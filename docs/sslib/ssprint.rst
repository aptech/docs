
ssPrint
==============================================

Purpose
----------------

Prints a fitted model's full results table to the screen -- header (return code, log-likelihood, AIC/AICc/BIC/HQIC, covariance method), parameter estimates with standard errors/t-stats/p-values/gradient, any confidence-interval tables CMLMT computed (Wald, inverse Wald, profile likelihood, bootstrap, Bayes), and residual/model diagnostics. Called automatically at the end of :func:`ssFit`/:func:`ssFitTVP`; exposed publicly for a caller who wants to re-print a previously-fit model's results.

Format
----------------
.. function:: ssPrint(out, ssctl, sOut)

    :param out: a filled instance of a :class:`cmlmtResults` structure (e.g. ``sOut.mleResults`` after :func:`ssFit`/:func:`ssFitTVP`).
    :type out: struct

    :param ssctl: the :class:`ssControl` structure the model was fit with -- specifically, ``ssctl.param_names`` is used to label the parameter table.
    :type ssctl: struct

    :param sOut: a filled instance of an :class:`ssOut` structure -- specifically its diagnostic fields (see :func:`ssResidDiagnostics`/:func:`ssSummaryStats`) are used for the header and the diagnostics block.
    :type sOut: struct

    :return: None -- prints directly to the screen; does not return a value.

Examples
----------------

::

    // A fragment: updateSSModel, param_vec_st, y and ssctl are set up
    // exactly as in the ssFit example.
    sOut = ssFit(&updateSSModel, param_vec_st, y, ssctl);

    // Re-print the results table, e.g. after modifying sOut
    ssPrint(sOut.mleResults, ssctl, sOut);

Remarks
-------

For a model fit via :func:`ssARIMA`/:func:`ssSARIMA` (which does not build a full :class:`ssControl` the way :func:`ssFit`/:func:`ssFitTVP` do), use :func:`ssPrintArima` instead -- it takes a plain parameter-name vector rather than an :class:`ssControl`.

Source
------

ssprintutil.src

.. seealso:: Functions :func:`ssFit`, :func:`ssFitTVP`, :func:`ssPrintArima`
