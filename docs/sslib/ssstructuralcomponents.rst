
ssStructuralComponents
==============================================

Purpose
----------------

Decomposes a fitted structural time series model into its smoothed, additive unobserved components on the **observation scale** -- trend, each seasonal block, each cycle, the regression contribution, their total (the *signal*), and the leftover *irregular*.

.. note::
   Requires **GAUSS 26.1.4+** (sslib 2.0.0). ``components`` needs no preceding ``struct ssStructuralComponents components;`` declaration -- the procedure declares its own return type. See :ref:`v1-to-v2-migration` on the landing page.

Format
----------------
.. function:: components = ssStructuralComponents(sOut, y)

    :param sOut: a filled :class:`ssOut` structure returned by :func:`ssStructuralTS`. The resolved structural specification travels on the result itself (``sOut.structural``), so the original ``trend``/``seasonal_period``/``seasonal_type``/``seasonal_harmonics``/``cycle`` arguments do **not** have to be repeated here, and fitting another model in between cannot corrupt this one. An :class:`ssOut` from :func:`ssFit`, :func:`ssFitTVP`, :func:`ssARIMA` or :func:`ssSARIMA` is rejected with a clear error.
    :type sOut: struct

    :param y: nobs x 1 matrix, the same observed data :func:`ssStructuralTS` was fitted to. Needed only for the irregular (``y - signal``); its row count is checked against the fitted model's.
    :type y: Matrix

    :return components: an :class:`ssStructuralComponents` structure with the members below.
    :rtype components: struct

Output members
----------------

Every component is **nobs x 1** (or nobs x n_blocks) -- one *row* per period.

