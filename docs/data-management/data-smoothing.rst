Data Smoothing
=============================

Data smoothing reduces noise in a series so that underlying trends and
patterns become easier to see. GAUSS provides several approaches, from
simple moving averages to nonparametric regression and spline
interpolation.

+------------------------+-----------------------------------------------------------------------------+
|      Function          |  Description                                                                |
+========================+=============================================================================+
|:func:`movingave`       | Computes moving average of a series.                                        |
+------------------------+-----------------------------------------------------------------------------+
|:func:`movingaveExpwgt` | Computes exponentially weighted moving average of a series.                 |
+------------------------+-----------------------------------------------------------------------------+
|:func:`movingaveWgt`    | Computes weighted moving average of a series.                               |
+------------------------+-----------------------------------------------------------------------------+
| :func:`loessmt`        | Computes coefficients of locally weighted regression.                       |
+------------------------+-----------------------------------------------------------------------------+
| :func:`curve`          | Computes a one-dimensional smoothing curve.                                 |
+------------------------+-----------------------------------------------------------------------------+
| :func:`spline`         | Computes a two-dimensional interpolatory spline.                            |
+------------------------+-----------------------------------------------------------------------------+


Moving Averages
----------------------------------------------

A moving average replaces each observation with the mean of its
neighboring values within a sliding window. This is the simplest form
of smoothing and is especially common in time-series work (e.g.,
3-month or 12-month moving averages).

Three variants are available:

- :func:`movingave` — equal-weight (simple) moving average.
- :func:`movingaveWgt` — weighted moving average with user-supplied weights.
- :func:`movingaveExpwgt` — exponentially weighted moving average,
  where recent observations receive more weight.

All three return a vector the same size as the input. The first
*d* − 1 rows are set to missing because a full window is not yet
available.

Simple moving average
+++++++++++++++++++++++++++++++++

::

    y_smooth = movingave(x, d);

- *x* — NxK matrix of data.
- *d* — scalar, window size (order of the moving average).

Example: 3-month moving average of Treasury bill rates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    // Load monthly 3-month T-bill rates
    fname = getGAUSSHome("examples/tbill_3mo.xlsx");
    y = loadd(fname, "date($obs_date, '%m/%d/%Y %T.%L') + tbill_3m");

    // Compute 3-month simple moving average
    ma3 = movingave(y[., "tbill_3m"], 3);

    // First two rows are missing (window not full yet)
    print y[1:6, "tbill_3m"] ~ ma3[1:6];

This prints:

::

        tbill_3m        tbill_3m
       12.920000               .
       14.280000               .
       13.310000       13.503333
       13.340000       13.643333
       12.710000       13.120000
       13.080000       13.043333

Weighted moving average
+++++++++++++++++++++++++++++++++

::

    y_smooth = movingaveWgt(x, d, w);

- *x* — NxK matrix of data.
- *d* — scalar, window size.
- *w* — dx1 vector of weights. The weights are applied directly (not
  normalized), so they should sum to 1 if you want a weighted average.

Example: Emphasize recent observations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    // Load data
    fname = getGAUSSHome("examples/tbill_3mo.xlsx");
    y = loadd(fname, "tbill_3m");

    // Weights: most recent observation gets the most weight
    w = { 0.2, 0.3, 0.5 };
    wma = movingaveWgt(y, 3, w);

    print y[1:6] ~ wma[1:6];

This prints:

::

        tbill_3m        tbill_3m
       12.920000               .
       14.280000               .
       13.310000       13.523000
       13.340000       13.519000
       12.710000       13.019000
       13.080000       13.021000


Exponentially weighted moving average
+++++++++++++++++++++++++++++++++++++++

::

    y_smooth = movingaveExpwgt(x, d, p);

- *x* — NxK matrix of data.
- *d* — scalar, window size.
- *p* — scalar, smoothing coefficient (0 < *p* < 1). Lower values
  make the average track recent observations more closely; higher
  values produce a smoother, more slowly responding series.

