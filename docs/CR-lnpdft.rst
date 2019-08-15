
lnpdft
==============================================

Purpose
----------------

Computes Student's t log-probabilities.

Format
----------------
.. function:: z = lnpdft(x, nu)

    :param x: data
    :type x: NxK matrix

    :param nu: degrees of freedom.
    :type nu: scalar

    :return z: log-probabilities.

    :rtype z: NxK matrix

Remarks
-------

This does not compute the log of the joint Student's t pdf. Instead, the
scalar Normal density function is computed element-by-element.

For multivariate probabilities with covariance matrix see :func:`lnpdfmvt`.

.. seealso:: Functions :func:`lnpdfmvt`

