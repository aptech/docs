fevdCompute
===========

Purpose
-------
Compute the forecast error variance decomposition from impulse responses.

Format
------

.. function:: fevd = fevdCompute(irf)

   :param irf: an instance of an :class:`irfResult` structure from :func:`irfCompute`.
   :type irf: struct

   :param quiet: Optional keyword, set to 1 to suppress printed output. Default = 0.
   :type quiet: scalar

   :return fevd: An instance of a :class:`fevdResult` structure containing:

       .. include:: include/fevdresult.rst

   :rtype fevd: struct

Examples
--------

From a VAR
++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    y = loadd(fname, "gdp_growth + cpi_inflation + fed_funds");

    fit = varFit(y, p=4, quiet=1);
    irf = irfCompute(fit, 12, quiet=1);

    fevd = fevdCompute(irf);

    // An ML fit gives the same variance shares
    fit_ml = varFit(y, p=4, resid_cov="ml", quiet=1);
    irf_ml = irfCompute(fit_ml, 12, quiet=1);
    fevd_ml = fevdCompute(irf_ml, quiet=1);

    // Share of GDP growth's 8-quarter forecast error variance due to each shock
    print fevd.fevd[7 * 3 + 1, .];

With posterior bands
++++++++++++++++++++

::

    fit = bvarFit(y, p=4, quiet=1);

    signs = signRestrictions({ "fed_funds"     "monetary" "0:4" "+",
                               "cpi_inflation" "monetary" "0:4" "-" });
    irf = irfCompute(fit, 20, restrictions=signs, quiet=1);

    fevd = fevdCompute(irf);

    // 68% band for the monetary shock's share of GDP growth at 8 quarters
    print fevd.bands[1].lower[7 * 3 + 1, 1] ~ fevd.fevd[7 * 3 + 1, 1]
          ~ fevd.bands[1].upper[7 * 3 + 1, 1];

Remarks
-------

**VAR covariance choice.** For the same fitted model, changing
:func:`varFit`'s *resid_cov* scales every one-standard-deviation response
by the same factor. It cancels from the variance shares, so FEVD is
unchanged. Generalized responses are refused because this function
requires orthogonal shocks. Recompute with Cholesky or long-run
identification. A :func:`vecmToVar` result cannot be passed through
:func:`irfCompute`; use :func:`vecmIrf` for VECM responses.

**Definition.** The share of variable *i*'s *h*-step forecast error
variance due to shock *j* is

.. math::

   \text{FEVD}_{i,j}(h) = \frac{\sum_{\ell=0}^{h-1} \Theta_\ell[i,j]^2}{\sum_{\ell=0}^{h-1} \sum_{k=1}^{m} \Theta_\ell[i,k]^2}

where :math:`\Theta_\ell` is the response matrix at horizon :math:`\ell`.
Each row of shares sums to 1.

**Layout.** *fevd.fevd* has *n_ahead* · *m* rows: rows *b* · *m* + 1 to
(*b* + 1) · *m* hold the (*b* + 1)-step shares, so the first block is the
one-step decomposition.

**Posterior results.** For posterior responses the shares are computed for
each draw and then summarized; *fevd.fevd* is the pointwise median and
*fevd.bands* the pointwise bands. Medians of shares need not sum exactly to
1; each draw's shares do. :func:`bvarSvFit` results with Cholesky
identification carry no draw-by-draw shares, so :func:`fevdCompute` does
not accept them.

**Sign restrictions.** Only the restricted shocks are identified; the
other shocks are an arbitrary rotation, so their individual shares mean
nothing. The printout shows the identified shocks only, and
*fevd.shown_shocks* lists their columns. Within each draw the identified
shares plus the remaining shocks' combined share sum to 1.

**Shock size.** Variance shares need one-standard-deviation shocks, so
responses computed with ``normalization="unit_own_impact"`` are rejected.

References
----------

- Lutkepohl, H. (2005). *New Introduction to Multiple Time Series Analysis*. Springer. Section 2.3.3.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`irfCompute`, :func:`hdCompute`, :func:`plotIrf`
