dmTest
======

Purpose
-------
Diebold-Mariano test for equal predictive ability between two forecast models.

Format
------

.. function:: t = dmTest(loss_a, loss_b)
              t = dmTest(loss_a, loss_b, h=4)
              t = dmTest(loss_a, loss_b, h=4, variant="hac_hln_t")

   :param loss_a: loss series for model A, for example squared forecast errors.
   :type loss_a: Nx1 vector

   :param loss_b: loss series for model B, on the same dates.
   :type loss_b: Nx1 vector

   :param h: Optional keyword, forecast horizon of the errors (1 for one step ahead). It sets the lags in the variance and the small-sample correction. Default = 1.
   :type h: scalar

   :param variant: Optional keyword, ``"hln"``, ``"hac_hln_t"`` or ``"asymptotic"`` (see Remarks). Default = ``"hln"``.
   :type variant: string

   :param quiet: Optional keyword, 1 to suppress printing. Default = 0.
   :type quiet: scalar

   :return t: An instance of an :class:`fcTestResult` structure containing *statistic*, *p_value* (two-sided), *p_value_one_sided* (model B better) and *n*.
   :rtype t: struct

Examples
--------

::

    new;
    library timeseries;

    // Squared errors of two 4-quarter-ahead forecasts on the same dates
    e_a = { 0.8, -0.4, 1.1, 0.2, -0.9, 0.6, 1.3, -0.2, 0.5, -0.7 };
    e_b = { 0.5, -0.6, 0.7, 0.4, -0.5, 0.3, 0.9, -0.4, 0.2, -0.3 };

    t = dmTest(e_a .^ 2, e_b .^ 2, h=4);

Remarks
-------

Tests H0: models A and B have equal expected loss. With
:math:`d_t = L_{A,t} - L_{B,t}`, a negative statistic means model A has the
smaller average loss; a positive one, model B. *p_value_one_sided* is the
upper-tail p-value (alternative: model B is better).

**Variants.**

.. list-table::
   :widths: auto

   * - ``"hln"``
     - The Harvey, Leybourne & Newbold (1997) test: long-run variance with
       equal weights on the autocovariances up to lag *h* - 1, their
       small-sample correction, and a Student-t reference with *N* - 1
       degrees of freedom. When that variance is not positive, which can
       happen for multi-step forecasts in small samples, it is recomputed
       with Bartlett weights 1 - j/*h* over the same lags (Harvey, Leybourne
       & Whitehouse 2017). :func:`forecastEval` uses this variant.
   * - ``"hac_hln_t"``
     - Newey-West (Bartlett) variance with an automatically chosen
       bandwidth, the same correction and t reference. Suited to one-step
       comparisons where the loss differential is persistent.
   * - ``"asymptotic"``
     - Newey-West variance with an automatic bandwidth and a standard normal
       reference, as in Diebold & Mariano (1995) for large samples. *h* must
       still be valid but does not enter the test.

If the variance is zero (a constant loss differential; for ``"hln"`` also
one whose spread is only rounding error) the result is neutral: statistic 0, two-sided
p-value 1.

Model
-----

.. math::

   DM = \frac{\bar{d}}{\sqrt{\hat\sigma^2_d / N}}, \qquad
   DM_{\text{HLN}} = DM \cdot \sqrt{\frac{N + 1 - 2h + h(h-1)/N}{N}}

For ``"hln"``, :math:`\hat\sigma^2_d = \hat\gamma_0 + 2\sum_{j=1}^{h-1}\hat\gamma_j`,
or :math:`\hat\gamma_0 + 2\sum_{j=1}^{h-1}(1 - j/h)\hat\gamma_j` when the first
is not positive, where :math:`\hat\gamma_j` are the sample autocovariances of
:math:`d_t` (divided by *N*).

References
----------

- Diebold, F.X. and R.S. Mariano (1995). "Comparing predictive accuracy." *Journal of Business & Economic Statistics*, 13(3), 253-263.
- Harvey, D., S. Leybourne, and P. Newbold (1997). "Testing the equality of prediction mean squared errors." *International Journal of Forecasting*, 13(2), 281-291.
- Harvey, D.I., S.J. Leybourne, and E.J. Whitehouse (2017). "Forecast evaluation tests and negative long-run variance estimates in small samples." *International Journal of Forecasting*, 33(4), 833-847.
- Newey, W.K. and K.D. West (1994). "Automatic lag selection in covariance matrix estimation." *Review of Economic Studies*, 61(4), 631-653.

Library
-------
timeseries

Source
------
var.src

.. seealso:: Functions :func:`forecastEval`, :func:`cwTest`, :func:`mcsTest`, :func:`fcScore`
