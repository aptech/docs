
ssControlCreate
==============================================

Purpose
----------------

Creates default ssControl structure.

.. note::
   **GAUSS 26.1.4+ (sslib 2.0.0).** This procedure declares its return
   type, so the result needs no preceding ``struct`` declaration, and the
   optional arguments below are keyword arguments that may be supplied by
   name, in any order. The positional order is unchanged from 1.0.0, so
   existing positional calls keep working. See :ref:`v1-to-v2-migration`.

Format
----------------
.. function:: ssctl = ssControlCreate(k_states, k_endog [, k_posdef, nobs])

    :param k_states: Number of states.
    :type k_states:  Scalar

    :param k_endog: Number of endogenous variables.
    :type k_endog: scalar

    :param k_posdef: Optional argument, default k_states, the dimension of the state innovation with a positive definite covariance matrix.
    :type k_posdef: scalar

    :param nobs: Optional argument, default 1, number of observations. Leaving this at its default (1) allocates a time-invariant model (``ssctl.ssm``, an :class:`ssModel`); supplying ``nobs > 1`` allocates a time-varying-parameter model instead (``ssctl.tvp``, a :class:`tvpModel`, for use with :func:`ssFitTVP`), and ``ssctl.ssm`` is left empty. See Remarks.
    :type nobs: scalar

    :return ssctl: Instance of :class:`ssControl` struct with members set to default values.

         .. list-table::
            :widths: auto

            * - sctl.param_names
              - String array, parameter names.
            * - sctl.stationary_vars
              - Vector, specifies the index of the variables which should be constrained stationary.
            * - sctl.positive_vars
              - Vector, specifies the index of the variables which should be constrained positive.
            * - sctl.init
              - String, Kalman filter initialization mode: ``"diffuse"`` (default), ``"stationary"``, or ``"mixed"``. See :func:`ssFit`.
            * - sctl.likelihoodburn
              - Scalar, default 1. Number of leading periods :func:`ssResidDiagnostics` excludes from its residual-based tests.
            * - sctl.gradproc
              - Scalar, default 0 (unset -- no analytic-gradient callback).
            * - sctl.ctl
              - Instance of a :class:`cmlmtControl` structure, used for fine-tuning maximum likelihood estimation. Further information is provided in the CMLMT documentation.
            * - sctl.ssm
              - When ``nobs`` is left at its default (1): instance of an :class:`ssModel` structure, contains the state space system matrices used in the Kalman filter, each initialized to zeros of the size shown. Contains the following members:

                .. list-table::
                    :widths: auto

                    * - ssm.Z
                      - k_endog x k_states, design matrix.
                    * - ssm.d
                      - k_endog x 1, observation intercept.
                    * - ssm.H
                      - k_endog x k_endog, observation disturbance covariance.
                    * - ssm.T
                      - k_states x k_states, transition matrix.
                    * - ssm.c
                      - k_states x 1, state intercept.
                    * - ssm.R
                      - k_states x k_posdef, selection matrix.
                    * - ssm.Q
                      - k_posdef x k_posdef, state disturbance covariance.
                    * - ssm.a_0
                      - k_states x 1, initial prior state mean.
                    * - ssm.p_0
                      - k_states x k_states, initial prior state covariance.
            * - sctl.tvp
              - When ``nobs > 1``: instance of a :class:`tvpModel` structure instead of ``ssctl.ssm`` -- same fields as above, except ``Z``/``d``/``H``/``T``/``c``/``R``/``Q`` are each an nobs-page array rather than a single matrix. See :func:`ssFitTVP`.

    :rtype ssctl: struct

Examples
----------------
Because :func:`ssControlCreate` declares its return type, the result needs
no preceding ``struct ssControl ssctl;`` declaration (the declaration is
still allowed).

::

    new;
    library sslib, cmlmt, tsmt;

    /*
    ** Model dimensions
    */
    // Number of endogenous variables
    k_endog = 1;

    // Number of states
    k_states = 2;

    // Initialize structure 'ssctl'
    ssctl = ssControlCreate(k_states, k_endog);

    // A time-varying-parameter model instead needs nobs > 1, which
    // allocates ssctl.tvp (a tvpModel) rather than ssctl.ssm
    nobs = 100;
    ssctlTVP = ssControlCreate(k_states, k_endog, nobs=nobs);

Remarks
-------

``k_posdef`` defaults to ``k_states`` when omitted. Whether ``nobs`` is left at its default (1) determines which of ``ssctl.ssm``/``ssctl.tvp`` is allocated -- there is no single call that allocates both; a model that needs to switch between the time-invariant and time-varying-parameter path needs a separate ``ssControlCreate`` call for each.

Source
------

ssmain.src

.. seealso:: Functions :func:`ssFit`, :func:`ssFitTVP`
