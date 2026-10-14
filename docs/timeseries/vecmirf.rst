vecmIrf
=======

Purpose
-------
Compute impulse responses of the levels of the series from a fitted VECM.

Format
------

.. function:: ir = vecmIrf(vr, n_ahead)
              ir = vecmIrf(vr, n_ahead, ident="cholesky", accumulated=0, quiet=0, normalization="chol_one_sd")

   :param vr: an instance of a :class:`vecmResult` structure returned by :func:`vecmFit` or :func:`vecmAuto`.
   :type vr: struct

   :param n_ahead: last horizon. Responses are computed for horizons 0 to *n_ahead*.
   :type n_ahead: scalar

   :param ident: Optional keyword, how the shocks are defined: ``"cholesky"`` (recursive, in the order of the columns of *y*) or ``"generalized"``. Default = ``"cholesky"``.
   :type ident: string

   :param accumulated: Optional keyword, set to 1 to return running sums of the responses over the horizons. Default = 0.
   :type accumulated: scalar

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :param normalization: Optional keyword, size of the Cholesky shocks: ``"chol_one_sd"`` (one standard deviation) or ``"unit_own_impact"`` (each shock moves its own series by 1 on impact). Generalized responses are always to one-standard-deviation shocks; ``"unit_own_impact"`` together with ``ident="generalized"`` is an error. Default = ``"chol_one_sd"``.
   :type normalization: string

   :return ir: An instance of an :class:`irfResult` structure. :func:`vecmIrf` fills these members:

       .. list-table::
          :widths: auto

          * - ir.irf
            - ((n_ahead+1)*M)xM matrix, the responses. Rows h*M+1 to (h+1)*M hold horizon *h*; within that block, element [i, j] is the response of series *i* to shock *j*. With ``accumulated=1`` these are the running sums.

          * - ir.n_ahead
            - Scalar, last horizon.

          * - ir.m
            - Scalar, number of series.

          * - ir.var_names
            - Mx1 string array, names of the responding series.

          * - ir.shock_names
            - Mx1 string array, names of the shocks (the names of the series).

          * - ir.identification
            - String, the value of *ident* as you passed it.

          * - ir.normalization
            - String, the shock size: ``"chol_one_sd"``, ``"unit_own_impact"``, or ``"one_sd"`` for generalized responses.

       The responses are point estimates without bands. The other members of the structure, which other impulse response procedures use, are left empty or zero; ``ir.fit_type`` is ``"VECM, rank r"`` with the fitted rank, the name shown on the Model line of the printout.

   :rtype ir: struct

Examples
--------

::

    new;
    library timeseries;

    // Canadian employment, productivity, real wage and unemployment, 1980Q1-2000Q4
    fname = getGAUSSHome("pkgs/timeseries/examples/data/canada.csv");
    y = loadd(fname);

    struct vecmResult vr;
    vr = vecmFit(y, 1, p=2, det_case=3, quiet=1);

    struct irfResult ir;
    ir = vecmIrf(vr, 8);

The first block of the printout:

::

    Impulse responses: Cholesky (recursive) identification
    ================================================================================
    Model             VECM, rank 1
    Shock size        one standard deviation
    Horizons          0 to 8

    Responses to e shock (point estimates)
    h              e       prod         rw          U
    -------------------------------------------------
    0         0.3743     0.0020    -0.0726    -0.2000
    1         0.6302     0.0282    -0.1691    -0.3758
    2         0.7987     0.0467    -0.1676    -0.4712
    3         0.9058     0.0228    -0.0876    -0.5209
    4         0.9623    -0.0243     0.0390    -0.5358
    5         0.9797    -0.0858     0.1956    -0.5238
    6         0.9679    -0.1557     0.3681    -0.4929
    7         0.9354    -0.2291     0.5456    -0.4494
    8         0.8890    -0.3023     0.7198    -0.3984

The response of unemployment (U) to an employment shock two quarters later:

::

    h = 2;
    print ir.irf[h*4 + 4, 1];       // -0.4712

Remarks
-------

**What is computed.** The fitted VECM is written as a VAR in levels, and the
responses are the moving-average matrices of that VAR multiplied by the
impact matrix of the shocks. They are responses of the levels of the series,
not of their differences.

In a cointegrated system the responses need not die out: a shock can move
the levels permanently.

**Shocks.** With ``ident="cholesky"`` the impact matrix is the Cholesky
factor of ``vr.sigma_u``: the first series responds on impact only to its own
shock, the second to the first two shocks, and so on, so the results depend
on the order of the columns of *y*. With ``ident="generalized"`` each shock
is a one-standard-deviation shock to one series' residual with the other
residuals moving as they are correlated with it (Pesaran and Shin 1998);
these responses do not depend on the order of the series, and the response to
the first shock equals the Cholesky one.

**Accumulated responses.** ``accumulated=1`` sums the responses from horizon
0 to *h*. The responses are already responses of the levels, so use this
only when the running sum has a meaning for your series, for example when a
series is a growth rate and you want the response of its level.

References
----------

- Lutkepohl, H. (2005). *New Introduction to Multiple Time Series Analysis*. Springer.
- Pesaran, H.H. and Y. Shin (1998). "Generalized impulse response analysis in linear multivariate models." *Economics Letters*, 58(1), 17-29.

Library
-------
timeseries

Source
------
vecm.src

.. seealso:: Functions :func:`vecmFit`, :func:`vecmForecast`, :func:`irfCompute`
