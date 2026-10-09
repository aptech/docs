varLagSelect
============

Purpose
-------
Select VAR lag order by information criteria.

Format
------

.. function:: ls = varLagSelect(y, max_p)
              ls = varLagSelect(y, max_p, ic="fpe", trend=1)

   :param y: endogenous variables.
   :type y: TxM matrix or dataframe

   :param max_p: maximum lag order to test.
   :type max_p: scalar

   :param ic: Optional keyword, selection criterion. ``"aic"`` (default), ``"bic"``, ``"hq"``, or ``"fpe"``.
   :type ic: string

   :param const: Optional keyword, 1 to include a constant (default), 0 to exclude it.
   :type const: scalar

   :param quiet: Optional keyword, set to 1 to suppress the IC table. Default = 0.
   :type quiet: scalar

   :param trend: Optional keyword, 1 to include a linear data-row trend, 0 to exclude it, independent of *const*. Default = 0.
   :type trend: scalar

   :return ls: An instance of a :class:`lagSelectResult` structure containing:

       .. list-table::
          :widths: auto

          * - ls.best_p
            - Scalar, selected lag order (argmin of chosen criterion).

          * - ls.criterion
            - String, criterion used for selection (``"aic"``, ``"bic"``, ``"hq"``, or ``"fpe"``).

          * - ls.ic_table
            - max_p x 4 matrix, one row per lag order 1 through max_p. Columns: AIC, BIC, HQ, FPE.

          * - ls.max_p
            - Scalar, maximum lag tested.

          * - ls.ic_names
            - 4x1 string array, ``"AIC"``, ``"BIC"``, ``"HQ"``, ``"FPE"``.

   :rtype ls: struct

Examples
--------

Basic Lag Selection
+++++++++++++++++++

::

    new;
    library timeseries;

    data = loadd(getGAUSSHome("pkgs/timeseries/examples/data/us_macro_quarterly.csv"),
                 "gdp_growth + cpi_inflation + fed_funds");

    // Test lags 1 through 8, select by AIC
    ls = varLagSelect(data, 8);

The printout shows all four criteria and marks the minimum of each.

Pipe into Estimation
++++++++++++++++++++

::

    // Select the lag order by BIC, then estimate
    ls = varLagSelect(data, 8, ic="bic", quiet=1);
    result = varFit(data, ls.best_p);

    // Keep the trend setting when fitting the selected model
    ls_trend = varLagSelect(data, 8, ic="fpe", trend=1, quiet=1);
    fit_trend = varFit(data, p=ls_trend.best_p, trend=1);

Remarks
-------

*max_p* must be a positive integer and cannot exceed the common sample's
feasible limit. An error reports the largest feasible value; the requested
limit is not silently reduced. *const* and *trend* must be 0 or 1. Missing
or nonfinite data raise an error naming the row and column. A generated
trend uses the original data-row numbers on the common sample.

The full IC table (*ls.ic_table*) reports all four criteria (AIC, BIC, HQ, FPE)
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

where :math:`K_p = mp + \mathrm{const} + \mathrm{trend}` and
:math:`T_p = T_c = T - \mathrm{max\_p}` for every candidate. All candidates
use the same response rows, starting at data row max_p + 1, and
:math:`\hat\Sigma_p = U_p'U_p/T_c` is the ML covariance. FPE is

.. math::

   \mathrm{FPE}(p) = \left(\frac{T_c+K_p}{T_c-K_p}\right)^m
   \det(\hat\Sigma_p).

FPE is the fourth table column; ``ic="fpe"`` selects its minimum. Criterion
names are accepted in any letter case. Lag zero is not a candidate.

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