Example: Smoothing with different coefficients
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    // Load data
    fname = getGAUSSHome("examples/tbill_3mo.xlsx");
    y = loadd(fname, "tbill_3m");

    // Smooth: p = 0.3 (tracks recent values closely)
    ema_close = movingaveExpwgt(y, 3, 0.3);

    // Smooth: p = 0.8 (heavier smoothing)
    ema_smooth = movingaveExpwgt(y, 3, 0.8);

    print y[3:8] ~ ema_close[3:8] ~ ema_smooth[3:8];

This prints:

::

        tbill_3m        tbill_3m        tbill_3m
       13.310000       13.236980       11.179810
       13.340000       13.139167       11.221951
       12.710000       12.639308       10.806369
       13.080000       12.768948       10.767480
       11.860000       11.946295       10.317886
        9.000000        9.693155        9.098645

The first smoothed column (p = 0.3) stays close to the original data,
while the second (p = 0.8) responds more slowly to changes.


Locally Weighted Regression (LOESS)
----------------------------------------------

The :func:`loessmt` procedure fits a smooth curve through scattered data
using locally weighted polynomial regression. Unlike a moving average,
LOESS adapts to the local density of the data and can handle
non-uniformly spaced observations. It is based on the method described
in Cleveland (1979).

::

    { yhat, ys, xs } = loessmt(depvar, indvars);
    { yhat, ys, xs } = loessmt(depvar, indvars, l_ctl);

- *depvar* — Nx1 vector, dependent variable (the values to smooth).
- *indvars* — NxK matrix, independent variables.
- *l_ctl* — optional :class:`loessmtControl` structure.

Returns:

- *yhat* — Nx1 fitted values at the original data points. Use this for
  residuals (``depvar - yhat``) or when you need predictions at the
  observed locations.
- *ys* — Mx1 fitted values at *M* equally spaced evaluation points.
  Use *ys* and *xs* together to plot a smooth curve.
- *xs* — Mx1 the evaluation points themselves.

Controlling the fit
+++++++++++++++++++++++++++++++++

Create a :class:`loessmtControl` structure to adjust the smoothing
behavior:

::

    struct loessmtControl l_ctl;
    l_ctl = loessmtControlCreate();

Key members and their defaults:

.. list-table::
    :widths: 20 15 65
    :header-rows: 1

    * - Member
      - Default
      - Description

    * - ``Span``
      - 0.6667
      - Fraction of data used in each local fit. Larger values produce
        smoother curves; smaller values follow the data more closely.
        Must be > 2/N.

    * - ``Degree``
      - 1
      - Polynomial degree: 1 = locally linear, 2 = locally quadratic.

    * - ``WgtType``
      - 2
      - Weight function: 1 = Gaussian, 2 = robust symmetric (bisquare).
        Use bisquare (default) when your data may contain outliers.

    * - ``NumEval``
      - 50
      - Number of equally spaced evaluation points for *ys* and *xs*.

    * - ``output``
      - 1
      - Set to 0 to suppress the printed table.


Example: LOESS with custom settings
+++++++++++++++++++++++++++++++++++++++

::

    // Load dataset
    fname = getGAUSSHome("examples/lowess1.dta");
    data = loadd(fname, "h1 + depth");

    depvar  = data[., "h1"];
    indvars = data[., "depth"];

    // Configure: tighter span, suppress printed output
    struct loessmtControl l_ctl;
    l_ctl = loessmtControlCreate();
    l_ctl.Span = 0.4;
    l_ctl.output = 0;

    { yhat, ys, xs } = loessmt(depvar, indvars, l_ctl);

    // yhat contains fitted values at the original data points
    // ys/xs contain the smooth curve at 50 equally spaced points
    print "Evaluation points:" rows(xs);
    print "First 5 fitted values:";
    print yhat[1:5];


Curve Smoothing
----------------------------------------------

