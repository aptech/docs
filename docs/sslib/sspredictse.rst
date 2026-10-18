
ssPredictSE
==============================================

Purpose
----------------

Computes the standard errors of the in-sample predictions or out-of-sample forecasts returned by :func:`ssPredict`, for building confidence intervals (e.g. ``forecast +/- 1.96*se`` for an approximate 95% interval).

.. note::
   **GAUSS 26.1.4+ (sslib 2.0.0).** The optional arguments below are
   keyword arguments and may be supplied by name, in any order. The
   positional order is unchanged from 1.0.0, so existing positional calls
   keep working. See :ref:`v1-to-v2-migration`.

Format
----------------
.. function:: se = ssPredictSE(sOut, y [, start_pred, end_pred])

    :param sOut: a filled instance of an :class:`ssOut` structure.
    :type sOut: Struct

    :param y: Matrix, observed data used to estimate the parameters.
    :type y: Matrix

    :param start_pred: Optional argument, the observation at which to start predictions/forecasts. Default is to compute out-of-sample forecasts starting immediately following the final observations.
    :type start_pred: Scalar

    :param end_pred: Optional argument, the observation at which to end predictions/forecasts. Default is to compute 20 out-of-sample forecasts such that end_pred = numObs + 20. Must be greater than *start_pred*.
    :type end_pred: Scalar

    :return se: k_endog x n matrix of standard errors, one for each value :func:`ssPredict` returns for the same inputs.
    :rtype se: Matrix

Examples
----------------

::

  new;
  library cmlmt, tsmt, sslib;

  /*
  ** Outline the state space process
  */
  // Filename
  fname = getGAUSShome $+ "pkgs/tsmt/examples/enders_sim2.dat";
  y = loadd(fname);
  y = y[., "ar2"];

  // Set up parameter vector and start values
  param_vec_st = asDF(zeros(3, 1), "param");

  param_vec_st[1] = -0.322;
  param_vec_st[2] = 0.433;
  param_vec_st[3] = 0.0025;

  // Declare shape
  k_endog = 1;
  k_states = 2;

  // Declare ssControl structure
  struct ssControl ssctl;
  ssCtl = ssControlCreate(k_states, k_endog);

  // Set fixed parameters of model
  ssctl.ssm.Z = { 1 0 };
  ssctl.ssm.R[1, 1] = 1;

  // Constraint variables
  ssCtl.stationary_vars = 1|2;
  ssCtl.positive_vars = 3;

  // Call ssFit function
  struct ssOut sOut;
  sOut = ssFit(&updateSSModel, param_vec_st, y, ssctl);

  // Compute forecasts and their standard errors
  forecasts = ssPredict(sOut, y);
  se = ssPredictSE(sOut, y);

  // Approximate 95% confidence interval
  lower = forecasts - 1.96*se;
  upper = forecasts + 1.96*se;

  // Set up procedure for updating SS model
  // structure
  proc (0) = updateSSModel(struct ssModel *ssmod, param);

      // Set up kalman filter matrices
      ssmod->T =  param[1 2]'|(1~0);
      ssmod->Q[1, 1] = param[3];

  endp;

Remarks
-------

This function should be called after the :class:`ssOut` structure has been filled by the :func:`ssFit` procedure, with the same *start_pred*/*end_pred* as the corresponding :func:`ssPredict` call so the two line up period-for-period. Kept as a separate function rather than a second return value from :func:`ssPredict` so existing calls that only capture the point forecast keep working unchanged.


Source
------

ssmain.src

.. seealso:: Functions :func:`ssFit`, :func:`ssPredict`, :func:`ssPredictSETVP`
