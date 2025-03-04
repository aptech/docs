cdfmvnatgbme
==============================================

Purpose
----------------

Approximates the cumulative distribution function (CDF) of a multivariate normal distribution using Trinh and Genz's approximation with bivariate screening (TGBME) approach.

Format
----------------
.. function:: w = cdfmvnaTGBME(a, rr, s)

    :param a: Abscissae values for probability approximation.
    :type a: 1xK matrix

    :param rr: Correlation matrix.
    :type rr: KxK matrix

    :param s: Seed value for random ordering of abscissae when `_optimal = 2`.
    :type s: Scalar

    :return w: Computed probability `Pr(X < a | rr)`.
    :rtype w: 1x1 scalar

Global Inputs
-------------

.. data:: _optimal

    Controls the ordering of the abscissae.

    .. list-table::
        :widths: auto

        * - [0]
          - uses a simple ascending order of abscissae.
        * - [1]
          - orders values so that outermost integral variables have the smallest expected values.
        * - [2]
          - applies a random ordering of abscissae.
        * - [3]
          -  retains the original order.

Source
----------------

cdfmvna-meldlt.src