.. list-table::
   :widths: 22 78
   :header-rows: 1

   * - Member
     - Description
   * - ``trend``
     - nobs x 1 smoothed observation-level trend contribution. For ``trend="trend"`` (local linear trend) this is the smoothed **level** contribution: the slope enters the observation equation only through the level it accumulates into, never directly.
   * - ``slope``
     - nobs x 1 smoothed slope **state** when the model has one, empty otherwise. This is a state, not a separately additive observation component -- it is deliberately *not* part of ``signal``, ``components``, or the reconstruction identity.
   * - ``seasonal``
     - nobs x n_seasonal, one column per seasonal block in the original ``seasonal_period`` input order. Each column is that block's full observation loading applied across its own state slice, so a trigonometric block's harmonics are already summed into one column. Empty when the model has no seasonal blocks.
   * - ``cycle``
     - nobs x n_cycle, one column per cycle in input order. Empty when the model has no cycles.
   * - ``regression``
     - nobs x 1 fitted observation-intercept contribution (``x_t'beta``), recovered from the fitted time-varying intercept. **Always present**; all zeros when the model has no ``xreg``.
   * - ``signal``
     - nobs x 1, ``trend + rowsum(seasonal) + rowsum(cycle) + regression``.
   * - ``irregular``
     - nobs x 1, ``y - signal`` at every observed period; **missing** wherever ``y`` is missing.
   * - ``components``
     - nobs x k combined additive observation components, in the documented order: trend, then each seasonal block, then each cycle, then regression. Its columns sum exactly to ``signal``. ``slope`` and ``irregular`` are excluded.
   * - ``component_names``
     - k x 1 string array naming the columns of ``components``, aligned exactly.
   * - ``smoothed_state``
     - k_states x nobs smoothed state means, exactly as :func:`ssKalmanSmooth` returns them (one *column* per period -- **not** transposed to match the component orientation).
   * - ``smoothed_state_cov``
     - nobs x k_states x k_states smoothed state covariances.

Column names follow the same "no suffix when there is exactly one" convention :func:`ssStructuralTS` uses for parameter names::

    "trend"  "seasonal"                  "cycle"              "regression"
    "trend"  "seasonal.1" "seasonal.2"   "cycle.1" "cycle.2"  "regression"

Absent-component convention
^^^^^^^^^^^^^^^^^^^^^^^^^^^

``slope``, ``seasonal`` and ``cycle`` are set to an **empty matrix** (``{}``, 0x0) when the fitted model has no slope / no seasonal blocks / no cycles. GAUSS cannot reliably carry an nobs x 0 matrix through a structure field, so an empty matrix is used rather than inventing placeholder all-zero columns that would be indistinguishable from a genuinely estimated zero component. Test with ``rows(components.cycle) == 0``, or read ``n_cycle`` and friends from ``sOut.structural``.

``regression`` is the one exception: it is **always** a genuine nobs x 1 vector, all zeros without ``xreg``, because it occupies exactly one additive slot whether or not it is estimated -- which keeps the reconstruction identity uniform.

The reconstruction identity
----------------------------

For every **observed** period, to numerical precision::

    y = trend + rowsum(seasonal) + rowsum(cycle) + regression + irregular
      = signal + irregular

This is an algebraic identity in whatever smoothed states the smoother produced, not a numerical approximation, and the test suite checks it at 1e-12 across every supported model configuration.

Examples
----------------

Trend + trigonometric seasonality + regression::

    new;
    library sslib, cmlmt, tsmt;

    // Monthly airline passengers, 1949-1960, in logs
    fname = getGAUSSHome("pkgs/sslib/examples/airline.dat");
    y = loadd(fname, "ln(passengers)");

    // An illustrative regressor: a step from the 61st month (1954) onward
    step = zeros(60, 1) | ones(rows(y)-60, 1);

    // Local linear trend, a monthly trigonometric seasonal block
    // truncated to 2 harmonics, and the regressor.
    // No `struct ssOut sOut;` declaration needed.
    sOut = ssStructuralTS(y,
                          trend="trend",
                          seasonal_period=12,
                          seasonal_type="trig",
                          seasonal_harmonics=2,
                          xreg=step);

    components = ssStructuralComponents(sOut, y);

    // trend, seasonal, regression -- each column nobs x 1
    print "component columns:" components.component_names';

    // Confirm the decomposition adds back up
    print "max reconstruction error:"
          maxc(abs(y - components.signal - components.irregular));

A simple local level decomposition::

    sOut = ssStructuralTS(y);
    components = ssStructuralComponents(sOut, y);

    // rows(components.seasonal) == 0 and rows(components.slope) == 0 here;
    // components.regression is an all-zero nobs x 1 column.

Remarks
-------

**Component estimates condition on the fitted parameters.** They are smoothed states evaluated at ``sOut.final_params`` and carry no allowance for parameter-estimation uncertainty. Treat them as "the decomposition implied by this fit", not as estimates with their own standard errors.

**Component standard errors are deliberately not provided.** ``smoothed_state_cov`` is returned as-is, but turning it into per-component intervals requires the cross-component covariance blocks and, for the irregular, the covariance of ``y`` conditioned on the smoothed signal -- neither of which can be read off a diagonal, and both of which are easy to get quietly wrong.

**No refiltering.** Smoothing uses :func:`ssKalmanSmooth`, or :func:`ssKalmanSmoothTVP` for a model fitted with ``xreg``, fed the :class:`kalmanResult` already stored on ``sOut``. The model is never refiltered and never refitted -- this is one backward pass over existing results.

**Diffuse-phase accuracy caveat.** :func:`ssStructuralTS` uses the exact diffuse filter, which reports only the *proper* part of the filtered state covariance (``P_star``) while the diffuse part (``P_inf``) is still nonzero. The Rauch-Tung-Striebel backward pass therefore reproduces an exact diffuse *smoother* only for periods after the **actual** diffuse phase has resolved.

For a fully observed, observable structural model that opening phase is generally covered by the configured ``sOut.likelihoodburn``, so in ordinary use "after the first ``sOut.likelihoodburn`` periods" is the right expectation. ``sOut.likelihoodburn`` is a *fixed* count, though -- the number of diffuse states -- and **not** a universal per-period accuracy boundary for component smoothing: missing or insufficiently informative observations at the start of the sample delay the resolution of the diffuse part and so extend the actual diffuse phase beyond that count.

A concrete case, pinned down in ``test/ssstructuralcomponentsref.inc``: fit a local level model whose first two observations are missing. ``sOut.likelihoodburn`` is 1, so period 2 is nominally "after the burn", yet it is still inside the unresolved diffuse phase -- its smoothed trend comes out ``0.582``, roughly half the ``1.164`` an exact diffuse smoother reports, while period 1 comes out exactly 0. For a local linear trend the same effect is easy to recognize at the very first period: the smoothed slope comes out exactly 0, because the proper covariance has no rank in that direction yet.

Within the actual diffuse phase, however long it runs, the components are still a well-defined, finite decomposition, and the reconstruction identity above still holds exactly wherever ``y`` is observed (it is algebraic) -- but they are not identical to what an exact diffuse smoother would report and should not be compared against one there. A genuine exact diffuse smoother, which would remove this caveat entirely, is separate future work and is not implemented here.

Validated against statsmodels' ``tsa.statespace.structural.UnobservedComponents``, evaluated at the same fitted parameters (so the comparison is between *smoothers*, not optimizers). Smoothed trend, level, slope and the seasonal block contribution all agree to ~1e-10 once the actual diffuse phase has resolved -- including for the leading-missing case above, where agreement over the tail of the sample is ~7e-10 despite the extended opening phase. See ``test/ssstructuralcomponentsref.inc``.

A dummy block and a full-harmonic trigonometric block of the same period produce the same seasonal component path to ~1e-13 despite using genuinely different state vectors -- an independent confirmation that each block's own observation loading is applied correctly.

Source
------

ssstructural.src

.. seealso:: Functions :func:`ssStructuralTS`, :func:`ssKalmanSmooth`, :func:`ssKalmanSmoothTVP`