The :func:`curve` function fits a smooth curve through one-dimensional
data using a **tension spline** — a curve that resists bending between
data points. The tension parameter controls how stiff the curve is:
low tension produces soft, cubic-like curves; high tension pulls the
curve toward straight-line segments between points.

::

    { u, v } = curve(x, y, d, s, sigma, G);

- *x* — Kx1 vector of x-coordinates (must be strictly increasing).
- *y* — Kx1 vector of y-coordinates.
- *d* — Kx1 vector or scalar, observation weights (standard deviations
  or 1 for equal weighting).
- *s* — scalar, smoothing parameter. Set to 0 for exact interpolation.
  A reasonable value when *d* contains standard deviations is K (the
  number of data points).
- *sigma* — scalar, tension factor. Values near 1 give a standard
  smooth curve; values near 0 produce cubic-like curves; large values
  (e.g. 50) produce nearly straight-line segments.
- *G* — scalar, grid refinement factor. The output will contain
  K × G points.

Returns:

- *u* — (K × G) x 1 vector of regularly spaced x-values.
- *v* — (K × G) x 1 vector of smoothed y-values.

Example: Smoothing noisy data
+++++++++++++++++++++++++++++++++

::

    rndseed 42;

    // Generate noisy sine wave
    x = seqa(1, 1, 20);
    y = sin(x / 3) + rndn(20, 1) * 0.3;

    // Smooth with moderate tension, grid factor of 5
    { u, v } = curve(x, y, 1, 20, 1, 5);

    // u and v contain 100 points (20 * 5)
    print "Output points:" rows(u);


Two-Dimensional Spline Interpolation
----------------------------------------------

The :func:`spline` function computes a smooth surface through data on
a two-dimensional grid using a tension spline.

::

    { u, v, w } = spline(x, y, z, sigma, g);

- *x* — Kx1 vector of x-coordinates.
- *y* — Nx1 vector of y-coordinates.
- *z* — KxN matrix of z-values (the surface heights).
- *sigma* — scalar, tension factor (same behavior as :func:`curve`).
- *g* — scalar, grid refinement factor.

Returns:

- *u* — (K × g) x 1 vector of refined x-coordinates.
- *v* — (N × g) x 1 vector of refined y-coordinates.
- *w* — (K × g) x (N × g) matrix of interpolated surface values.

Example: Interpolating a surface
+++++++++++++++++++++++++++++++++

::

    rndseed 42;

    // Create a small 5x4 grid
    x = seqa(0, 1, 5);
    y = seqa(0, 1, 4);
    z = rndn(5, 4);

    // Interpolate with grid factor 3 (produces 15x12 output)
    { u, v, w } = spline(x, y, z, 1, 3);

    print "Output grid:" rows(u) "x" cols(w);


Choosing a Method
----------------------------------------------

.. list-table::
    :widths: 20 35 25 20
    :header-rows: 1

    * - Method
      - Best for
      - Data requirement
      - Key parameter

    * - :func:`movingave`
      - Quick smoothing of evenly spaced time series
      - Evenly spaced
      - Window size *d*

    * - :func:`movingaveWgt`
      - When certain observations in the window matter more
      - Evenly spaced
      - Weight vector *w*

    * - :func:`movingaveExpwgt`
      - Tracking trends with exponential decay
      - Evenly spaced
      - Smoothing coefficient *p*

    * - :func:`loessmt`
      - Nonparametric regression; unevenly spaced data
      - Any spacing
      - Span (bandwidth)

    * - :func:`curve`
      - Smooth interpolation of 1-D scattered data
      - Strictly increasing *x*
      - Smoothing *s*, tension *sigma*

    * - :func:`spline`
      - Smooth interpolation of 2-D gridded data
      - Regular grid
      - Tension *sigma*

.. seealso:: Functions :func:`movingave`, :func:`movingaveWgt`, :func:`movingaveExpwgt`, :func:`loessmt`, :func:`curve`, :func:`spline`
