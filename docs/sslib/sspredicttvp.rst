
ssPredictTVP
==============================================

Purpose
----------------

Computes in-sample predictions or out-of-sample forecasts for a fitted time-varying-parameter model.

.. note::
   **GAUSS 26.1.4+ (sslib 2.0.0).** The optional arguments below are
   keyword arguments and may be supplied by name, in any order. The
   positional order is unchanged from 1.0.0, so existing positional calls
   keep working. See :ref:`v1-to-v2-migration`.

Format
----------------
.. function:: forecasts = ssPredictTVP(sOut, y [, start_pred, end_pred])

    :param sOut: a filled instance of an :class:`ssOut` structure, as returned by :func:`ssFitTVP`.
    :type sOut: Struct

    :param y: Matrix, observed data used to estimate the parameters.
    :type y: Matrix

    :param start_pred: Optional argument, the observation at which to start predictions/forecasts. Default is to compute out-of-sample forecasts starting immediately following the final observations.
    :type start_pred: Scalar

    :param end_pred: Optional argument, the observation at which to end predictions/forecasts. Default is to compute 20 out-of-sample forecasts such that end_pred = numObs + 20. Must be greater than *start_pred*.
    :type end_pred: Scalar

    :return forecasts: Predicted observations.
    :rtype forecasts: Matrix

Examples
----------------

::

  new;
  library cmlmt, tsmt, sslib;

  // Local level model with a known break in Z after period 30
  y = loadd(getGAUSSHome("pkgs/sslib/examples/tvp_local_level.csv"), "y");
  nobs = rows(y);

  proc (1) = buildZ(nobs);
      local a, i;
      a = arrayinit(nobs|1|1, 0);
      for i(1, 30, 1);
          a[i,.,.] = 1.0;
      endfor;
      for i(31, nobs, 1);
          a[i,.,.] = 1.5;
      endfor;
      retp(a);
  endp;

  struct ssControl ssctl;
  ssctl = ssControlCreate(1, 1, 1, nobs);
  ssctl.tvp.Z = buildZ(nobs);
  ssctl.tvp.T = 1;
  ssctl.tvp.c = 0;
  ssctl.tvp.R = 1;
  ssctl.tvp.d = 0;
  ssctl.tvp.H = 0.25;
  ssctl.param_names = "Q";
  ssctl.positive_vars = 1;

  proc (0) = updateTVPModel(struct tvpModel *tvpmod, param);
      tvpmod->Q = param[1];
  endp;

  struct ssOut sOut;
  sOut = ssFitTVP(&updateTVPModel, { 0.3 }, y, ssctl);

  // Compute forecasts
  forecasts = ssPredictTVP(sOut, y);

Remarks
-------

In-sample values come directly from ``sOut.kfResults`` and are already correctly time-varying, since :func:`ssFitTVP` ran the filter with the real period-by-period system matrices throughout. Out-of-sample forecasts have no known future ``Z``/``T``/``R``/``Q``/``H``/``c``/``d`` -- there is no evolution model for how a time-varying matrix would keep changing beyond the fitted sample -- so they are produced by freezing the system at its last fitted period (``nobs``) and propagating forward from there, a "last value carried forward" assumption for the time-varying parameters themselves (not just the state). This function should be called after the :class:`ssOut` structure has been filled by :func:`ssFitTVP`. See also :func:`ssPredictSETVP` for the standard errors of these forecasts.


Source
------

sstvp.src

.. seealso:: Functions :func:`ssFitTVP`, :func:`ssPredict`, :func:`ssPredictSETVP`, :func:`ssIRFTVP`
