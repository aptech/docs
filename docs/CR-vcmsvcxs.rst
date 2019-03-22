
vcms, vcxs
==============================================

Purpose
----------------
Computes the observed variance-covariance matrix. NOTE: vcms and vcxs have been replaced with functions varCovX and varCovM whose descriptions use more standard statistical nomenclature. vcxs and vcms will continue to be available for backwards compatibility.

Format
----------------
.. function:: vcms(m) 
			  vcxs(x)

    :param m:  A constant term MUST have been the first variable when the moment matrix was computed.
    :type m: KxK moment (x'x) matrix

    :param x: 
    :type x: NxK matrix of data

    :returns: vc (*KxK variance-covariance matrix*) .



Remarks
-------

The variance covariance matrix is that of the input data matrix. It is
computed as the moment matrix of deviations about the mean divided by
the number of observations N. For an unbiased estimator covariance
matrix which uses N - 1 rather than N see vcm or vcx.



Source
------

corrs.src

.. seealso:: Functions :func:`momentd`, :func:`corrms`
