
vcm, vcx
==============================================

Purpose
----------------
Computes an unbiased estimate a variance-covariance matrix.

.. NOTE:: :func:`vcm` and :func:`vcx` have been replaced with functions :func:`varCovXS` and :func:`varCovMS` 
    whose descriptions use more standard statistical nomenclature. :func:`vcx` and :func:`vcm` will continue 
    to be available for backwards compatibility.

Format
----------------
.. function:: vc = vcm(m)
              vc = vcx(x)

    :param m:  A constant term MUST have been the first variable when the moment matrix was computed.
    :type m: KxK moment (:math:`x'x`) matrix

    :param x: data
    :type x: NxK matrix

    :returns: vc (*KxK variance-covariance matrix*)

Remarks
-------

The variance-covariance matrix is computed as an unbiased estimator of
the population variance-covariance. It is computed as the moment matrix
of deviations about the mean divided by the number of observations minus
one, :math:`N - 1`. For an observed variance-covariance matrix which uses :math:`N`
rather than :math:`N - 1` see :func:`vcms` or :func:`vcxs`.

Source
------

corr.src

.. seealso:: Functions :func:`momentd`

