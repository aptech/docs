
ssStructuralTS
==============================================

Purpose
----------------

Estimates a univariate structural time series model (Harvey 1989's "Basic Structural Model" family) -- an unobserved-components decomposition of ``y_t`` into a trend and, optionally, a seasonal component and a stochastic cycle, plus an irregular (observation-noise) term -- via :func:`ssFit`/:func:`ssFitTVP`, exactly the same way a user-defined custom model would be, just with the state space representation and update procedure built internally. Unlike :func:`ssARIMA`/:func:`ssSARIMA` (which delegate the actual optimization to TSMT's ``sarimaSS``), there is no TSMT equivalent for structural models, so this is built directly on this library's own :func:`ssFit`/:func:`ssFitTVP` and its exact diffuse Kalman filter.

.. note::
   **GAUSS 26.1.4+ (sslib 2.0.0).** This procedure declares its return
   type, so the result needs no preceding ``struct`` declaration, and the
   optional arguments below are keyword arguments that may be supplied by
   name, in any order. The positional order is unchanged from 1.0.0 (see
   the note after the examples). See :ref:`v1-to-v2-migration`.

Format
----------------
.. function:: sOut = ssStructuralTS(y [, trend, seasonal_period, cycle, cycle_period_guess, xreg, param_start, ssctl, seasonal_type, seasonal_harmonics])

    ``y`` is the only required argument. Every argument after it is an
    optional keyword argument with the default shown below::

        sOut = ssStructuralTS(y, seasonal_period=12);

        sOut = ssStructuralTS(y,
                              trend="trend",
                              seasonal_period=4|12,
                              seasonal_type={"dummy", "trig"},
                              seasonal_harmonics=0|2);

    :param y: Vector, observed data.
    :type y: Vector

    :param trend: Optional keyword argument, string, default ``"level"``. ``"level"`` for a local level trend (``mu[t+1] = mu[t] + eta[t]`` -- a random walk) or ``"trend"`` for a local linear trend (``mu[t+1] = mu[t] + beta[t] + eta[t]``; ``beta[t+1] = beta[t] + zeta[t]`` -- a random walk with a stochastically evolving slope).
    :type trend: String

    :param seasonal_period: Optional keyword argument, scalar 0 (the default, no seasonal component) or a scalar/vector of periods ``s >= 2``, one per seasonal block (e.g. 4 for quarterly, 12 for monthly data) -- each block has its own independently estimated variance. A vector may not mix 0 with real periods -- 0 only ever means "no seasonal blocks at all," as a lone value. A scalar ``s >= 2`` is just the one-block case.
    :type seasonal_period: Scalar or Vector

    :param cycle: Optional keyword argument, scalar. 0 (the default, no cycle) or a positive integer COUNT of independent stochastic cycle components (Harvey 1989): each is a damped, stochastically-perturbed sine wave ``[psi[t]; psi*[t]]`` with transition matrix ``rho*[[cos(lambda), sin(lambda)], [-sin(lambda), cos(lambda)]]``, only ``psi[t]`` entering the observation equation. Each cycle's own ``rho`` (damping, in (0,1)) and ``lambda`` (frequency, in (0,pi), i.e. period ``2*pi/lambda``) are both estimated, parameterized via sigmoid transforms applied internally. ``rho`` is capped at ``0.999999`` rather than at 1, because the sigmoid confines it to (0,1) only in exact arithmetic: a ``rho`` that reaches 1 in floating point leaves the cycle with no stationary distribution to initialize from, which previously aborted the whole program from inside a likelihood evaluation. A fit whose reported damping sits *at* that cap should be read as a diagnostic rather than an estimate -- the data wanted a nonstationary cycle, which this model cannot represent -- and is worth comparing against a specification that puts the component in the trend instead.
    :type cycle: Scalar

    :param cycle_period_guess: Optional keyword argument, scalar or a vector with one entry per cycle. Default ``{}``, meaning that for a single cycle (``cycle = 1``) the period is **estimated from the data**: the dominant periodogram peak of the differenced series, after subtracting the spectral shapes the model's other components are known to contribute (including a stochastic slope's, for ``trend = "trend"``) and excluding the frequencies the model's seasonal blocks represent -- every harmonic of a dummy or full trigonometric block, only the first ``h`` of a trigonometric block truncated to ``h`` harmonics. Only used to seed each cycle's frequency starting value (``2*pi/cycle_period_guess``); the actual period is freely estimated from there, this is not a constraint. Ignored if ``cycle = 0``. When a scalar is supplied and ``cycle > 1``, the single guess is auto-spread geometrically across cycles (``period_guess_k = cycle_period_guess * 1.5^(k-1)``) rather than repeated literally, since identical starting frequencies for two cycles create an exact, degenerate exchange symmetry between them -- a bad optimizer starting point. Supply an explicit vector to override this spread.

        The default **changed** from a fixed ``10``. With ``cycle > 1`` the default is still ``10`` spread geometrically, because a single periodogram measurably shows only the dominant cycle: seeding several cycles from it broke a two-cycle fit that the fixed default got right. Supplying a value is unaffected, and ``10`` is still what you get wherever the estimate declines -- fewer than 12 usable differences, a gap in the series, or every candidate frequency belonging to a seasonal block. The estimate is only moderately accurate (on a steep stochastic slope it still tends to seed a cycle too long), which in measured cases cost iterations rather than a worse optimum. The change is measured rather than theoretical: on a near-unit-root cycle with a true period of 40, the old fixed default converged to a local optimum 37.3 log-likelihood below the one the same series reaches from a period seeded near the truth. **If you know the periodicity you are looking for, pass it** -- that is still strictly better than any estimate from the data.
    :type cycle_period_guess: Scalar or Vector

    :param xreg: Optional keyword argument, default ``{}`` (no regressors), an nobs x k_reg matrix of explanatory regressors (e.g. a known intervention dummy, temperature, price -- anything observed every period). When supplied, ``y[t] = mu[t] + gamma[t] + [cycle] + x[t]'*beta + epsilon[t]``, with ``beta`` a free (unconstrained, not variance-constrained) coefficient vector estimated alongside the variance parameters, named ``"beta.1"``, ``"beta.2"``, etc. This changes HOW the model is fit and what ``sOut`` contains -- see Remarks.
    :type xreg: Matrix

    :param param_start: Optional keyword argument, default ``{}``, k_params x 1 starting values, in the same order as ``sctl.param_names`` (``"sigma2.irregular"``, ``"sigma2.level"``, [``"sigma2.slope"``], [``"sigma2.seasonal"``], [``"sigma2.cycle"``, ``"frequency.cycle"``, ``"damping.cycle"``], [``"beta.1"``, ..., ``"beta.k_reg"``]). Default: splits an estimate of the total innovation variance (from the first difference of ``y``) evenly across whichever *variance* components are active, seeds frequency/damping as described above, and starts every ``beta`` at zero.
    :type param_start: Vector

    :param ssctl: Optional keyword argument, default ``{}``, an instance of an :class:`ssControl` structure for fine-tuning estimation (e.g. ``sctl.ctl`` for cmlmt options). If supplied, ``sctl.param_names``/``positive_vars``/``init``/``gradproc`` are overwritten to the values this function requires; everything else (e.g. ``sctl.ctl``) passes through.
    :type ssctl: struct

    :param seasonal_type: Optional keyword argument, string ``"dummy"`` (the default) or ``"trig"``, or a string array with one entry per seasonal block. ``"trig"`` builds a trigonometric (Fourier) seasonal block instead of a dummy-variable one -- see ``seasonal_harmonics`` below and Remarks. A scalar broadcasts to every block; a vector must have exactly one entry per ``seasonal_period`` entry.
    :type seasonal_type: String or String array

    :param seasonal_harmonics: Optional keyword argument, scalar 0 (the default) or a vector with one entry per seasonal block, giving the integer number of harmonics a ``"trig"`` block uses (ignored for ``"dummy"`` blocks). 0 means "full harmonics" (``floor(period/2)`` for that block's own period) -- NOT "this block is absent" (that is ``seasonal_period``'s own, different, 0 sentinel; 0 is never a valid EXPLICIT harmonics count, so there is no ambiguity between the two). A value below ``floor(period/2)`` retains harmonics 1 through ``h``, using far fewer states than a dummy block of the same period -- see Remarks for why this matters.
    :type seasonal_harmonics: Scalar or Vector

    :return sOut: an instance of an :class:`ssOut` structure. Without ``xreg``, exactly as :func:`ssFit` returns -- :func:`ssIRF`/:func:`ssPredict`/:func:`ssPredictSE` and every diagnostic in ``sOut`` work on a fitted structural model exactly as they do on a custom :func:`ssFit` model. WITH ``xreg``, exactly as :func:`ssFitTVP` returns instead -- the fitted model is in ``sOut.tvpFinal``, not ``sOut.ssmFinal``, and post-estimation needs :func:`ssIRFTVP`/:func:`ssPredictTVP`/:func:`ssPredictSETVP`, not :func:`ssIRF`/:func:`ssPredict`/:func:`ssPredictSE` (see Remarks for why).
    :rtype sOut: struct

