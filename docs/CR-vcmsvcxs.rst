
vcms, vcxs
==============================================

Purpose
----------------
Computes the observed variance-covariance matrix. 

.. NOTE:: :func:`vcms` and :func:`vcxs` have been replaced with functions :func:`varCovX` and :func:`varCovM` 
    whose descriptions use more standard statistical nomenclature. :func:`vcxs` and :func:`vcms` will continue 
    to be available for backwards compatibility.

Format
----------------
.. function:: vc = vcms(m)
              vc = vcxs(x)

    :param m: A constant term MUST have been the first variable when the moment matrix was computed.
    :type m: KxK moment (:math:`x'x`) matrix

    :param x: data
    :type x: NxK matrix

    :return vc: 

    :type vc: KxK variance-covariance matrix

Remarks
-------

The variance covariance matrix is that of the input data matrix. It is
computed as the moment matrix of deviations about the mean divided by
the number of observations :math:`N`. For an unbiased estimator covariance
matrix which uses :math:`N - 1` rather than :math:`N` see :func:`vcm` or :func:`vcx`.

Source
------

corrs.src

.. seealso:: Functions :func:`momentd`, :func:`corrms`

