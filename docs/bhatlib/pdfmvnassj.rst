pdfmvnassj
==============================================

Purpose
----------------

Computes the gradient of the approximated cumulative distribution function (CDF) of a multivariate normal distribution using the Switzer, Solow, and Joe (SSJ) approach.

Format
----------------
.. function:: { w, gC, gcor } = pdfmvnaSSJ(a, rr, s)

    :param a: Abscissae values.
    :type a: 1xK matrix

    :param rr: Correlation matrix.
    :type rr: KxK matrix

    :param s: Seed value for random ordering of abscissae when `_optimal = 2`.
    :type s: Scalar

    :return w: Computed probability `Pr(X < a | rr)`.
    :rtype w: 1x1 scalar

    :return gC: Gradients with respect to abscissae.
    :rtype gC: Kx1 matrix

    :return gcor: Gradients with respect to correlation parameters, arranged as the upper diagonal.
    :rtype gcor: ((K-1) * K / 2) x 1 matrix

Global Inputs
-------------

.. data:: _perms

   Specifies the number of permutations of abscissae that will be used in the Switzer, Solow, Joe analytic approach, n=1 means only one permutation will be used.

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
