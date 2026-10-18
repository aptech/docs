
ssARIMA
==============================================

Purpose
----------------

Estimates an ARIMA(p, d, q) model via its state space representation, using Kalman filtering and maximum likelihood estimation, and returns the fitted model in this library's own :class:`ssOut` interface -- the same output shape :func:`ssFit` produces for a custom model. A thin convenience wrapper around :func:`ssSARIMA` with every seasonal order fixed at 0; the actual optimization is delegated to TSMT's ``sarimaSS``, not this library's own :func:`ssFit`.

.. note::
   **GAUSS 26.1.4+ (sslib 2.0.0).** This procedure declares its return
   type, so the result needs no preceding ``struct`` declaration, and the
   optional arguments below are keyword arguments that may be supplied by
   name, in any order. The positional order is unchanged from 1.0.0, so
   existing positional calls keep working. See :ref:`v1-to-v2-migration`.

Format
----------------
.. function:: sOut = ssARIMA(y, p [, d, q, const, trend])

    :param y: Vector, observed data.
    :type y: Vector

    :param p: Scalar, autoregressive (AR) order.
    :type p: Scalar

    :param d: Optional argument, scalar, default 0. Order of regular (non-seasonal) differencing.
    :type d: Scalar

    :param q: Optional argument, scalar, default 0. Moving-average (MA) order.
    :type q: Scalar

    :param const: Optional argument, scalar, default 0. Nonzero to include a constant term.
    :type const: Scalar

    :param trend: Optional argument, scalar, default 0. Nonzero to include a linear time trend.
    :type trend: Scalar

    :return sOut: an instance of an :class:`ssOut` structure -- see :func:`ssFit` for the full member list. ``sOut.ssmFinal`` holds the state space representation of the fitted ARIMA model.
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

    // Fit an ARIMA(2, 0, 0) model
    struct ssOut sOut;
    sOut = ssARIMA(y, 2);

Remarks
-------

Equivalent to ``ssSARIMA(y, p, d, q, 0, 0, 0, 0, const, trend)`` -- see :func:`ssSARIMA` for the seasonal generalization and for how parameters are ordered/named in the printed output.

Source
------

ssarima.src

.. seealso:: Functions :func:`ssSARIMA`, :func:`ssFit`, :func:`ssStructuralTS`, :func:`ssIRF`, :func:`ssPredict`
