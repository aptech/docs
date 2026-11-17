varResults
==========

Purpose
-------
Reprint the estimation summary table from a fitted OLS VAR model.

Format
------

.. function:: varResults(result)

   :param result: an instance of a :class:`varResult` structure returned by :func:`varFit`.
   :type result: struct

Examples
--------

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_fred_qd.csv");
    data = loadd(fname, "date + gdp_growth + inflation + fed_funds");
    // Use 1960Q1-2019Q4 from the shipped vintage.
    data = selif(data, between(data[., "date"], "1960", "2020", "left"));

    // Fit with output suppressed, then print the stored OLS VAR summary.
    result = varFit(data, p=1, quiet=1);
    call varResults(result);

Remarks
-------

Reprints the stored OLS VAR estimates, standard errors, t-statistics and
p-values. It has no ``level`` keyword. A :func:`vecmToVar` result is refused;
use :func:`vecmResults` for the original VECM. Bayesian fits print their own
summaries when ``quiet=0``.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`varFit`, :func:`bvarFit`, :func:`bvarSvFit`, :func:`varCoefTable`
