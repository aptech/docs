
ssSARIMA
==============================================

Purpose
----------------

Estimates a seasonal ARIMA(p, d, q)(P_s, D_s, Q_s)\ :sub:`s` model via its state space representation, using Kalman filtering and maximum likelihood estimation, and returns the fitted model in this library's own :class:`ssOut` interface -- the same output shape :func:`ssFit` produces for a custom model. The actual optimization is delegated to TSMT's ``sarimaSS``; this function translates TSMT's own output (an ``arimamtOut`` structure) into :class:`ssOut`, and builds the state space representation (``sOut.ssmFinal``) of the fitted model.

.. note::
   **GAUSS 26.1.4+ (sslib 2.0.0).** This procedure declares its return
   type, so the result needs no preceding ``struct`` declaration, and the
   optional arguments below are keyword arguments that may be supplied by
   name, in any order. The positional order is unchanged from 1.0.0, so
   existing positional calls keep working. See :ref:`v1-to-v2-migration`.

Format
----------------
.. function:: sOut = ssSARIMA(y, p, d, q, P_s, D_s, Q_s, s [, const, trend])

    :param y: Vector, observed data.
    :type y: Vector

    :param p: Scalar, autoregressive (AR) order.
    :type p: Scalar

    :param d: Scalar, order of regular (non-seasonal) differencing.
    :type d: Scalar

    :param q: Scalar, moving-average (MA) order.
    :type q: Scalar

    :param P_s: Scalar, seasonal autoregressive order.
    :type P_s: Scalar

    :param D_s: Scalar, order of seasonal differencing.
    :type D_s: Scalar

    :param Q_s: Scalar, seasonal moving-average order.
    :type Q_s: Scalar

    :param s: Scalar, seasonal period/frequency (e.g. 4 for quarterly, 12 for monthly data). Ignored when ``P_s = D_s = Q_s = 0``.
    :type s: Scalar

    :param const: Optional argument, scalar, default 0. Nonzero to include a constant term.
    :type const: Scalar

    :param trend: Optional argument, scalar, default 0. Nonzero to include a linear time trend.
    :type trend: Scalar

    :return sOut: an instance of an :class:`ssOut` structure -- see :func:`ssFit` for the full member list. ``sOut.ssmFinal`` holds the state space representation of the fitted SARIMA model; ``sOut.final_params`` holds the estimated AR/seasonal-AR/MA/seasonal-MA coefficients, the innovation variance, and (if requested) the constant/trend coefficients, in that order -- the same order the printed parameter table (see :func:`ssPrintArima`) names them in.
    :rtype sOut: struct

Examples
----------------

::

    new;
    library cmlmt, tsmt, sslib;

    // Load data
    fname = getGAUSShome $+ "pkgs/tsmt/examples/enders_sim2.dat";
    y = loadd(fname);
    y = y[., "ar2"];

    // Fit a seasonal ARIMA(1, 0, 0)(1, 0, 0)_4 model with a constant
    struct ssOut sOut;
    sOut = ssSARIMA(y, 1, 0, 0, 1, 0, 0, 4, 1);

Remarks
-------

``y`` is differenced (regular order ``d``, seasonal order ``D_s`` at period ``s``) internally, via TSMT's ``simpleDiff``, before computing summary statistics -- ``sOut``'s residual diagnostics and information criteria are therefore based on the differenced series, matching TSMT's own ``sarimaSS`` convention.

:func:`ssARIMA` is a thin convenience wrapper around this function with every seasonal order fixed at 0. :func:`ssStructuralTS` (``ssstructural.src``) is this library's alternative unobserved-components approach to modeling trend/seasonality, built directly on :func:`ssFit`/:func:`ssFitTVP` rather than on TSMT's ``sarimaSS`` -- see :func:`ssStructuralTS` for when that may be a better fit than SARIMA.

Source
------

ssarima.src

.. seealso:: Functions :func:`ssARIMA`, :func:`ssFit`, :func:`ssStructuralTS`, :func:`ssIRF`, :func:`ssPredict`, :func:`ssPrintArima`
