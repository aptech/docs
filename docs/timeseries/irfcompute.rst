irfCompute
==========

Purpose
-------
Compute impulse responses from a VAR, BVAR or SV-BVAR fit, with Cholesky,
generalized, sign-restricted or long-run identification.

Format
------

.. function:: irf = irfCompute(fit, n_ahead)
              irf = irfCompute(fit, n_ahead, identification="generalized")
              irf = irfCompute(fit, n_ahead, restrictions=signs)
              irf = irfCompute(fit, n_ahead, identification="long_run")

   :param fit: result from :func:`varFit`, :func:`bvarFit` or :func:`bvarSvFit`.
   :type fit: struct

   :param n_ahead: last horizon. Responses are returned for horizons 0 (impact) to *n_ahead*.
   :type n_ahead: scalar

   :param identification: Optional keyword, how the structural shocks are identified.

       .. list-table::
           :widths: auto

           * - "cholesky"
             - Recursive ordering of the variables (default).
           * - "generalized"
             - Generalized responses, which do not depend on the ordering.
           * - "sign"
             - Sign and zero restrictions given with *restrictions*. Implied when *restrictions* is given.
           * - "long_run"
             - Long-run restrictions: shock *j* has no long-run effect on variables 1 to *j*-1.

       Supported combinations:

       .. list-table::
           :widths: auto
           :header-rows: 1

           * - Fit
             - Identifications
           * - :func:`varFit`
             - cholesky, generalized, long_run
           * - :func:`bvarFit`
             - cholesky, sign, long_run
           * - :func:`bvarSvFit`
             - cholesky, sign

   :type identification: string

   :param normalization: Optional keyword, the size of the shock under Cholesky identification.

       .. list-table::
           :widths: auto

           * - "chol_one_sd"
             - One standard deviation (default for :func:`varFit` and :func:`bvarFit` results).
           * - "unit_own_impact"
             - Each shock moves its own variable by exactly 1 on impact (:func:`varFit` and :func:`bvarSvFit` results).
           * - "one_sd_at(t)"
             - :func:`bvarSvFit` results only: one standard deviation at period *t*, where *t* is the last sample period (``fit.n_obs``).

       Under stochastic volatility the size of a one-standard-deviation shock changes
       every period, so :func:`bvarSvFit` results have no default: choose
       ``"unit_own_impact"`` or ``"one_sd_at(t)"``. Sign, generalized and long-run
       responses are one-standard-deviation shocks.
   :type normalization: string

   :param restrictions: Optional keyword, sign and zero restrictions from :func:`signRestrictions`, or the restriction table itself.
   :type restrictions: struct or Nx4 string array

   :param levels: Optional keyword, central masses of the pointwise credible bands. Default = ``0.68|0.90``. Sign-restricted responses, long-run responses from :func:`bvarFit` results and :func:`bvarSvFit` results support 0.68 and 0.90.
   :type levels: scalar or vector

   :param n_draws: Optional keyword, :func:`bvarFit` results only: number of posterior draws to use. Default = all stored draws.
   :type n_draws: scalar

   :param max_tries: Optional keyword, sign identification: random rotations tried for each posterior draw before the draw is dropped. Default = 10000.
   :type max_tries: scalar

   :param seed: Optional keyword, sign identification: random seed. Default = 42.
   :type seed: scalar

   :param cumulative: Optional keyword, set to 1 to also return cumulative responses in *irf.cirf*. Default = 0.
   :type cumulative: scalar

   :param ctl: Optional keyword, an instance of an :class:`svarControl` structure (:func:`svarControlCreate`) with narrative restrictions and the rotation sampler choice.
   :type ctl: struct

   :param var_names: Optional keyword, variable names for the output. Default = the names stored in *fit*.
   :type var_names: Mx1 string array

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :return irf: An instance of an :class:`irfResult` structure containing:

       .. include:: include/irfresult.rst

   :rtype irf: struct

Examples
--------

Cholesky responses from a VAR
+++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    y = loadd(fname, "gdp_growth + cpi_inflation + fed_funds");

    // The ordering GDP, inflation, funds rate lets the funds rate react to
    // output and prices within the quarter.
    fit = varFit(y, p=4, quiet=1);

    irf = irfCompute(fit, 12);

The printout starts with the model and shock description, followed by one
table per shock. Row *h* of the table for a shock holds the responses of
every variable *h* quarters after the shock.

Posterior bands from a BVAR
+++++++++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    y = loadd(fname, "gdp_growth + cpi_inflation + fed_funds");

    fit = bvarFit(y, p=4, quiet=1);

    irf = irfCompute(fit, 12, quiet=1);

    // Response of GDP growth to a funds rate shock, with the 68% band
    h = seqa(0, 1, 13);
    gdp_row = 3 * h + 1;
    print h ~ irf.bands[1].lower[gdp_row, 3] ~ irf.irf[gdp_row, 3]
            ~ irf.bands[1].upper[gdp_row, 3];

Each posterior draw gives one set of responses; *irf.irf* is the pointwise
median and *irf.bands* holds the pointwise quantiles across draws.

