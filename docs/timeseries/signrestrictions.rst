signRestrictions
================

Purpose
-------
Build a table of sign and zero restrictions on impulse responses for
:func:`irfCompute`.

Format
------

.. function:: signs = signRestrictions(table)

   :param table: one restriction per row, four columns:

       .. list-table::
           :widths: auto

           * - variable
             - Name of a variable in the fit (for example ``"fed_funds"``), or its number.
           * - shock
             - A name you choose for the shock (for example ``"monetary"``), or a shock number.
           * - horizons
             - One horizon (``"0"`` is the impact period) or a range such as ``"0:4"``, which restricts every horizon from 0 to 4.
           * - sign
             - ``"+"`` for a positive response, ``"-"`` for a negative response, ``"0"`` for a zero response.

       Pass the rows in braces, ``{ "FFR" "monetary" "0:5" "+", ... }``, one row
       per line. To keep the table in a variable, declare it with ``string``:
       ``string table = { ... };``.
   :type table: Nx4 string array

   :return signs: an instance of an :class:`irfRestrictions` structure, passed to :func:`irfCompute` with ``restrictions=signs``.
   :rtype signs: struct

Examples
--------

Uhlig (2005) monetary policy shock
++++++++++++++++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv");
    y = loadd(fname, "date + gdp_growth + inflation + fed_funds");
    // Use 1960Q1-2019Q4 from the shipped vintage.
    y = selif(y, between(y[., "date"], "1960", "2020", "left"));

    // Growth is centered at 0; persistent inflation and the funds rate at 1.
    fit = bvarFit(y, p=4, lag1_prior_mean={ 0, 1, 1 }, quiet=1);

    signs = signRestrictions(
        { "fed_funds"     "monetary" "0:4" "+",
                               "inflation" "monetary" "0:4" "-" }
    );

    irf = irfCompute(fit, 20, restrictions=signs);

Several shocks and a zero restriction
+++++++++++++++++++++++++++++++++++++

::

    signs = signRestrictions(
        { "gdp_growth"    "demand"   "0" "+",
                               "inflation" "demand"   "0" "+",
                               "gdp_growth"    "supply"   "0" "-",
                               "inflation" "supply"   "0" "+",
                               "fed_funds"     "monetary" "0" "+",
                               "gdp_growth"    "monetary" "0" "0" }
    );

    irf = irfCompute(fit, 20, restrictions=signs);

The last row says that the monetary shock has no effect on GDP growth in
the quarter it occurs.

Remarks
-------

**Shock numbers.** Shocks named in the table are numbered in the order they
first appear: in the second example *demand* is shock 1, *supply* shock 2
and *monetary* shock 3. A shock given by number keeps that number, and
named shocks take the lowest numbers still free. Results and plots label
shocks by name; shocks without restrictions are called ``shock1``,
``shock2``, and so on. Narrative restrictions (see :func:`svarControlCreate`)
refer to shocks by these numbers.

**Checks.** :func:`signRestrictions` checks the shape of the table, the
horizons and the signs, and names the row of any error. :func:`irfCompute`
then checks the variable names against the fit and that no horizon is
beyond *h*.

**A table can be passed directly.** ``irfCompute(fit, 20, restrictions=table)``
calls :func:`signRestrictions` on the table.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`irfCompute`, :func:`svarControlCreate`
