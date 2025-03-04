cdfmvna
==============================================

Purpose
----------------

Approximates multivariate orthant probability using only bivariate and univariate cumulative normals.

Format
----------------
.. function:: {w, s1} = cdfmvna(a, r, s)

    :param a: Abscissae values.
    :type a: 1xK matrix

    :param r: Correlation matrix.
    :type r: KxK matrix

    :param s: Seed value to use to generate random permutations; use s = 0 if _randd = 0.
    :type s: scalar

    :return w: Probability Pr(X < a | r).
    :rtype w: 1x1 vector

    :return s1: New seed value.
    :rtype s1: scalar

Source
----------------

cdfmvna.src
