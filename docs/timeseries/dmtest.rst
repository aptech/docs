dmTest
======

Purpose
-------
Diebold-Mariano test for equal predictive ability between two forecast models.

Format
------

.. function:: t = dmTest(loss_a, loss_b)
              t = dmTest(loss_a, loss_b, h=4)

   :param loss_a: loss series for model A (e.g., squared forecast errors).
   :type loss_a: Nx1 vector

   :param loss_b: loss series for model B.
   :type loss_b: Nx1 vector

   :param h: Optional keyword, forecast horizon for HLN small-sample correction (Harvey, Leybourne & Newbold 1997). Default = 1 (no correction).
   :type h: scalar

   :return t: An instance of a :class:`testResult` structure containing statistic, p_value, p_value_one_sided, and n.
   :rtype t: struct

Examples
--------

::

    new;
    library timeseries;

    // Squared errors from two models
    loss_a = e_arima .^ 2;
    loss_b = e_bvar .^ 2;

    t = dmTest(loss_a, loss_b);

    print "DM statistic:" t.statistic;
    print "p-value (two-sided):" t.p_value;
    print "p-value (A better):" t.p_value_one_sided;

    // With HLN correction for h=4 ahead
    t = dmTest(loss_a, loss_b, h=4);

Remarks
-------

Tests H0: models A and B have equal predictive ability. A negative statistic
indicates model A is better. Uses HAC standard errors (Newey-West) to account
for serial correlation in multi-step forecast errors.

The HLN correction adjusts for small-sample bias when the forecast horizon
*h* > 1.

Library
-------
timeseries

Source
------
scoring.src

.. seealso:: Functions :func:`cwTest`, :func:`mcsTest`, :func:`fcScore`
