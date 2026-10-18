
ssIRFTVP
==============================================

Purpose
----------------

Computes the impulse response function for a fitted time-varying-parameter model, with the system matrices frozen at their values for one specific period ("time-specific" impulse responses).

.. note::
   **GAUSS 26.1.4+ (sslib 2.0.0).** The optional arguments below are
   keyword arguments and may be supplied by name, in any order. The
   positional order is unchanged from 1.0.0, so existing positional calls
   keep working. See :ref:`v1-to-v2-migration`.

Format
----------------
.. function:: irf = ssIRFTVP(tvpFinal, base_period, horizon, impulse [, orthogonalized, cumulative])

    :param tvpFinal: a filled instance of a :class:`tvpModel` structure (e.g. ``sOut.tvpFinal`` after :func:`ssFitTVP`).
    :type tvpFinal: Struct

    :param base_period: The period (1..nobs) whose system matrices are held fixed over the horizon.
    :type base_period: Scalar

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

  // Impulse response computed with the system frozen at period 10
  // (Z = 1.0) versus period 40 (Z = 1.5)
  irf_early = ssIRFTVP(sOut.tvpFinal, 10, 4, 1);
  irf_late = ssIRFTVP(sOut.tvpFinal, 40, 4, 1);

After running the above code, ``irf_early`` is constant at 1.0 and ``irf_late`` is constant at 1.5 across the horizon (this model's ``T = 1``, so the state never decays; only ``Z``, and therefore the scale of the response, differs between the two frozen periods).

Remarks
-------

A time-varying ``Z``/``T``/``R``/``Q`` has no defined value beyond the fitted sample and no evolution model of its own, so "what happens after a shock" isn't answerable without first freezing the system at some point in time -- this is the standard convention for impulse responses in time-varying-parameter models (e.g. Primiceri, 2005). This function should be called after the :class:`ssOut` structure has been filled by :func:`ssFitTVP`. A model whose matrices are all time-invariant (a constant wrapped in a one-page array, as with ``T``/``c``/``R``/``d``/``H`` in the example above) gives the same impulse response regardless of *base_period*, since there is then nothing to freeze differently from one period to the next.


Source
------

sstvp.src

.. seealso:: Functions :func:`ssFitTVP`, :func:`ssIRF`, :func:`ssPredictTVP`
