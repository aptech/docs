
ssKalmanSmooth
==============================================

Purpose
----------------

Performs the Rauch-Tung-Striebel backward recursion smoother for state variables and state covariances.

Format
----------------
.. function:: { a_smooth, p_smooth } = ssKalmanSmooth(ssm, y)
              { a_smooth, p_smooth } = ssKalmanSmooth(ssm, kfRslt)

    :param ssm: A filled instance of a :class:`ssModel` structure.
    :type ssm: Structure

    :param y: Optional, data. If a data matrix is passed, a first stage Kalman filtering will be performed.
    :type y: Matrix

    :param y: Optional, a filled instance of the :class:`kalmanResult` structure. If a :class:`kalmanResult` structure is passed, no first stage Kalman filtering is performed.
    :type y: Matrix

    :return a_smooth: Smoothed state variable.
    :rtype a_smooth: Vector

    :return p_smooth: Smoothed state covariances.
    :rtype p_smooth: Array

Examples
----------------

::

  new;
  library tsmt, sslib, cmlmt;

  y = loadd(getGAUSSHome $+ "pkgs/tsmt/examples/nile.dat");

  sigma_e = 15099;
  sigma_n = 1469.1;

  // Initialize Kalman filter
  a_0 = 0;
  p_0 = 10e7;

  // Specify state-space system matrices
  struct ssModel ssm;
  ssm.Z = 1;
  ssm.H = sigma_e;
  ssm.T = 1;
  ssm.Q = sigma_n;
  ssm.R = 1;
  ssm.d = 0;
  ssm.c = 0;

  struct kalmanResult rslt;
  rslt = sskalmanFilter(y, ssm, a_0, p_0);

  // Smooth data
  { a_smooth, p_smooth } = kalmanSmooth(ssm, rslt);


The first five observations of the filtered state variable compared to the smoothed state variable are:

::

    rslt.filtered_state[1:5]
     1119.830917
     1140.845842
     1072.750253
     1117.275521
     1129.948494

    a_smooth[1:5]
     1111.623497
     1110.824812
     1105.241488
     1113.497953
     1112.364977

Source
------

ssmain.src

.. seealso:: Functions :func:`ssgetAICC`, :func:`ssgetBIC`, :func:`ssgetHQIC`
