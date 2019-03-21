
vcm, vcx
==============================================

Purpose
----------------
Computes an unbiased estimate a variance-covariance matrix.
		NOTE: vcm and vcx have been replaced with functions varCovXS and varCovMS whose descriptions use more standard statistical nomenclature. vcx and vcm will continue to be available for backwards compatibility.

Format
----------------
.. function:: vcm(m) 
			  vcx(x)

    :param m:  A constant term MUST have
        been the first variable when the moment matrix was computed.
    :type m: KxK moment (x'x) matrix

    :param x: 
    :type x: NxK matrix of data

    :returns: vc (*TODO*), KxK variance-covariance matrix.



Remarks
-------

The variance-covariance matrix is computed as an unbiased estimator of
the population variance-covariance. It is computed as the moment matrix
of deviations about the mean divided by the number of observations minus
one, N - 1. For an observed variance-covariance matrix which uses N
rather than N - 1 see vcms or vcxs.

