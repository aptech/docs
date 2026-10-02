hdCompute
=========

Purpose
-------
Decompose the observed series of a VAR or BVAR fit into the contributions of
the structural shocks and of the initial conditions.

Format
------

.. function:: hd = hdCompute(fit)
              hd = hdCompute(fit, bands=1)

   :param fit: result from :func:`varFit` or :func:`bvarFit`.
   :type fit: struct

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :param identification: Optional keyword, ``"cholesky"`` (the only option at present).
   :type identification: string

   :param bands: Optional keyword, :func:`bvarFit` results: set to 1 to add pointwise posterior bands for each shock's contribution. Default = 0.
   :type bands: scalar

   :param levels: Optional keyword, central masses of the bands. Default = ``0.68|0.90``.
   :type levels: scalar or vector

   :param n_draws: Optional keyword, number of posterior draws used for the bands. Default = all stored draws.
   :type n_draws: scalar

   :return hd: An instance of an :class:`hdResult` structure containing:

       .. include:: include/hdresult.rst

   :rtype hd: struct

Examples
--------

Contributions to GDP growth
+++++++++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    y = loadd(fname, "gdp_growth + cpi_inflation + fed_funds");

    fit = varFit(y, p=4, quiet=1);
    hd = hdCompute(fit);

    // Contribution of the funds rate shock (shock 3) to GDP growth (column 1)
    t = hd.t_eff;
    ffr_to_gdp = hd.hd[2 * t + 1:3 * t, 1];

The contributions add up to the data
++++++++++++++++++++++++++++++++++++

::

    gdp = hd.initial[., 1];
    for j (1, hd.m, 1);
        gdp = gdp + hd.hd[(j - 1) * t + 1:j * t, 1];
    endfor;

    // Equals the data after the first p observations
    print maxc(abs(gdp - y[fit.p + 1:rows(y), 1]));

Posterior bands from a BVAR
+++++++++++++++++++++++++++

::

    fit = bvarFit(y, p=4, quiet=1);
    hd = hdCompute(fit, bands=1, n_draws=1000);

Remarks
-------

**Decomposition.** Each observation is the sum of the contributions of the
structural shocks up to that date plus the contribution of the initial
conditions:

.. math::

   y_t = \sum_{j=1}^{m} \sum_{s=p+1}^{t} \Theta_{t-s}[\cdot, j]\, \varepsilon_{j,s} + y_t^{\text{init}}

where :math:`\Theta_h` are the Cholesky responses and
:math:`\varepsilon_t = P^{-1} u_t` the structural shocks, with
:math:`\Sigma = P P'`. *hd.max_abs_gap* reports the largest difference
between the data and the sum of the parts.

**Layout.** *hd.hd* stacks the shocks: rows (*j* - 1) · *t_eff* + 1 to
*j* · *t_eff* hold the contribution of shock *j*, one column per variable.

**BVAR fits.** The decomposition is evaluated at the posterior mean of the
coefficients and covariance matrix, so it adds up exactly. With
``bands=1``, *hd.hd_median* and *hd.hd_bands* summarize the contributions
draw by draw; these summaries do not add up to the data, only each draw's
contributions do.

References
----------

- Lutkepohl, H. (2005). *New Introduction to Multiple Time Series Analysis*. Springer. Section 2.3.4.
- Kilian, L. and H. Lutkepohl (2017). *Structural Vector Autoregressive Analysis*. Cambridge University Press.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`irfCompute`, :func:`fevdCompute`, :func:`varFit`, :func:`bvarFit`