Examples
----------------

::

    new;
    library sslib, cmlmt, tsmt;

    // Monthly airline passengers, 1949-1960, in logs
    fname = getGAUSSHome("pkgs/sslib/examples/airline.dat");
    y = loadd(fname, "ln(passengers)");

    // Local linear trend with a dummy-variable monthly seasonal
    // component. No `struct ssOut sOut;` declaration needed.
    sOut = ssStructuralTS(y, trend="trend", seasonal_period=12);

    // The same model with a trigonometric seasonal block truncated to
    // 2 harmonics instead of a dummy-variable block's 11 states
    sOut2 = ssStructuralTS(y, trend="trend", seasonal_period=12,
                           seasonal_type="trig", seasonal_harmonics=2);

    // Decompose a fit into its smoothed unobserved components
    components = ssStructuralComponents(sOut, y);

    // Annual Nile river flow, 1871-1970
    nile = loadd(getGAUSSHome("pkgs/tsmt/examples/nile.dat"));

    // Local level model with a level-shift regressor from 1899
    // (observation 29) onward -- post-estimation needs the TVP variants
    shift = zeros(28, 1) | ones(rows(nile)-28, 1);
    sOut3 = ssStructuralTS(nile, xreg=shift);
    forecasts = ssPredictTVP(sOut3, nile);

    // Local level model with a stochastic cycle. With cycle_period_guess
    // omitted, the cycle's starting period is estimated from the data.
    sOut4 = ssStructuralTS(nile, cycle=1);

