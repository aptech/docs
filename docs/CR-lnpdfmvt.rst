
lnpdfmvt
==============================================

Purpose
----------------

Computes multivariate Student's t log-probabilities.

Format
----------------
.. function:: z = lnpdfmvt(x, s, nu)

    :param x: data
    :type x: NxK matrix

    :param s: covariance matrix.
    :type s: KxK matrix

    :param nu: degrees of freedom.
    :type nu: scalar

    :return z: log-probabilities.

    :rtype z: Nx1 vector

Source
------

lnpdfn.src

.. seealso:: Functions :func:`lnpdft`

