
ssIRF
==============================================

Purpose
----------------

Computes the impulse response functions based on the final parameters contained in the filled :class:`ssOut` structure.

Format
----------------
.. function:: irf = ssIRF(ssmFinal, horizon, impulse [, orthogonalized, cumulative] )

    :param ssmFinal: a filled instance of an :class:`ssModel` structure.
    :type ssmFinal: Struct

    :param horizon: The number of impulse responses to compute.
    :type horizon: Scalar

    :param impulse: The state innovation to pulse. Must be between 1 and the dimension of the state innovation with a positive definite covariance matrix.
    :type impulse: Scalar

    :param orthogonalized: Optional argument, when set to anything other than 0, orthogonalized impulses are computed. Default = 0.
    :type orthogonalized: Scalar

    :param cumulative: Optional argument, when set to anything other than 0, cumulative impulses are computed. Default = 0.
    :type cumulative: Scalar

    :return irf: Computed impulse responses.
    :rtype irf: Matrix

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

  /*
  ** Impulse response functions
  */
  // Number of horizons
  h = 20;

  // State variable to shock
  impulse = 1;

  // Compute IRFs
  irf = ssIRF(sOut.ssmFinal, h, impulse);

  // Set up procedure for updating SS model
  // structure
  proc (0) = updateSSModel(struct ssModel *ssmod, param);

      // Set up kalman filter matrices
      ssmod->T =  param[1 2]'|(1~0);
      ssmod->Q[1, 1] = param[3];

  endp;

After running the above code, the first five impulse response are:

::

  1.0000000
  0.68445237
  0.0045511204
 -0.31441880
 -0.21731607

Remarks
-------

This function should be called after the :class:`ssOut` structure has been filled by the :func:`ssFit` procedure.


Source
------

ssmain.src

.. seealso:: Functions :func:`ssFit`, :func:`ssPredict`
