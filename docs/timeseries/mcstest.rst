mcsTest
=======

Purpose
-------
Model Confidence Set: identify the set of models with equal predictive ability.

Format
------

.. function:: mcs = mcsTest(losses)
              mcs = mcsTest(losses, alpha=0.10)

   :param losses: loss series for M models. Each column is one model's loss series.
   :type losses: NxM matrix

   :param alpha: Optional keyword, significance level. Default = 0.15.
   :type alpha: scalar

   :param n_boot: Optional keyword, bootstrap replications. Default = 5000.
   :type n_boot: scalar

   :param block: Optional keyword, block length for block bootstrap. Default = auto.
   :type block: scalar

   :param seed: Optional keyword, RNG seed. Default = 42.
   :type seed: scalar

   :param quiet: Optional keyword, set to 1 to suppress output. Default = 0.
   :type quiet: scalar

   :return mcs: An instance of a :class:`mcsResult` structure containing surviving model indices, p-values, and elimination order.
   :rtype mcs: struct

Examples
--------

::

    new;
    library timeseries;

    // Squared errors from 5 models
    losses = e1^2 ~ e2^2 ~ e3^2 ~ e4^2 ~ e5^2;

    mcs = mcsTest(losses);

    print "Surviving models:" mcs.surviving;
    print "MCS p-values:" mcs.p_values;
    print "Elimination order:" mcs.elimination_order;

Remarks
-------

Implements Hansen, Lunde & Nason (2011). The MCS is the smallest set of
models that contains the best model with probability 1-alpha. Models are
sequentially eliminated until the null of equal predictive ability cannot
be rejected for the remaining set.

The surviving set includes all models whose MCS p-value exceeds *alpha*.

Library
-------
timeseries

Source
------
scoring.src

.. seealso:: Functions :func:`dmTest`, :func:`cwTest`
