
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

    :returns: z (*Nx1 vector*), log-probabilities.

Source
------

lnpdfn.src

.. seealso:: Functions :func:`lnpdft`

