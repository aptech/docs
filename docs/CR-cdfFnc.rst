
cdfFnc
==============================================

Purpose
----------------
Computes the cumulative distribution function of the noncentral F distribution.

Format
----------------
.. function:: cdfFnc(x,  n1,  n2,  d)

    :param x: values of upper limits of integrals, x > 0.
    :type x: Nx1 vector

    :param v1: degrees of freedom of numerator, n1 > 0.
    :type v1: scalar

    :param v2: degrees of freedom of denominator, n2 > 0.
    :type v2: scalar

    :param d: noncentrality parameter, d > 0.
        
        This is the square root of the noncentrality parameter
        that sometimes goes under the symbol lambda. (See Scheffe,
        The Analysis of Variance, App. IV, 1959.)
    :type d: scalar

    :returns: y (*TODO*), Nx1 vector.

