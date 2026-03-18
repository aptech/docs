varResults
==========

Purpose
-------
Reprint the estimation summary table from a fitted VAR or BVAR model.

Format
------

.. function:: call varResults(result)
              call varResults(result, level=0.90)

   :param result: an instance of a :class:`varResult`, :class:`bvarResult`, or :class:`bvarSvResult` structure.
   :type result: struct

   :param level: Optional keyword, credible interval level for Bayesian models. Default = 0.68 (68% bands, standard in macro). For frequentist :class:`varResult`, controls the confidence level.
   :type level: scalar

Examples
--------

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/macro.dat"));

    // Fit with output suppressed
    result = bvarFit(data, quiet=1);

    // Print with default 68% credible bands
    call varResults(result);

    // Reprint with 90% credible bands
    call varResults(result, level=0.90);

Remarks
-------

Accepts any of the three VAR result struct types (:class:`varResult`,
:class:`bvarResult`, :class:`bvarSvResult`). The printed format adapts
automatically:

- **varResult:** frequentist table with Coef, SE, t-stat, p-value
- **bvarResult:** Bayesian table with Mean, SD, lower/upper credible bands
- **bvarSvResult:** Bayesian table + SV parameters + acceptance rates + PIPs (if SSVS)

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`varFit`, :func:`bvarFit`, :func:`bvarSvFit`, :func:`varCoefTable`