Positional calls keep the 1.0.0 argument order, so a 1.0.0 call such as
``ssStructuralTS(y, "trend", 12)`` still runs. Positional arguments cannot
be skipped, however: to reach ``seasonal_type`` or ``seasonal_harmonics``
positionally, every argument before them needs a real value, including
``param_start`` (a k_params x 1 vector) and ``ssctl`` (an
:class:`ssControl` structure). A placeholder ``0`` for ``param_start`` is
rejected because it does not have k_params rows (in 1.0.0 as well), and
2.x also rejects a ``0`` for ``ssctl``. Use the keyword form instead,
as in the examples above. An unchanged call can still return different
estimates than it did in 1.0.0, for example because a single cycle's
default starting period is now estimated from the data; see the upgrade
notes in ``CHANGELOG.md``. See :ref:`v1-to-v2-migration`.

Remarks
-------

``sctl.init`` is always forced internally: ``"diffuse"`` (every state diffuse) when there is no cycle, or ``"mixed"`` when there is -- every cycle's own unconditional/stationary covariance (solving its own small Lyapunov equation) for its own 2 states (all cycles occupy one contiguous trailing ``2*cycle``-state block, since cycles are always assembled last), diffuse for the non-stationary trend/seasonal states. This is a deliberate choice on state-space-theory grounds (a genuinely stationary component's own unconditional distribution is the natural, most information-efficient prior for it -- Durbin & Koopman 2012), NOT a move to match statsmodels: statsmodels' ``UnobservedComponents`` does NOT treat a stochastic cycle this way -- a plain ``UnobservedComponents(cycle=True)`` run is not the right independent check for this function's cycle likelihood. Both a pure-diffuse and a mixed treatment give a valid (consistent) MLE; they differ only in how the likelihood contribution of the first few observations is computed, so this function's own reported log-likelihood with a cycle differs from what a same-parameters statsmodels ``UnobservedComponents`` run reports, deliberately. It WAS validated, precisely (~1e-9 per period), against statsmodels' lower-level ``Initialization`` primitives configured by hand for this exact same mixed scheme -- see ``test/ssstructuralcycle.inc`` for exactly how.

