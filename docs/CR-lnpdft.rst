
lnpdft
==============================================

Purpose
----------------

Computes Student's t log-probabilities.

Format
----------------
.. function:: lnpdft(x, nu)

    :param x: data.
    :type x: NxK matrix

    :param nu: degrees of freedom.
    :type nu: scalar

    :returns: z (*NxK matrix*), log-probabilities.



Remarks
-------

This does not compute the log of the joint Student's t pdf. Instead, the
scalar Normal density function is computed element-by-element.

For multivariate probabilities with covariance matrix see lnpdfmvt.

