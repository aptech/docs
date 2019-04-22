
lnpdfmvn
==============================================

Purpose
----------------

Computes multivariate Normal log-probabilities.

Format
----------------
.. function:: lnpdfmvn(x, s)

    :param x: data.
    :type x: NxK matrix

    :param s: covariance matrix.
    :type s: KxK matrix

    :returns: z (*Nx1 vector*), log-probabilities.

Remarks
-------

This computes the multivariate Normal log-probability for each row of *x*.

Source
------

lnpdfn.src