The returned ``sOut`` carries a resolved copy of the specification actually fitted in ``sOut.structural`` (an :class:`ssStructuralInfo` structure): ``is_structural``, ``trend``, ``seasonal_periods``, ``seasonal_types`` and ``seasonal_harmonics`` **after** scalar broadcasting, ``n_cycle``, ``has_xreg``, ``k_reg``, ``beta_index`` (where ``beta`` starts inside ``final_params``), ``k_states``, ``k_posdef`` and ``nobs``. :func:`ssStructuralComponents` reads its specification from there, so the original arguments never have to be repeated, and fitting another model afterwards cannot corrupt an earlier result. Results from :func:`ssFit`, :func:`ssFitTVP`, :func:`ssARIMA` and :func:`ssSARIMA` set ``structural.is_structural = 0`` and are rejected by :func:`ssStructuralComponents`.

.. seealso:: Function :func:`ssStructuralComponents`

Every *variance* parameter is constrained positive via ``sctl.positive_vars`` (``theta = u^2``, as elsewhere in this library). ``sctl.gradproc`` is set internally, so CMLMT receives an analytic gradient rather than numerically differentiating the whole likelihood; any ``gradproc``/``init``/``stationary_states`` supplied via an input ``ssctl`` is overwritten the same way ``param_names``/``positive_vars`` already are.

