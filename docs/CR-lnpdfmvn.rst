
lnpdfmvn
==============================================

Purpose
----------------

Computes multivariate Normal log-probabilities.

Format
----------------
.. function:: z = lnpdfmvn(x, s)

    :param x: data.
    :type x: NxK matrix

    :param s: covariance matrix.
    :type s: KxK matrix

    :return z: log-probabilities.

    :type z: Nx1 vector

Remarks
-------

This computes the multivariate Normal log-probability for each row of *x*.

Source
------

lnpdfn.src

