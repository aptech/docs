varLagSelect
============

Purpose
-------
Select VAR lag order by information criteria.

Format
------

.. function:: ls = varLagSelect(y, max_p)
              ls = varLagSelect(y, max_p, ic="bic")

   :param y: endogenous variables.
   :type y: TxM matrix or dataframe

   :param max_p: maximum lag order to test.
   :type max_p: scalar

   :param ic: Optional keyword, selection criterion. ``"aic"`` (default), ``"bic"``, or ``"hq"``.
   :type ic: string

   :param xreg: Optional keyword, exogenous regressors.
   :type xreg: TxK matrix

   :param const: Optional keyword, 1 to include constant (default), 0 to exclude.
   :type const: scalar

   :param quiet: Optional keyword, set to 1 to suppress the IC table. Default = 0.
   :type quiet: scalar

   :return ls: An instance of a :class:`lagSelectResult` structure containing:

       .. list-table::
          :widths: auto

          * - ls.best_p
            - Scalar, selected lag order (argmin of chosen criterion).

          * - ls.criterion
            - String, criterion used for selection (``"aic"``, ``"bic"``, or ``"hq"``).

          * - ls.ic_table
            - max_p x 3 matrix, information criterion values for each lag order. Columns: AIC, BIC, HQ.

          * - ls.max_p
            - Scalar, maximum lag tested.

          * - ls.ic_names
            - 3x1 string array, ``{"AIC", "BIC", "HQ"}``.

   :rtype ls: struct

Examples
--------

Basic Lag Selection
+++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    data = loadd(fname);

    // Test lags 1 through 8, select by AIC
    ls = varLagSelect(data, 8);

::

    ================================================================================
    VAR Lag Selection (M=3, T=200)
    ================================================================================
    Lag      AIC         BIC         HQ
    ----------------------------------------
      1   -12.384     -11.927*    -12.198*
      2   -12.401*    -11.689     -12.115
      3   -12.378     -11.410     -11.993
      4   -12.356     -11.133     -11.871
      5   -12.331     -10.853     -11.746
      6   -12.312     -10.578     -11.627
      7   -12.289     -10.300     -11.504
      8   -12.270     -10.026     -11.385
    ================================================================================
    Selected: p=2 (AIC)
    ================================================================================

Pipe into Estimation
++++++++++++++++++++

::

    new;
    library timeseries;

    fname = getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv");
    data = loadd(fname);

    // Select lag order, then estimate
    ls = varLagSelect(data, 8, ic="bic", quiet=1);
    result = varFit(data, ls.best_p);

Remarks
-------

The full IC table (*ls.ic_table*) reports all three criteria (AIC, BIC, HQ)
regardless of which criterion was used for selection. This allows comparison
when the criteria disagree — AIC tends to select more lags than BIC.

Model
-----

For each candidate lag order :math:`p = 1, \ldots, p_{\max}`, the VAR(p) is estimated
by OLS and the information criteria are computed:

.. math::

   \text{AIC}(p) &= \log|\hat\Sigma_p| + \frac{2 K_p m}{T_p} \\
   \text{BIC}(p) &= \log|\hat\Sigma_p| + \frac{K_p m \log T_p}{T_p} \\
   \text{HQ}(p)  &= \log|\hat\Sigma_p| + \frac{2 K_p m \log \log T_p}{T_p}

where :math:`K_p = mp + 1` and :math:`T_p = T - p` (sample shrinks with more lags).

The selected :math:`p^*` minimizes the chosen criterion. AIC tends to select larger
models; BIC tends to select smaller models (Lutkepohl 2005, Section 4.3).


Troubleshooting
---------------

**AIC and BIC disagree:**
This is common. AIC optimizes forecast accuracy; BIC optimizes model consistency
(converges to the true order as T → ∞). For forecasting, prefer AIC. For structural
analysis, prefer BIC. When in doubt, report both.


References
----------

- Lutkepohl, H. (2005). *New Introduction to Multiple Time Series Analysis*. Springer. Section 4.3.


Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`varFit`, :func:`bvarFit`, :func:`bvarHyperopt`
