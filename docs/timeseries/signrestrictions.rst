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

       Build each row with ``$~`` and stack the rows with ``$|``.
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

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    y = loadd(fname, "gdp_growth + cpi_inflation + fed_funds");

    fit = bvarFit(y, p=4, quiet=1);

    signs = signRestrictions(
        "fed_funds"     $~ "monetary" $~ "0:4" $~ "+" $|
        "cpi_inflation" $~ "monetary" $~ "0:4" $~ "-");

    irf = irfCompute(fit, 20, restrictions=signs);

Several shocks and a zero restriction
+++++++++++++++++++++++++++++++++++++

::

    signs = signRestrictions(
        "gdp_growth"    $~ "demand"   $~ "0" $~ "+" $|
        "cpi_inflation" $~ "demand"   $~ "0" $~ "+" $|
        "gdp_growth"    $~ "supply"   $~ "0" $~ "-" $|
        "cpi_inflation" $~ "supply"   $~ "0" $~ "+" $|
        "fed_funds"     $~ "monetary" $~ "0" $~ "+" $|
        "gdp_growth"    $~ "monetary" $~ "0" $~ "0");

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
beyond *n_ahead*.

**A table can be passed directly.** ``irfCompute(fit, 20, restrictions=table)``
calls :func:`signRestrictions` on the table.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`irfCompute`, :func:`svarControlCreate`
