longRunSvar
===========

Purpose
-------
Fit a VAR by least squares and identify structural shocks with a lower-triangular long-run impact matrix.

Format
------

.. function:: lr = longRunSvar(y, n_ahead)
              lr = longRunSvar(y, n_ahead, p=2, resid_cov="df")
              lr = longRunSvar(y, n_ahead, p=2, ctl=ctl, quiet=1)

   :param y: Endogenous data, at least two variables. A dataframe's column names label the output; a date-typed column is removed before estimation.
   :type y: Txm matrix or dataframe

   :param n_ahead: Positive integer last horizon. Responses include horizons 0 through n_ahead.
   :type n_ahead: scalar

   :param p: Optional keyword, positive integer lag order. Default = 1.
   :type p: scalar

   :param xreg: Optional keyword, finite exogenous regressors with one row per observation. Default = none.
   :type xreg: TxJ matrix

   :param quiet: Optional keyword, 1 to suppress printing. Default = 0.
   :type quiet: scalar

   :param ctl: Optional keyword, a *longRunSvarControl* from ``longRunSvarControlCreate()``. Its *const* (0 or 1, default 1), *xreg* and *resid_cov* fields control the fit. With *ctl* supplied, the *xreg* and *resid_cov* keywords are ignored; *p* remains a keyword. There is no trend keyword; a deterministic regressor can be supplied through *xreg*.
   :type ctl: struct

   :param resid_cov: Optional keyword, ``"df"`` (default) or ``"ml"``, accepted in any letter case. The first divides residual cross-products by T - p - K, the second by T - p, where K = mp + const + number of xreg columns. An empty *ctl.resid_cov* uses ``"df"``.
   :type resid_cov: string

   :return lr: A *longRunSvarResult* with the following members:

       .. list-table::
          :widths: auto

          * - lr.impact
            - mxm structural impact matrix, response i to shock j in element [i, j].
          * - lr.irf
            - :class:`irfResult`, one-standard-deviation responses, with long-run identification. Each block of m rows holds one horizon, starting at horizon 0.
          * - lr.resid_cov
            - String, covariance choice stored in lowercase: ``"df"`` or ``"ml"``.
          * - lr.m
            - Scalar, number of variables.
          * - lr.p
            - Scalar, lag order.
          * - lr.n_ahead
            - Scalar, last response horizon.
          * - lr.var_names
            - mx1 string array, variable names.

   :rtype lr: struct

Examples
--------

::

    new;
    library timeseries;

    canada_data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/canada.csv"));
    struct longRunSvarResult lr;
    lr = longRunSvar(canada_data, 20, p=2);
    print lr.impact;

    // Use the ML covariance for one-standard-deviation responses
    struct longRunSvarControl lr_ctl;
    lr_ctl = longRunSvarControlCreate();
    lr_ctl.resid_cov = "ml";
    lr = longRunSvar(canada_data, 20, p=2, ctl=lr_ctl, quiet=1);

Remarks
-------

The long-run impact matrix is lower triangular: shock j has no long-run
effect on variables 1 through j - 1. If those variables enter as changes,
the restriction means no permanent effect on their levels. Identification
uses the Cholesky factor of the long-run covariance and maps it back to
the contemporaneous impact matrix (Blanchard and Quah 1989).

The fitted VAR must be stable: all companion eigenvalues must have modulus
below 1. An unstable fit raises an error giving the largest root. The
regression must have full rank and enough residual observations for a
nonsingular covariance; missing or nonfinite data are errors.

The impact matrix and responses follow *resid_cov*. Switching from ML to
df covariance for the same fit increases their size by
:math:`\sqrt{(T-p)/(T-p-K)}`. Forecast error variance shares are unchanged
by this scalar choice. Use :func:`fevdCompute` on *lr.irf* for the shares.

The *quiet* keyword controls printing; *ctl.quiet* is not used.

References
----------

- Blanchard, O.J. and D. Quah (1989). "The dynamic effects of aggregate demand and supply disturbances." *American Economic Review*, 79(4), 655-673.
- Lutkepohl, H. (2005). *New Introduction to Multiple Time Series Analysis*. Springer, section 9.2.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`varFit`, :func:`irfCompute`, :func:`fevdCompute`
