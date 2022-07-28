
ssPredict
==============================================

Purpose
----------------

Computes in-sample predictions or out-of-sample forecasts based on the final parameters contained in the filled :class:`ssOut` structure.

Format
----------------
.. function:: forecasts = ssPredict(sOut, y [, start_pred, end_pred])

    :param sOut: a filled instance of an :class:`ssOut` structure.
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
  library cmlmt, tsmt, ssdev;

  /*
  ** Outline the state space process
  */
  // Filename
  fname = getGAUSShome $+ "pkgs/tsmt/examples/enders_sim2.dat";
  y = loadd(fname, "ar2");

  // Set up parameter vector and start values
  param_vec_st = asDF(zeros(3, 1), "param");

  param_vec_st[1] = -0.322;
  param_vec_st[2] = 0.433;
  param_vec_st[3] = 0.0025;

  // Declare shape
  k_endog = 1;
  k_states = 2;

  // Declare ssControl structure
  struct ssControl ssCtl;
  ssCtl = ssControlCreate(k_states, k_endog);

  // Set fixed parameters of model
  ssCtl.ssm.Z = { 1 0 };
  ssCtl.ssm.R[1, 1] = 1;

  // Constraint variables
  ssCtl.stationary_vars = 1|2;
  ssCtl.positive_vars = 3;

  // Call ssFit function
  struct ssOut sOut;
  sOut = ssFit(&updateSSModel, param_vec_st, y, ssCtl);

  // Compute forecasts
  forecasts= ssPredict(sOut, y);

  // Set up procedure for updating SS model
  // structure
  proc (0) = updateSSModel(struct ssModel *ssmod, param);

      // Set up kalman filter matrices
      ssmod->T =  param[1 2]'|(1~0);
      ssmod->Q[1, 1] = param[3];

  endp;

After running the above code, the first five forecasts are:

::

  -0.10856698
  -0.047276077
   0.018008595
   0.034258528
   0.015093713

Remarks
-------

This function should be called after the :class:`ssOut` structure has been filled by the :func:`ssFit` procedure.


Source
------

ssmain.src

.. seealso:: Functions :func:`ssFit`, :func:`ssIRF`
