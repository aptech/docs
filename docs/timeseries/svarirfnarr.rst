svarIrfNarr
===========

Purpose
-------
Convenience wrapper for computing narrative sign-restricted SVAR impulse responses. Merges narrative restrictions with sign restrictions and delegates to :func:`svarIrf`.

Format
------

.. function:: sir = svarIrfNarr(result, sign_restr, narr_restr)
              sir = svarIrfNarr(result, sign_restr, narr_restr, n_ahead)
              sir = svarIrfNarr(result, sign_restr, narr_restr, adv)
              sir = svarIrfNarr(result, sign_restr, narr_restr, n_ahead, adv)

   :param result: an instance of a :class:`bvarSvResult` structure with posterior draws from :func:`bvarSvFit`.
   :type result: struct

   :param sign_restr: Nx4 matrix of sign restrictions on impulse responses. Each row specifies one restriction:

       === ==================================================================
       1   Variable index (1 to m) -- the responding variable.
       2   Shock index (1 to m) -- the structural shock.
       3   Horizon (0 = impact, 1 = one step ahead, etc.).
       4   Sign: 1 for positive response, -1 for negative response.
       === ==================================================================

   :type sign_restr: Nx4 matrix

   :param narr_restr: Nx6 matrix of narrative restrictions. Each row specifies one restriction:

       === ==================================================================
       1   Type: narrative restriction type (see table below).
       2   Variable index (1 to m).
       3   Shock index (1 to m).
       4   Date 1: observation index (1-indexed) for point restrictions, or start of range.
       5   Date 2: end observation index for range restrictions (0 if unused).
       6   Sign: 1 for positive, -1 for negative.
       === ==================================================================

       Narrative restriction types:

       .. list-table::
          :widths: auto
          :header-rows: 1

          * - Type
            - Name
            - Meaning
          * - 1
            - ``shock_sign``
            - The structural shock *j* at date *t* has the specified sign.
          * - 2
            - ``shock_dominance``
            - Shock *j* is the dominant contributor to variable *i* at date *t* (its contribution exceeds all others).
          * - 3
            - ``decomposition_sign``
            - The historical decomposition contribution of shock *j* to variable *i* at date *t* has the specified sign.

   :type narr_restr: Nx6 matrix

   :param n_ahead: Optional, number of IRF horizons to compute. Default = 20.
   :type n_ahead: scalar

   :param adv: Optional, an instance of an :class:`svarControl` structure for zero restrictions and advanced settings. An instance is initialized by calling :func:`svarControlCreate` and the following members can be set:

       .. include:: include/svarcontrol.rst

   :type adv: struct

   :return sir: An instance of an :class:`svarPosteriorResult` structure containing:

       .. include:: include/svarposteriorresult.rst

   :rtype sir: struct

Examples
--------

Oil Market SVAR with Narrative Restrictions
+++++++++++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/oil_market.csv");
    y = loadd(fname, "oil_production + real_activity + real_oil_price");

    // Estimate SV-BVAR
    struct bvarSvControl svctl;
    svctl = bvarSvControlCreate();
    svctl.p = 12;
    svctl.n_draws = 10000;
    svctl.n_burn = 5000;
    svctl.quiet = 1;

    result = bvarSvFit(y, svctl);

    // Sign restrictions: oil supply shock
    sign_restr = { 1 1 0 -1,       // Production falls
                   3 1 0  1 };      // Oil price rises

    // Narrative restrictions:
    // 1990:M8 (obs 200): supply shock was negative (Gulf War)
    // 2008:M7 (obs 415): demand shock dominated oil price
    narr_restr = { 1 1 1 200 0 -1,    // shock_sign: supply shock negative
                   2 3 2 415 0  1 };   // shock_dominance: demand shock
                                       //   dominated oil price

    sir = svarIrfNarr(result, sign_restr, narr_restr);

    print "Acceptance rate:" sir.accept_rate;

Narrative with Custom Horizon
+++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    y = loadd(fname, "gdp_growth + cpi_inflation + fed_funds");

    result = bvarSvFit(y, quiet=1);

    // Sign restrictions: monetary policy shock
    sign_restr = { 3 3 0  1,
                   1 3 0 -1,
                   2 3 0 -1 };

    // Volcker disinflation: monetary shock was positive
    narr_restr = { 1 3 3 84 0 1 };

    // Compute 40-step IRFs
    sir = svarIrfNarr(result, sign_restr, narr_restr, 40);

Remarks
-------

**Convenience wrapper:**
This function is equivalent to creating an :class:`svarControl` struct,
setting ``adv.narrative_restr = narr_restr``, and calling :func:`svarIrf`.
It exists to simplify the common case of sign + narrative identification
without requiring the user to manually construct the advanced struct.

**Narrative restriction types:**

- **Type 1 (shock_sign):** The most basic narrative restriction. It constrains the sign of a specific structural shock at a known date. Example: the monetary policy shock was contractionary in 1979:Q4.
- **Type 2 (shock_dominance):** Constrains a specific shock to be the single largest contributor to the forecast error of a given variable at the specified date. Stronger than shock_sign.
- **Type 3 (decomposition_sign):** Constrains the sign of the historical decomposition contribution of a specific shock to a given variable. Useful when the event is known to have moved a variable in a particular direction.

**Observation indexing:**
The *date1* and *date2* columns use 1-based observation indices matching the
estimation sample. For quarterly data starting in 1960:Q1, observation 84
corresponds to 1980:Q4.

**Algorithm:**
When narrative restrictions are present, the function dispatches to the
v3 narrative engine which uses importance-weighted accept-reject sampling
(Antolin-Diaz & Rubio-Ramirez 2018).

References
----------

- Antolin-Diaz, J. and J.F. Rubio-Ramirez (2018). "Narrative sign restrictions for SVARs." *American Economic Review*, 108(10), 2802-2829.
- Rubio-Ramirez, J.F., D.F. Waggoner, and T. Zha (2010). "Structural vector autoregressions: Theory of identification and algorithms for inference." *Review of Economic Studies*, 77(2), 665-696.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`svarIrf`, :func:`svarControlCreate`, :func:`bvarSvFit`, :func:`irfPlotData`