A monetary policy shock identified with sign restrictions
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    y = loadd(fname, "gdp_growth + cpi_inflation + fed_funds");

    fit = bvarFit(y, p=4, quiet=1);

    // A contractionary monetary shock raises the funds rate and lowers
    // inflation for the first four quarters (Uhlig 2005).
    signs = signRestrictions({ "fed_funds"     "monetary" "0:4" "+",
                               "cpi_inflation" "monetary" "0:4" "-" });

    irf = irfCompute(fit, 20, restrictions=signs);

    plotIrf(irf);

The printout lists the restrictions as resolved against the fit, the number
of posterior draws for which a rotation satisfying every restriction was
found, and the responses to the *monetary* shock. Shocks without
restrictions are not identified and are left out of the printout and the
plot.

Narrative restrictions
++++++++++++++++++++++

Narrative restrictions constrain the identified shocks in particular
historical episodes. Continuing the example above, set them on an
:class:`svarControl` structure:

::

    ctl = svarControlCreate();

    // The monetary shock (shock 1, the first shock named in the table)
    // was positive at observation 95 of the estimation sample.
    ctl.narrative_restr = { 1 0 1 95 0 1 };

    irf_n = irfCompute(fit, 20, restrictions=signs, ctl=ctl);

Long-run identification
+++++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/blanchard_quah_1989.csv");
    y = loadd(fname, "gnp_growth + unemployment");

    fit = varFit(y, p=8, quiet=1);

    // Shock 2 has no long-run effect on the level of output
    irf = irfCompute(fit, 40, identification="long_run", quiet=1);

    // Block 0 of the responses is the structural impact matrix
    print irf.irf[1:2, .];

Remarks
-------

**Layout of the responses.** *irf.irf* has (*n_ahead* + 1) · *m* rows and
*m* columns. Rows *h* · *m* + 1 to (*h* + 1) · *m* hold horizon *h*;
element [*i*, *j*] of that block is the response of variable *i* to shock
*j*. The first block is the impact matrix. The bands, the cumulative
responses and the point responses use the same layout.

**Cholesky identification** orthogonalizes the innovations with the lower
Cholesky factor of their covariance matrix, so variable 1 can affect all
others within the period and variable *m* affects none of the others
within the period. Reorder the data columns to change the ordering.

**Generalized responses** (Pesaran and Shin 1998) shock one innovation at a
time and integrate out the others using their historical correlation. They
do not depend on the ordering, but the shocks are not orthogonal.

**Sign restrictions** (Uhlig 2005; Rubio-Ramirez, Waggoner and Zha 2010).
For each posterior draw of the coefficients and covariance matrix, random
orthogonal rotations of the Cholesky factor are drawn until one satisfies
every restriction; if none does within *max_tries*, the draw is dropped and
counted in *irf.n_attempted* but not in *irf.n_accepted*. Zero restrictions
are imposed exactly by building the rotation one column at a time (Arias,
Rubio-Ramirez and Waggoner 2018). Narrative restrictions (Antolin-Diaz and
Rubio-Ramirez 2018) are checked on each accepted draw and are available for
:func:`bvarFit` results. Sign identification needs posterior draws, so it is
not available for :func:`varFit` results.

**Long-run restrictions** (Blanchard and Quah 1989) make the long-run
impact matrix lower triangular: shock *j* has no permanent effect on the
level of variables 1 to *j*-1 when those variables enter in differences.

**Posterior summaries are pointwise.** Responses are computed draw by draw
and then summarized horizon by horizon; the band at one horizon is not a
joint statement about the whole path.

**SV-BVAR fits.** Cholesky responses from a :func:`bvarSvFit` result use
the posterior draws of the contemporaneous structure; sign-restricted
responses use the covariance matrix of the last sample period.

References
----------

- Antolin-Diaz, J. and J.F. Rubio-Ramirez (2018). "Narrative sign restrictions for SVARs." *American Economic Review*, 108(10), 2802-2829.
- Arias, J.E., J.F. Rubio-Ramirez and D.F. Waggoner (2018). "Inference based on structural vector autoregressions identified with sign and zero restrictions: theory and applications." *Econometrica*, 86(2), 685-720.
- Blanchard, O.J. and D. Quah (1989). "The dynamic effects of aggregate demand and supply disturbances." *American Economic Review*, 79(4), 655-673.
- Lutkepohl, H. (2005). *New Introduction to Multiple Time Series Analysis*. Springer. Chapters 2.3 and 9.
- Pesaran, M.H. and Y. Shin (1998). "Generalized impulse response analysis in linear multivariate models." *Economics Letters*, 58(1), 17-29.
- Rubio-Ramirez, J.F., D.F. Waggoner and T. Zha (2010). "Structural vector autoregressions: theory of identification and algorithms for inference." *Review of Economic Studies*, 77(2), 665-696.
- Uhlig, H. (2005). "What are the effects of monetary policy on output? Results from an agnostic identification procedure." *Journal of Monetary Economics*, 52(2), 381-419.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`signRestrictions`, :func:`fevdCompute`, :func:`hdCompute`, :func:`plotIrf`, :func:`irfPlotData`, :func:`svarControlCreate`