Any number of seasonal blocks and cycles are supported, each independently either a dummy-variable or a trigonometric block (see ``seasonal_type``/``seasonal_harmonics`` above). Parameter names stay exactly as before (``"sigma2.seasonal"``, ``"sigma2.cycle"``, ``"frequency.cycle"``, ``"damping.cycle"``) when there's exactly one of that block type, and gain a ``".1"``/``".2"``/... suffix per block, in input order, when there's more than one (mirroring how ``xreg``'s own ``"beta.1"``/``"beta.2"`` naming already works) -- a block's TYPE is never encoded in its parameter name, only in the internal spec. The full parameter vector orders as: all *variance* parameters first (irregular, level, [slope], one per seasonal block, one per cycle -- this contiguous grouping is what keeps ``sctl.positive_vars`` a simple range), then each cycle's own (frequency, damping) pair in turn, then ``beta`` (if ``xreg`` is supplied). Every seasonal block, dummy or trig, still consumes exactly ONE variance parameter regardless of how many states/harmonics it uses.

A trigonometric ("trig") seasonal block of period ``s`` with ``h`` harmonics (Harvey 1989) represents the same kind of seasonal effect as a dummy block but as a sum of ``h`` rotating harmonic components instead of ``period-1`` lagged dummy states, letting ``h`` be truncated well below ``floor(period/2)`` -- important for a long period such as annual seasonality in hourly data (``period=8760``). Using full harmonics makes the trig block a reparameterization-equivalent alternative to a dummy block. The equivalence requires every harmonic state to share the dummy block's one scalar seasonal disturbance. For each ordinary harmonic ``j``, with ``lambda[j] = 2*pi*j/s``, the fixed cosine/sine loading vector in ``R`` is ``[(2/s)*(1-cos(lambda[j])); -(2/s)*sin(lambda[j])]``; the Nyquist state, present only for even ``s``, has loading ``2/s``. These are the real Fourier coefficients of the dummy block's one-period impulse response ``(1, -1, 0, ..., 0)``. Consequently ``R`` has one column per trig block and ``Q`` contains that block's single ``sigma2`` parameter. A truncated block keeps these loadings for harmonics 1 through ``h`` and is the corresponding low-frequency projection. Since ``R``/``Z``/``T`` depend only on fixed period/harmonics, ``dR``/``dZ``/``dT`` remain exactly zero.

A full-harmonics trig block's diffuse log-likelihood need not numerically equal an equivalent dummy block's: both representations initialize ``P_inf`` as identity rather than transforming the diffuse prior through the non-orthogonal Fourier change of basis, which can introduce a fixed additive offset. The underlying transfer dynamics are nevertheless identical; ``test/ssstructuraltrigseasonal.inc`` verifies the exact impulse-response identity directly for periods 2 through 11.

**Regressors (xreg)** require a time-varying intercept (``d[t] = x[t]'*beta``), which the time-invariant :class:`ssModel`/:func:`ssFit` this function otherwise uses cannot express at all (``d`` is a single fixed vector there, not one value per period) -- this function builds the SAME trend/seasonal/cycle ``Z``/``T``/``R``/``Q`` as the no-regressor case (wrapped as constant, one-page :class:`tvpModel` arrays, splitting out only ``d`` as genuinely time-varying) and fits via :func:`ssFitTVP` instead of :func:`ssFit`, exactly the same "custom model" pattern, just against the time-varying rather than time-invariant escape hatch. This means the returned ``sOut`` differs from the no-regressor case exactly the way :func:`ssFitTVP`'s own output always differs from :func:`ssFit`'s: the fitted model is in ``sOut.tvpFinal``, and post-estimation needs :func:`ssIRFTVP`/:func:`ssPredictTVP`/:func:`ssPredictSETVP`. Those freeze the system at one period (:func:`ssIRFTVP`) or the last fitted period (:func:`ssPredictTVP`/:func:`ssPredictSETVP`) for anything beyond the fitted sample -- for a model with regressors this means ``beta``'s contribution to the forecast is frozen at ``x[t]'*beta`` using the LAST period's ``x[t]`` forever after, since there is no known future ``x[t]`` to use instead.

Validated against statsmodels' ``tsa.statespace.structural.UnobservedComponents`` (an independent, third-party structural-time-series implementation, whose state space construction matches this one exactly, element for element, for every model configuration tested, including the cycle's ``T``/``Z``/``R``/``Q``) for local level and local linear trend, with and without a single seasonal component (WITHOUT a cycle -- see above for why a cycle needs a different, more precise comparison) -- see ``test/ssstructural.inc``. Parameter estimates match to ~1e-4, but the reported log-likelihood itself will NOT match statsmodels' ``llf`` directly: statsmodels' default ``loglikelihood_burn`` excludes the first ``k_states`` periods (the diffuse phase) from its reported total, while ``sOut``'s loglikelihood/aic/bic here include the exact diffuse contribution for every period, unburned -- this library's existing convention, not a bug; summing this library's own per-period loglikelihood from period ``k_states+1`` onward reproduces statsmodels' ``llf`` exactly in this (no-cycle, every state diffuse) case. ``sOut.likelihoodburn`` IS set to the number of diffuse states here (``k_states`` without a cycle, or ``k_states`` minus ``2*cycle`` states when ``"mixed"`` init is in effect), but that only protects :func:`ssResidDiagnostics`'s residual-based tests from the diffuse phase -- it does not trim the reported likelihood itself.

**Multiple seasonal blocks and cycles** were validated differently, per block type: the underlying Z/T/R/Q assembly for N dummy-variable seasonal blocks and N cycles was validated with direct hand-computed construction checks (``test/ssstructuralmultiseasonal.inc``, ``test/ssstructuralmulticycle.inc``), and the corresponding likelihood/analytic-gradient math was validated against central finite differences (``test/ssstructuralgrad.inc``, Configs C and D). The trig block has its own deterministic construction checks, exact full-harmonic impulse-response equivalence checks, and finite-difference gradient check in ``test/ssstructuraltrigseasonal.inc`` and Config E of ``test/ssstructuralgrad.inc``. No independent implementation supports fitting more than one stochastic cycle, so the multi-cycle case has no external end-to-end comparison.

Regressor support (``xreg``) was validated against statsmodels' ``UnobservedComponents(exog=...)`` the same way as the rest of this function: ``beta`` estimates match to ~1e-4, and the burn-adjusted loglikelihood reproduces statsmodels' ``llf`` exactly -- see ``test/ssstructuralreg.inc``.

Source
------

ssstructural.src

.. seealso:: Functions :func:`ssFit`, :func:`ssFitTVP`, :func:`ssARIMA`, :func:`ssSARIMA`, :func:`ssIRF`, :func:`ssPredict`, :func:`ssKalmanSmooth`
