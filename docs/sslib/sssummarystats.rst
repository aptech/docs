
ssSummaryStats
==============================================

Purpose
----------------

Computes model summary statistics and information criteria from a filled :class:`ssOut` structure -- degrees of freedom, SSE/MSE/R-squared, and AIC/AICc/BIC/HQIC/likelihood-ratio statistic. Called automatically by :func:`ssFit`/:func:`ssFitTVP`/:func:`ssARIMA`/:func:`ssSARIMA`/:func:`ssStructuralTS` as part of filling their own returned :class:`ssOut`; exposed publicly for a caller who has otherwise built or modified an :class:`ssOut` and wants these summary statistics (re)computed.

.. note::
   **GAUSS 26.1.4+ (sslib 2.0.0).** This procedure declares its return
   type, so the result needs no preceding ``struct`` declaration. See
   :ref:`v1-to-v2-migration`.

Format
----------------
.. function:: sOut = ssSummaryStats(y, sOut)

    :param y: Vector, observed data (the same data the model was fit to).
    :type y: Vector

    :param sOut: a partially-filled instance of an :class:`ssOut` structure -- specifically needs ``sOut.resid``, ``sOut.final_params``, and ``sOut.mleResults.fct`` already set (as :func:`ssFit`/:func:`ssFitTVP` already do).
    :type sOut: struct

    :return sOut: the same structure, with the following members filled in:

        .. list-table::
            :widths: auto

            * - sOut.numObs
              - Scalar, number of observations.
            * - sOut.df_model
              - Scalar, degrees of freedom of the model (number of estimated parameters).
            * - sOut.df_resid
              - Scalar, degrees of freedom of the residuals.
            * - sOut.sse
              - Scalar, sum of squared errors.
            * - sOut.mse
              - Scalar, mean squared error.
            * - sOut.rsquared
              - Scalar, model R-squared.
            * - sOut.ssy
              - Scalar, sum of squares total (deviations of y from the mean of y).
            * - sOut.aic
              - Scalar, Akaike's information criterion.
            * - sOut.aicc
              - Scalar, corrected Akaike's information criterion.
            * - sOut.bic
              - Scalar, Schwarz' Bayesian information criterion.
            * - sOut.hqic
              - Scalar, Hannan-Quinn information criterion.
            * - sOut.lrs
              - Scalar, likelihood-ratio statistic.

    :rtype sOut: struct

Examples
----------------

::

    // A fragment: updateSSModel, param_vec_st, y and ssctl are set up
    // exactly as in the ssFit example.
    sOut = ssFit(&updateSSModel, param_vec_st, y, ssctl);

    // Recompute the summary statistics, e.g. after modifying sOut
    sOut = ssSummaryStats(y, sOut);

Remarks
-------

``sOut.df_model`` is taken as ``rows(sOut.final_params)`` -- the number of estimated parameters, regardless of how they entered the model (e.g. a structural model's variance, frequency/damping, and regression coefficients all count equally). See :func:`ssgetAIC`/:func:`ssgetAICC`/:func:`ssgetBIC`/:func:`ssgetHQIC` for the individual information-criterion formulas.

Source
------

ssdiagnostics.src

.. seealso:: Functions :func:`ssFit`, :func:`ssResidDiagnostics`, :func:`ssgetAIC`, :func:`ssgetAICC`, :func:`ssgetBIC`, :func:`ssgetHQIC`
